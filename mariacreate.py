import mysql.connector as mariadb

u = input("User:")
p = input('Password:')
mariadb = mariadb.connect(user=u, password=p)

cursor = mariadb.cursor()
cursor.execute("CREATE DATABASE mydb")
cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)