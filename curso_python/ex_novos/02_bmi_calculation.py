# Exercise Description:
# Write a program that stores a person's name, height, and weight in variables. Then calculate their BMI (Body Mass Index) using the formula:

# BMI = weight / (height * height)

# Finally, print the information in a formatted way using f-strings.

name = "Luiz Otávio"
height = 1.80
weight = 95
bmi = weight / (height * height)

print(f"{name} is {height} meters tall,")
print(f"weighs {weight} kilograms and their BMI is")
print(bmi)

