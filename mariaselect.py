import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
cursor.execute("SELECT * FROM customers")
#cursor.execute("SELECT name, address FROM customers")
result = cursor.fetchall() #result = mycursor.fetchone() returns first raw

for x in result:
  print(x)
