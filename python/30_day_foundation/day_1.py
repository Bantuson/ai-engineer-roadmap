# Day 1 — Transform (Strings)

# Problems

# Reverse a string

name = "Fana"
reversed_name = ""

for char in name:
    reversed_name = char + reversed_name


print(reversed_name)

# Convert a sentence to uppercase

sentence = " Marty Supreme"

print(sentence.upper())

# Replace spaces with underscores 

place = "Johannesburg South Africa"
new_place =  ""

for char in place:
    if char == " ":
        new_place += "_"
    else:
        new_place += char

print(new_place)