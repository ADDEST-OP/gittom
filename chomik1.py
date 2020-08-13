import mysql.connector as mariadb 
import sys
import msvcrt as m
from tabulate import tabulate
import getpass
import time

count = 0
while True: # We used this loop to prompt for user credentials again and again in case those would be incorrect.
    if count == 5: # In the case the user will prompt wrong credentials 5 times
        print("\nFive Username and Password Attempts used.\nThis incident will be reported in:")
        for i in range(10, 0, -1): # the system will wait 10 secondds
            sys.stdout.write(str(i) + ' ')
            sys.stdout.flush()
            time.sleep(1)
        print("Goodbye. :)")
        sys.exit() # and exit.
    else:
        h = input("Host: ") # Otherwise you will be prompt to write in login credentials
        if h == "":
            h = "127.0.0.1"
        u = getpass.getpass(prompt="User:") # prompt were used to hide the login credentials.
        p = getpass.getpass(prompt='Password:')
        try:
            mariadb = mariadb.connect(host=h, user=u, password=p)

        except mariadb.errors.ProgrammingError: # try and except were used to manage an error so that
            print('Wrong credentials were entered. Please try again.') #the script wouldn't crash.
            count += 1
            m.getch() # This function which was called from m modul is used to make script wait for users keystroke.
            continue
        break

cursor = mariadb.cursor()

def creatdb(): # The user can by himself choose the name of the database he/she wants to create.
    db = input("Enter the name of the database you want to create: ")
    cursor.execute(f"CREATE DATABASE `{db}`")
    print("The database has been successfully created.") # and gets the acknowledge message.

def showdb(): # The user can choose to see all databases that exists in a nice psql format.
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()
    print(tabulate(result,  headers=['Database'], tablefmt='psql'))

def deldb(): # The user can delete the database
    try:
        dbd = input("Enter the database name you want to delete: ")
        cursor.execute(f"DROP DATABASE `{dbd}`")
        print("The database has been successfully deleted.")
    except Exception as e: #and in the case it doesn't exists the message will be prompted.
        print("\nThe database you are trying to delete doesn't exist.\n")
        m.getch()

def usedb(): # The user can choose to enter any database he/she wants
    try:
        udb = input("Enter database name you want to access: ")
        cursor.execute(f"USE `{udb}`")
        main()
    except Exception as e: # and in the case the user enters non existing database name,
        print("\nYou've entered the wrong database name, please try again.\n") #this message will be displayed.
        m.getch()

def mainmain():
    ans = True
    while ans: # The loop were used to make a menu with different choices for the outside the database operations.
        print("\nActions:\n1.To create database.\n2.To show databases."
              "\n3.To delete database.\n4.To access database.\n5.Exit.\n")

        ans = input("Which action you would like to perform?\n")
        if ans == "1": # and if the input will be 1 then the function to create database will be called.
            creatdb()
            m.getch()
        elif ans == "2": # and if the input will be 2 then the function to show database will be called.
            showdb()
            m.getch()
        elif ans == "3": # and if the input will be 3 then the function to delete database will be called.
            deldb()
            m.getch()
        elif ans == "4": # and if the input will be 4 then the function to use database will be called.
            usedb()
        elif ans == "5": # and if the input will be 5 then the function to exit will be called.
            mariadb.close() # This function will close the connection with server.
            sys.exit() # This function will make script exit.


def create(): # The user can create the table with any number of columns
    tableName = input("Table name: ") # The user chooses the name of the new table.

    userInputcolums = int(input("How many columns: ")) # The user chooses the number of columns he/she desire.

    incert = []  # The variable which stores the list of column names
    for x in range(userInputcolums): # for loop used to get column names
        columName = input("kollum-`" + str(x) + "`:")
        incert.append(columName)

    print("DEBUG: ", incert)

    sql = f"CREATE TABLE `{tableName}` (" # The beginning of sql query with input for tableName

    x = 0
    for x in range(userInputcolums): # for loop with range used to generate
        if x < (userInputcolums - 1): # the chosen before number of columns with chosen before names of columns
            print(x + 1)
            sql = sql + f"`{incert[x]}` VARCHAR(255),"
        else:
            sql = sql + f"`{incert[x]}` VARCHAR(255));" # with condition for the last loop to end with this string.

    cursor.execute(sql) # function used to execute the sql query

def insert():
    try:
        x = input("Enter table: ") # The user chooses any table he/she wants.
        incert_culumn_name = [] # The variable which stores the list of column names

        sql = f"SHOW COLUMNS FROM `{x}`;" # Code which shows all the columns
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        sql = ''
        sql = f"INSERT INTO `{x}` (" # starts the sql query with x as the name of the table.
        userInputcolums = len(result) # Variable that takes the length of the result from the above code.

        x = 0
        for x in range(userInputcolums): # for loop with range taken from the length of the columns in table
            if x < (userInputcolums - 1):
                sql = sql + f"`{result[x][0]}`, " # adds table column names to a query in loop
            else:
                sql = sql + f"`{result[x][0]}`)" # with condition for the ending loop to end with this string.

        sql = sql + " VALUES (" # adds values part to a query
        x = 0
        for x in range(userInputcolums - 1): # for loop with range taken from the length of the columns in table
            sql = sql + "%s, " # adds new value to a query in loop
        else:
            sql = sql + "%s);" # with condition for the ending loop to end with this string.

        x = 0
        inputs = [] # Variable that is a list of user inputs
        for x in range(userInputcolums):  # for loop with range taken from the length of the columns in table
            inputs.append(input('Enter the new data: ')) # The user appends new data

        cursor.execute(sql, inputs) # sql query is executed
        mariadb.commit() # This function makes sure that the data were saved

        ans = True
        while ans: # while loop which gives options to repeat the above code or exit to menu or to exit different menu
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
    while ans: # This is smaller menu which was made to manage different data operation
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

def showt(): # The user can choose to se the tables
    cursor.execute("SHOW TABLES")
    result = cursor.fetchall()
    print(tabulate(result, headers=['Tables'], tablefmt='psql'))

def showc(): # The user can choose to see columns from any chosen table
    try:
        y = input("From table: ")
        cursor.execute(f"SHOW COLUMNS FROM `{y}`")
        result = cursor.fetchall()
        print(tabulate(result, headers=['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'], tablefmt='psql'))
    except Exception as e:
        print("The table name you want to see doesn't exist.")
        m.getch()
        main()

def addc(): # The user can add one column to any chosen table
    try:
        table = input("Select table: ")
        col = input("New column: ")
        cursor.execute(f"ALTER TABLE `{table}` ADD COLUMN `{col}` VARCHAR(255)")
        print("Column has been added.")
    except Exception as e:
        print("Something went wrong, the column could not been added.")
        m.getch()
        main()

def dropt(): #The user can delete any chosen table
    try:
        dt = input("Enter table you want to delete: ")
        cursor.execute(f"DROP TABLE `{dt}`")
        print("Table has been successfully deleted.")
    except Exception as e:
        print("The table you've entered doesn't exist.")
        m.getch()
        main()

def dropc(): # The user can delete any chosen column
    try:
        table = input("Select table: ")
        col = input("Column you want to delete: ")
        cursor.execute(f"ALTER TABLE `{table}` DROP COLUMN `{col}`")
        print("Column has been deleted.")
    except Exception as e:
        print("Ether table or column you've enter doesn't exist.")

def sel(): # The user can select to see any chosen data from tables
    try:
        sel1 = input("What you want to select: ")
        sel2 = input("Where you want to select it from: ")
        cursor.execute(f"SELECT {sel1} FROM {sel2}")
        result = cursor.fetchall()
        print(tabulate(result, tablefmt='psql'))
    except Exception as e:
        print("Something doesn't match.")

def where(): # The user can select to see any chosen data from tables
     try:
         whe1 = input("What you want to select: ")
         whe2 = input("Where you want to select it from: ")
         whe3 = input("Column: ")
         sql = f"SELECT {whe1} FROM {whe2} WHERE {whe3} = %s" #and those data will be filtered based on a chosen condition
         adr = (input("Filtered by: "),)

         cursor.execute(sql, adr)
         result = cursor.fetchall()
         print(tabulate(result, tablefmt='psql'))
     except Exception as e:
         print("Something doesn't match.")

def orderby(): # The user can select to see any chosen data from tables
     try:
         sel = input("Select: ")
         cus = input("From: ")
         na = input("By column: ")
         sql = f"SELECT {sel} FROM {cus} ORDER BY {na}" # and those data will be ordered by a condition
         cursor.execute(sql)
         result = cursor.fetchall()
         print(tabulate(result, tablefmt='psql'))
     except Exception as e:
         print("Something is wrong.")

def update(): # The user can change a data in a column/updates data in column
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

def deldata(): # The user can delete data from any chosen column in any chosen table
     try:
         co = input("From table: ")
         cu = input("From column: ")
         sql = f"DELETE FROM `{co}` WHERE `{cu}` = %s"
         ans = True
         while ans: # while loop with option to delete more data in the same table and same column
             ans = input("Do you want to remove more data? yes/no/maybe\n") #exit to menu or exit to a different menu
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

def join():  # The user can join two different columns from two diffrente tables based on the two different columns
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
    while ans: # The menu with the choices for the inside database operations
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
            mainmain() # function used to get back into the outside database menu
        elif ans == "16":
            mariadb.close()
            sys.exit()

if __name__ == '__main__': # if statment that check if the module has been imported or not
    mainmain() #and if it's not imported then it's calling the function mainmain()
                #which send us to the outside database menu
