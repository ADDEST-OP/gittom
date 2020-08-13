import mysql.connector as mariadb
from tabulate import tabulate

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')
cursor = mariadb.cursor()

sel = input("Select: ")
cus = input("From: ")
na = input("By column: ")
sql = f"SELECT `{sel}` FROM `{cus}` ORDER BY `{na}`" # and those data will be ordered by a condition
cursor.execute(sql)
result = cursor.fetchall()
print(tabulate(result, tablefmt='psql'))