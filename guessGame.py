import random

number = random.randint(0, 10)

guess = int(input("I'm thinking of a number between zero and ten. Can you guess it?"))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope. Try again: "))

print("You guessed it. I was thinlking about", number)
