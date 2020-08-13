import mysql.connector as mariadb

h = input("Host: ")
u = input("User: ")
p = input("Password: ")
d = input("Database: ")

mariadb = mariadb.connect(host=h, user=u, password=p, database=d)

cursor = mariadb.cursor()
cursor.execute(f"SHOW TABLES")

for x in cursor:
  print(x)

table = input("To which table you would like to add a column: ")
col = input("Enter new column name: ")

cursor.execute(f"ALTER TABLE `{table}` ADD COLUMN `{col}` VARCHAR(255);")

cursor.execute(f"SHOW COLUMNS FROM `{table}`")

for x in cursor:
  print(x)

