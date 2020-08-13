import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
#cursor.execute("SELECT * FROM customers LIMIT 5")
cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
result = cursor.fetchall()

for x in result:
  print(x)