# Making a user guess a number. It should generate a random number between.
# Should the user guess wrong, the program should respond by telling them their guess is either too low or too high.
# When the user guesses right, your program should ask them if they want to play again.
# For a little added challenge, you can limit the number of guesses to 5, for example.
import random

random_number = random.randint(1, 10)
guess_number = int(input("Guess the number: "))
lives = 5

while guess_number != random_number and lives > 1:
    if guess_number >= random_number:
        print("Too high")
    else:
        print("Too low")
    lives -= 1
    print(f"You have " + str(lives) + " lives")
    guess_number = int(input("Try again: "))

if guess_number == random_number:
    print("You guessed it!!!")
else:
    print(f"You didn't guess! The number was: " + str(random_number))
