import pymysql
import smtplib
import random
import calendar
from datetime import datetime, date
from decimal import Decimal


def connect():

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
            print(record)
            id=record[0]
            name=record[1]
            surname=record[2]
            
            if record:
                role=record[5]
                # If str returns, then it is either 'Human Resources' or 'Employee'
                if role=='Human resources':
                    return role,id,name,surname
                else:
                    return role,id,name,surname
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
            return employees
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()



def not_working(selected_employee:int): #changes employees is_active value 1 to 0
    connection=connect()
    try:
        with connection.cursor() as cursor:
           query="update employees set is_active=0 where employee_id=%s"
           cursor.execute(query,selected_employee)
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
            return items
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

#selected_item format =('1', 'hammer', '37')

def update_quantity_add(selected_item,add_quantity):
    connection=connect()
    item_id=selected_item[0] #item id çekme işlemi
    try:
        with connection.cursor() as cursor:
            
            item_id=item_id #item_id
            add_query="update items set quantity=quantity + %s where id=%s"
            cursor.execute(add_query,(add_quantity,item_id))
            connection.commit()
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()


#selected_item format =('1', 'hammer', '37')
def update_quantity_sub(selected_item,sub_quantity):
    connection=connect()
    item_id=selected_item[0] 
    try:
        with connection.cursor() as cursor:

            substract_query="update items set quantity=quantity - %s where id=%s"
            cursor.execute(substract_query,(sub_quantity,item_id))
            connection.commit()
    except pymysql.MySQLError as e:
        return str(e)
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
            query="select * from employee_items_with_names"
            cursor.execute(query)
            employee_item_list=cursor.fetchall()
            return employee_item_list

    except pymysql.MySQLError as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()

def remain_quantity(item_id): #return integer value which is remain stock by item_id. For employee
    connection=connect()
    try:
        with connection.cursor() as cursor:

            remain_quantity_query="select quantity from items where id =%s"
            cursor.execute(remain_quantity_query,(item_id))
            remain_quantity=cursor.fetchone()
            return remain_quantity[0]
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()

def assign_item_to_employee_no_checking(id,item_id,quantity): # assign item to employee not checking stock
    connection=connect()
    
    try:
        with connection.cursor() as cursor:
            emp_id=id  #id çekme işlemi
            item_id=item_id #item_id
            quantity=quantity
            query="insert into employee_items(employee_id,item_id,assignment_date,quantity) values(%s,%s,NOW(),%s)"
            cursor.execute(query,(emp_id,item_id,quantity))
            substract_query="update items set quantity=quantity - %s where id=%s"
            cursor.execute(substract_query,(quantity,item_id))
            connection.commit()
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()

def assign_item_to_employee(id,item_id,quantity):
    connection=connect()
    
    try:
        with connection.cursor() as cursor:
            emp_id=id  #id çekme işlemi
            item_id=item_id #item_id
            quantity=quantity
            remain_quantity_query="select quantity from items where id =%s"
            cursor.execute(remain_quantity_query,(item_id))
            remain_quantity=cursor.fetchone()

            if remain_quantity[0]>=quantity: #stok atanandan fazlaysa update database günceller 

                query="insert into employee_items(employee_id,item_id,assignment_date,quantity) values(%s,%s,NOW(),%s)"
                cursor.execute(query,(emp_id,item_id,quantity))
                substract_query="update items set quantity=quantity - %s where id=%s"  #stoktan atanan ürün  sayısı kadar düşer
                cursor.execute(substract_query,(quantity,item_id))
                connection.commit()
            else:
                return "not enough product"
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()

#assign_item_to_employee(3,2,50) # 3 numaralı personelin 2 numaralı itemi 50 adet alması



# employee_id, first_name, last_name, item_id, item_name, assignment_date
"""assigned_list=[
('1', 'Alvin', 'Fernier', '5', 'Welding Machine', '2010-07-27 11:54:10')
]"""

#örnek liste formatı direkt selected_emp olarakta işlem yapılabilir @FEVZİ
def remove_item_from_employee(assigned_list):
    connection=connect()
    selected_emp=assigned_list[0] # buraya qt widget list gelmeli  >>>FEVZİ<<<
    print(selected_emp)
    item_id=selected_emp[3]
    try:
        with connection.cursor() as cursor:
            assign_id = selected_emp[5]  # id çekme işlemi
            quantity_query = "select quantity from employee_items where assign_id=%s"
            cursor.execute(quantity_query, (assign_id,))
            result = cursor.fetchone()
            
            if result is None:
                return f"No records found for assignment id: {assign_id}"
            
            quantity = result[0]
            
            
            # Delete the record
            query = "delete from employee_items where assign_id=%s"
            cursor.execute(query, (assign_id,))
            
            # Update the quantity in the items table
            add_query = "update items set quantity=quantity + %s where id=%s"
            cursor.execute(add_query, (quantity, item_id))
            
            connection.commit()
            
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

def show_assigned_items_employee_side(emp_id): #^^# kullanıcıya zimmetli eşyalarını ve teslim edilme tarihlerini  gösteren fonksiyon 
    connection=connect()
    #selected_emp=assigned_list[1]
    query="""select i.item_name,ei.quantity,ei.assignment_date from employee_items ei 
    join items i on ei.item_id=i.id 
    where ei.employee_id=%s
    """
    try:
        with connection.cursor() as cursor:

            cursor.execute(query,(emp_id,))
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
        with connection.cursor() as cursor:
            sql = "UPDATE employees SET salary = %s WHERE employee_id = %s"
            cursor.execute(sql, (new_salary, emp_id))
            connection.commit()
    except Exception as e:
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
        return str(e)
    finally:
        cursor.close()
        connection.close()
        
def send_message_anyone(from_id,employee_ids,message,subject): #for both side ##^^##
    try:
        connection=connect()
        with connection.cursor() as cursor:

            
            query = """ 
            INSERT INTO messages (from_emp_id,to_emp_id,message_text,subject) 
            VALUES (%s, %s, %s,%s);
            """

            # Prepare recipient tuples
            recipients = [(from_id, emp_id, message,subject) for emp_id in employee_ids]
            
            cursor.executemany(query, recipients)
            connection.commit()              

            return "Messages sent successfully!" #message alert

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
        
#send_message_anyone(3,[8],"this is single message attempting2","acil!!")

def see_message(emp_id): # for both side  ##^^##
    
    """ emp id is taken from login form to see messages which are sent to him. """
    try:
        connection=connect()
        with connection.cursor() as cursor:
            
            query="""select  m.id,e.first_name,e.last_name,m.message_text,m.message_date,m.subject from messages m join employees e on  m.from_emp_id=e.employee_id where to_emp_id=%s; 
"""
            cursor.execute(query,(emp_id))
            messages=cursor.fetchall()
            
            """
            ---- you can use this if you want to access each message information ----
            messages = records[0] 
            for (id, name, surname, text, date,subject) in messages:
             """
            return messages
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()
        
def see_messagev2(emp_id): # for both side  Provide sending message to sender #^^#
    
    """ emp id is taken from login form to see messages which are sent to him. """
    try:
        connection=connect()
        with connection.cursor() as cursor:
            
            query="select  m.id,e.first_name,e.last_name,m.subject,m.message_text,m.message_date,m.from_emp_id from messages m join employees e on  m.from_emp_id=e.employee_id where to_emp_id=%s;"
            cursor.execute(query,(emp_id))
            messages=cursor.fetchall()
            

            return messages
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()

"""  output format
((10,
  'Bradan',
  'Beisley',
  'this is single message attempting',
  datetime.datetime(2024, 11, 27, 0, 34, 44),
  None),
 (19,
  'Bradan',
  'Beisley',
  'this is single message attempting2',
  datetime.datetime(2024, 12, 3, 0, 56, 1),
  'acil!!'))
 """
# Mark a message as sent
def mark_message_as_read(message_id): ##^^##
    try:
        connection = connect()  
        with connection.cursor() as cursor:
            query = "UPDATE messages SET is_read = TRUE WHERE id = %s"
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
            query="""select * from pending_email pe join employees e on pe.from_emp_id=e.employee_id where is_sent=0"""
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
                send_date = record[5]
                
                if send_date<current_time:
                        name = record[8]
                        surname = record[9]
                        email_title=record[1]
                        email_description=record[2]
                        role=record[12]
                        to_emp_id=record[4]
                        pend_id=record[0]
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
    

import datetime
from decimal import Decimal
def send_email(records,email_title,email_description,from_emp_id,from_name,from_surname,from_role):
    # Each sublist in records list includes 2 items; first is to_emp_id, second is to_email
    for record in records:
        print(record)
        to_email = record[1]
        print(to_email)
        if not to_email:
            return f"No email found for employee ID: {to_emp_id}"
        to_emp_id=record[0]
        sender_email ='gmail'
        sender_password="pswrd"
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = email_title
        body_with_footer = f"{email_description}\n\n{from_name} {from_surname} - {from_role}"
        msg.attach(MIMEText(body_with_footer, 'plain', 'utf-8'))

        try:
            # Send email
            with smtplib.SMTP("smtp.gmail.com",587) as smtp:
                smtp.starttls()
                smtp.login(sender_email,sender_password)
                smtp.sendmail(sender_email, to_email, msg.as_string())
            
            # Update database on success
            try:
                connection = connect()
                with connection.cursor() as cursor:
                    query = "insert into email(email_title, email_description, from_emp_id, to_emp_id)values(%s,%s,%s,%s)"
                    cursor.execute(query, (email_title, email_description, from_emp_id, to_emp_id))
                    connection.commit()
                return "Email sent and status updated in database."
            except Exception as e:
                return f"Error updating database: {e}"
        except Exception as e:
            return f"Error sending email: {e}"

"""datas=[(1,
  'Alvin',
  'Fernier',
  datetime.date(1967, 9, 18),
  'Male',
  'Human resources',
  'IT',
  Decimal('31980.52'),
  datetime.date(2017, 9, 7),
  'hikmetcatak99@gmail.com',
  '243-979-3929',
  '123',
  1)]
send_email(datas,"DENEMEv2-title","denev2-description",3,"hkmt","ctk","Ai eng")"""


"""
emails_not_sent=check_pend_email()
send_pend_email(emails_not_sent)
"""


def load_employee_for_message_selection(search_term=""): #  for message interface
    connection=connect()
    try:

        with connection.cursor() as cursor:
            query="""select employee_id,
            first_name, 
            last_name, 
            department,
            job_title,
            email from employees where first_name like %s or  last_name=%s """
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            employees=cursor.fetchall()
            return employees
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()
def load_employee_for_salary_adjustment():  #  for adjustment interface
    connection=connect()
    try:

        with connection.cursor() as cursor:
            query="select employee_id, first_name, last_name, department, job_title, salary from employees"
            cursor.execute(query)
            employees=cursor.fetchall()
            return employees
    except pymysql.MySQLError as e:
        return str(e)
    finally:
        connection.close()


'''ÖZEL TALEPLER'''



def create_special_request(employee_id, request_type, request_amount=None,):#Çalışan id'si ile talep oluşturur
    

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO special_requests 
            (employee_id, request_type, request_amount, request_date,) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                employee_id, 
                request_type, 
                request_amount, 
                date.today(), 
            ))
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        return str(e)
    
    finally:
        cursor.close()
        connection.close()
        
    


def get_pending_special_requests():#Beklemede Olan tüm talepleri getirir enum type dikkat

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM special_requests 
            WHERE status_of_special_request = 'Pending'
            """
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Bekleyen özel talepler getirilirken hata: {e}")
        return str(e)

    finally:
        cursor.close()
        connection.close



def process_special_request(request_id, status, approved_by):#Yönetici talebi onaylar veya ret eder
    
    connection = connect()

    try:
        with connection.cursor() as cursor:
            answer_date = date.today()
            sql = """
            UPDATE special_requests 
            SET status_of_special_request = %s, 
                approved_by = %s, 
                answer_date = %s
            WHERE request_id = %s
            """
            cursor.execute(sql, (status, approved_by, answer_date,request_id))
            connection.commit()
            
    except Exception as e:
        
        print(f"Özel talep işlenirken hata: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()


def get_employee_special_requests_history(employee_id):#ID'si verilen çalışanın talep geçmişini getirir.
    
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM special_requests 
            WHERE employee_id = %s 
            ORDER BY request_date DESC
            """
            cursor.execute(sql, (employee_id,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Özel talep geçmişi getirilirken hata: {e}")
        return str(e)
    
    finally:
        cursor.close()
        connection.close()



'''İzin talepleri için'''

def create_leave_request(employee_id, leave_type, start_date, end_date):#Çalışan id'si ile izin oluşturur


    connection = connect()
    
    try:
        # Toplam izin günü hesaplaması
        total_days = (datetime.strptime(str(end_date), '%Y-%m-%d').date() - 
                        datetime.strptime(str(start_date), '%Y-%m-%d').date()).days + 1
        
        created_at = datetime.now()
        
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO employee_leaves 
            (employee_id, request_date, leave_type, Start_date, end_date, total_dates,created_at) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                employee_id,
                date.today(), 
                leave_type, 
                start_date, 
                end_date, 
                total_days, 
                created_at
            ))
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        print(f"İzin talebi oluşturulurken hata: {e}")
        return str(e)

    finally:
        cursor.close()
        connection.close()



def get_pending_leave_requests():#Beklemede Olan tüm izinleri getirir
    
    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM employee_leaves 
            WHERE status_of_leave_asking = 'Pending'
            """
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(f"Bekleyen talepler getirilirken hata: {e}")
        return str(e)
    
    finally:
        cursor.close()
        connection.close

    


def process_leave_request(leave_request_id, status_of_leave_request, approved_by):#Yönetici izin talebini onaylar veya ret eder database'de status_of_leave_asking Enum type dikkat 
    
    connection = connect()

    try:
        with connection.cursor() as cursor:
            answer_date = date.today()
            sql = """
            UPDATE employee_leaves 
            SET status_of_leave_asking = %s, 
                approved_by = %s, 
                answer_date = %s,
            WHERE leave_request_id = %s
            """
            cursor.execute(sql, (status_of_leave_request, approved_by, answer_date,leave_request_id))
            connection.commit()
            return cursor.rowcount > 0
    except Exception as e:
        connection.rollback()
        print(f"İzin talebi işlenirken hata: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()





def get_employee_leave_history(employee_id):#ID'si verilen çalışanın izin geçmişini getirir.
    
    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM employee_leaves 
            WHERE employee_id = %s 
            ORDER BY Start_date DESC
            """
            cursor.execute(sql, (employee_id,))
            return cursor.fetchall()
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()




def calculate_employee_paid_leaves(employee_id):#ID'si verilen çalışanın tüm ücretli izinleri hesaplanır(isterseniz not in kısmını in yaparak ücretsiz izinleride bulabilirsiniz)leave_type enum database için dikkat 

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT sum(total_dates) AS sum_total 
            FROM employee_leaves 
            WHERE employee_id = %s AND leave_type NOT IN ('Ücretsiz İzin') AND status_of_leave_asking IN ('Onaylandı')
            """
            cursor.execute(sql, (employee_id,))
            result = cursor.fetchone() # bu kod Decimal('20') bu şekilde bir değer döndürür önce type sonra rakam
            if result is not None:
                employee_paid_leaves = int(result['sum_total'])
                return employee_paid_leaves
            else:
                return None
            
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()




'''Aylık tablo için'''





def create_monthly_work(employee_id, work_year, work_month, 
                        total_work_hours, total_overtime_hours, total_absence_hours,
                        Average_Hours, Number_of_Days_Off,
                        total_work_days, total_worked_days, total_half_days, 
                        attendance_percentage,paid_leave_days, notes):#Çalışan id'si ile aylık çalışma oluşturur.
    

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO monthly_work_hours 
            (employee_id, work_year, work_month, 
            total_work_hours, total_overtime_hours, total_absence_hours,
            total_work_days, total_worked_days, total_half_days, Number_of_Days_Off, 
            Average_Hours, attendance_percentage,paid_leave_days, notes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            total_work_hours = %s, 
            total_overtime_hours = %s, 
            total_absence_hours = %s,
            total_work_days = %s, 
            total_worked_days = %s, 
            total_half_days = %s, 
            Number_of_Days_Off = %s, 
            Average_Hours = %s, 
            attendance_percentage = %s,
            paid_leave_days = %s, 
            notes = %s
            """
            cursor.execute(sql, (
                employee_id,
                work_year, 
                work_month, 
                total_work_hours,
                Average_Hours,
                Number_of_Days_Off,   
                total_overtime_hours, 
                total_absence_hours,
                total_work_days, 
                total_worked_days, 
                total_half_days, 
                attendance_percentage, 
                paid_leave_days, 
                notes,
                total_work_hours,
                Average_Hours,
                Number_of_Days_Off,   
                total_overtime_hours, 
                total_absence_hours,
                total_work_days, 
                total_worked_days, 
                total_half_days, 
                attendance_percentage, 
                paid_leave_days, 
                notes,
            ))
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        return str(e)
    
    finally:
        cursor.close()
        connection.close()



def get_monthly_work(work_month):#İstenen günkü tüm çalışan verilerini getirir

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM monthly_work_hours 
            WHERE work_month = %s
            """
            cursor.execute(sql,(work_month))
            return cursor.fetchall()
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close



def get_employee_monthly_history(employee_id):#ID'si verilen çalışanın aylık çalışma geçmişini getirir.
    
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM monthly_work_hours 
            WHERE employee_id = %s 
            ORDER BY work_month DESC
            """
            cursor.execute(sql, (employee_id,))
            return cursor.fetchall()
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()




def calculate_salary(employee_id,work_month,hour_salary,overtime_salary):#Basit salary hesabı

    if isinstance(hour_salary, int) and isinstance(overtime_salary, int):

        connection = connect()

        try:
            with connection.cursor() as cursor:
                sql = """
                SELECT total_work_hours FROM monthly_work_hours 
                WHERE employee_id = %s AND  work_month = %s
                """
                cursor.execute(sql, (employee_id, work_month))
                result1 = cursor.fetchone()
                total_hour = float(result1['total_work_hours'])


                sql2 = """
                SELECT total_overtime_hours FROM monthly_work_hours 
                WHERE employee_id = %s AND  work_month = %s
                """
                cursor.execute(sql2, (employee_id, work_month))
                result = cursor.fetchone()
                total_overtime = float(result['total_overtime_hours'])

                total_hour = total_hour - total_overtime
                
                
                total_normal_time_salary = total_hour * hour_salary
                total_overtime_salary = total_overtime * overtime_salary

                total_salary = total_overtime_salary + total_normal_time_salary

                return total_salary


        except Exception as e:
            return str(e)
        
        finally:
            cursor.close()
            connection.close()
    
    else:
        return str('Lütfen Geçerli değerli giriniz')



'''Günlük Tablo için'''

def add_daily_working_hours(employee_id, work_date, attendance, clock_in_time, 
                            clock_out_time, overtime_hours, break_duration, 
                            absence_hours, work_status, Project_id, notes, day_id = None):#Çalışan id'si ile talep oluşturur

    date_format = "%Y-%m-%d %H:%M:%S" #Hazır kod aldım isterseniz değiştirirsiniz yapmanız gereken tek şey, total_work_hours parametresine dikkat etmek decimal(5,2) alıyor.
    
    date1 = datetime.strptime(clock_in_time, date_format)
    date2 = datetime.strptime(clock_out_time, date_format)


    difference = abs(date2 - date1)

    total_work_hours = float(difference.total_seconds() / 3600)

    connection = connect()
    updated_at = datetime.now()

    try:
        with connection.cursor() as cursor:
            if day_id == None:
                sql = """
                INSERT INTO daily_working_hours
                (employee_id, work_date, attendance, clock_in_time, clock_out_time, total_work_hours, overtime_hours, break_duration, absence_hours, work_status, Project_id, notes) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    employee_id,
                    work_date, 
                    attendance, 
                    clock_in_time, 
                    clock_out_time, 
                    total_work_hours, 
                    overtime_hours,
                    break_duration, 
                    absence_hours, 
                    work_status, 
                    Project_id, 
                    notes)
                )
                connection.commit()
                return cursor.lastrowid
            


            else:#Duplicate key yapmadım çünkü çakışmada direkt updatelesin istemedim
                sql = """
                UPDATE daily_working_hours
                SET employee_id = %s,
                    work_date = %s,
                    attendance = %s,
                    clock_in_time = %s,
                    clock_out_time = %s,
                    total_work_hours = %s, 
                    overtime_hours = %s, 
                    break_duration = %s,
                    absence_hours = %s,
                    work_status = %s, 
                    Project_id = %s, 
                    notes = COALESCE(%s, notes),
                    updated_at = %s 
                WHERE day_id = %s
                """
                cursor.execute(sql, (
                    employee_id,
                    work_date, 
                    attendance, 
                    clock_in_time, 
                    clock_out_time, 
                    total_work_hours, 
                    overtime_hours,
                    break_duration, 
                    absence_hours, 
                    work_status, 
                    Project_id, 
                    notes,
                    updated_at,
                    day_id)
                )
                connection.commit()
                return cursor.lastrowid


    except Exception as e:
        connection.rollback()
        return str(e)
    
    finally:
        cursor.close()
        connection.close()


def get_today_working_hours(work_date):#İstenen günkü tüm çalışan verilerini getirir

    connection = connect()

    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM daily_working_hours 
            WHERE work_date = %s
            """
            cursor.execute(sql,(work_date))
            return cursor.fetchall()
    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        connection.close()


def get_employee_working_hours_history(employee_id):#ID'si verilen çalışanın çalışma geçmişini getirir.
    
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT * FROM  daily_working_hours
            WHERE employee_id = %s 
            ORDER BY work_date DESC
            """
            cursor.execute(sql, (employee_id,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Özel talep geçmişi getirilirken hata: {e}")
        return str(e)
    
    finally:
        cursor.close()
        connection.close()




'''Günlük verileri Aylığa çeviren kod bu beni çok uğraştırdı o yüzden atladığım nokta olabilir.'''


def calculate_monthly_work_statistics(employee_id, year, month):#Bu kod günlük verileri aylığa çeviriyor ve save_monthly_analysis tarafından çağrılıyor

    connection = connect()

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Ayın toplam iş günü sayısını hesapla
            _, last_day = calendar.monthrange(year, month)
            total_workdays = last_day

            # Aylık çalışma verilerini çek
            cursor.execute("""
                SELECT 
                    work_date,
                    total_work_hours,
                    overtime_hours,
                    absence_hours,
                    work_status
                FROM daily_working_hours
                WHERE employee_id = %s 
                AND YEAR(work_date) = %s 
                AND MONTH(work_date) = %s
                ORDER BY work_date
            """, (employee_id, year, month))
            
            daily_records = cursor.fetchall()

            # İstatistikleri hesapla
            monthly_stats = {
                'total_work_hours': 0,
                'total_overtime_hours': 0,
                'total_absence_hours': 0,
                'worked_days': 0,
                'present_days': 0,
                'half_days': 0,
                'absent_days': 0,
                'average_daily_work_hours': 0,
                'attendance_percentage': 0
            }

            for record in daily_records:
                # Toplam çalışma saatleri
                monthly_stats['total_work_hours'] += float(record['total_work_hours']) or 0
                monthly_stats['total_overtime_hours'] += float(record['overtime_hours']) or 0
                monthly_stats['total_absence_hours'] += float(record['absence_hours']) or 0

                # Çalışma günü sayısı ve türü
                if record['work_status'] == 'Tam gün':
                    monthly_stats['worked_days'] += 1
                    monthly_stats['present_days'] += 1
                elif record['work_status'] == 'Yarım gün':
                    monthly_stats['worked_days'] += 0.5
                    monthly_stats['half_days'] += 1
                else:  # 'Yok' durumu
                    monthly_stats['absent_days'] += 1

            # Ortalama günlük çalışma saati
            if monthly_stats['worked_days'] > 0:
                monthly_stats['average_daily_work_hours'] = monthly_stats['total_work_hours'] / monthly_stats['worked_days']

            else:
                monthly_stats['average_daily_work_hours'] = 0

            # Katılım yüzdesi
            monthly_stats['attendance_percentage'] = (monthly_stats['worked_days'] / total_workdays) * 100

            return monthly_stats

    except Exception as e:
        print(f"Hata oluştu: {e}")
        return str(e)
    
    finally:
        cursor.close()
        connection.close()
        

def save_monthly_analysis(employee_id, year, month):#Aylık verileri günlüğe çevirip database'e kayıt ediyor

    connection = connect()

    try:
        monthly_stats = calculate_monthly_work_statistics(employee_id, year, month)
        
        if monthly_stats is None or isinstance(monthly_stats, str):
            return False
        
        else:
            with connection.cursor() as cursor:
                # Aylık analiz sonuçlarını kaydet
                cursor.execute("""
                    INSERT INTO monthly_work_hours 
                    (employee_id, work_year, work_month, 
                        total_work_hours, total_overtime_hours, total_absence_hours,
                        Number_of_Days_Off, Average_Hours,
                        total_work_days, total_worked_days, total_half_days, 
                        attendance_percentage)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        total_work_hours = %s, 
                        total_overtime_hours = %s, 
                        total_absence_hours = %s,
                        Number_of_Days_Off = %s, 
                        Average_Hours = %s, 
                        total_work_days = %s, 
                        total_worked_days = %s, 
                        total_half_days = %s,  
                        attendance_percentage = %s
                """, (
                    employee_id, year, month,
                    float(monthly_stats['total_work_hours']), 
                    float(monthly_stats['total_overtime_hours']), 
                    float(monthly_stats['total_absence_hours']),
                    int(monthly_stats['absent_days']), 
                    float(monthly_stats['average_daily_work_hours']),
                    calendar.monthrange(year, month)[1],  # Toplam iş günü
                    float(monthly_stats['worked_days']), 
                    float(monthly_stats['half_days']),
                    float(monthly_stats['attendance_percentage']),
                    # Update için aynı değerler
                    float(monthly_stats['total_work_hours']), 
                    float(monthly_stats['total_overtime_hours']), 
                    float(monthly_stats['total_absence_hours']),
                    int(monthly_stats['absent_days']), 
                    float(monthly_stats['average_daily_work_hours']),
                    calendar.monthrange(year, month)[1],  # Toplam iş günü
                    float(monthly_stats['worked_days']), 
                    float(monthly_stats['half_days']),
                    float(monthly_stats['attendance_percentage']),
                ))

                connection.commit()
                return True

    except Exception as e:
        connection.rollback()
        print(f"Kaydetme sırasında hata oluştu: {e}")
        return False
    

    finally:
        cursor.close()
        connection.close()

def special_request_status_for_employee(employee_id):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="select request_type,status_of_special_request,answer_date from special_requests where employee_id=%s"
            cursor.execute(query,(employee_id))
            records=cursor.fetchall()
            return records
    except  Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()
        

def leave_request_status_for_employee(employee_id):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            query="select leave_type,status_of_leave_asking,answer_date from employee_leaves where employee_id=%s"
            cursor.execute(query,(employee_id))
            records=cursor.fetchall()
            return records
    except  Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()
         

def update_employee(employee_id, first_name, last_name, date_of_birth, gender, job_title,
                    department, salary, hire_date, email, phone_number, password, is_active):

    connection=connect()
    try:
       with connection.cursor() as cursor:
            sql = """
            UPDATE employees
            SET first_name = %s,
                last_name = %s,
                date_of_birth = %s,
                gender = %s,
                job_title = %s,
                department = %s,
                salary = %s,
                hire_date = %s,
                email = %s,
                phone_number = %s,
                password = %s,
                is_active = %s
            WHERE employee_id = %s
            """
            cursor.execute(sql,(first_name,
                                last_name,
                                date_of_birth,
                                gender,
                                job_title,
                                department,
                                salary,
                                hire_date,
                                email,
                                phone_number,
                                password,
                                is_active,
                                employee_id))

            connection.commit()
            
           
    except Exception as e:
        print("123")
        print(str(e))
        
    finally:
            cursor.close()
            connection.close()
       


import unicodedata
import re
def arrangeText(text:str) -> str:
    text = unicodedata.normalize('NFKD', text).casefold()
    arranged =  re.sub(r'\W+', '', text).casefold()
    return arranged

def generateRandomPassword(length:int) -> str:
    from random import choice
    import string

    characters = string.ascii_letters + string.digits
    password = ''.join(choice(characters) for i in range(length))
    return password

#no need

"""
def get_infos_from_selected(selected_person:tuple): 
    employee_id=selected_person[0]
    first_name = selected_person[1]
    last_name = selected_person[2]
    date_of_birth = selected_person[3]
    gender = selected_person[4]
    job_title = selected_person[5]
    department = selected_person[6]
    salary = selected_person[7]
    hire_date = selected_person[8]
    email = selected_person[9]
    phone_number = selected_person[10]
    password = selected_person[11]
    is_active = selected_person[12]
    return employee_id,first_name,last_name,date_of_birth,gender,job_title,department,salary,hire_date,email,phone_number,password,is_active
"""
