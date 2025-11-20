# Exercise Description:

# This exercise reads a text and finds which character appears the most in the sentence.
# The program converts the whole text to uppercase, loops through each letter, counts how many times it appears, and finally prints the most frequent character and its count.

# The goal of this exercise is to practice:

# String manipulation
# Counting character occurrences
# Loops and conditionals
# Handling repeated values
# Writing readable logic in English

sentence = (
    'Python is a multiparadigm programming language. '
    'Python was created by Guido van Rossum.'
).upper()

i = 0
most_common_letter = ''
highest_count = 0

while i < len(sentence):
    letter = sentence[i]
    count = sentence.count(letter)

    if letter == ' ':
        i += 1
        continue

    if count > highest_count:
        highest_count = count
        most_common_letter = letter

    i += 1

print(f'{most_common_letter} = {highest_count}')