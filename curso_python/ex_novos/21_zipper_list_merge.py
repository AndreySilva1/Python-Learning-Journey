# Exercise Description:

# -Merge lists
# Create a function called zipper (like a clothes zipper)
# The job of this function is to merge two lists
# in order, pairing their elements.
# Use all values from the shortest list.
#
# Example:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
#
# Result:
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(x, y):
    result = []
    for a, b in zip(x, y):
        result.append((a, b))
    return result

print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'],
             ['BA', 'SP', 'MG', 'RJ']))


