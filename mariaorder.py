import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
#sql = "SELECT * FROM customers ORDER BY name"
sql = "SELECT * FROM customers ORDER BY name DESC"
cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)