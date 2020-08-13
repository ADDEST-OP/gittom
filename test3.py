x = "users"


sql = f"INSERT INTO {x} ("

incert_culumn_name = []

incert_culumn_name.append("Kalle")
incert_culumn_name.append("Nalle")
incert_culumn_name.append("Pelle")
incert_culumn_name.append("Valle")
incert_culumn_name.append("Talle")

userInputcolums = len(incert_culumn_name)

x = 0
for x in range(userInputcolums):
    if x < (userInputcolums - 1):
        print(x + 1)
        sql = sql + f"{incert_culumn_name[x]}, "
    else:
        sql = sql + f"{incert_culumn_name[x]})"

sql = sql + " VALUES ("
x = 0
for x in range(userInputcolums - 1):
    sql = sql + "%s, "
else:
    sql = sql + "%s);"

print(sql)