# Exercise Description:

# Create a function that returns another function (a closure).
# The outer function receives a base number, and the inner function multiplies 
# that base number by another value provided later.
# Then, test the closure by creating multiple multiplier functions and 
# printing the results in a loop.

def multiply(base_number):
    def inner(multiplier):
        result = base_number * multiplier
        return f'{base_number} X {multiplier} = {result}'
    return inner

num1 = multiply(10)
num2 = multiply(20)

for i in [2, 3, 4, 5]:
    print(num1(i))
    print(num2(i))