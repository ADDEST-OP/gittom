import mysql.connector as mariadb

p = input("Password: ")

mariadb_connection = mariadb.connect(user='root', password=p, database='information_schema')

cursor = mariadb_connection.cursor()
cursor.execute("USE information_schema")
cursor.execute("SHOW TABLES")
result = cursor.fetchall()

print(result)
