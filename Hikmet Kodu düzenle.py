def update_employee(employee_id,first_name,last_name,date_of_birth,gender,job_title,department,salary,hire_date,email,phone_number,password,is_activate):

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
                is_activate = %s
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
                                is_activate,
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
                password,is_activate
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
                is_activate =user['is_activate']
                return (first_name,last_name,date_of_birth,
                    gender,job_title,
                    department,salary,hire_date,
                    email,phone_number,
                    password,is_activate)
            else:
                return str('Dönüştürme Hatası')
            
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        connection.close()
