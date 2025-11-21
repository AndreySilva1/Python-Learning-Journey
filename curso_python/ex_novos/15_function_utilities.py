# Exercise Description:

# This script contains two simple utility functions:

# mult(*args):
# Receives any number of numeric arguments and returns the product of all values.

# even_or_odd(number):
# Receives a number and prints whether it is even or odd.

# Both functions help practice function creation, argument unpacking (*args), 
# loops, conditionals, and return values.

def mult(*args):
    total = 1
    for value in args:
        total *= value
    return total

multiplication = mult(1, 2, 3, 4, 5)
print(multiplication)


def even_or_odd(number):
    if number % 2 == 0:
        print(f'The number {number} is even!')
    else:
        print(f'The number {number} is odd!')

even_or_odd(26)
