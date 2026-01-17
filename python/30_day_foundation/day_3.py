"""
Day 3 — Filter (Conditions)

Problems

Extract even numbers

Remove empty strings

Keep numbers greater than 10

Focus

Yes / No logic

Conditional checks
"""

# Extract even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# Remove empty strings
place = "Johannesburg South Africa"
new_place = ""

for char in place:
    if char == " ":
        new_place += ""
    else:
        new_place += char


# Keep numbers greater than 10
random_numbers = [3, 6, 9, 12, 15, 18, 21]
numbers_greater_10 = []

for num in random_numbers:
    if num > 10:
        numbers_greater_10.append(num)

print(numbers_greater_10)


