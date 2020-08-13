sect = "Bunny"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != sect and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")



for letter in "Catty Cat":
    print(letter)
for index in range(10):
    print(index)
friends = ["John", "Katty", "Karen"]
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print("nn")
    else:
        print("Not")

def trans(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(trans(input("Enter a phrase: ")))