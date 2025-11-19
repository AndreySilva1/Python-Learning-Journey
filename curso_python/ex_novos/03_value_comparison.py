# Exercise Description:
# Create a program that asks the user to input two values. Then, compare them and display which one is greater. If both values are equal, print a message indicating equality. The output should use f-strings to show the variable names and their values.

first_value = input("Enter a value: ")
second_value = input("Enter another value: ")

if first_value > second_value:
    print(f"{first_value=} is greater than {second_value=}")
elif second_value > first_value:
    print(f"{second_value=} is greater than {first_value=}")
else:
    print(f"{first_value=} is equal to {second_value=}")

