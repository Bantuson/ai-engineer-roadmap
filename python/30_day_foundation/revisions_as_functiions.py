"""
Day 1 — Transform (Strings)

Problems

Reverse a string

Convert a sentence to uppercase

Replace spaces with underscores
"""

# Reverse a string
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(reverse_string("GPT"))


# Convert a sentence to uppercase
def to_uppercase(sentence):
    return sentence.upper()

print(to_uppercase("learning python"))


# Replace spaces with underscores
def replace_spaces(sentence):
    result = ""
    for char in sentence:
        if char == " ":
            result += "_"
        else:
            result += char
    return result

print(replace_spaces("South Africa"))


"""
DAY 2
Double every number in a list

Add ! to the end of every word

Convert temperatures (C → F)
"""

# Double every number in a list

def double_list(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

print(double_list([1, 2, 4, 5]))


# Add ! to the end of every word
def word_list(words):
    appended_words = []
    for word in words:
        appended_words.append(word + "!")
    return appended_words

print(word_list(["time", "show", "snow"]))



# Convert temperatures (C → F)
def convert_temp(tamparature):
    temp_in_f = []
    for temp in tamparature:
        temp_in_f.append(temp * 1.8 + 32)
    return temp_in_f

print(convert_temp([25, 40, 90]))


"""
DAY 3

Extract even numbers

Remove empty strings

Keep numbers greater than 10
"""

# Extract even numbers
def extract_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(extract_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Remove empty strings
def remove_empty_strings(string):
    result = ""
    for char in string:
        if char != " ":
            result += char
    return result



# Keep numbers greater than 10
def num_greater_ten(numbers):
    greater_ten = []
    for num in numbers:
        if num > 10:
            greater_ten.append(num)
    return greater_ten


"""
DAY 4
Keep words longer than 5 characters

Extract vowels from a string

Remove punctuation (basic)
"""

# Keep words longer than 5 characters
def long_words(words):
    longer_words = []
    for word in words:
        if len(word) > 5:
            longer_words.append(word)
    return longer_words



# Extract vowels from a string
def vowels_in_string(string):
    extracted_vowels = ""
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            extracted_vowels += char
    return extracted_vowels


# Remove punctuation
def remove_punctuation(text):
    punctuation = "!,.?"
    new_text = ""
    for char in text:
        if char not in punctuation:
            new_text += char
    return new_text


"""
DAY 5
Count vowels

Count words

Count numbers above a threshold
"""

# Count vowels
def count_vowels(string):
    counted = 0
    vowels = "aeiou"

    for char in string:
        if char in vowels:
            counted += 1
    return counted

# Count words
def word_count(sentence):
    words = sentence.split()
    count = 0

    for _ in words:
        count += 1
    return count


# Count numbers above a threshold
def count_numbers(numbers, threshold=50):
    count = 0

    for num in numbers:
        if num > threshold:
            count += 1
    return count




"""
DAY 6
Find largest number

Find shortest word

Find most frequent letter
"""
    
# Find largest number
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Find shortest word
def shortest_word(sentence):
    words = sentence.split()
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest



# Find most frequent letter
def frequent_letter(string):
    highest_count = 0
    most_frequent = ""

    for char in string:
        if char == " ":
            continue

        count = 0
        for c in string:
            if c == char:
                count += 1

        if count > highest_count:
            highest_count = count
            most_frequent = char

    return most_frequent



"""
DAY 8
Grade calculator

Age category classifier

Password length checker
"""

# Grade calculator
def grade_calculator(grades):
    grade_labels = []

    for grade in grades:
        if grade >= 75:
            grade_labels.append("Distinction")
        elif grade >= 50:
            grade_labels.append("Pass")
        else:
            grade_labels.append("Fail")
    return grade_labels

# Age category classifier
def age_classifier(ages):
    classification = []

    for age in ages:
        if age < 5:
            classification.append("toddler")
        elif age < 12:
            classification.append("young")
        elif age < 20:
            classification.append("teenager")
        elif age < 35:
            classification.append("yound adult")
        elif age < 65:
            classification.append("middle_aged")
        else:
            classification.append("elderly")
    return classification


# Password length checker
def secure_length_checker(password):
    if len(password) < 8:
        return "Weak password"
    elif len(password) < 12:
        return "Moderate password"
    else:
        return "Strong password"
  


"""
DAY 9
Shipping cost calculator

Discount eligibility

Login validation
"""

# Shipping cost calculator
def shipping_cost():
    item_price = 2999
    base_shipping = 150
    weight = 120
    distance = 1.6

    total_cost = item_price + base_shipping

    if weight > 100 and distance > 1.5:
        total_cost += 20

    return total_cost


# Discount eligibility
def check_eligibility():
    spend = 200
    has_coupon = True
    eligible = False

    if spend > 100 or has_coupon:
        eligible = True
    return eligible


# Login validation
def login_validator(email, password):
    stored_email = "admin@python.org"
    stored_password = "asdsd"

    if email == stored_email and password == stored_password:
        return True
    else:
        return False
    

"""
Day 10

Simple calculator

Temperature converter

Unit converter
"""

# Simple calculator
def simple_calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Invalid operator"
    
print(simple_calculator(20, 2, "*"))


# Temperature converter
def temperature_converter(value, unit):
    if unit == "C":
        return value * 1.8 + 32
    elif unit == "F":
        return (value - 32) * 5 / 9
    else:
        return "Invalid temperature unit"
    
print(temperature_converter(25, "C"))
print(temperature_converter(77, "F"))


# Unit converter
def unit_converter(value, from_unit, to_unit):
    if from_unit == "kg" and to_unit == "g":
        return value * 1000
    elif from_unit == "g" and to_unit == "kg":
        return value / 1000
    elif from_unit == "kg" and to_unit == "lb":
        return value * 2.205
    elif from_unit == "lb" and to_unit == "kg":
        return value / 2.205
    else:
        return "Unsupported unit conversion"

print(unit_converter(5, "kg", "g"))
print(unit_converter(10, "kg", "lb"))


"""
DAy 11
Text menu with options

Repeating until exit

Invalid input handling
"""

# Text menu with options
def select_option(options, choice):
    if choice in options:
        return f"Your selection is: {choice}"
    else:
        return "Invalid selection"

menu = ["Town", "City", "Province"]
print(select_option(menu, "City"))


# Repeating until exit
def repeat_until_exit(commands):
    running = True
    index = 0

    while running and index < len(commands):
        command = commands[index]

        if command == "exit":
            running = False
        else:
            print("Running...")
        
        index += 1

    return "Program exited"

commands = ["run", "run", "run", "exit"]
print(repeat_until_exit(commands))


# Invalid input handling
def validate_date(date_string):
    parts = date_string.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    return True


print(validate_date("2023-12-15"))   # True
print(validate_date("15-12-2023"))   # False


"""
Day 12
Guess the number

Limited attempts

Win / lose state
"""

# Guess the number
def guess_number(secret, guesses):
    for guess in guesses:
        if guess == secret:
            return "Win"
    return "Lose"

print(guess_number(7, [3, 5, 7, 9]))

# Limited attempts
def limited_attempts(secret, guesses, max_attempts):
    attempts = 0

    for guess in guesses:
        attempts += 1

        if guess == secret:
            return "Win"

        if attempts == max_attempts:
            break

    return "Lose"

print(limited_attempts("japan", ["china", "korea", "japan"], 3))


# Win / lose state
def win_lose_game(secret, guesses, max_attempts):
    attempts = 0
    game_state = "Running"

    for guess in guesses:
        attempts += 1

        if guess == secret:
            game_state = "Win"
            break

        if attempts == max_attempts:
            game_state = "Lose"
            break

    return game_state


print(win_lose_game(5, [1, 2, 3, 4, 6], 4))
print(win_lose_game(5, [1, 2, 5], 4))


"""
Day 13
Countdown timer

Turn-based counter

Step-by-step process
"""

# Countdown timer
def countdown_timer(start):
    timeline = []

    while start > 0:
        timeline.append(start)
        start -= 1

    timeline.append("Time's up")
    return timeline

print(countdown_timer(5))


# Turn-based counter
def turn_based_counter(max_turns):
    counter = 0
    turn = "Player A"
    history = []
    current_turn = 1

    while current_turn <= max_turns:
        history.append((turn, counter))

        counter += 1

        if turn == "Player A":
            turn = "Player B"
        else:
            turn = "Player A"

        current_turn += 1

    return history

print(turn_based_counter(6))


# Step-by-step process
def step_process(steps):
    completed = []
    index = 0

    while index < len(steps):
        completed.append(steps[index])
        index += 1

    return completed


steps = ["Start engine", "Warm up", "Drive", "Park"]
print(step_process(steps))

"""
initialize state
while condition:
    record state
    update state
return result
"""
