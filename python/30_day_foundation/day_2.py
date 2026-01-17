# Day 2 — Transform (Lists)
"""
Problems

Double every number in a list

Add ! to the end of every word

Convert temperatures (C → F)
"""

# Double every number in a list

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# Add ! to the end of every word

words = ["love", "beauty", "trust"]
new_words = []

for word in words:
    new_words.append(word + "!")

print(new_words)

# Convert temperatures (C → F)

temparature_c = [25, 45, 90]
temparature_f = []

for temp in temparature_c:
    temparature_f.append(temp * 1.8 + 32)

print(temparature_f)