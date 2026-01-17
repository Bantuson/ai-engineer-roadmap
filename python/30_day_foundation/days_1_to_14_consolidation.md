# CONSOLIDATION DRILL — DAYS 1–13

## Master Pattern 1 — Transform

**(Days 1–2)**

> “For every item, produce a new item.”

### Template

```python
def transform(items):
    result = []
    for item in items:
        result.append(process(item))
    return result
```

### Use when:

- Doubling numbers
- Uppercasing strings
- Converting units

---

## Master Pattern 2 — Filter

**(Days 3–4)**

> “Keep some items, discard others.”

### Template

```python
def filter_items(items):
    result = []
    for item in items:
        if condition(item):
            result.append(item)
    return result
```

### Use when:

- Extracting evens
- Removing punctuation
- Keeping long words

---

## Master Pattern 3 — Aggregate (Count / Sum)

**(Day 5)**

> “Collapse many items into one value.”

### Template

```python
def aggregate(items):
    total = 0
    for item in items:
        if condition(item):
            total += 1
    return total
```

### Use when:

- Counting vowels
- Counting words
- Counting values above a threshold

---

## Master Pattern 4 — Aggregate (Best So Far)

**(Day 6)**

> “Track the best candidate seen so far.”

### Template

```python
def best_item(items):
    best = items[0]
    for item in items:
        if better(item, best):
            best = item
    return best
```

### Use when:

- Largest number
- Shortest word
- Most frequent letter

---

## Master Pattern 5 — Rule Systems

**(Days 8–9)**

> “Multiple conditions decide outcomes.”

### Template

```python
def rules(input):
    if rule_1:
        return outcome_1
    elif rule_2:
        return outcome_2
    else:
        return default
```

### Use when:

- Grades
- Age categories
- Discounts
- Login validation

---

## Master Pattern 6 — Input → Process → Output

**(Day 10)**

> “Explicit inputs, predictable outputs.”

### Template

```python
def program(input):
    processed = logic(input)
    return processed
```

### Use when:

- Calculators
- Converters
- Validators

---

## Master Pattern 7 — Loop + State

**(Day 11)**

> “Run until exit.”

### Template

```python
def loop_system(commands):
    state = initial
    while condition:
        state = update(state)
    return state
```

### Use when:

- Menus
- Repeating actions
- Exit conditions

---

## Master Pattern 8 — Simulation

**(Days 12–13)**

> “State changes over time.”

### Template

```python
def simulate(initial):
    state = initial
    history = []

    while not finished(state):
        history.append(state)
        state = next_state(state)

    return history
```

### Use when:

- Games
- Countdown timers
- Turn-based systems

---

## One Drill (do this once, slowly)

Take **any new problem** and answer **before coding**:

1. Is this Transform, Filter, Aggregate, Rule, or Simulation?
2. What is the **state**?
3. What changes?
4. What ends it?

If you can answer those, the code is mechanical.

---

## The key realization you just earned

You are no longer learning _problems_.

You are learning **shapes of problems**.

From here on:

- New days won’t feel like new skills
- They’ll feel like **new combinations**

That’s the turning point.

---
