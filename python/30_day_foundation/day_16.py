"""
Day 16 — Helper Functions

Problems

Text analyzer

Input cleaner

Reusable checks

Focus

Function boundaries
"""

# Text analyzer
def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def text_analyzer(text):
    analysis = {}

    analysis["characters"] = count_characters(text)
    analysis["words"] = count_words(text)
    analysis["vowels"] = count_vowels(text)

    return analysis

        


# Input cleaner
"""
Remove extra spaces

Normalize case

Leave non-strings untouched
"""
def clean_input(user_input):
    if isinstance(user_input, str):
        return user_input.strip().lower()

    return user_input


# Reusable checks
def is_empty(value):
    return value == ""


def is_positive_number(value):
    if isinstance(value, (int, float)):
        return value > 0
    return False


def is_valid_string(value):
    return isinstance(value, str) and value != ""


"""

"""

        
        
        