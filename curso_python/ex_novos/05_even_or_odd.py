# Exercise Description:
# Create a program that asks the user to enter an integer.
# Your program should:

# Convert the input to an integer using int().
# Check whether the number is even or odd using the modulo operator (%).
# If the conversion fails (the user enters something that is not an integer), show an error message using try/except.

try:
    integer_number = int(input("Enter an integer number: "))

    if integer_number % 2 == 0:
        print("The number you entered is even!")
    else:
        print("The number you entered is odd!")
except:
    print("The value you entered is not an integer!")

