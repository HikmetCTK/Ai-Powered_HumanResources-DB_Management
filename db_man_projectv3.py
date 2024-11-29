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

def login(email,password): #id eklendi yeni login fonk
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="select * from employees where email=%s and password=%s"
            cursor.execute(query,(email,password))
            record=cursor.fetchone()
            id=record[0]
            if record:
                role=record[5]
                # If str returns, then it is either 'Human Resources' or 'Employee'
                if role=='Human Resources':
                    return "Human Resources",id
                else:
                    return "Employee",id
            else:
                # If None returns, then it means that login failed
                return None
    except Exception as e:
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

def send_verification_code(user_email):
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
            query="select * from employees"
            cursor.execute(query)
            employees=cursor.fetchall()
            for emp in employees:
                employe_list.append(emp)
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()



def not_working(selected_employee): #changes employees is_active value 1 to 0
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

# assigned_list=[] #^^# QLİSTWİDGET

def load_item_list_with_name(assigned_list): # çalışan ismiyle birlikte zimmetli eşyayı gösteren kod .!tablo view ile oluşturuldu sanal bir görüntü için !! bknz:create view
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




def search_for_employee(search_term): #tabloya göre arama yapan fonksiyon 
    table=[]
    connection = connect()
    try:
            with connection.cursor() as cursor:
                query = f"SELECT * FROM employees WHERE first_name LIKE %s OR last_name LIKE %s"
                cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
                results = cursor.fetchall()
                for item in results:
                      table.append(item)
                return table

    except pymysql.MySQLError as e:
            return str(e)
    finally:
            connection.close()



def update_employee_salary(emp_id,new_salary):
    connection=connect()
    try:
        emp_id = emp_id
        new_salary = new_salary
        
           
        if new_salary > int(0):  
            try:
                with connection.cursor() as cursor:
                    sql = "UPDATE employees SET salary = %s WHERE employee_id = %s"
                    cursor.execute(sql, (new_salary, emp_id))
                    connection.commit()
            finally:
                connection.close()
        else: 
            print('Geçersiz değer girildi')
            
    except Exception as e: #deleted sys.exit(1)
        return str(e)
    finally:
        cursor.close()
        connection.close()
        

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
        
def send_message_anyone(from_id,employee_ids,message): #for both side ##^^##
    try:
        connection=connect()
        with connection.cursor() as cursor:

            
            query = """ 
            INSERT INTO messages (from_emp_id, to_emp_id, message_text) 
            VALUES (%s, %s, %s);
            """

            # Prepare recipient tuples
            recipients = [(from_id, emp_id, message) for emp_id in employee_ids]
            
            cursor.executemany(query, recipients)
            #connection.commit()              

            return "Messages sent successfully!" #message alert

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
    
#send_message_anyone(3,[8],"this is single message attempting")
def see_message(emp_id): # for both side  ##^^##
    
    """ emp id is taken from login form to see messages which are sent to him. """
    try:
        connection=connect()
        with connection.cursor() as cursor:
            
            query="""select  m.id,e.first_name,e.last_name,m.message_text,m.message_date from messages m join employees e on  m.from_emp_id=e.employee_id where to_emp_id=%s; 
"""
            cursor.execute(query,(emp_id))
            messages=cursor.fetchall()
            
            """
            ---- you can use this if you want to access each message information ----
            messages = records[0] 
            for (id, name, surname, text, date) in messages:
             """
            return messages
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        
        
        connection.close()
        
#records=see_message(7) # id si 7 olan kişiye  gelen mesajlar. 

"""  output format
(((6,
   'Bradan',
   'Beisley',
   'this is single message attempting',
   datetime.datetime(2024, 11, 27, 0, 7, 24)),
  (7,
   'Bradan',
   'Beisley',
   'this is single message attempting',
   datetime.datetime(2024, 11, 27, 0, 18, 44))),
 1)
 """
# Mark a message as sent
def mark_message_as_read(message_id): ##^^##
    try:
        
        connection = connect()  
        with connection.cursor() as cursor:

            query = "UPDATE Messages SET is_read = TRUE WHERE id = %s"
            cursor.execute(query, (message_id,))
            connection.commit()
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()



def add_event(event_name,event_text,event_date): ##^^##
    try:
        
        connection = connect()  
        with connection.cursor() as cursor:
            query="""insert into events_(event_name,event_text,event_date) values(%s,%s,%s)  """
            cursor.execute(query,(event_name,event_text,event_date))
            connection.commit()
            return " event planned succesfully "
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()

#add_event("football","come to foootball this saturday","2024-12-02 20:30:34")
def see_events(): ##^^##
    try:
        connection=connect()
        with connection.cursor() as cursor:
            
            query="""select  * from events_; 
"""
            cursor.execute(query)
            events=cursor.fetchall()
            
            """
            ---- you can use this if you want to access each message information ----
            events = records[0] 
            for (id, eventsname, text, date) in events:
             """
            return events
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        
        
        connection.close()

        
import pymysql
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def add_pending_email(email_title,email_description,from_emp_id,to_emp_id,send_date): 
    """add pending email ---"""
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="""insert into pending_email(email_title,email_description,from_emp_id,to_emp_id,send_date) values (%s,%s,%s,%s,%s)"""
            cursor.execute(query,(email_title,email_description,from_emp_id,to_emp_id,send_date))
            connection.commit()
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()

def check_pend_email():
    """" returns not_sent emails from database in tuple form """
    connection=connect()
    with connection.cursor() as cursor:
        try:
            query="""select e.first_name,e.last_name,pe.send_date,pe.email_title,pe.email_description,e.job_title,pe.to_emp_id,pe.id from pending_email pe join employees e on pe.from_emp_id=e.employee_id where is_sent=0"""
            cursor.execute(query)
            records=cursor.fetchall()
            return records
        
        finally:
            cursor.close()
            connection.close()

def get_email(emp_id):
    """ get email from employee id """
    connection=connect()
    with connection.cursor() as cursor:
        try:
            query=""" select email from employees where employee_id=%s """
            cursor.execute(query,emp_id)
            email=cursor.fetchone()
            return email
        except Exception as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()
    
def send_pend_email(records): 
    """ records is should be  taken from check_pend_email func. this func checks this tuple includes date to send or not if yes, it will send email based on condition"""
    current_time=datetime.now()

    try:
        if records:
            for record in records:
                send_date = record[2]
                
                if send_date<current_time:
                        name = record[0]
                        surname = record[1]
                        email_title=record[3]
                        email_description=record[4]
                        role=record[5]
                        to_emp_id=record[6]
                        pend_id=record[7]
                        sender_email ='gmail'
                        sender_password = "google app password"            
                        msg = MIMEMultipart()
                        msg['From'] =sender_email
                        to_email= get_email(to_emp_id)
                        msg['Subject'] = email_title
                        # Mesaj içeriğini UTF-8 olarak ekliyoruz
                        body_with_footer = f"{email_description}\n\n{name} {surname}-{role}"
                        msg.attach(MIMEText(body_with_footer, 'plain', 'utf-8'))

                                
                        try:
                            with smtplib.SMTP("smtp.gmail.com",587) as smtp:
                                smtp.starttls()
                                smtp.login(sender_email,sender_password)
                                #msg= f"Subject: {title}\n\n{body_with_footer}"

                                smtp.sendmail(sender_email,to_email,msg.as_string())
                                try:
            
                                    connection = connect()  
                                    with connection.cursor() as cursor:
                                        query = "UPDATE pending_email SET is_sent =1 WHERE id = %s"
                                        cursor.execute(query,pend_id)
                                        connection.commit()
                                except Exception as e:
                                    return str(e)
                        except Exception as e:
                            return str(e)
        else:
            return "gönderilecek mesaj yok"
    except Exception as e:
        return e
    




"""
emails_not_sent=check_pend_email()
send_pend_email(emails_not_sent)
"""


import unicodedata

def arrangeText(self, text:str) -> str:
    text = unicodedata.normalize('NFKD', text).casefold()
    arranged =  re.sub(r'\W+', '', text).casefold()
    return arranged
