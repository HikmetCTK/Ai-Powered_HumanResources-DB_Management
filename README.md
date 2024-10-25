SQL KOMUTLARI (değiştirdikçe eklemeleri buraya yapabilirsiniz)

alter table employees add column is_active boolean default true;

import pymysql
def connection_check():
    try:
        connection=pymysql.connect(host='mysql-3091cfbc-hikmetcatak26-d460.d.aivencloud.com',
                               user='avnadmin',
                               password="AVNS_3j_9FSqiRHqstuWvnNw",
                               database='defaultdb')
        print("connected successfully")
        return connection
    except pymysql.MySQLError as e:
        
        
        return str(e)

connection=connection_check()
