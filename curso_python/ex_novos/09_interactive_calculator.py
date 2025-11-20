# Exercise Description:

# This exercise is a refactored version of a basic interactive calculator written in Python.
# The goal is to create a simple command-line calculator that:

#  Accepts two numbers and a math operator
#  Validates all user inputs
#  Prevents crashes caused by invalid values
#  Performs basic operations (+, -, *, /)
#  Repeats until the user chooses to stop
#  Uses clean and readable English variables and messages

# This improved version focuses on better structure, clarity, and error handling
# while keeping the logic simple and true to my learning process.

import os

def read_number(message):
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")

def read_operator():
    valid_ops = "+-/*"
    while True:
        op = input("Enter the operator (+, -, *, /): ")
        if len(op) == 1 and op in valid_ops:
            return op
        print("Invalid operator. Please enter only one of: +, -, *, /")

while True:
    num1 = read_number("Enter the first number: ")
    operator = read_operator()
    num2 = read_number("Enter the second number: ")

    print("\nResult:")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)

    # Ask user if they want to exit
    while True:
        choice = input("\nDo you want to exit? (y/n): ").lower()
        if choice.startswith("y"):
            print("Exiting the program. Goodbye!")
            exit()
        elif choice.startswith("n"):
            os.system("cls")
            break
        else:
            print("Please enter only 'y' for yes or 'n' for no.")