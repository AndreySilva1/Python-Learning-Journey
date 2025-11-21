# Exercise Description:

# This exercise is a simple word-guessing game where the user must discover a 
# secret word by entering one letter at a time.
# The program checks whether each typed letter is part of the secret word and 
# reveals the correct letters while hiding the rest with *.
# It also counts the number of attempts the user makes until they guess the full word.

# The goals of this exercise are:

# Practice loops (while)
# Work with string comparison
# Track correct guesses
# Build and update a hidden word display
# Count user attempts
# Strengthen logic and flow control

import os

secret_word = 'Python'
correct_letters = ''
attempts = 0

while True:
    letter = input('Type a letter: ')
    attempts += 1

    revealed_word = ''

    if len(letter) == 1:
        if letter in secret_word:
            correct_letters += letter

        for secret_letter in secret_word:
            if secret_letter in correct_letters:
                revealed_word += secret_letter
            else:
                revealed_word += '*'

        print(revealed_word)
    else:
        print('Type only one letter!')

    if revealed_word == secret_word:
        os.system('cls')
        print('CONGRATS, YOU WON!')
        print(f'The secret word was: "{secret_word}"')
        print(f'Attempts: {attempts}')
        correct_letters = ''
        attempts = 0
