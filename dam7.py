# Comment
try:
    numb = 10/0
    num = int(input("Enter: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

# open("files name", "type of mod"), external file, mod r, w, a, r+
Names = open("Names.txt", "r")
print(Names.readable())
print(Names.read())
print(Names.readline())
print(Names.readlines()[0])
for names in Names.readlines():
    print(names)
#Names.write("fff") mod a \n add a line
Names.close()
#import modules
