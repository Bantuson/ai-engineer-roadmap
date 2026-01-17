"""
Day 6 — Aggregate (Comparison)

Problems

Find largest number

Find shortest word

Find most frequent letter (simple)

Focus

Tracking best-so-far state
"""

# Find largest number

"""
Input: list of numbers
Output: largest number
state: scan starts at index 0 to -1
transition: scan each number comparing against the rest 
stop: all numbers scanned, largest number found
"""

numbers = [12, 25, 3, 9, 157, 12]

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print(max_number)



# Find shortest word

"""
Input: Sentence
Output: shortest word in sentence
State: get length of each word
Transition: compare length of words
stop: shortest word found
"""

sentence = "Learning python day 6"
words = sentence.split()

shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print(shortest_word)


# Find most frequent letter

"""
Input: string
Output: frequent letter in string
State: frequent letter unknown/empty
Transition: scan characters in string, count when each character is reused
Stop: most used letter found
"""

name = "Mfanafuthi Mhlanga"
most_frequent = ""
highest_count = 0

for char in name:
    if char == " ":
        continue

    count = 0
    for c in name:
        if c == char:
            count += 1

    if count > highest_count:
        highest_count = count
        most_frequent = char

print(most_frequent)

"""
1. Day 6 Core Concept (Lock This In)

Aggregation by comparison means:

You are not collecting many things —
you are tracking one “best-so-far” value while scanning.

That “best-so-far” must:

start as a valid candidate

be updated only when beaten

Everything today flows from that.

Aggregation by comparison means remembering the best answer so far and replacing it only when proven wrong.
"""




