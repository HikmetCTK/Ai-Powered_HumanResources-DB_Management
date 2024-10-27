import pymysql
import sys

def update_employee_salary(employee_id, new_salary):
    try:
        # Veritabanı bağlantısı
        connection = pymysql.connect(
            host='localhost',          
            user='root',      
            password='1215173,',  
            database='dump',  
        )
        
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE employees SET salary = %s WHERE employee_id = %s"
                

                cursor.execute(sql, (new_salary, emp_id))
                

                connection.commit()



                if cursor.rowcount > 0:
                    print(f"employee_ID {emp_id} olan çalışanın maaşı {new_salary} olarak güncellendi.")
                else:
                    print(f"employee_ID {emp_id} olan çalışan bulunamadı.")
                    
        finally:
            connection.close()
            
    except pymysql.Error as e:
        print(f"Hata oluştu: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        Asg_ucret = int(17500)
        print("\n=== Çalışan Maaş Güncelleme Sistemi ===")
        emp_id = int(input("Çalışan ID'sini girin: "))
        new_salary = int(input("Yeni maaş miktarını girin: "))
        
        if new_salary >= int(Asg_ucret):
            update_employee_salary(emp_id, new_salary)
        
        else:
             print('Maaş miktarı asgari ücretten düşük olamaz')
            

    except ValueError:
        print("Lütfen geçerli bir ID ve maaş değeri girin!")