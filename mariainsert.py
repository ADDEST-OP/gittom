import mysql.connector as mariadb

mariadb = mariadb.connect(user='root', password='toortoor', database='mydatabase')

cursor = mariadb.cursor()
sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
  ('154', 'Chocolate Heaven'),
  ('155', 'Tasty Lemons'),
  ('156', 'Vanilla Dreams')
]

cursor.executemany(sql, val) #for many objects, cursor.execute for one

mariadb.commit()

print(cursor.rowcount, "was inserted.")
#print("1 record inserted, ID:", mycursor.lastrowid) #to return id