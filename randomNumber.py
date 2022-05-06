import random

print("Number Guessing Game")

number = random.randint(1,9)

chances = 0

print("Guess a number between 1 and 9: ")

while chances <5:

    guess = int(input("enter your guess: "))

    if guess == number:
        print("Congrats! you WON!!")
        break
    elif guess< number:
        print("Your Guess was too low: Guess a number higher than", guess)
    else:
        print("your guess is too high: guess a number lower than", guess)

    chances += 1


if not chances <5:
    print("You LOST!! The number is ", number)