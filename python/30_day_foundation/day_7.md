## MICRO-DRILLS: DICTIONARIES

### Drill 1 — Read

**Mental model:** “Given a name, get a fact.”

```python
person = {"name": "Fana", "age": 27}
print(person["age"])
```

---

### Drill 2 — Update

**Mental model:** “Change a known fact.”

```python
player = {"score": 10}
player["score"] += 5
print(player)
```

---

### Drill 3 — Add

**Mental model:** “Introduce a new fact.”

```python
task = {}
task["title"] = "Learn Python"
task["done"] = False
print(task)
```

---

### Drill 4 — Count (FOUNDATIONAL)

**Mental model:** “Each key remembers its own total.”

```python
word = "apple"
counts = {}

for char in word:
    counts[char] = counts.get(char, 0) + 1

print(counts)
```

Stop here and notice:

- **No lists**
- **No searching**
- Key = thing being counted

---

## MICRO-DRILLS: TUPLES

### Drill 5 — Fixed position

**Mental model:** “I know what lives at index 0 and 1.”

```python
point = (4, 9)
x = point[0]
y = point[1]
print(x, y)
```

---

### Drill 6 — Unpacking

**Mental model:** “Split structure into variables.”

```python
user = ("Fana", 27)
name, age = user
print(name)
```

---

### Drill 7 — Return multiple values

**Mental model:** “Functions can return a package.”

```python
def get_min_max():
    return 3, 10

low, high = get_min_max()
print(low, high)
```

---

### Drill 8 — Loop unpacking

**Mental model:** “Each item has a fixed shape.”

```python
pairs = [("a", 1), ("b", 2)]

for letter, number in pairs:
    print(letter, number)
```

---

## MICRO-DRILLS: SETS

### Drill 9 — Remove duplicates

**Mental model:** “Uniqueness enforced.”

```python
nums = [1, 1, 2, 3]
unique = set(nums)
print(unique)
```

---

### Drill 10 — Membership

**Mental model:** “Is it allowed?”

```python
roles = {"admin", "user"}

if "admin" in roles:
    print("Access granted")
```

---

### Drill 11 — Track seen

**Mental model:** “Have I seen this before?”

```python
seen = set()

for char in "hello":
    seen.add(char)

print(seen)
```

---

### Drill 12 — Validate list

**Mental model:** “All must belong.”

```python
allowed = {"A", "B", "C"}
items = ["A", "C", "B"]

is_valid = True
for item in items:
    if item not in allowed:
        is_valid = False

print(is_valid)
```

---

# PART B — DAY 17 **LITE**

### (No helpers. No validation functions. No abstraction.)

We focus on **data first**, logic second.

---

## DAY 17 LITE — TODO LIST

**Mental model:** “A todo is just stored information.”

```python
todo = []

todo.append("Buy milk")
todo.append("Study Python")

print(todo)
```

That’s it. No functions yet.

---

## DAY 17 LITE — SHOPPING CART

**Mental model:** “Each product has a price.”

```python
cart = {}

cart["bread"] = 15
cart["milk"] = 12

total = 0
for price in cart.values():
    total += price

print(total)
```

Key insight:

- Dictionary stores **facts**
- Loop processes **values**

---

## DAY 17 LITE — SCORE TRACKER

**Mental model:** “Each name remembers its score.”

```python
scores = {}

scores["Fana"] = 0
scores["Fana"] += 10
scores["Fana"] += 5

print(scores)
```

This is **the same pattern as counting**.

---

# CORE CLARITY: DICT COUNTING vs LIST COUNTING

### LIST COUNTING = searching

- You must _find_ where the item lives
- You must _keep indexes aligned_
- High mental load

### DICT COUNTING = remembering

- The key _is_ the item
- The value _is_ the memory
- Direct access

**This is why dictionaries exist.**

---

# FINAL MENTAL CHECKLIST (USE THIS DAILY)

Before writing code, ask:

1. Am I storing **many things**? → List
2. Am I storing **facts about something**? → Dict
3. Is the structure **fixed**? → Tuple
4. Do I only care if something **exists**? → Set

If you answer this correctly, the code almost writes itself.

---

You are not struggling because you are “bad at Python”.
You are struggling because you are **learning to think structurally** — that takes time.

Next step (when ready):

- Day 17 **Medium** (same problems, single function only)
- Or **counting mastery drills** (the most important skill here)

Just tell me which one.
