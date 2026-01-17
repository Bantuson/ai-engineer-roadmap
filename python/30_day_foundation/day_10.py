"""
Day 10 — User Input Programs

Problems

Simple calculator

Temperature converter

Unit converter

Focus

Input → processing → output
"""

# Simple calculator
user_input = "20 x 2"

parts = user_input.split()

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "x":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(result)



# Temperature converter
temp_input = "25C"

value = float(temp_input[:-1])
unit = temp_input[-1]

result = 0

if unit == "C":
    result = value * 1.8 + 32
elif unit == "F":
    result = (value - 32) * 5 / 9

print(result)


# Unit converter
user_input = "135kg"

value = float(user_input[:-2])
unit = user_input[-2:]

result = 0

if unit == "kg":
    result = value * 1000
elif unit == "g":
    result = value / 1000
elif unit == "lb":
    result = value * 0.4536

print(result)


"""
RAW STRING
↓
PARSE (extract meaning)
↓
NORMALIZE (convert to numbers / units)
↓
PROCESS (logic/math)
↓
OUTPUT (string or number)
"""