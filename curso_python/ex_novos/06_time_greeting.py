# Exercise Description:
# Write a program that asks the user for the current hour in 24-hour format (0–24).
# Based on the input, display an appropriate greeting:

# 0 to 11 → “Good morning!”
# 12 to 17 → “Good afternoon!”
# 18 to 24 → “Good evening!”

# The program must convert the input to an integer and use try/except to handle invalid values.
# If the number is outside the valid range, show an error message.

try:
    hour = int(input("What time is it now?: "))

    if hour <= 11:
        print("Good morning!")
    elif hour <= 17:
        print("Good afternoon!")
    elif hour <= 24:
        print("Good evening!")
    else:
        print("Enter a value between 0 and 24.")
except:
    print("Enter a valid value!")