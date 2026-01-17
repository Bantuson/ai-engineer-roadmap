# 🐍 Python Basics Cheat Sheet
## Variables, Data Types, Loops & Conditionals

---

## 1. Variables & Assignment

Variables store data values. Python uses **dynamic typing**—no need to declare types explicitly.

### Basic Assignment
```python
name = "Fana"           # String
age = 25                # Integer
price = 99.99           # Float
is_active = True        # Boolean
```

### Multiple Assignment
```python
x, y, z = 1, 2, 3       # Assign multiple values
a = b = c = 0           # Same value to multiple variables
```

### Variable Swapping
```python
a, b = b, a             # Pythonic swap (no temp variable needed)
```

### Naming Rules
| Rule | Example | Valid? |
|------|---------|--------|
| Start with letter or underscore | `my_var`, `_private` | ✅ |
| Can contain letters, numbers, underscores | `user2`, `total_sum` | ✅ |
| Case-sensitive | `Name` ≠ `name` | ✅ |
| Cannot start with number | `2fast` | ❌ |
| Cannot use reserved words | `class`, `if`, `for` | ❌ |

### Naming Conventions
```python
my_variable = 1         # snake_case for variables and functions
MY_CONSTANT = 3.14      # UPPER_CASE for constants
MyClass = "example"     # PascalCase for classes
_private = "internal"   # Leading underscore for internal use
```

---

## 2. Data Types

Use `type()` to check a variable's type.

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers | `age = 25`, `count = -10` |
| `float` | Decimal numbers | `price = 19.99`, `pi = 3.14159` |
| `str` | Text/strings | `name = "Python"`, `msg = 'Hello'` |
| `bool` | True or False | `is_valid = True`, `has_error = False` |
| `None` | Absence of value | `result = None` |

### Type Conversion (Casting)
```python
# String to Number
int("42")           # → 42
float("3.14")       # → 3.14

# Number to String
str(100)            # → "100"
str(3.14)           # → "3.14"

# To Boolean
bool(1)             # → True
bool(0)             # → False
bool("")            # → False (empty string)
bool("hello")       # → True (non-empty string)

# Check type
type(42)            # → <class 'int'>
isinstance(42, int) # → True
```

---

## 3. Operators

### Arithmetic Operators
| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `6 * 7` | `42` |
| `/` | Division (float) | `15 / 4` | `3.75` |
| `//` | Floor Division (int) | `15 // 4` | `3` |
| `%` | Modulus (remainder) | `17 % 5` | `2` |
| `**` | Exponentiation | `2 ** 8` | `256` |

### Comparison Operators
| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 3` | `True` |

### Logical Operators
```python
True and False      # → False (both must be True)
True or False       # → True (at least one True)
not True            # → False (inverts boolean)

# Short-circuit evaluation
x = 5
x > 0 and x < 10    # → True
x < 0 or x > 3      # → True
```

### Assignment Operators
```python
x = 10              # Assign
x += 5              # x = x + 5  → 15
x -= 3              # x = x - 3  → 12
x *= 2              # x = x * 2  → 24
x /= 4              # x = x / 4  → 6.0
x //= 2             # x = x // 2 → 3.0
x %= 2              # x = x % 2  → 1.0
x **= 3             # x = x ** 3 → 1.0
```

---

## 4. Conditionals (if/elif/else)

Control program flow based on conditions. Python uses **indentation** (4 spaces) to define code blocks.

### Simple if
```python
age = 18
if age >= 18:
    print("You are an adult")
```

### if-else
```python
score = 75
if score >= 50:
    print("Pass")
else:
    print("Fail")
```

### if-elif-else
```python
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

### Nested if
```python
logged_in = True
is_admin = True

if logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in")
```

### Ternary Operator (One-line if)
```python
age = 20
status = "Adult" if age >= 18 else "Minor"

# Same as:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# Can be nested (but avoid for readability)
result = "A" if score >= 90 else "B" if score >= 80 else "C"
```

### Truthy and Falsy Values
```python
# Falsy values (evaluate to False):
if not 0:           print("0 is falsy")
if not "":          print("Empty string is falsy")
if not []:          print("Empty list is falsy")
if not None:        print("None is falsy")

# Truthy values (evaluate to True):
if 1:               print("Non-zero numbers are truthy")
if "hello":         print("Non-empty strings are truthy")
if [1, 2]:          print("Non-empty lists are truthy")
```

---

## 5. Loops

### For Loops
Iterate over sequences (lists, strings, ranges, etc.)

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):       # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step of 2)
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1 (countdown)
    print(i)

# Iterate over string
for char in "Python":
    print(char)             # P, y, t, h, o, n

# enumerate() - get index and value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# enumerate with start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

### While Loops
Repeat while a condition is True.

```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1      # Don't forget to update!

# User input loop
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

### Loop Control Statements

| Statement | Purpose | Example |
|-----------|---------|---------|
| `break` | Exit loop entirely | `if x == 5: break` |
| `continue` | Skip to next iteration | `if x == 5: continue` |
| `pass` | Do nothing (placeholder) | `if x < 0: pass` |
| `else` | Runs if loop completes without break | See below |

```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break           # Stop at 5
    print(i)            # Prints 0, 1, 2, 3, 4

# continue - skip current iteration
for i in range(5):
    if i == 2:
        continue        # Skip 2
    print(i)            # Prints 0, 1, 3, 4

# else with loops (runs if no break occurred)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")

# pass - placeholder for empty blocks
for i in range(5):
    if i < 3:
        pass            # TODO: implement later
    else:
        print(i)
```

---

## 6. String Operations

### String Creation
```python
single = 'Hello'
double = "World"
multi = """This is a
multiline string"""
raw = r"C:\new\path"    # Raw string (no escape)
```

### String Concatenation & Formatting
```python
# Concatenation
greeting = "Hello" + " " + "World"

# f-strings (Python 3.6+) - RECOMMENDED
name = "Fana"
age = 25
print(f"My name is {name} and I'm {age} years old")
print(f"Next year I'll be {age + 1}")   # Expressions work!
print(f"{name:>10}")    # Right-align in 10 chars
print(f"{3.14159:.2f}") # 2 decimal places → "3.14"

# .format() method
print("Hello, {}!".format(name))
print("{0} is {1} years old".format(name, age))

# % formatting (old style)
print("Hello, %s!" % name)
```

### Common String Methods
```python
s = "  Hello, World!  "

# Case methods
s.upper()               # "  HELLO, WORLD!  "
s.lower()               # "  hello, world!  "
s.capitalize()          # "  hello, world!  "
s.title()               # "  Hello, World!  "
s.swapcase()            # "  hELLO, wORLD!  "

# Whitespace
s.strip()               # "Hello, World!"
s.lstrip()              # "Hello, World!  "
s.rstrip()              # "  Hello, World!"

# Search
s.find("World")         # 9 (index, -1 if not found)
s.index("World")        # 9 (raises error if not found)
s.count("l")            # 3
s.startswith("  Hello") # True
s.endswith("!  ")       # True
"World" in s            # True

# Replace & Split
s.replace("World", "Python")    # "  Hello, Python!  "
"a,b,c".split(",")              # ["a", "b", "c"]
"-".join(["a", "b", "c"])       # "a-b-c"

# Check content
"hello".isalpha()       # True (only letters)
"123".isdigit()         # True (only digits)
"hello123".isalnum()    # True (letters or digits)
"   ".isspace()         # True (only whitespace)
```

### String Slicing
```python
s = "Python"
#    012345  (positive index)
#   -6-5-4-3-2-1 (negative index)

s[0]        # "P" (first character)
s[-1]       # "n" (last character)
s[0:3]      # "Pyt" (index 0, 1, 2)
s[:3]       # "Pyt" (from start to index 2)
s[3:]       # "hon" (from index 3 to end)
s[::2]      # "Pto" (every 2nd character)
s[::-1]     # "nohtyP" (reversed)
s[1:5:2]    # "yh" (index 1 to 4, step 2)
```

---

## 7. Input & Output

### Output with print()
```python
print("Hello, World!")

# Multiple values
x, y = 10, 20
print(x, y)                     # "10 20"
print(x, y, sep=", ")           # "10, 20"
print(x, y, sep=" | ")          # "10 | 20"

# No newline at end
print("Hello", end=" ")
print("World")                  # "Hello World"

# Print to file
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
```

### User Input
```python
# input() always returns a string!
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Convert input to other types
age = int(input("Enter your age: "))
height = float(input("Enter height in meters: "))

# Handle invalid input
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

---

## 💡 Pro Tips

1. **Use meaningful variable names**: `user_age` instead of `x`

2. **Python is case-sensitive**: `Name` ≠ `name` ≠ `NAME`

3. **Use f-strings for formatting** — cleaner than concatenation or `.format()`

4. **Avoid infinite loops**: Always ensure your `while` condition eventually becomes `False`

5. **Use `enumerate()`** instead of `range(len(list))` when you need both index and value

6. **Use ternary for simple conditions**: `result = "yes" if condition else "no"`

7. **Remember**: `input()` always returns a string — convert with `int()` or `float()`

8. **Use `in` for membership testing**: `if "a" in "abc":` is cleaner than using `.find()`

---

*Created for W Chats Marketplace*
