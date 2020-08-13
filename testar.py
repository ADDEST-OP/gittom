
tableName = input("Table namn:")
tableName = "users"

userInputcolums = int(input("Hur många kollumer: "))

incert = []
# for loop för satt få in kolum namn
for x in range(userInputcolums):
    columName = input("kollum-" + str(x) + ":")
    incert.append(columName)

print("DEBUG: ", incert)

#sql = ("CREATE TABLE {} ({} VARCHAR(255), {} VARCHAR(255))").format(x, y, z)
sql = f"CREATE TABLE {tableName} ("

x = 0
for x in range(userInputcolums):
    if x < (userInputcolums - 1):
        print(x+1)
        sql = sql + f"{incert[x]} VARCHAR(255),"
    else:
        sql = sql + f"{incert[x]} VARCHAR(255));"

# cursor.execute(sql)
print(sql)
