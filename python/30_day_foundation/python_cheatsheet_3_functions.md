# ⚡ Python Functions Cheat Sheet
## Defining, Calling, Arguments & Advanced Techniques

---

## 1. Function Basics

Functions are reusable blocks of code that perform a specific task.

### Defining & Calling Functions
```python
# Basic function definition
def greet():
    """A simple greeting function."""  # Docstring
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with return value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)  # result = 8

# Multiple return values (returns tuple)
def get_stats(numbers):
    """Return min, max, and average."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
# minimum=1, maximum=5, average=3.0
```

### Return Statement
```python
# Single return
def square(x):
    return x ** 2

# Multiple returns (early exit)
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Return None (implicit)
def print_message(msg):
    print(msg)
    # No return statement = returns None

result = print_message("Hi")  # result is None

# Return multiple values
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns tuple

q, r = divide_with_remainder(17, 5)  # q=3, r=2
```

---

## 2. Function Arguments

### Positional Arguments
```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

greet("Fana", "Hello")      # "Hello, Fana!"
greet("Hello", "Fana")      # "Fana, Hello!" (order matters!)
```

### Keyword Arguments
```python
def greet(name, greeting):
    return f"{greeting}, {name}!"

# Using keyword arguments (order doesn't matter)
greet(name="Fana", greeting="Hello")    # "Hello, Fana!"
greet(greeting="Hello", name="Fana")    # "Hello, Fana!"

# Mix positional and keyword (positional must come first)
greet("Fana", greeting="Hello")         # "Hello, Fana!"
# greet(name="Fana", "Hello")           # SyntaxError!
```

### Default Arguments
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Fana")                   # "Hello, Fana!" (uses default)
greet("Fana", "Hi")             # "Hi, Fana!" (overrides default)
greet("Fana", greeting="Hey")   # "Hey, Fana!"

# Multiple defaults
def create_user(name, age=0, city="Unknown", active=True):
    return {"name": name, "age": age, "city": city, "active": active}

create_user("Fana")                         # Uses all defaults
create_user("Fana", 25)                     # age=25
create_user("Fana", city="Johannesburg")    # Skip age, set city

# ⚠️ DANGER: Mutable default arguments!
# DON'T do this:
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

bad_append(1)  # [1]
bad_append(2)  # [1, 2] - Same list is reused!

# DO this instead:
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### *args (Variable Positional Arguments)
```python
def sum_all(*args):
    """Accept any number of positional arguments."""
    print(f"args = {args}")  # args is a tuple
    return sum(args)

sum_all(1, 2, 3)           # 6
sum_all(1, 2, 3, 4, 5)     # 15
sum_all()                   # 0

# Combine with regular arguments
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### **kwargs (Variable Keyword Arguments)
```python
def print_info(**kwargs):
    """Accept any number of keyword arguments."""
    print(f"kwargs = {kwargs}")  # kwargs is a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Fana", age=25, city="Johannesburg")
# kwargs = {'name': 'Fana', 'age': 25, 'city': 'Johannesburg'}
# name: Fana
# age: 25
# city: Johannesburg

# Combine with regular and *args
def full_example(required, *args, default="value", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

full_example("first", 1, 2, 3, default="custom", x=10, y=20)
```

### Argument Order
```python
# The correct order for function parameters:
def func(
    positional,           # 1. Regular positional arguments
    *args,                # 2. *args (variable positional)
    keyword_only,         # 3. Keyword-only arguments
    default="value",      # 4. Arguments with defaults
    **kwargs              # 5. **kwargs (variable keyword)
):
    pass
```

### Unpacking Arguments
```python
# Unpack list/tuple with *
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
add(*numbers)  # Same as add(1, 2, 3) → 6

# Unpack dict with **
def greet(name, greeting):
    return f"{greeting}, {name}!"

params = {"name": "Fana", "greeting": "Hello"}
greet(**params)  # Same as greet(name="Fana", greeting="Hello")

# Combine both
args = [1, 2]
kwargs = {"c": 3}
add(*args, **kwargs)  # Same as add(1, 2, c=3)
```

---

## 3. Lambda Functions

Anonymous, single-expression functions.

### Basic Syntax
```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

# Usage
square(5)  # 25

# Multiple arguments
add = lambda a, b: a + b
add(3, 5)  # 8

# With default arguments
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
greet("Fana")  # "Hello, Fana!"
```

### Common Use Cases
```python
# Sorting with custom key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted(students, key=lambda s: s["grade"])

# Sort by name length
sorted(students, key=lambda s: len(s["name"]))

# Sort descending
sorted(students, key=lambda s: s["grade"], reverse=True)

# With filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# With map()
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With reduce()
from functools import reduce
product = reduce(lambda a, b: a * b, numbers)
# 3628800 (1*2*3*...*10)

# Conditional expression in lambda
classify = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
classify(5)   # "positive"
classify(-3)  # "negative"
classify(0)   # "zero"
```

### Lambda vs Regular Functions

| Feature | Lambda | Regular Function |
|---------|--------|------------------|
| Name | Anonymous | Named |
| Statements | Single expression only | Multiple statements |
| Docstring | No | Yes |
| Annotations | No | Yes |
| Best for | Simple, one-off operations | Reusable, complex logic |

```python
# Use lambda for simple operations
sorted(items, key=lambda x: x.value)

# Use regular function for complex logic
def complex_key(item):
    """Calculate complex sort key."""
    if item.priority == "high":
        return 0
    elif item.priority == "medium":
        return 1
    else:
        return 2

sorted(items, key=complex_key)
```

---

## 4. Scope & Closures

### Variable Scope
```python
# Global scope
global_var = "I'm global"

def outer():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner():
        # Local scope
        local_var = "I'm local"
        print(local_var)      # ✅ Accessible
        print(enclosing_var)  # ✅ Accessible
        print(global_var)     # ✅ Accessible
    
    inner()
    print(enclosing_var)      # ✅ Accessible
    # print(local_var)        # ❌ NameError

outer()
print(global_var)             # ✅ Accessible
# print(enclosing_var)        # ❌ NameError
```

### The `global` Keyword
```python
counter = 0

def increment():
    global counter  # Use global variable
    counter += 1

increment()
increment()
print(counter)  # 2

# Without global keyword:
def bad_increment():
    counter = 0     # Creates LOCAL variable!
    counter += 1
```

### The `nonlocal` Keyword
```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Use enclosing variable
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Closures
```python
# A closure "remembers" variables from enclosing scope
def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor  # 'factor' is captured from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10
triple(5)   # 15

# Practical example: Counter
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter_a = make_counter()
counter_b = make_counter(100)

counter_a()  # 1
counter_a()  # 2
counter_b()  # 101
counter_b()  # 102
```

---

## 5. Decorators

Functions that modify the behavior of other functions.

### Basic Decorator
```python
def my_decorator(func):
    """A simple decorator."""
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# Apply decorator
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Fana")
# Output:
# Before function call
# Hello, Fana!
# After function call

# Same as:
# say_hello = my_decorator(say_hello)
```

### Practical Decorators
```python
import time
from functools import wraps

# Timer decorator
def timer(func):
    @wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()  # slow_function took 1.0012 seconds

# Logger decorator
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# Calling add with args=(3, 5), kwargs={}
# add returned 8

# Retry decorator
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"
```

### Decorators with Arguments
```python
def repeat(times):
    """Decorator that repeats function call."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

greet("Fana")  # ["Hello, Fana!", "Hello, Fana!", "Hello, Fana!"]
```

### Class-Based Decorators
```python
class CountCalls:
    """Decorator that counts function calls."""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()  # Call 1 of say_hi \n Hi!
say_hi()  # Call 2 of say_hi \n Hi!
print(say_hi.count)  # 2
```

### Stacking Decorators
```python
@decorator1
@decorator2
@decorator3
def func():
    pass

# Same as: func = decorator1(decorator2(decorator3(func)))
# Execution order: decorator3 → decorator2 → decorator1
```

---

## 6. Built-in Functions

### Commonly Used Built-ins

| Function | Description | Example |
|----------|-------------|---------|
| `len(x)` | Length | `len([1,2,3])` → `3` |
| `range(start, stop, step)` | Number sequence | `range(0, 10, 2)` |
| `enumerate(iterable)` | Index + value pairs | `enumerate(['a','b'])` |
| `zip(a, b)` | Combine iterables | `zip([1,2], ['a','b'])` |
| `map(func, iterable)` | Apply function | `map(str, [1,2,3])` |
| `filter(func, iterable)` | Filter by function | `filter(bool, [0,1,2])` |
| `sorted(iterable)` | Return sorted list | `sorted([3,1,2])` |
| `reversed(sequence)` | Reverse iterator | `reversed([1,2,3])` |
| `any(iterable)` | Any True? | `any([False, True])` |
| `all(iterable)` | All True? | `all([True, True])` |
| `sum(iterable)` | Sum of elements | `sum([1,2,3])` |
| `min(iterable)` | Minimum | `min([3,1,2])` |
| `max(iterable)` | Maximum | `max([3,1,2])` |
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `round(x, n)` | Round to n decimals | `round(3.14159, 2)` |
| `pow(x, y)` | x to power y | `pow(2, 3)` → `8` |
| `isinstance(obj, type)` | Type check | `isinstance(5, int)` |
| `callable(obj)` | Is callable? | `callable(print)` |
| `getattr(obj, name)` | Get attribute | `getattr(obj, 'x')` |
| `setattr(obj, name, val)` | Set attribute | `setattr(obj, 'x', 5)` |
| `hasattr(obj, name)` | Has attribute? | `hasattr(obj, 'x')` |

### Higher-Order Functions
```python
# map() - apply function to all elements
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Same with list comprehension (often preferred)
squares = [x**2 for x in numbers]

# filter() - keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Same with list comprehension
evens = [x for x in numbers if x % 2 == 0]

# reduce() - combine elements (requires import)
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
# 15 (1+2+3+4+5)

# Practical example: Compose functions
def compose(*functions):
    """Compose multiple functions."""
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

# (5 + 1) * 2 ^ 2 = 144
f = compose(square, double, add_one)
f(5)  # 144
```

---

## 7. Type Hints (Python 3.5+)

Type hints improve code readability and enable static analysis.

### Basic Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process(data: list) -> None:
    print(data)

# Variable annotations
age: int = 25
name: str = "Fana"
prices: list[float] = [9.99, 19.99, 29.99]
```

### Advanced Type Hints
```python
from typing import (
    List, Dict, Tuple, Set,     # Generic types
    Optional,                    # Can be None
    Union,                       # Multiple possible types
    Callable,                    # Function type
    Any,                         # Any type
    TypeVar,                     # Generic type variable
)

# Collections
def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    """Return username or None if not found."""
    users = {1: "Fana", 2: "Bongani"}
    return users.get(user_id)

# Union (multiple types)
def process(data: Union[str, int]) -> str:
    return str(data)

# Python 3.10+ syntax
def process(data: str | int) -> str:
    return str(data)

# Callable
def apply_operation(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return func(a, b)

# With *args and **kwargs
def wrapper(
    *args: int,
    **kwargs: str
) -> None:
    pass

# Generic functions
T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

first([1, 2, 3])      # Returns int
first(["a", "b"])     # Returns str
```

---

## 8. Generators

Functions that yield values one at a time, saving memory.

### Basic Generators
```python
# Generator function (uses yield)
def count_up_to(n):
    """Generate numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5

# Convert to list
list(count_up_to(5))  # [1, 2, 3, 4, 5]

# Manual iteration
gen = count_up_to(3)
next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # StopIteration error
```

### Generator Expressions
```python
# Generator expression (like list comprehension but lazy)
squares_gen = (x**2 for x in range(1000000))  # No memory used yet!
squares_list = [x**2 for x in range(1000000)]  # All in memory!

# Iterate
for sq in squares_gen:
    if sq > 100:
        break
    print(sq)

# Use with functions
sum(x**2 for x in range(10))      # 285
max(len(word) for word in words)  # Longest word length
```

### Practical Generator Examples
```python
# Read large files line by line
def read_large_file(filepath):
    """Memory-efficient file reading."""
    with open(filepath) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("huge_file.txt"):
    process(line)

# Infinite sequence
def fibonacci():
    """Generate Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
[next(fib) for _ in range(10)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Pipeline of generators
def integers():
    i = 1
    while True:
        yield i
        i += 1

def squares(nums):
    for n in nums:
        yield n ** 2

def take(n, iterable):
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

# Chain them together
pipeline = take(5, squares(integers()))
list(pipeline)  # [1, 4, 9, 16, 25]
```

### yield from
```python
# Delegate to sub-generator
def flatten(nested):
    """Flatten nested lists."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate to recursive call
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6]
list(flatten(nested))  # [1, 2, 3, 4, 5, 6]
```

---

## 💡 Pro Tips

1. **Use `*args` and `**kwargs`** for flexible function signatures
   ```python
   def flexible_func(*args, **kwargs):
       pass
   ```

2. **Never use mutable default arguments**
   ```python
   # Bad:  def func(lst=[])
   # Good: def func(lst=None): lst = lst or []
   ```

3. **Use `functools.wraps`** in decorators to preserve function metadata

4. **Prefer generators** for large datasets to save memory

5. **Use type hints** for better code documentation and IDE support

6. **Keep functions small** - each function should do one thing well

7. **Use docstrings** to document what functions do:
   ```python
   def func(x):
       """
       Brief description.
       
       Args:
           x: Description of x
           
       Returns:
           Description of return value
       """
       pass
   ```

8. **Return early** to reduce nesting:
   ```python
   # Instead of nested if-else
   def process(x):
       if not x:
           return None
       if x < 0:
           return "negative"
       return "positive"
   ```

9. **Use lambda sparingly** - prefer named functions for anything non-trivial

10. **Test your functions** with different inputs including edge cases

---

*Created for W Chats Marketplace*
