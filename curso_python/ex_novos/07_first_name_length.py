# Exercise Description:
# Create a program that asks the user for their first name.
# Then:

# Calculate how many letters the name has.
# If the name has 4 or fewer letters → print “Your name is short!”
# If it has 5 or 6 letters → print “Your name is normal!”
# If it has 7 or more letters → print “Your name is very long!”

# This exercise practices input handling, string length with len(), and conditional logic.

first_name = input("Enter your first name: ")
length = len(first_name)

if length <= 4:
    print("Your name is short!")
elif length <= 6:
    print("Your name is normal!")
else:
    print("Your name is very long!")