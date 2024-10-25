import pymysql
import smtplib
import random
def connection_check():
    try:
        connection=pymysql.connect(host='localhost',
                               user='root',
                               password="sql5858",
                               database='human_resources')
        print("connected successfully")
        return connection
    except pymysql.MySQLError as e:
        
        
        return str(e)

connection=connection_check()




#  email and password for testing
# email=123@gmail.com 
# password=123

def login(email,password):
    connection=connection_check()
    print(connection)
    try:
        with connection.cursor() as cursor:
            query="select * from employees where email=%s and password=%s"
            cursor.execute(query,(email,password))
            record=cursor.fetchone()
            print(record)
            if record:
                role=record[5]
                if role=='Human Resources':
                    manager_side=True
                    return True
                else:
                    worker_side=True
                #print(record)
                #print('Login successfull')
                #print("loading interface...")
                return True
            else:
                #print('Login failed')
                return False
    except pymysql.MySQLError as e:
        return str(e)

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
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        
        subject = "Your Password Reset Code"
        body = f"Your verification code is {verification_code}."
        msg = f"Subject: {subject}\n\n{body}"
        
        
        smtp.sendmail(sender_email,user_email,msg)
    
    return verification_code

def reset_change_password(new_password, entered_code, verification_code, user_email):
    if entered_code == verification_code:
        connection = connection_check()  # Assuming this function checks connection
        cursor = connection.cursor()
        

        update_query = "UPDATE employees SET password = %s WHERE email = %s"
        
        cursor.execute(update_query, (new_password, user_email))
        
        connection.commit()
        #print("Password changed successfully")
        return True
    else:
        #print("Invalid verification code.")
        return False
    

def hiring(name,surname,birth,gender,job_title,derpatment,salary,hire_date,email,phone_no,password):
    connection=connection_check()
    cursor=connection.cursor()
    query="""insert into employees(first_name, last_name, date_of_birth, gender, job_title, department, salary, hire_date, email, phone_number, password) values 
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=name,surname,birth,gender,job_title,derpatment,salary,hire_date,email,phone_no,password
    try:

        cursor.execute(query,values)
        cursor.commit()
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()

#verification_code = send_verification_code()

#entered_code = int(input("Enter verification code: "))
#new_password = input("Enter new password: ")


#reset_change_password(new_password, entered_code, verification_code, user_email)
