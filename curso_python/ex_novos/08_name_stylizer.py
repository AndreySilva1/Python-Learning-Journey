# Exercise Description:
# Create a program that takes a name (string) and builds a new version of it 
# where each letter is preceded by an asterisk (*).
# You must implement the logic twice:

# 1. Using a while loop
# 2. Using a for loop

# Both versions should output something like:
# [*a*n*d*r*e*y* *s*i*l*v*a*]

# This exercise practices iteration, string assembly, indexing, and loop control.

# Using while
name = "andrey silva"
name_length = len(name)
i = 0
result = ""

while i < name_length:
    result += f"*{name[i]}"
    i += 1

print(f"{result}*")

# Using for
modified_name = ""

for letter in name:
    modified_name += "*" + letter

print(f"{modified_name}*")
