'''
import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
#sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
cursor.execute(sql)
result = cursor.fetchall()

for x in result:
  print(x)
'''

#to prevent SQL injections, escape query values
import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)

cursor.execute(sql, adr)

result = cursor.fetchall()

for x in result:
    print(x)