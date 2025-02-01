import pymysql
import json
import google.generativeai as genai
genai.configure(api_key="Api_key")
def connect():
    # Connection function

    try:
        connection=pymysql.connect(host='localhost',
                               user='user',
                               password="password",
                               database='human_resources')
        return connection
    except pymysql.MySQLError as e:
        return str(e)

def convert_to_sql(user_query:str)->str:
    """
    This function  will convert user queries to sql queries and process json format output.
    """
    prompt="""Kullanıcıdan gelen isteği Sql formatına uygun sorguya dönüştür. Sorguların tablo isimleri ve sütun isimleri altta belirtilen tablo ve sütun isimleri olmalıdır.Atanan eşya ile ilgili bir soru sorulursa adet bilgisi ile birlikte sorgu yaz. Eğer alakasız bir şey yazıyorsa kararlılık 0 olmalıdır.
* Asla bu komutları kullanma *: 'drop', 'truncate', 'delete', 'update', 'insert', 'alter','create', 'replace', 'rename', 'grant', 'revoke'
Aşağıda tablo ve  her bir tablodaki sütun isimleri verilmiştir:

Tablo: email
Sütunlar: id, email_title, email_description, from_emp_id, to_emp_id

Tablo: employee_items
Sütunlar: employee_id, item_id, assignment_date, quantity, assign_id

Tablo: employee_leaves
Sütunlar:leave_request_id,employee_id,status_of_request('Pending','Accepted','Rejected'),request_date,approved_by,answer_date,leave_type('Annual Leave','Health Leave','Unpaid Leave','Excuse Leave'),Start_date,end_date,total_dates,desc_request,created_at

Tablo: employees
Sütunlar: employee_id, first_name, last_name, date_of_birth, gender, job_title, department, salary, hire_date, email, phone_number, password, is_active

Tablo: events_
Sütunlar: id, event_name, event_text, event_date

Tablo: items
Sütunlar: id, item_name, quantity

Tablo: messages
Sütunlar: id, from_emp_id, to_emp_id, message_text, is_read, message_date, subject

Tablo: pending_email
Sütunlar: id, email_title, email_description, from_emp_id, to_emp_id, send_date, is_sent

Tablo: special_requests
Sütunlar: request_id, employee_id, request_type('Advance','Salary Increase','Payback','Other), request_amount, request_date, status_of_request('Pending','Accepted)

*Örnek Senaryo:*
 {
      "query": "en çok maaş alan eleman kimdir.",
      "sql_query": "SELECT first_name, last_name, salary FROM employees ORDER BY salary DESC LIMIT 1",
      "confidence":0.94
    },
    {
      "query": "It departmanında olan çalışanları getir.",
      "sql_query": "SELECT * FROM employees WHERE department = 'IT'",
      "confidence":0.97
    },
    {
      "query": "Hikmet'e atanan eşyaları söyle.",
      "sql_query": "SELECT i.item_name, ei.quantity FROM items i JOIN employee_items ei ON i.id = ei.item_id JOIN employees e ON ei.employee_id = e.employee_id WHERE e.first_name = 'Hikmet'",
      "confidence":1.0}

Yanıtın Json formatında olmalı:
**Json formatı**
{"query:str,
"sql_query":str,
"confidence":int}

 """
    generation_config={
    "temperature":0.1,
    "top_p":0.96,
    "top_k":64,
    "response_mime_type": "application/json"}
    model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,
                                system_instruction=prompt)
    response=model.generate_content(user_query)
    try:
        json_response=json.loads(response.text)  # taking and processing output
        sql_query=json_response["sql_query"]
        #print(sql_query)
        confidence=json_response["confidence"]
        if confidence>0.7:
          return sql_query
        else:
          return False
    except Exception as e:
        return str(e)


def fix_sql_query(sql_query:str,error_reason:str)->str:
    """
    This function will check the sql query and if it is  wrong,it will return fixed query.
    """
    prompt=f"""Sen gelen  sql sorgusundaki hatayı  kontrol et ve Yanlış kısmı düzelt.
    hata:{error_reason}
    Cevabın json formatında olmalıdır.
    Örnek senaryo:
    {{
      "query": "SELECT first_name, last_name, MAX(salary) FROM employees",
      "fixed_query":"SELECT first_name, last_name FROM employees ORDER BY salary DESC LIMIT 1"
    }}
    Json formatı:
    {{"query":str,
    "fixed_query":str}}
    """
    generation_config={
    "temperature":0.1,
    "top_p":0.96,
    "top_k":64,
    "response_mime_type": "application/json"}
    model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,
                                system_instruction=prompt)
    response=model.generate_content(sql_query)
    
    try:
        json_response=json.loads(response.text)
        #sorgu=json_response["sorgu"]
        fixed_query=json_response["fixed_query"]
        #print(fixed_query)
        return fixed_query
    except Exception as e:
        return str(e)

def run_in_sql(sorgu:str,deneme=0,maksimum_deneme=3)->str:
    """
    This function will run sql queries which is taken from chatbot in database and return the output.
    """
    
    connection=connect()
    cursor=connection.cursor()
    dangerous_operations = [
        'drop', 'delete',
    ]
    try:
        for operation in dangerous_operations:
            if operation in sorgu.lower():
                return "Bu sorguyu çalıştıramazsınız."
            else:
                
                cursor.execute(sorgu)
                result=cursor.fetchall()
                return result
    except pymysql.MySQLError as e:   
        if deneme<maksimum_deneme:
            fixed_query=fix_sql_query(sorgu,str(e))
            
            deneme+=1
            return (run_in_sql(fixed_query,deneme,maksimum_deneme))
        else:
            return "maksimum  deneme sayısına ulaşıldı,hata düzeltilemedi.Daha farklı bir sorgu deneyin"
        
    finally:
        cursor.close()
        connection.close()
        


def ask_chatbot(user_query:str) -> str:
    """This function takes the user query and returns the response of the sql query."""
    try:
        query = convert_to_sql(user_query)
        if query:
            response = run_in_sql(query)
            output=friendly_chatbot(user_query,response,query)
            return output
        else:
            return "Your query could not converted to a proper SQL query. Please try something else..."
    except Exception as e:
        response = "Something went wrong and we encountered an error. Error related information:\n"\
                f"{e}\n"\
                "You can try something else or you can contact the developers."
        return response
    
def friendly_chatbot(user_query,sql_result,sql_query):
    """This function takes the response of the sql_query and returns  it in a friendly way ."""
    friendly_prompt=f"""Veri tabanından gelen cevabı, kullanıcının sorusu ve gelen sql komutunu dikkate alarak güzel okunabilir formatta dost canlısı cevap veren bir asistansın.Eğer aynı sonuçtan birden fazla varsa toplam şeklinde göster.Kullanıcının sorusu ,sql cevabı ve sql sorgusu altta belirtilmiştir. 
    örnek senaryo:
    user:Hikmet’e atanmış eşyalar nedir
    sql_query:SELECT i.item_name, ei.quantity FROM items i JOIN employee_items ei ON i.id = ei.item_id JOIN employees e ON ei.employee_id = e.employee_id WHERE e.first_name = 'Hikmet'
    response:(('hammer', 1), ('gloves', 50), ('safety shoes', 1))
    friendly_response:Hikmet’e atanmış eşyalar şöyle:
                        - 1 adet hammer
                        - 50 adet gloves
                        - 1 adet safety shoes
    Bilgiler:
    sql sorgusu ={sql_query} 
    sql cevabı:{sql_result} 
    
    """
    model=genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config={"temperature":0.7},system_instruction=friendly_prompt)
    response=model.generate_content(user_query)
    # print(user_query)
    # print("*\n",sql_result)
    # print("*\n",sql_query)
    # print(friendly_prompt)
    return response.text


# END
