# Exercise Description:

# -Sum two lists
# Given two lists of integers or floats (list_a and list_b),
# create a new list where each element is the sum of the
# corresponding elements from both lists.
#
# The summation must only consider the size of the shortest list.
# If one list is longer, the extra elements must be ignored.
#
# Example:
# list_a = [1, 2, 3, 4, 5, 6, 7]
# list_b = [1, 2, 3, 4]
# Output: [2, 4, 6, 8]

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

min_size = len(list_b)
result = []

for i in range(min_size):
    result.append(list_a[i] + list_b[i])

print(result)

# Alternative using enumerate
result = []
for index, _ in enumerate(list_b):
    result.append(list_a[index] + list_b[index])
print(result)

# Alternative using list comprehension
result = [x + y for x, y in zip(list_a, list_b)]
print(result)

# Bonus: sum using the longest list, filling missing values with 0
from itertools import zip_longest

list_a = [10, 2, 3, 4, 5]
list_b = [12, 2, 3, 6, 50, 60, 70]

result = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(result)
