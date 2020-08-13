x = input("Enter table: ")

incert_culumn_name = []

sql = f"SHOW COLUMNS FROM `{x}`;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
sql = ''
sql = f"INSERT INTO `{x}` ("
userInputcolums = len(result)

x = 0
for x in range(userInputcolums):
    if x < (userInputcolums - 1):
        sql = sql + f"`{result[x][0]}`, "
    else:
        sql = sql + f"`{result[x][0]}`)"

sql = sql + " VALUES ("
x = 0
for x in range(userInputcolums - 1):
    sql = sql + "%s, "
else:
    sql = sql + "%s);"


x = 0
inputs = []
for x in range(userInputcolums):
    inputs.append(input('Enter the new data: '))

cursor.execute(sql, inputs)
mariadb.commit()


