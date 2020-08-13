import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
cursor.execute("SELECT * FROM customers")
#cursor.execute("SELECT name, address FROM customers")
result = cursor.fetchall() #result = mycursor.fetchone() returns first raw

for x in result:
  print(x)