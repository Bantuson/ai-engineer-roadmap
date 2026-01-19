"""
Day 7: Regex Basics
===================
Learn regular expressions for pattern matching and text processing.

Key concepts:
- Basic patterns and metacharacters
- re.match(), re.search(), re.findall()
- Character classes and quantifiers
- Groups and capturing
- Common patterns
"""

import re

# =============================================================================
# CONCEPT: Regex Basics
# =============================================================================

# Basic matching
def demo_match_vs_search():
    """Show difference between match and search."""
    text = "Hello World"

    # match() only matches at beginning
    print(re.match(r'Hello', text))  # Match object
    print(re.match(r'World', text))  # None

    # search() finds anywhere in string
    print(re.search(r'World', text))  # Match object


# Common patterns
PATTERNS = {
    'digit': r'\d',           # Single digit
    'word_char': r'\w',       # Word character (a-z, A-Z, 0-9, _)
    'whitespace': r'\s',      # Whitespace
    'word': r'\w+',           # One or more word characters
    'digits': r'\d+',         # One or more digits
    'any_char': r'.',         # Any character except newline
}


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_patterns():
    """Demonstrate basic regex patterns."""
    print("=== Basic Patterns ===")

    text = "The price is $19.99 for 3 items"

    # Find all digits
    digits = re.findall(r'\d', text)
    print(f"Digits: {digits}")  # ['1', '9', '9', '9', '3']

    # Find all numbers
    numbers = re.findall(r'\d+', text)
    print(f"Numbers: {numbers}")  # ['19', '99', '3']

    # Find words
    words = re.findall(r'\w+', text)
    print(f"Words: {words}")


def example_character_classes():
    """Demonstrate character classes."""
    print("\n=== Character Classes ===")

    text = "Contact: john@example.com or call 555-1234"

    # [abc] - matches a, b, or c
    vowels = re.findall(r'[aeiou]', text)
    print(f"Vowels: {vowels}")

    # [a-z] - range
    lowercase = re.findall(r'[a-z]+', text)
    print(f"Lowercase words: {lowercase}")

    # [^abc] - NOT a, b, or c
    non_vowels = re.findall(r'[^aeiou\s@.\-\d]+', text)
    print(f"Consonant groups: {non_vowels}")

    # Combined ranges
    alphanumeric = re.findall(r'[a-zA-Z0-9]+', text)
    print(f"Alphanumeric: {alphanumeric}")


def example_quantifiers():
    """Demonstrate quantifiers."""
    print("\n=== Quantifiers ===")

    text = "aaa ab abbb ac abbbb"

    # * - zero or more
    print(f"ab*: {re.findall(r'ab*', text)}")  # ['a', 'ab', 'abbb', 'a', 'abbbb']

    # + - one or more
    print(f"ab+: {re.findall(r'ab+', text)}")  # ['ab', 'abbb', 'abbbb']

    # ? - zero or one
    print(f"ab?: {re.findall(r'ab?', text)}")  # ['a', 'ab', 'ab', 'a', 'ab']

    # {n} - exactly n
    print(f"ab{{3}}: {re.findall(r'ab{3}', text)}")  # ['abbb', 'abbb']

    # {n,m} - between n and m
    print(f"ab{{2,3}}: {re.findall(r'ab{2,3}', text)}")  # ['abbb', 'abbb']


def example_anchors():
    """Demonstrate anchors."""
    print("\n=== Anchors ===")

    lines = ["Hello World", "World Hello", "Say Hello"]

    # ^ - start of string/line
    for line in lines:
        if re.match(r'^Hello', line):
            print(f"Starts with Hello: {line}")

    # $ - end of string/line
    for line in lines:
        if re.search(r'Hello$', line):
            print(f"Ends with Hello: {line}")

    # Word boundaries \b
    text = "hello helloworld worldhello"
    print(f"Whole word 'hello': {re.findall(r'\bhello\b', text)}")


def example_groups():
    """Demonstrate capturing groups."""
    print("\n=== Groups ===")

    # Basic groups
    text = "John Smith, Jane Doe, Bob Wilson"
    names = re.findall(r'(\w+) (\w+)', text)
    print(f"Names (first, last): {names}")

    # Named groups
    pattern = r'(?P<first>\w+) (?P<last>\w+)'
    for match in re.finditer(pattern, text):
        print(f"First: {match.group('first')}, Last: {match.group('last')}")

    # Non-capturing groups (?:...)
    text = "cat cats dog dogs"
    with_capture = re.findall(r'(cat|dog)s?', text)
    without_capture = re.findall(r'(?:cat|dog)s?', text)
    print(f"With capture: {with_capture}")
    print(f"Without capture: {without_capture}")


def example_substitution():
    """Demonstrate regex substitution."""
    print("\n=== Substitution ===")

    text = "Call 555-1234 or 555-5678"

    # Simple replacement
    result = re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', text)
    print(f"Masked: {result}")

    # Replacement with groups
    text = "John Smith"
    result = re.sub(r'(\w+) (\w+)', r'\2, \1', text)
    print(f"Swapped: {result}")

    # Replacement with function
    def mask_middle(match):
        s = match.group()
        if len(s) > 2:
            return s[0] + '*' * (len(s) - 2) + s[-1]
        return s

    text = "Contact john@example.com"
    result = re.sub(r'\w+@\w+\.\w+', mask_middle, text)
    print(f"Email masked: {result}")


def example_common_patterns():
    """Demonstrate common regex patterns."""
    print("\n=== Common Patterns ===")

    # Email (simplified)
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    text = "Email us at support@example.com or sales@company.org"
    emails = re.findall(email_pattern, text)
    print(f"Emails: {emails}")

    # Phone (US format)
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    text = "Call (555) 123-4567 or 555.987.6543"
    phones = re.findall(phone_pattern, text)
    print(f"Phones: {phones}")

    # URL
    url_pattern = r'https?://[\w\.-]+(?:/[\w\.-]*)*'
    text = "Visit https://example.com/page or http://test.org"
    urls = re.findall(url_pattern, text)
    print(f"URLs: {urls}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Date Extractor

    Write a function that extracts dates in format MM/DD/YYYY or MM-DD-YYYY.

    text = "Events on 01/15/2026 and 12-25-2026"
    extract_dates(text) -> ['01/15/2026', '12-25-2026']
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Hashtag Finder

    Write a function that extracts hashtags from text.

    text = "Loving #Python and #MachineLearning! #AI2026"
    find_hashtags(text) -> ['#Python', '#MachineLearning', '#AI2026']
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Password Validator

    Write a function that validates passwords using regex:
    - At least 8 characters
    - Contains at least one uppercase
    - Contains at least one lowercase
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)

    validate_password("Passw0rd!") -> True
    validate_password("password") -> False
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: HTML Tag Extractor

    Write a function that extracts HTML tags and their content.

    text = "<h1>Title</h1><p>Paragraph</p>"
    extract_tags(text) -> [('h1', 'Title'), ('p', 'Paragraph')]

    Handle self-closing tags too: <br/>, <img src="..."/>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Log Parser

    Create a log file parser using regex that extracts structured data.

    Sample log format:
    2026-01-19 10:30:45 [INFO] user=alice action=login ip=192.168.1.1 duration=0.5s
    2026-01-19 10:30:46 [ERROR] user=bob action=upload error="File too large" size=50MB
    2026-01-19 10:30:47 [WARN] user=alice action=download rate_limit=true

    Functions to implement:

    1. parse_log_line(line) -> dict
       Returns: {
           'timestamp': '2026-01-19 10:30:45',
           'level': 'INFO',
           'fields': {'user': 'alice', 'action': 'login', ...}
       }

    2. filter_logs(lines, level=None, user=None, time_range=None)
       Filter logs by various criteria

    3. aggregate_logs(lines, group_by='user')
       Count logs grouped by a field

    4. find_errors(lines, pattern=None)
       Find error logs, optionally matching an error pattern

    5. generate_report(lines)
       Generate summary: counts by level, top users, error types, etc.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 7: Regex Basics\n")
    print("=" * 50)

    # Run examples
    example_basic_patterns()
    example_character_classes()
    example_quantifiers()
    example_anchors()
    example_groups()
    example_substitution()
    example_common_patterns()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
