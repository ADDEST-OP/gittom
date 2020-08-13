import mysql.connector as mariadb

h = input("Host: ")
u = input("User: ")
p = input("Password: ")
d = input("Database: ")
table = input("Enter the name of the table you want to create: ")
col1 = input("Enter the name of the first column: ")
col2 = input("Enter the name of the second column: ")

mariadb = mariadb.connect(host=h, user=u, password=p, database=d)

cursor = mariadb.cursor()


cursor.execute(f"CREATE TABLE {table} ({col1} VARCHAR(255), {col2} VARCHAR(255))")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

