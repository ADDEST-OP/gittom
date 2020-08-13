char_name = "John"
char_age = "35"
print("Hello " + char_name + ".\nYou are " + char_age + " years old " + char_name + ".")

phrase = "I don't know it."
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("I"))
print(phrase.replace("don't", "do"))

my_num = -6
print(str(my_num) + " hello.")
print(abs(my_num))
print(pow(3, 2))
print(max(4, 6))
print(min(4, 6))
print(round(3.2))

from math import *
print(sqrt(25))
print(floor(3.4))
print(ceil(3.5))

friends = ["Kevin", "Karen", "Jim", "John"]
friends[1] = "Karen"

lucky_numbers = [1, 6, 8, 3, 6, 9, 0]
friends = ["Kevin", "Karen", "Karen", "Jim", "John"]
friends.extend(lucky_numbers)
friends.append("Greg")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.clear()
friends.pop()
friends.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends.index(3))
print(friends.count("Karen"))
print(friends[1:4])

#dictionary = "Really."
monthcon = {
    "Nov": "November"
}
print(monthcon["Nov"])
print(monthcon.get("Nov"))