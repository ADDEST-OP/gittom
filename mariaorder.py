import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
#sql = "SELECT * FROM customers ORDER BY name"
sql = "SELECT * FROM customers ORDER BY name DESC"
cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)
