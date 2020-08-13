import mysql.connector as mariadb

h = input("Host: ")
u = input("User: ")
p = input("Password: ")
d = input("Database: ")

mariadb = mariadb.connect(host=h, user=u, password=p, database=d)
cursor = mariadb.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

table = input("To which table you want to insert data into? ")
cursor.execute(f"SHOW COLUMNS FROM `{table}`")

for x in cursor:
  print(x)

col1 = input("Column name: ")
col2 = input("Column name: ")
sql = f"INSERT INTO `{table}` (`{col1}`, `{col2}`) VALUES (%s, %s)"
val = (input("New data: "), input("New data: "))


cursor.execute(sql, val)
mariadb.commit()
print(cursor.rowcount, "was inserted.")

cursor.execute(f"SELECT * FROM `{table}`")

for x in cursor:
  print(x)


