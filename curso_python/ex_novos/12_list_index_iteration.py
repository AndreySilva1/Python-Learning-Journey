# Exercise Description:

# This exercise practices iterating over a list using indices 
# instead of a direct for element in list.
# The goal is to understand:

# How range(len(list)) works
# How to access elements by index
# The difference between iterating over values vs. iterating over indices
# How Python treats each element's type

names = ['Maria', 'Helena', 'Luiz']

indexes = range(len(names))

for i in indexes:
    print(i, names[i], type(names[i]))
