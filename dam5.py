i = 1
while i <= 10:
    print(i)
    i += 1
print("Done.")

num1 = float(input("Enter number 1: "))
op = input("Enter operator: ")
num2 = float(input("Enter number 2: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator.")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 2))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(col)
