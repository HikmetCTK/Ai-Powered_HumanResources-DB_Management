import pymysql
import smtplib
import random

def connect():
    """
    This function will be used to handle connections in other functions.
    """
    try:
        connection=pymysql.connect(host='localhost',
                               user='root',
                               password="sql5858",
                               database='human_resources')
        return connection
    except pymysql.MySQLError as e:
        return str(e)

def connection_check():
    """
    This function will be used to check whether database
    connection can be handled or not, regularly with a timer.
    """
    try:
        connection=pymysql.connect(host='localhost',
                               user='root',
                               password="sql5858",
                               database='human_resources')
        
    except pymysql.MySQLError as e:
        # If an error occurs trying to create a connection, there is no need in trying to close it.
        return (False, str(e))

    else:
        # If it does not encounter any error, close the connection.
        connection.close()
        return (True, None)

#connection=connection_check()




#  email and password for testing
# email=123@gmail.com 
# password=123

def login(email,password):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="select * from employees where email=%s and password=%s"
            cursor.execute(query,(email,password))
            record=cursor.fetchone()
            if record:
                role=record[5]
                # If str returns, then it is either 'Human Resources' or 'Employee'
                if role=='Human Resources':
                    return "Human Resources"
                else:
                    return "Employee"
            else:
                # If None returns, then it means that login failed
                return None
    except pymysql.MySQLError as e:
        # If the returning str is neither 'Human Resources' nor 'Employee', that means that an error has occurred!
        return str(e)
    
    finally:
        connection.close()

"""
if connection:
    user_email=input('enter your mail:').strip()
    user_password=input('enter your password:').strip()
    login(user_email,user_password)
    connection.close()
    print("connection closed")
else:
    print("connection failed")
"""

user_email='' # E mail address where the code will be sent. 
              #This is just to check if the code appears in Gmail. You can use any gmail you want.

def send_verification_code():
    verification_code = random.randint(100000, 999999)
    
    sender_email ='system  mail'  #this e-mail should provide app password on google
    sender_password = "app password from gmail is here" # app password
    try:

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            
            subject = "Your Password Reset Code"
            body = f"Your verification code is {verification_code}."
            msg = f"Subject: {subject}\n\n{body}"
            
            
            smtp.sendmail(sender_email,user_email,msg)
        
        return verification_code
    except pymysql.MySQLError as e:
        return str(e)



def reset_change_password(new_password, entered_code, verification_code, user_email):
    if entered_code == verification_code:
        connection = connect()  # Assuming this function checks connection
        
        try:
            with connection.cursor() as cursor:


             update_query = "UPDATE employees SET password = %s WHERE email = %s"
        
            cursor.execute(update_query, (new_password, user_email))
        
            connection.commit()
            #print("Password changed successfully")
            return True
        except pymysql.MySQLError as e:
            return str(e)
        finally:
            connection.close()
            
    else:
        #print("Invalid verification code.")
        return False
    

def hiring(name,surname,birth,gender,job_title,derpatment,salary,hire_date,email,phone_no,password):
    connection=connect()
    cursor=connection.cursor()
    
    try:
        with connection.cursor() as cursor:
    
            query="""insert into employees(first_name, last_name, date_of_birth, gender, job_title, department, salary, hire_date, email, phone_number, password) values 
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values=name,surname,birth,gender,job_title,derpatment,salary,hire_date,email,phone_no,password
            cursor.execute(query,values)
            connection.commit()
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()

employe_list=[] #qlistwidget  #FEVZİ 

def load_employee():  #load  id,name,surname of employees
    connection=connect()
    try:

        with connection.cursor() as cursor:
            query="select employee_id,first_name,last_name from employees"
            cursor.execute(query)
            employees=cursor.fetchall()
            for emp in employees:
                employe_list.append(emp)
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()



def not_working(): #changes employees is_active value 1 to 0
    selected_employee=employe_list[1] #selected_employee by user from list .!>>>FEVZİ BURAYI  DEĞİŞTİR 
    connection=connect()
    try:
        with connection.cursor() as cursor:
           query="update employees set is_active=0 where employee_id=%s"
           employee_id=selected_employee[0]  #selecting id
           cursor.execute(query,employee_id)
           connection.commit()
    except pymysql.MySQLError as e:
        return str(e)       
    finally:
        connection.close()

#load_employee()
#not_working()

#verification_code = send_verification_code()

#entered_code = int(input("Enter verification code: "))
#new_password = input("Enter new password: ")


#reset_change_password(new_password, entered_code, verification_code, user_email)

item_list=[]
def load_infos(table_name): #^^# Brings all records from specific table 

    connection=connect()
    try:

        with connection.cursor() as cursor:
            query=f"select * from {table_name}"
            cursor.execute(query)
            items=cursor.fetchall()
            for item in items:
                item_list.append(item)
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()
# load_infos('items') #sample usage

def  add_item(item_name,quantity):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="insert into items(item_name,quantity) values (%s,%s)"
            values=item_name,quantity
            cursor.execute(query,values)
            connection.commit()
    except pymysql.MySQLError as e:
        return str (e)
    finally:
        connection.close()
    
#add_item('Chip',250) #^^# onaylandı
def delete_item(item_id): #id yazınca  itemi silen fonksiyon 
    connection=connect()
    #selected_item=item_list[1]
    try:
        with connection.cursor() as cursor:
            #item_id=selected_item[0]
            query="delete from items where id=%s"
            cursor.execute(query,item_id)
            connection.commit()
    except pymysql.MySQLError as e:
        return str (e)
    finally:
        connection.close()
#delete_item(14)

# assigned_list=[] #^^# Qlistwidget

def load_item_list_with_name(): # çalışan ismiyle birlikte zimmetli eşyayı gösteren kod .!tablo view ile oluşturuldu sanal bir görüntü için !! bknz:create view
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="select employee_id,first_name,last_name,item_id,item_name,assignment_date from employee_items_with_names"
            cursor.execute(query)
            employee_item_list=cursor.fetchall()
            
            for emp_item in employee_item_list:
                assigned_list.append(emp_item)

    except pymysql.MySQLError as e:
        return str(e)
    
    finally:
        connection.close()


# (1, 'Alvin', 'Fernier', 3, 'gloves', datetime.datetime(1948, 5, 22, 2, 24, 37)) örnek çıktı 
def assign_item_to_employee(assigned_list):
    connection=connect()
    selected_emp=assigned_list[1] # buraya qt widget list gelmeli  >>>FEVZİ<<<
    try:
        with connection.cursor() as cursor:
            emp_id=selected_emp[0]  #id çekme işlemi
            item_id=selected_emp[3] #item_id
            query="insert into employee_items(employee_id,item_id,assignment_date) values(%s,%s,NOW())"
            cursor.execute(query,(emp_id,item_id))
            connection.commit()
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()


def remove_item_from_employee(assigned_list):
    connection=connect()
    selected_emp=assigned_list[1] # buraya qt widget list gelmeli  >>>FEVZİ<<<
    print(selected_emp)
    try:
        with connection.cursor() as cursor:
            assign_date=selected_emp[5]  #id çekme işlemi
            query="delete from employee_items where assignment_date=%s"
            cursor.execute(query,(assign_date,))
            connection.commit()
            print(f"Deleted records with assignment date: {assign_date}")
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()

def get_assigned_items(assigned_list): #^^# seçilen kullanıcının id sini alıp sadece zimmetli eşyalarını ve teslim edilme tarihlerini  gösteren fonksiyon 
    connection=connect()
    selected_emp=assigned_list[1]
    employee_id=selected_emp[0]
    query="""select i.item_name,ei.assignment_date from employee_items ei 
    join items i on ei.item_id=i.id 
    where ei.employee_id=%s
    """
    try:
        with connection.cursor() as cursor:

            cursor.execute(query,(employee_id,))
            resultss=cursor.fetchall()
            return resultss
    
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()




def search(table_name,search_term): #tabloya göre arama yapan fonksiyon 
    table=[]
    connection = connect()
    try:
            with connection.cursor() as cursor:
                query = f"SELECT first_name, last_name FROM {table_name} WHERE first_name LIKE %s OR last_name LIKE %s"
                cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
                results = cursor.fetchall()
                for item in results:
                      table.append(item)
                return table

    except pymysql.MySQLError as e:
            return str(e)
    finally:
            connection.close()

"""
view ile oluşturulan tablonun sql komutu 

SELECT employee_id,first_name,last_name,item_id,item_name,assignment_date FROM employee_items_with_names;

"""



def update_employee_salary():
    try:
        emp_id = int(input("Please enter worker ID: "))
        new_salary = int(input("Please enter new salary value: "))
        
           
        if new_salary > int(0):  
            try:
                with connection.cursor() as cursor:
                    sql = "UPDATE employees SET salary = %s WHERE employee_id = %s"
                    cursor.execute(sql, (new_salary, emp_id))
                    connection.commit()
            finally:
                connection.close()
        else: 
            handle_value_error()#BURAYI İSTERSEK DİREKT SİLERİZ
            
    except pymysql.Error as e:
        sys.exit(1)

def search(keyword,table_name,column_name): #istenilen tablonun istenilen sütununda arama yapılmasını sağlayan fonksiyon.
    connection=connect()
    cursor = connection.cursor()
    query=f"select * from {table_name} where {column_name} like %s;"
    try:
        cursor.execute(query,(f"%{keyword}%"))
        results=cursor.fetchall()
        return results
    except Exception as e:
        return e
    finally:
        cursor.close()
        connection.close()


def handle_value_error():#BEYLER İLERİDE OLASI DEĞERLERİ İSTEDİĞİMİZ GİBİ HANDLE ETMEMİZ GEREKEBİLİR DİYE BÖYLE BİR FONK YAZDIM KALDIRILABİLİR SİZE KALMIŞ
    print('Geçersiz değer girildi')

