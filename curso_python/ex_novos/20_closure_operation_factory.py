# Exercise Description:

# This exercise demonstrates how closures work in Python.

# Two simple functions are defined:
# add(x, y) → returns the sum
# multiply(x, y) → returns the product

# The function create_function(func, x) creates and returns another 
# function (inner) that “remembers” the value of x, thanks to the closure mechanism.

# With this, we create:
# always adds 5 to the given value
# multiply_by_ten → always multiplies by 10

# The final print calls show the closure in action.

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def create_function(func, x):
    def inner(y):
        return func(x, y)
    return inner


add_five = create_function(add, 5)
multiply_by_ten = create_function(multiply, 10)

print(add_five(10))
print(multiply_by_ten(10))
