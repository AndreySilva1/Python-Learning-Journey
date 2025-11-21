# Exercise Description:

# This exercise creates a simple CLI-based shopping list where the user can:

# Insert items
# Delete items by index
# List all current items

# The program must not crash when the user tries to delete an invalid index.
# The goal is to practice:

# Lists and list manipulation
# Input handling
# Basic error prevention using try/except
# Loops and menu-based interaction
# Safe deletion with index validation

import os

shopping_list = []

while True:
    option = input(
        'Select an option:\n'
        '[i]nsert  [d]elete  [l]ist: '
    )

    if option == 'i':
        os.system('cls')
        item = input('Item: ')
        shopping_list.append(item)

    elif option == 'd':
        os.system('cls')
        try:
            index = int(input('Choose the index to delete: '))
            shopping_list.pop(index)
        except:
            print("Couldn't delete this index!")

    elif option == 'l':
        os.system('cls')
        if shopping_list:
            for i, item in enumerate(shopping_list):
                print(i, item)
        else:
            print('Nothing to list!')

    else:
        print('Enter a valid option!')
