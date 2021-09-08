# Write a small Python program that asks the user for a number and tells them if it is odd or even

x = "y"
while x == "y":
    number = int(input("Insert a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    x = input("play again? y/n: ")
