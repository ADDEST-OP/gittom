import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
#cursor.execute("SELECT * FROM customers LIMIT 5")
cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
result = cursor.fetchall()

for x in result:
  print(x)
