import mysql.connector as mariadb #Importerar en modul mysql och ger den allias mariadb.

#Variabel 'mariadb' som kommer ansluta sig mot sql databasen
# loga in med root access och få tillgång till mydatabase.

p = input()

mariadb = mariadb.connect(user='root', password=p, database='mydatabase')

#Exekverar sql commandos inom databas session.
cursor = mariadb.cursor()

#Variabel som hämtar från databasen från två tabeler som kallas users och products kolumner som kallas namn
#(users.name, products.name) och kombinerar/joinar de ihop baserad
# på deras id nummret och fav nummret(users.fav = product.id). Allt inom sql variabel är en sql commando.
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"  # LEFT JOIN and RIGHT JOIN works as well

cursor.execute(sql)  #Den exekverar sql variabel som är ovan.
result = cursor.fetchall() #Hämtar alla rader från databasen som en lista av tuples.

for x in result:   #En loop som listar ut resultatet på skärmet.
  print(x)                    #Damian Holiczko
