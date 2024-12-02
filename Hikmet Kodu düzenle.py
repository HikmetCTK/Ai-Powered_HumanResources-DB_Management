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
a=(4,
 'Sibylle',
 'Houtby',
 datetime.date(1965, 11, 12),
 'Female',
 'Senior Cost Accountant',
 'IT',
 Decimal('70327.65'),
 datetime.date(2017, 9, 24),
 'shoutby3@slate.com',
 '773-887-2470',
 '409_8`',
 1)
selected=a
employee_id,first_name,last_name,date_of_birth,gender,job_title,department,salary,hire_date,email,phone_number,password,is_active=get_infos_from_selected(selected) # listeden seçilen elemanı bu fonksiyona bağlamadan alttaki update çalışmaz !!!!!!
"""

def update_employee(
employee_id=employee_id,
first_name=first_name,
last_name=last_name,
date_of_birth=date_of_birth,
gender=gender,
job_title=job_title,
department=department,
salary=salary,
hire_date=hire_date,
email=email,
phone_number=phone_number,
password=password,
is_active=is_active):

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
            return cursor.lastrowid

            
    except Exception as e:
        connection.rollback()
        return str(e)

    finally:
            cursor.close()
            connection.close()
       




def get_important_infos(employee_id):
    connection=connect()
    try:
       with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT first_name,last_name,date_of_birth,
                gender,job_title,
                department,salary,hire_date,
                email,phone_number,
                password,is_active
                FROM employees
                WHERE employee_id = %s
            """
            cursor.execute(sql,(employee_id))
            user = cursor.fetchone()
            if user != None:
                first_name = user['first_name']
                last_name = user['last_name']
                date_of_birth = user['date_of_birth']
                gender = user['gender']
                job_title = user['job_title']
                department = user['department']
                salary = float(user['salary'])
                hire_date = user['hire_date']
                email = user['email']
                phone_number = user['phone_number']
                password = user['password']
                is_active =user['is_active']
                return (first_name,last_name,date_of_birth,
                    gender,job_title,
                    department,salary,hire_date,
                    email,phone_number,
                    password,is_active)
            else:
                return str('Dönüştürme Hatası')
            
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()
