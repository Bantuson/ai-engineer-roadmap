— Data Structures Foundations

---

## PART 1: DICTIONARIES (4 problems)

### Mental Model — Dictionary

> “Facts about something”
> “Given a name, get the value”

Use when:

- Values have meaning
- Order does not matter
- You want fast lookup

---

### Problem 1 — Read values

**Task:** Print the name and city.

```python
person = {
    "name": "Fana",
    "age": 27,
    "city": "Johannesburg"
}

print(person["name"])
print(person["city"])
```

**Focus:**

- Access by key
- No loops

---

### Problem 2 — Update a value

**Task:** Increase the score by 5.

```python
player = {
    "name": "Katlego",
    "score": 10
}

player["score"] = 15
```

**Focus:**

- Mutating dictionary state

---

### Problem 3 — Add a new fact

**Task:** Add `"completed": True`

```python
task = {
    "title": "Learn Python",
    "priority": "High"
}

task["completed"] = "True"
```

**Focus:**

- Expanding state

---

### Problem 4 — Count occurrences

**Task:** Count how many times each letter appears.

```python
word = "banana"

counts = {}

for char in word:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

print(counts)

```

**Focus:**

- Dictionary as counter
- Initialize vs update

---

## PART 2: TUPLES (4 problems)

### Mental Model — Tuple

> “Fixed structure”
> “Known shape, fixed positions”

Use when:

- Order matters
- Values belong together
- Structure does not change

---

### Problem 5 — Access by position

**Task:** Print x and y.

```python
point = (10, 25)

x = point[0]
y = point[1]
print(x)
print(y)
```

**Focus:**

- Index-based access

---

### Problem 6 — Tuple unpacking

**Task:** Assign name and score.

```python
record = ("Fana", 85)

name, score = record
```

**Focus:**

- Unpacking syntax
- Readability

---

### Problem 7 — Fixed return values

**Task:** Store width and height.

```python
dimensions = (1920, 1080)
width = dimensions[0]
height = dimensions[1]
```

**Focus:**

- Grouping related values

---

### Problem 8 — Loop through tuples

**Task:** Print each city and temperature.

```python
weather = [
    ("Johannesburg", 25),
    ("Cape Town", 18),
    ("Durban", 22)
]

city = weather[()]
```

**Focus:**

- Tuples inside lists
- Structured iteration

---

## PART 3: SETS (4 problems)

### Mental Model — Set

> “Unique items only”
> “Is it in or out?”

Use when:

- Duplicates don’t matter
- Membership checks matter
- Order is irrelevant

---

### Problem 9 — Remove duplicates

**Task:** Remove duplicate numbers.

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

**Focus:**

- Set creation
- Deduplication

---

### Problem 10 — Membership check

**Task:** Check if `"admin"` is allowed.

```python
roles = {"user", "editor", "admin"}
```

**Focus:**

- `in` keyword
- Boolean thinking

---

### Problem 11 — Track seen items

**Task:** Print only unique letters.

```python
word = "mississippi"
```

**Focus:**

- Set as memory
- Ignore repeats

---

### Problem 12 — Validate against allowed values

**Task:** Print valid days only.

```python
days = ["Monday", "Friday", "Funday", "Sunday"]
allowed_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
```

**Focus:**

- Filtering using sets

---

## How to Approach Each Problem (Repeat This)

Before coding, say:

1. **What is the container?**
2. **Do values have names?**
3. **Does order matter?**
4. **Do duplicates matter?**
5. **Is structure fixed?**

Then choose:

- List
- Dict
- Tuple
- Set

---

## Why This Works

This day:

- Removes abstraction pressure
- Builds intuition
- Creates muscle memory
- Makes Day 17 feel _reasonable_

You are now learning **data modeling**, not just Python.

---

### Next Step Options

1. You attempt Day 16.5 — I review line-by-line
2. We refactor earlier list problems using dicts/sets
3. We resume Day 17 slowly with **only one problem**

Tell me how you want to proceed.
