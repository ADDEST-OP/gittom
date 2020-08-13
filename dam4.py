name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + ".")
num1 = input("Enter a number: ")
num2 = input("Enter another: ")
result = float(num1) + float(num2)
print(result)

#tuple = "Cannot be modify ()"
coordinates = (4, 5)
print(coordinates[0:3])

def say_hi(name, age):
    print("Hello " + name + ". You are " + age)
say_hi("Kevin", "40")

def cube(num1):
    return num1*num1*num1
print(cube(3))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(300, 26, 60))

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are a tall female.")
else:
    print("You are a short female.")