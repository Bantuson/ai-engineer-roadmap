"""
Day 5 — Aggregate (Counting)

Problems

Count vowels

Count words

Count numbers above a threshold

Focus

Accumulators

Initialization
"""



# Count vowels
"""
State:
- count starts at 0
Transition:
- when a vowel is found, increase count by 1
Stop:
- end of string
"""
name = "Mfanafuthi"
vowels = "aeiou"
vowel_count = 0

for char in name.lower():
    if char in vowels:
        vowel_count += 1

print(vowel_count)




# Count words
"""
Input: sentence
State:
- word counter starts at 0
Transition:
- detect word boundaries
Stop:
- end of sentence
"""
sentence = "Learning python is awesome"

words = sentence.split()
word_count = 0

for word in words:
    word_count += 1

print(word_count)




# Count numbers above a threshold
"""
State:
- counter starts at 0
Transition:
- if number > threshold, increment counter
Stop:
- end of list

"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
threshold = 50
count_above_threshold = 0

for num in numbers:
    if num > threshold:
        count_above_threshold += 1

print(count_above_threshold)





"""
The Core Concept of Day 5 (Read This First)

Aggregation is not transformation.
Aggregation is not filtering.

Aggregation answers this question:

“How do many things collapse into one thing?”

That “one thing” is almost always:

a number (count, sum, max)

sometimes a boolean

sometimes a summary structure

This means:

The result does not grow in size.
It changes in value.

This is the key mental shift.

2. The One Rule of Aggregation

Memorize this:

Aggregations require an accumulator initialized to a neutral value.

Examples:

Counting → start at 0

Summing → start at 0

Building text → start at ""

Building a list → start at []

If your accumulator starts as the wrong type, the program cannot work.
"""