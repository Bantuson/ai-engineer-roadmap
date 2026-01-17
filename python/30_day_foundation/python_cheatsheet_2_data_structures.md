# 📦 Python Data Structures Cheat Sheet

## Lists, Dictionaries, Sets & Tuples

---

## Quick Comparison

| Type      | Syntax      | Ordered  | Mutable | Duplicates | Use Case                   |
| --------- | ----------- | -------- | ------- | ---------- | -------------------------- |
| **List**  | `[1, 2, 3]` | ✅ Yes   | ✅ Yes  | ✅ Allowed | General-purpose collection |
| **Tuple** | `(1, 2, 3)` | ✅ Yes   | ❌ No   | ✅ Allowed | Fixed data, dict keys      |
| **Dict**  | `{"a": 1}`  | ✅ Yes\* | ✅ Yes  | Keys: ❌   | Key-value mapping          |
| **Set**   | `{1, 2, 3}` | ❌ No    | ✅ Yes  | ❌ No      | Unique items, fast lookup  |

\*Dicts maintain insertion order in Python 3.7+

---

## 1. Lists [ ]

Ordered, mutable collections that can hold items of any type.

### Creating Lists

```python
# Empty list
empty = []
empty = list()

# With initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

# From other iterables
from_range = list(range(1, 6))      # [1, 2, 3, 4, 5]
from_string = list("hello")          # ['h', 'e', 'l', 'l', 'o']
from_tuple = list((1, 2, 3))         # [1, 2, 3]

# List comprehension
squares = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
```

### Accessing & Slicing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#          0        1         2         3       4
#         -5       -4        -3        -2      -1

# Indexing
fruits[0]       # "apple" (first)
fruits[-1]      # "elderberry" (last)
fruits[2]       # "cherry"

# Slicing [start:stop:step]
fruits[0:3]     # ["apple", "banana", "cherry"]
fruits[:3]      # ["apple", "banana", "cherry"]
fruits[2:]      # ["cherry", "date", "elderberry"]
fruits[::2]     # ["apple", "cherry", "elderberry"] (every 2nd)
fruits[::-1]    # Reversed list
fruits[1:4:2]   # ["banana", "date"] (1 to 3, step 2)

# Nested access
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0]       # [1, 2, 3]
matrix[0][1]    # 2
matrix[1][2]    # 6
```

### List Methods

| Method         | Description                          | Example                                |
| -------------- | ------------------------------------ | -------------------------------------- |
| `append(x)`    | Add item to end                      | `lst.append(4)`                        |
| `extend(iter)` | Add all items from iterable          | `lst.extend([4, 5])`                   |
| `insert(i, x)` | Insert at index i                    | `lst.insert(0, "first")`               |
| `remove(x)`    | Remove first occurrence              | `lst.remove("apple")`                  |
| `pop([i])`     | Remove & return item (default: last) | `lst.pop()`, `lst.pop(0)`              |
| `clear()`      | Remove all items                     | `lst.clear()`                          |
| `index(x)`     | Find index of item                   | `lst.index("apple")`                   |
| `count(x)`     | Count occurrences                    | `lst.count("a")`                       |
| `sort()`       | Sort in place                        | `lst.sort()`, `lst.sort(reverse=True)` |
| `reverse()`    | Reverse in place                     | `lst.reverse()`                        |
| `copy()`       | Shallow copy                         | `new = lst.copy()`                     |

```python
# Examples
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.append(7)              # [3, 1, 4, 1, 5, 9, 2, 6, 7]
nums.extend([8, 9])         # [..., 7, 8, 9]
nums.insert(0, 0)           # [0, 3, 1, 4, ...]
nums.remove(1)              # Removes first 1
last = nums.pop()           # Removes and returns last item
first = nums.pop(0)         # Removes and returns first item
nums.sort()                 # Sorts in place
nums.reverse()              # Reverses in place

# Sorting with key
words = ["banana", "apple", "Cherry"]
words.sort()                        # ['Cherry', 'apple', 'banana']
words.sort(key=str.lower)           # ['apple', 'banana', 'Cherry']
words.sort(key=len)                 # ['apple', 'Cherry', 'banana']

# sorted() returns new list (doesn't modify original)
sorted_nums = sorted(nums)
sorted_nums_desc = sorted(nums, reverse=True)
```

### List Comprehensions {need more explanation}

```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With if-else: [expr1 if condition else expr2 for item in iterable]
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]
```

### List Operations

```python
# Concatenation
[1, 2] + [3, 4]         # [1, 2, 3, 4]

# Repetition
[0] * 5                 # [0, 0, 0, 0, 0]
[1, 2] * 3              # [1, 2, 1, 2, 1, 2]

# Membership
3 in [1, 2, 3]          # True
5 not in [1, 2, 3]      # True

# Length
len([1, 2, 3])          # 3

# Comparison
[1, 2] == [1, 2]        # True
[1, 2] < [1, 3]         # True (compares element by element)
```

---

## 2. Dictionaries { }

Key-value pairs with fast lookups. Keys must be immutable (strings, numbers, tuples).

### Creating Dictionaries

```python
# Empty dict
empty = {}
empty = dict()

# With initial values
user = {
    "name": "Fana",
    "age": 25,
    "city": "Johannesburg",
    "skills": ["Python", "JavaScript"]
}

# From list of tuples
d = dict([("a", 1), ("b", 2), ("c", 3)])

# From keyword arguments
d = dict(name="Fana", age=25)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# fromkeys (same value for all keys)
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)      # {"a": 0, "b": 0, "c": 0}
```

### Accessing & Modifying

```python
user = {"name": "Fana", "age": 25}

# Access by key
user["name"]                    # "Fana"
user["email"]                   # KeyError!

# Safe access with .get()
user.get("name")                # "Fana"
user.get("email")               # None (no error)
user.get("email", "N/A")        # "N/A" (default value)

# Add or modify
user["email"] = "fana@example.com"  # Add new key
user["age"] = 26                    # Modify existing

# Delete
del user["email"]               # Remove key
removed = user.pop("age")       # Remove & return value (26)
user.pop("missing", None)       # No error with default
last = user.popitem()           # Remove & return last item

# Check key exists
"name" in user                  # True
"email" not in user             # True
```

### Dictionary Methods

| Method                     | Description               | Returns            |
| -------------------------- | ------------------------- | ------------------ |
| `keys()`                   | All keys                  | dict_keys view     |
| `values()`                 | All values                | dict_values view   |
| `items()`                  | Key-value pairs           | dict_items view    |
| `get(key, default)`        | Get value or default      | value or default   |
| `pop(key, default)`        | Remove & return value     | value or default   |
| `popitem()`                | Remove & return last item | (key, value) tuple |
| `update(other)`            | Merge another dict        | None               |
| `setdefault(key, default)` | Get or set default        | value              |
| `clear()`                  | Remove all items          | None               |
| `copy()`                   | Shallow copy              | new dict           |

```python
user = {"name": "Fana", "age": 25}

# Get keys, values, items
list(user.keys())       # ["name", "age"]
list(user.values())     # ["Fana", 25]
list(user.items())      # [("name", "Fana"), ("age", 25)]

# update - merge dictionaries
user.update({"city": "JHB", "age": 26})
# {"name": "Fana", "age": 26, "city": "JHB"}

# Python 3.9+ merge operators
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2        # {"a": 1, "b": 3, "c": 4}
d1 |= d2                # In-place merge

# setdefault - get or set
user.setdefault("country", "South Africa")  # Adds if missing
user.setdefault("name", "Unknown")          # Returns "Fana" (exists)
```

### Iterating Over Dictionaries

```python
user = {"name": "Fana", "age": 25, "city": "Johannesburg"}

# Keys (default)
for key in user:
    print(key)

# Values
for value in user.values():
    print(value)

# Both key and value
for key, value in user.items():
    print(f"{key}: {value}")

# With index
for i, (key, value) in enumerate(user.items()):
    print(f"{i}. {key}: {value}")
```

### Nested Dictionaries

```python
users = {
    "user1": {"name": "Fana", "age": 25},
    "user2": {"name": "Bongani", "age": 30}
}

# Access nested
users["user1"]["name"]          # "Fana"

# Safe nested access
users.get("user3", {}).get("name", "Unknown")

# Add to nested
users["user1"]["city"] = "JHB"

# Iterate nested
for user_id, user_data in users.items():
    print(f"{user_id}: {user_data['name']}")
```

---

## 3. Sets { }

Unordered collections of unique elements. Great for membership testing and removing duplicates.

### Creating Sets

```python
# Empty set (NOT {} - that's a dict!)
empty = set()

# With values
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}      # Different types OK

# From other iterables
from_list = set([1, 2, 2, 3, 3, 3])     # {1, 2, 3}
from_string = set("hello")               # {'h', 'e', 'l', 'o'}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

### Basic Operations

```python
s = {1, 2, 3}

# Add elements
s.add(4)                # {1, 2, 3, 4}
s.add(2)                # {1, 2, 3, 4} (no duplicates)
s.update([5, 6, 7])     # Add multiple: {1, 2, 3, 4, 5, 6, 7}

# Remove elements
s.remove(4)             # Removes 4 (KeyError if not found)
s.discard(10)           # Removes if exists (no error if missing)
item = s.pop()          # Remove and return arbitrary element
s.clear()               # Remove all

# Membership (very fast!)
3 in {1, 2, 3}          # True
5 not in {1, 2, 3}      # True

# Length
len({1, 2, 3})          # 3
```

### Set Operations

| Operation      | Method                      | Operator | Result                 |
| -------------- | --------------------------- | -------- | ---------------------- |
| Union          | `a.union(b)`                | `a \| b` | All elements from both |
| Intersection   | `a.intersection(b)`         | `a & b`  | Common elements        |
| Difference     | `a.difference(b)`           | `a - b`  | In a, not in b         |
| Symmetric Diff | `a.symmetric_difference(b)` | `a ^ b`  | In either, not both    |
| Subset         | `a.issubset(b)`             | `a <= b` | Is a contained in b?   |
| Superset       | `a.issuperset(b)`           | `a >= b` | Does a contain b?      |
| Disjoint       | `a.isdisjoint(b)`           | -        | No common elements?    |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union - all unique elements
a | b                   # {1, 2, 3, 4, 5, 6}
a.union(b)              # {1, 2, 3, 4, 5, 6}

# Intersection - common elements
a & b                   # {3, 4}
a.intersection(b)       # {3, 4}

# Difference - in a but not in b
a - b                   # {1, 2}
a.difference(b)         # {1, 2}
b - a                   # {5, 6}

# Symmetric difference - in either but not both
a ^ b                   # {1, 2, 5, 6}
a.symmetric_difference(b)   # {1, 2, 5, 6}

# Subset / Superset
{1, 2} <= {1, 2, 3}     # True (subset)
{1, 2, 3} >= {1, 2}     # True (superset)
{1, 2} < {1, 2, 3}      # True (proper subset)

# Disjoint - no common elements
{1, 2}.isdisjoint({3, 4})   # True
{1, 2}.isdisjoint({2, 3})   # False
```

### Common Use Cases

```python
# Remove duplicates from list
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))     # [1, 2, 3, 4]

# Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))  # [3, 4]

# Find unique to first list
only_in_list1 = list(set(list1) - set(list2))  # [1, 2]

# Check if all elements are unique
def all_unique(lst):
    return len(lst) == len(set(lst))
```

### Frozen Sets (Immutable)

```python
# Immutable set - can be used as dict key or in other sets
fs = frozenset([1, 2, 3])

# Can't modify
fs.add(4)               # AttributeError!

# Can use as dict key
d = {frozenset([1, 2]): "value"}
```

---

## 4. Tuples ( )

Ordered, immutable sequences. Use when data shouldn't change.

### Creating Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# With values
point = (10, 20)
rgb = (255, 128, 0)
mixed = (1, "hello", 3.14)

# Single element (comma required!)
single = (1,)           # Tuple
not_tuple = (1)         # Just integer 1!

# Without parentheses
coords = 10, 20, 30     # Also a tuple!

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("abc")  # ('a', 'b', 'c')
```

### Accessing Tuples

```python
t = (1, 2, 3, 4, 5)

# Same as lists (but can't modify!)
t[0]            # 1
t[-1]           # 5
t[1:4]          # (2, 3, 4)
t[::-1]         # (5, 4, 3, 2, 1)

# Only 2 methods
t.count(3)      # Count occurrences of 3
t.index(3)      # Find index of 3
```

### Tuple Unpacking

```python
# Basic unpacking
point = (10, 20)
x, y = point            # x=10, y=20

# Multiple values
data = ("Fana", 25, "Johannesburg")
name, age, city = data

# Swap values
a, b = b, a

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

*start, last = (1, 2, 3, 4, 5)
# start = [1, 2, 3, 4], last = 5

first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5

# Ignore values with _
x, _, z = (1, 2, 3)     # Ignore middle value
_, *rest = (1, 2, 3, 4) # Ignore first

# Function returns
def get_user():
    return "Fana", 25   # Returns tuple

name, age = get_user()
```

### Named Tuples

```python
from collections import namedtuple

# Create a named tuple class
Point = namedtuple("Point", ["x", "y"])
Person = namedtuple("Person", "name age city")  # String also works

# Create instances
p = Point(10, 20)
user = Person("Fana", 25, "Johannesburg")

# Access by name or index
p.x                     # 10
p[0]                    # 10
user.name               # "Fana"
user[0]                 # "Fana"

# Still immutable
p.x = 30               # AttributeError!

# Convert to dict
user._asdict()          # {'name': 'Fana', 'age': 25, 'city': 'Johannesburg'}
```

---

## 5. Common Built-in Functions

| Function        | Description              | Example                                 |
| --------------- | ------------------------ | --------------------------------------- |
| `len(x)`        | Number of elements       | `len([1,2,3])` → `3`                    |
| `sum(x)`        | Sum of elements          | `sum([1,2,3])` → `6`                    |
| `min(x)`        | Smallest element         | `min([3,1,2])` → `1`                    |
| `max(x)`        | Largest element          | `max([3,1,2])` → `3`                    |
| `sorted(x)`     | Return sorted copy       | `sorted([3,1,2])` → `[1,2,3]`           |
| `reversed(x)`   | Return reversed iterator | `list(reversed([1,2,3]))`               |
| `enumerate(x)`  | Index-value pairs        | `list(enumerate(['a','b']))`            |
| `zip(a, b)`     | Combine iterables        | `list(zip([1,2], ['a','b']))`           |
| `any(x)`        | Any element True?        | `any([False, True])` → `True`           |
| `all(x)`        | All elements True?       | `all([True, True])` → `True`            |
| `filter(fn, x)` | Filter by function       | `list(filter(lambda x: x>0, [-1,0,1]))` |
| `map(fn, x)`    | Apply function to all    | `list(map(str, [1,2,3]))`               |

```python
# zip - combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
# letters = ('a', 'b', 'c'), numbers = (1, 2, 3)

# enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# any / all
numbers = [1, 2, 0, 4]
any(numbers)            # True (at least one truthy)
all(numbers)            # False (0 is falsy)

# filter / map
numbers = [-2, -1, 0, 1, 2]
positives = list(filter(lambda x: x > 0, numbers))  # [1, 2]
doubled = list(map(lambda x: x * 2, numbers))       # [-4, -2, 0, 2, 4]
```

---

## 💡 Pro Tips

1. **Use list** for ordered, changeable data; **tuple** for fixed data like coordinates

2. **Use dict** for key-value mapping; **set** for unique elements and fast membership testing

3. **List comprehensions** are faster and more Pythonic than loops for transforming data

4. **Use `.get(key, default)`** on dicts to avoid KeyError

5. **`set()`** for empty set, not `{}` (that's an empty dict!)

6. **Use `enumerate()`** instead of `range(len(list))` when you need both index and value

7. **Tuple unpacking** makes code cleaner: `x, y = point` instead of `x = point[0]`

8. **Named tuples** are great when you need lightweight, immutable objects with named fields

9. **Use `in`** for membership testing - it's very fast for sets and dicts (O(1)), slower for lists (O(n))

10. **Copy carefully**: `new_list = old_list` creates a reference, use `old_list.copy()` or `old_list[:]` for a shallow copy

---

_Created for W Chats Marketplace_
