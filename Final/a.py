from typing import Optional
def connect():
    try:
        connection=pymysql.connect(host='localhost',
                               user='root',
                               password="sql5858",
                               database='human_resources')
        return connection
    except pymysql.MySQLError as e:
        return str(e)

def execute_search(cursor, sql: str, first_name: Optional[str], last_name: Optional[str]):
   
    conditions = []
    params = []
    
    if first_name:
        conditions.append["AND e.first_name LIKE %s"]
        params.append(f"%{first_name}%")
    else:
        conditions.append[""]
        
    if last_name:
        conditions[ "AND e.last_name LIKE %s"]
        params.append(f"%{last_name}%")
    else:
        conditions.append[""]
    formatted_sql = sql.format(**conditions)
    cursor.execute(formatted_sql, params)
    return cursor.fetchall()
from typing import Optional
def search_special_requests(first_name: Optional[str] = None, last_name: Optional[str] = None):
    try:
        connection= connect()
        cursor = connection.cursor()
        
        sql = """
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            e.department,
            e.job_title,
            sr.request_id,
            sr.request_type,
            sr.request_amount,
            sr.request_date,
            sr.status_of_request,
            sr.approved_by,
            sr.description,
            sr.answer_date
        FROM 
            employees e
            INNER JOIN special_requests sr ON e.employee_id = sr.employee_id
        WHERE 
            1=1
            {first_name_condition}
            {last_name_condition}
        ORDER BY 
            sr.request_date DESC
        """
        
        return execute_search(cursor, sql, first_name, last_name)
        
    except Exception as e:
        print(f"Arama sırasında hata oluştu: {str(e)}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
import pymysql
search_special_requests(first_name="b",)
