'''       
def update_employee(employee_id,first_name,last_name,date_of_birth,gender,job_title,department,salary,hire_date,email,phone_number,password,is_active):

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




#x = update_employee(
    employee_id=1005,
    first_name="Can",
    last_name="Öztürk",
    date_of_birth="1993-07-30",
    gender="Erkek",
    job_title="Pazarlama Müdürü",
    department="Pazarlama",
    salary=80000.50,
    hire_date="2016-11-12",
    email="can.ozturk@sirket.com",
    phone_number="5557419630",
    password="pazarlamaSifre567$",
    is_active=1
)

'''        
