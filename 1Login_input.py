import mysql.connector as mariadb

h = input("Host: ")
u = input("User: ")
p = input("Password: ")
d = input("Database: ")

mariadb = mariadb.connect(host=h, user=u, password=p, database=d)

cursor = mariadb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

