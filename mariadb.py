import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='toortoor', database='information_schema')

cursor = mariadb_connection.cursor()
cursor.execute("USE information_schema")
cursor.execute("SHOW TABLES")
result = cursor.fetchall()

print(result)

