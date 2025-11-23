# Exercise Description:

# This program analyzes multiple lists of integers and identifies the 
# first duplicated number in each one.
# A duplicated number is considered “first” based on which value repeats 
# with the earliest second appearance, not simply the first repeated value found.

# The program works in three steps:

# first_duplicate()
# Scans a list and detects the first number that appears twice using a tracking dictionary.

# process_lists()
# Iterates through several lists and prints the result for each one.

# Runs with example lists
# The sample variable list_of_integer_lists contains multiple lists to test.

def first_duplicate(numbers):
    seen = {}
    duplicate = -1
    lowest_second_index = float('inf')

    for index, number in enumerate(numbers):
        if number in seen:
            if index < lowest_second_index:
                lowest_second_index = index
                duplicate = number
        else:
            seen[number] = index

    return duplicate


def process_lists(list_of_lists):
    for i, numbers in enumerate(list_of_lists, start=1):
        result = first_duplicate(numbers)

        print(f"\n{i}° List")
        if result == -1:
            print("No duplicate number found.")
        else:
            print("The first duplicate is:", result)


list_of_integer_lists = [
    [1, 2, 3, 2, 5],
    [7, 8, 9],
    [4, 4, 1, 2],
    [10, 20, 30, 10],
]

process_lists(list_of_integer_lists)
