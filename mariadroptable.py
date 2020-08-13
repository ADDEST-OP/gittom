import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
sql = "DROP TABLE customers"
#sql = "DROP TABLE IF EXISTS customers" #if table exists
cursor.execute(sql)