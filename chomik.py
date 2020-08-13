import mysql.connector as mariadb
import sys
import msvcrt as m
from tabulate import tabulate
import getpass
import time

count = 0
while True:
    if count == 5:
        print("\nFive Username and Password Attempts used.\nThis incident will be reported in:")
        for i in range(10, 0, -1):
            sys.stdout.write(str(i) + ' ')
            sys.stdout.flush()
            time.sleep(1)
        print("Goodbye. :)")
        sys.exit()
    else:
        h = input("Host: ")
        if h == "":
            h = "127.0.0.1"
        u = getpass.getpass(prompt="User:")
        p = getpass.getpass(prompt='Password:')
        try:
            mariadb = mariadb.connect(host=h, user=u, password=p)

        except mariadb.errors.ProgrammingError:
            print('Wrong credentials were entered. Please try again.')
            count += 1
            m.getch()
            continue
        break

cursor = mariadb.cursor()

def creatdb():
    db = input("Enter the name of the database you want to create: ")
    cursor.execute(f"CREATE DATABASE `{db}`")
    print("The database has been successfully created.")

def showdb():
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()
    print(tabulate(result,  headers=['Database'], tablefmt='psql'))

def deldb():
    try:
        dbd = input("Enter the database name you want to delete: ")
        cursor.execute(f"DROP DATABASE `{dbd}`")
        print("The database has been successfully deleted.")
    except Exception as e:
        print("\nThe database you are trying to delete doesn't exist.\n")
        m.getch()

def usedb():
    try:
        udb = input("Enter database name you want to access: ")
        cursor.execute(f"USE `{udb}`")
        main()
    except Exception as e:
        print("\nYou've entered the wrong database name, please try again.\n")
        m.getch()

def mainmain():
    ans = True
    while ans:
        print("\nActions:\n1.To create database.\n2.To show databases."
              "\n3.To delete database.\n4.To access database.\n5.Exit.\n")

        ans = input("Which action you would like to perform?\n")
        if ans == "1":
            creatdb()
            m.getch()
        elif ans == "2":
            showdb()
            m.getch()
        elif ans == "3":
            deldb()
            m.getch()
        elif ans == "4":
            usedb()
        elif ans == "5":
            mariadb.close()
            sys.exit()


def create():
    tableName = input("Table name: ")

    userInputcolums = int(input("How many columns: "))

    incert = []
    # for loop för satt få in kolum namn
    for x in range(userInputcolums):
        columName = input("kollum-`" + str(x) + "`:")
        incert.append(columName)

    print("DEBUG: ", incert)

    # sql = ("CREATE TABLE {} ({} VARCHAR(255), {} VARCHAR(255))").format(x, y, z)
    sql = f"CREATE TABLE `{tableName}` ("

    x = 0
    for x in range(userInputcolums):
        if x < (userInputcolums - 1):
            print(x + 1)
            sql = sql + f"`{incert[x]}` VARCHAR(255),"
        else:
            sql = sql + f"`{incert[x]}` VARCHAR(255));"

    cursor.execute(sql)

def insert():
    try:
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

        ans = True
        while ans:
            ans = input("Do you want to add more data into a table? yes/no/maybe\n")
            if ans.lower() == 'yes':
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

            elif ans.lower() == 'no':
                main()
            elif ans.lower() == 'maybe':
                new_insert()
    except Exception as e:
        print("Something went wrong, the data has not been inserted.")
        m.getch()
        main()

def new_insert():
    ans = True
    while ans:
        print("\nActions:\n1.To see tables.\n2.To see columns.\n3.To delete data from table."
              "\n4.To insert data into table.\n5.To return to menu.\n6.To exit.\n")

        ans = input("Which action would you like to perform?\n")
        if ans == "1":
            showt()
            m.getch()
        elif ans == "2":
            showc()
            m.getch()
        elif ans == "3":
            deldata()
            m.getch()
        elif ans == "4":
            insert()
            m.getch()
        elif ans == "5":
            main()
        elif ans == "6":
            mariadb.close()
            sys.exit()

def showt():
    cursor.execute("SHOW TABLES")
    result = cursor.fetchall()
    print(tabulate(result, headers=['Tables'], tablefmt='psql'))

def showc():
    try:
        y = input("From table: ")
        cursor.execute(f"SHOW COLUMNS FROM `{y}`")
        result = cursor.fetchall()
        print(tabulate(result, headers=['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'], tablefmt='psql'))
    except Exception as e:
        print("The table name you want to see doesn't exist.")
        m.getch()
        main()

def addc():
    try:
        table = input("Select table: ")
        col = input("New column: ")
        cursor.execute(f"ALTER TABLE `{table}` ADD COLUMN `{col}` VARCHAR(255)")
        print("Column has been added.")
    except Exception as e:
        print("Something went wrong, the column could not been added.")
        m.getch()
        main()

def dropt():
    try:
        dt = input("Enter table you want to delete: ")
        cursor.execute(f"DROP TABLE `{dt}`")
        print("Table has been successfully deleted.")
    except Exception as e:
        print("The table you've entered doesn't exist.")
        m.getch()
        main()

def dropc():
    try:
        table = input("Select table: ")
        col = input("Column you want to delete: ")
        cursor.execute(f"ALTER TABLE `{table}` DROP COLUMN `{col}`")
        print("Column has been deleted.")
    except Exception as e:
        print("Ether table or column you've enter doesn't exist.")

def sel():
    try:
        sel1 = input("What you want to select: ")
        sel2 = input("Where you want to select it from: ")
        cursor.execute(f"SELECT {sel1} FROM {sel2}")
        result = cursor.fetchall()
        print(tabulate(result, tablefmt='psql'))
    except Exception as e:
        print("Something doesn't match.")

def where():
     try:
         whe1 = input("What you want to select: ")
         whe2 = input("Where you want to select it from: ")
         whe3 = input("Column: ")
         sql = f"SELECT {whe1} FROM {whe2} WHERE {whe3} = %s"
         adr = (input("Filtered by: "),)

         cursor.execute(sql, adr)
         result = cursor.fetchall()
         print(tabulate(result, tablefmt='psql'))
     except Exception as e:
         print("Something doesn't match.")

def orderby():
     try:
         sel = input("Select: ")
         cus = input("From: ")
         na = input("By column: ")
         sql = f"SELECT {sel} FROM {cus} ORDER BY {na}"
         cursor.execute(sql)
         result = cursor.fetchall()
         print(tabulate(result, tablefmt='psql'))
     except Exception as e:
         print("Something is wrong.")

def update():
     try:
         tabe = input("Tabel you want to update: ")
         add = input("Column you want to change data in: ")
         sql = f"UPDATE `{tabe}` SET `{add}` = %s WHERE `{add}` = %s"
         val1 = input("New input: ")
         val2 = input("Old input: ")
         val = (val1, val2)

         cursor.execute(sql, val)
         mariadb.commit()
         print(cursor.rowcount, "record(s) affected")
     except Exception as e:
         print("The data did not been updated due to incorrect input.")

def deldata():
     try:
         co = input("From table: ")
         cu = input("From column: ")
         sql = f"DELETE FROM `{co}` WHERE `{cu}` = %s"
         ans = True
         while ans:
             ans = input("Do you want to remove more data? yes/no/maybe\n")
             if ans == 'yes':
                 adr = (input("What: "),)
                 cursor.execute(sql, adr)
                 mariadb.commit()
                 print(cursor.rowcount, "record(s) deleted")
             elif ans == 'no':
                 main()
             elif ans == 'maybe':
                 new_insert()
     except Exception as e:
         print("Something doesn't work.")

def join():
     try:
         one = input("First column: ")
         two = input("Second column: ")
         ta = input("Table: ")
         ta1 = input("Table: ")
         te = input("Based on: ")
         te1 = input("Based on: ")
         sql = f"SELECT \
                {one} AS user, \
                {two} AS favorite \
                FROM {ta} \
                INNER JOIN {ta1} ON {te} = {te1}"

         cursor.execute(sql)
         result = cursor.fetchall()
         print(tabulate(result, tablefmt='psql'))
     except Exception as e:
         print("IT, doesn't working.")

def main():
    ans = True
    while ans:
        print("\nActions:\n1.To create tables.\n2.To insert data into tables.\n3.To insert data with options."
              "\n4.To see tables.\n5.To see columns.\n6.To add column.\n7.To delete table.\n8.To delete column."
              "\n9.Select data.\n10.Select with filter.\n11.To delete data from tables.\n12.Order by.\n13.Update."
              "\n14.Join.\n15.Return to Main menu.\n16.Exit.\n")

        ans = input("Which action would you like to perform?\n")
        if ans == "1":
            create()
            m.getch()
        elif ans == "2":
            insert()
            m.getch()
        elif ans == "3":
            new_insert()
            m.getch()
        elif ans == "4":
            showt()
            m.getch()
        elif ans == "5":
            showc()
            m.getch()
        elif ans == "6":
            addc()
            m.getch()
        elif ans == "7":
            dropt()
            m.getch()
        elif ans == "8":
            dropc()
            m.getch()
        elif ans == "9":
            sel()
            m.getch()
        elif ans == "10":
            where()
            m.getch()
        elif ans == "11":
            deldata()
            m.getch()
        elif ans == "12":
            orderby()
            m.getch()
        elif ans == "13":
            update()
            m.getch()
        elif ans == "14":
            join()
            m.getch()
        elif ans == "15":
            mainmain()
        elif ans == "16":
            mariadb.close()
            sys.exit()

if __name__ == '__main__':
    mainmain()
