"""
Day 4 — Filter (Text Rules)

Problems

Keep words longer than 5 characters

Extract vowels from a string

Remove punctuation (basic)

Focus

Rule-based filtering

Character inspection
"""

# Keep words longer than 5 characters
words = ["Tom", "Luke", "Jamesone", "Robenson", "Johnson"]
longer_words = []

for word in words:
    if len(word) > 5:
        longer_words.append(word)

print(longer_words)


# Extract vowels from a string
string = "Mfanafuthi"
vowels = "aeiou"
vowels_string = ""

for char in string:
    if char.lower() in vowels:
        vowels_string += char
        
print(vowels_string)


# Remove punctuation
text = "python revision"
panctuation = "!,.?"
text_no_panctuation = ""

for char in text:
    if char not in panctuation:
        text_no_panctuation += char

print(text_no_panctuation)
        
