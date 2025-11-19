# Exercise Description:
# Create a program that asks the user for their name and age.
# If both fields are filled, the program should:

# Display the user's name
# Display the name in reverse
# Check whether the name contains spaces
# Show how many letters the name has
# Print the first and the last letter of the name

# If either field is empty, display an error message informing the user.

name = input("Enter your name: ")
age = input("Enter your age: ")

if name and age:
    print(f"Your name is {name}")
    print(f"Your name reversed is {name[::-1]}")

    if " " in name:
        print("Your name contains spaces")
    else:
        print("Your name does not contain spaces")

    print(f"Your name has {len(name)} letters")
    print(f"The first letter of your name is {name[0]}")
    print(f"The last letter of your name is {name[-1]}")
else:
    print("Sorry, you left empty fields.")

