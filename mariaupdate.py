'''
import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
cursor.execute(sql)
mariadb.commit()

print(cursor.rowcount, "record(s) affected")
'''

#Escaping query value
import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

cursor.execute(sql, val)
mariadb.commit()

print(cursor.rowcount, "record(s) affected")