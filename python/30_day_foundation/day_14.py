"""
PART 1: DICTIONARIES

> “Facts about something”
> “Given a name, get the value”

Use when:

* Values have meaning
* Order does not matter
* You want fast lookup

Problem 1 — Read values
Problem 2 — Update a value
Problem 3 — Add a new fact
Problem 4 — Count occurrences
"""

# Problem 1 — Read values
person = {
    "name": "Fana",
    "age": 27,
    "city": "Johannesburg"
}

print(person["name"])
print(person["city"])


# Problem 2 — Update a value
player = {
    "name": "Katlego",
    "score": 10
}

player["score"] = 15


# Problem 3 — Add a new fact
task = {
    "title": "Learn Python",
    "priority": "High"
}

task["completed"] = True


# Problem 4 — Count occurrences
word = "banana"

counts = {}

for char in word:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

print(counts)


"""
PART 2: TUPLES (4 problems)

> “Fixed structure”
> “Known shape, fixed positions”

Use when:

* Order matters
* Values belong together
* Structure does not change
Problem 5 — Access by position
Problem 6 — Tuple unpacking
Problem 7 — Fixed return values
Problem 8 — Loop through tuples
"""

# Problem 5 — Access by position
point = (10, 25)

x = point[0]
y = point[1]

print(x)
print(y)


# Problem 6 — Tuple unpacking
record = ("Fana", 85)

name, score = record


# Problem 7 — Fixed return values
dimensions = (1920, 1080)

def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()

# Problem 8 — Loop through tuples
weather = [
    ("Johannesburg", 25),
    ("Cape Town", 18),
    ("Durban", 22)
]

city = weather[("Johannesburg", "Cape Town", "Durban")]
temparature =  weather[(25, 18, 22)]

for city, temperature in weather:
    print(city, temperature)


"""
PART 3: SETS (4 problems)

> “Unique items only”
> “Is it in or out?”

Use when:

* Duplicates don’t matter
* Membership checks matter
* Order is irrelevant

Problem 9 — Remove duplicates
Problem 10 — Membership check
Problem 11 — Track seen items
Problem 12 — Validate against allowed values
"""

# Problem 9 — Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
new_numbers = set(numbers)

# Problem 10 — Membership check
roles = {"user", "editor", "admin"}

"user" in roles #True
"exit" not in roles #True

# Problem 11 — Track seen items
word = "mississippi"
seen = set()

for char in word:
    seen.add(char)

print(seen)


# Problem 12 — Validate against allowed values
days = ["Monday", "Friday", "Funday", "Sunday"]
allowed_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
is_valid = True

for day in days:
    if day not in allowed_days:
        is_valid = False
        break

print(is_valid)
