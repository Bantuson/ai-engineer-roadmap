"""
Day 18 — Multiple Aggregations

Problems

Word frequency counter

Sentence analyzer

Log summary

Focus

Parallel state tracking
"""

# Word frequency counter
text = "python is fun and python is powerful"

words = text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print(word_counts)


#  Word frequency counter as function
def frequency_counter(text):
    words = text.split()
    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts += 1

    return word_counts



# Sentence analyzer
sentence = "Learning python takes time"

char_count = 0
word_count = 0
vowel_count = 0
vowels = "aeiou"

words = sentence.split()
word_count = len(words)

for char in sentence:
    char_count += 1
    if char.lower() in vowels:
        vowel_count += 1

print(char_count)
print(word_count)
print(vowel_count)

# Sentence analyzer as function
def character_counter(sentence):
    char_count = 0

    for char in sentence:
        char_count += 1

    return char_count

def word_counter(sentence):
    words = sentence.split()
    return len(words)


def vowel_counter(sentence):
    vowel_count = 0
    vowels = "aeiou"

    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count


def sentence_analyzer(sentence):
    analysis = {}

    analysis["characters"] = character_counter(sentence)
    analysis["words"] = word_counter(sentence)
    analysis["vowels"] = vowel_counter(sentence)

    return analysis



# Log summary
logs = ["INFO", "ERROR", "INFO", "WARNING", "ERROR"]
summary = {}

for entry in logs:
    if entry not in summary:
        summary[entry] = 1
    else:
        summary[entry] += 1

print(summary)

# Log summary as function
def entry_logs(logs):
    summary = {}

    for entry in logs:
        if entry not in summary:
            summary[entry] = 1
        else:
            summary[entry] += 1

    return summary
