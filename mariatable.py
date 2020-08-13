import mysql.connector as mariadb

p = input()

mariadb = mariadb.connect(user='root', password=p, database="mydatabase")

cursor = mariadb.cursor()
cursor.execute("CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))")
#cursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)
