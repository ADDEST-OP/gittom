'''
import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
cursor.execute(sql)
mariadb.commit()

print(cursor.rowcount, "record(s) deleted")
'''

#Escaping query value
import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

cursor = mariadb.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

cursor.execute(sql, adr)
mariadb.commit()

print(cursor.rowcount, "record(s) deleted")
