"""
Day 8 — Simple Decisions

Problems

Grade calculator

Age category classifier

Password length checker

Focus

Order of conditions

Edge cases
"""

# Grade calculator
grades = [35, 93, 82, 86, 52, 48, 74, 66]
grade_labels = []

for grade in grades:
    if grade >= 75:
        grade_labels.append("Distinction")
    elif grade >= 50:
        grade_labels.append("Pass")
    else:
        grade_labels.append("Fail")

print(grade_labels)


# Age category classifier
ages = [2, 7, 13, 24, 40, 85]
age_classified = []

for age in ages:
    if age < 5:
        age_classified.append("toddler")
    elif age < 12:
        age_classified.append("young")
    elif age < 18:
        age_classified.append("teenager")
    elif age < 35:
        age_classified.append("young_adult")
    elif age < 65:
        age_classified.append("middle_aged")
    else:
        age_classified.append("elderly")

print(age_classified)


# Password length checker
password = "Iaod89832b"

if len(password) < 8:
    print("Weak password")
elif len(password) < 12:
    print("Moderate password")
else:
    print("Strong password")




"""
Rules You Must Lock In for Decisions
Rule 1: Compare the Item, Not the Collection

Always:

for x in items: → compare x, never items

Rule 2: Avoid This Pattern Entirely
elif age > 5 < 12   # ❌ wrong mental model


Instead, think:

elif age < 12      # ✅ previous conditions already failed

Rule 3: Order Is Part of the Logic

This is valid:

if age < 5
elif age < 12
elif age < 18


This is broken:

if age < 18
elif age < 5


Even if conditions are “true”, order controls behavior.

Rule 4: Decisions Produce One Outcome Per Input

If you find yourself:

appending multiple categories

unsure which branch runs

You have violated the decision contract.

4. Why Day 8 Feels Tricky

Because humans think:

“Check all conditions”

Programs think:

“Take the first valid exit”

This is a mindset shift, not a syntax issue.

5. One Sentence to Carry Forward

A decision problem is about choosing one path, not evaluating all possibilities.

You are progressing exactly as expected.
Day 9 (nested decisions + validation) will feel easier once this ordering rule sticks.
"""