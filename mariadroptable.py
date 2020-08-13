import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
sql = "DROP TABLE customers"
#sql = "DROP TABLE IF EXISTS customers" #if table exists
cursor.execute(sql)
