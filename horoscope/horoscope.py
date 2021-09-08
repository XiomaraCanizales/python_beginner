# Create a simple horoscope program that asks the user for their star sign and outputs a fun horoscope for them.
# Bear in mind that your program should display an error message if the user types in their sign wrong.
import csv
import random

signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn',
         'aquarius', 'leo']


def read_file():
    with open('quotes.txt') as file:
        reader = csv.reader(file)
        chosen_row = random.choice(list(reader))
        return chosen_row


user_input = input('Insert your zodiac sign: ')
if user_input.lower() in signs:
    print(*read_file())
else:
    print("That sign doesn't exist")
