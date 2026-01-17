Day 1 — Transform (Strings)

Problems

Reverse a string
```python
name = "Fana"
reversed_name = ""

for char in name:
    reversed_name = char + reversed_name

print(reversed_name)
```

Convert a sentence to uppercase
```python
name = "Fana"

print(name.upper())
```

Replace spaces with underscores
```python
place = "Johannesburg South Africa"
new_place = ""

for char in place:
    if char == " ":
        new_place += "_":
    else:
        new_place += char

print(new_place)
```
Focus

Traversing data

Order vs value

Temporary state

Ask Yourself

What changes?

What stays the same?

Day 2 — Transform (Lists)

Problems

Double every number in a list
```python
numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)
```

Add ! to the end of every word
```python
words = ["tom", "jerry"]
new_words = []

for word in words:
    new_words.append(word + "!")

print(new_words)
```

Convert temperatures (C → F)
```python
temp_c = [25, 40, 90]
temp_f = []

for temp in temp_c:
    temp_f.append(temp * 1.8 + 32)

print(temp_f)
```

Focus

One-to-one transformation

Output list creation

Day 3 — Filter (Conditions)

Problems

Extract even numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    
print(even_numbers)
```

Remove empty strings
```python
description = "Time for a party"
new_description = ""

for char in description:
    if char == " ":
        new_deescription += ""
    else:
        new_description += char

print(new_description)
```

Keep numbers greater than 10
```python
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num_above_10 = []

for num in numbers:
    if num > 10:
        num_above_10.append(num)
    
print(num_above_10)
```
Focus

Yes / No logic

Conditional checks

Day 4 — Filter (Text Rules)

Problems

Keep words longer than 5 characters
```python
sentence = "New day in python revision"
words = sentence.split()
new_sentence = ""

for word in words:
    if len(word) > 5:
        new_sentence += word

print(new_sentence)
```

Extract vowels from a string
```python
name "Mfanafuthi"
vowels = "aeiou"
vowels_of_name = ""

for char in name:
    if char in vowels:
        vowels_of_name += char

print(vowels_of_name)
```

Remove punctuation (basic)
```python
sentence = "Learning python, no days off!"
punctuation = ",.!?"
new_sentence = ""

for char in sentence:
    if char not in punctuation:
        new_sentence += ""

print(new_sentence)
```

Focus

Rule-based filtering

Character inspection

Day 5 — Aggregate (Counting)

Problems

Count vowels
```python
name = "Mfanafuthi"
vowels = "aeiou"
count = 0

for char in name.lower():
    if char in vowels:
        count += 1 

print(count)
```

Count words
```python
sentence = "Learning python is awesome"
words = sentence.split()
word_count = 0

for word in words:
    word_count += 1

print(word_count)
```


Count numbers above a threshold
```python
numbers = [10, 20, 40, 50, 60, 70, 80, 90]
threshold = 50
count = 0 
new_numbers = []

for num in numbers:
    in num > threshold:
        new_numbers.append(num)

print(new_numbers)
```

Focus

Accumulators

Initialization

Day 6 — Aggregate (Comparison)

Problems

Find largest number
```python
numbers = [24, 875, 94, 157]
largest_number = numbers[0]

for num in numbers:
    if num > largest_numbers:
        largest_number = num

print(largest_number)
```

Find shortest word
```python
sentence = "Learning python, no days off!"
words = sentence.split()
shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print(shortest_word)

```
Find most frequent letter (simple)

Focus

Tracking best-so-far state

Day 7 — Reflection (No Coding)

Pick one problem from the week and write:

Input:
Output:
State variables:
Transitions:
Why this solution works:

WEEK 2 — DECISIONS & CONTROL FLOW

Goal: Make branching and loops feel natural.

Day 8 — Simple Decisions

Problems

Grade calculator
```python
grades = [23, 41, 75, 86, 50, 98]
grade_labels = []

for grade in grades:
    if grade >= 75:
        grade_labels.append("Distinction")
    elif grade >= 50:
        grade_labels.append("Pass")
    else:
        grand_labels.append("Fails")

print(grade_labels)

def grade_calculator(grades):
    for grade in grades:
    if grade >= 75:
        grade_labels.append("Distinction")
    elif grade >= 50:
        grade_labels.append("Pass")
    else:
        grand_labels.append("Fails")
    return grade_labels
```

Age category classifier
```python
ages = [4, 12, 15, 27, 40, 77]
classification = []

for age in ages:
    if age < 4:
        classification.append("toddler")
    elif age < 12:
        classification.append("young")
    elif age < 20:
        classification.append("teenager")
    else:
        classification.append("adult")

def age_classifier(ages):
    for age in ages:
        if age < 4:
        classification.append("toddler")
    elif age < 12:
        classification.append("young")
    elif age < 20:
        classification.append("teenager")
    else:
        classification.append("adult")
    return classification
```

Password length checker
```python
password = "asdasdas"
if len(password) < 8:
    print("Weak password")
elif len(password) < 12:
    print("Moderate password")
else:
    print("Strong password")

```

Focus

Order of conditions

Edge cases

Day 9 — Rule Systems

Problems
```python
# Shipping cost calculator
base_cost = 50
order_price = 2999
weight = 1.8
distance = 7
total_cost = base_cost + order_price / weight

if weight > 1.5 and the distance > 5:
    total_cost += 20

print(total_cost)
```

Discount eligibility
```python
spend = 299
has_coupon = True
is_eligible = False

if spend > 150 or has_coupon:
    is_eligible = True
```
Login validation (mock rules)
```python
input_email = "jajbdjasn@gmail.com"
input_password = "asdada"

stored_email = "dajhdbajbd@gmail.com"
stored_password = "adasdawdw"

login_success = False
if input_email == stored_email and input_password == stored_password:
    login_success = True

print(login_sucess)
```

Focus

Multiple conditions

Logical grouping

Day 10 — User Input Programs

Problems

Simple calculator
```python
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
```


Temperature converter
```python
input_temp = "20C"

value = float(temp_input[:-1])
unit = temp_input[-1]

result = 0

if unit == "C":
    result = value * 1.8 + 32
elif unit == "F":
    result = (value - 32) * 5 / 9

print(result)
```

Unit converter
```python
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
```



Day 11 — Menu Systems

Problems

Text menu with options
```python
menu = ["set", "tuple", "dictionary", "list"]
choice = input(f"please select from {menu}")

if choice in menu:
    print(f"Your selection is {choice}")
else:
    print("Invalid selection")
```

Repeating until exit
```python
menu_options = ["Town", "City", "Province", "Exit"]
running = True

while running:
    choice = input(f"Choose an option {menu_options}: ")

    if choice == "Exit":
        running = False
        print("Exiting menu")
    elif choice in menu_options:
        print(f"You selected {choice}")
    else:
        print("Invalid option")
```

Invalid input handling
```python
user_input = "01-02-2020"
is_valid = True

parts = user_input.split("-")

if parts != 3:
    is_valid = False
else:
    day, month, year = parts

    if not day.isdigit() and month.isdigit() and year.isdigit():
        is_valid = False
    else:
        day = int(day)
        month = int(month)
        year = int(year)

        if not (1 <= day <= 31):
            is_valid = False
        if not (1 <= month <= 12):
            is_valid = False
        if not (1900 <= year <= 2025):
            is_valid = False

print(is_valid)
```


Day 12 — Game Logic

Problems

Guess the number
```python
number = 7
guess = input(f"guess number: ")
correct_guess = False

if guess == number:
    correct_guess = True:

print(correct_guess)
```

Limited attempts
```python
place = "japan"
max_tries = 3
tries = 0
correct_guess = False

while tries < max_tries and not correct guess:
    attempt = input("Guess the place: ")

    if attempt == place:
        correct_guess = True
        print("Correct!")
    else:
        tries += 1
        print("Incorrect, try again")

if not correct_guess:
    print("No tries left. You lose.")
```


Win / lose state
```python
number = 7
max_tries = 3
tries = 0
won = False

while tries < max_tries:
    guess = int(input("Guess the number: "))

    if guess == number:
        won = True
        break
    else:
        tries += 1
        print("Wrong guess")

if won:
    print("You win!")
else:
    print("You lose!")
    
```
Focus

State over time

Loop exit conditions

Day 13 — Simulation Thinking

Problems

Countdown timer

Turn-based counter

Step-by-step process

Focus

State changes per iteration

Day 14 — Rewrite from Memory

Rebuild any program from Week 2

No reference code

Only your English steps

WEEK 3 — DECOMPOSITION (THINKING IN FUNCTIONS)

Goal: Split problems naturally.

Day 15 — Validation Functions

Problems

Email validation (basic rules)

Password validation

Focus

One responsibility per function

Day 16 — Helper Functions

Problems

Text analyzer

Input cleaner

Reusable checks

Focus

Function boundaries

Day 17 — Data-Driven Programs

Problems

Todo list

Shopping cart

Score tracker

Focus

Lists & dictionaries

CRUD logic

Day 18 — Multiple Aggregations

Problems

Word frequency counter

Sentence analyzer

Log summary

Focus

Parallel state tracking

Day 19 — Command Parsing

Problems

Interpret user commands

Split input into actions

Execute behavior

Focus

Mapping input → behavior

Day 20 — Mini System

Build

Small CLI tool of your choice

Rules

At least 3 functions

Persistent state (in memory)

Day 21 — Reflection

Write answers to:

When did functions feel necessary?

What repetition disappeared?

What still feels unclear?

WEEK 4 — OOP (NOW IT ACTUALLY MAKES SENSE)

Goal: Feel why classes exist.

Day 22 — Encapsulated State

Problems

Counter class

Bank account

Game player

Focus

State stored in object

Day 23 — Behavior + Data

Problems

Order class

User session

Inventory item

Focus

Methods modifying internal state

Day 24 — Multi-Object Interaction

Problems

User + Cart

Player + Game

Order + Payment

Focus

Object communication

Day 25 — Refactor Procedural → OOP

Take an old program

Convert to classes

Compare complexity

Day 26 — Rule-Based Agent

Problems

Simple chatbot rules

Command router

Focus

State-driven responses

Day 27 — Simulation System

Build

Turn-based system

Finite states

Day 28 — Clean Up & Refactor

Rename variables

Simplify logic

Improve readability

Day 29 — Rebuild Without Looking

Rebuild your favorite program

From memory

English → Code

Day 30 — Final Mental Model Lock-In

Write this (seriously):

How do I approach a new programming problem now?
What questions do I ask first?
What do I do before writing code?
