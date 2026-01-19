# Python Proficiency for AI Engineers

## Overview

AI Engineer interviews test Python skills beyond basic syntax. You need to demonstrate:
- Data structure fluency
- Functional programming patterns
- Library ecosystem knowledge
- Clean, production-quality code

## Core Competencies

### 1. Data Structures

**Lists and Comprehensions**
```python
# List comprehension
squares = [x**2 for x in range(10)]

# Filtered comprehension
evens = [x for x in range(20) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]

# Dictionary comprehension
word_lengths = {word: len(word) for word in words}
```

**Dictionaries**
```python
# Common operations
d = {}
d.setdefault(key, []).append(value)  # Avoid KeyError
d.get(key, default_value)            # Safe access

# Merging (Python 3.9+)
merged = dict1 | dict2

# Counter for frequency
from collections import Counter
freq = Counter(text.split())
most_common = freq.most_common(10)
```

**Sets**
```python
# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

intersection = a & b  # {2, 3}
union = a | b         # {1, 2, 3, 4}
difference = a - b    # {1}
symmetric = a ^ b     # {1, 4}
```

### 2. Functions

**Args and Kwargs**
```python
def flexible_function(required, *args, **kwargs):
    """Accept any number of positional and keyword arguments."""
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

# Usage
flexible_function("must have", 1, 2, 3, option="value")
```

**Lambda and Higher-Order Functions**
```python
# Lambda
square = lambda x: x**2

# Map
doubled = list(map(lambda x: x*2, numbers))

# Filter
positives = list(filter(lambda x: x > 0, numbers))

# Sorted with key
sorted_by_length = sorted(words, key=lambda w: len(w))

# Reduce
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)
```

**Decorators**
```python
import functools
import time

def timer(func):
    """Measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### 3. Error Handling

```python
def safe_process(data):
    """Demonstrate proper error handling."""
    try:
        result = risky_operation(data)
    except ValueError as e:
        # Handle specific exception
        logger.warning(f"Invalid value: {e}")
        return None
    except Exception as e:
        # Handle unexpected exceptions
        logger.error(f"Unexpected error: {e}")
        raise
    else:
        # Runs if no exception
        return result
    finally:
        # Always runs (cleanup)
        cleanup()
```

### 4. File Operations

```python
# Context manager (recommended)
with open("file.txt", "r") as f:
    content = f.read()

# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        process(row)
```

### 5. Generators

```python
def read_large_file(filepath):
    """Memory-efficient file reading."""
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Generator expression
squares_gen = (x**2 for x in range(1000000))
# Uses almost no memory until iterated

# Practical example: batch processing
def batch_items(items, batch_size):
    """Yield batches of items."""
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
```

## AI-Specific Python Skills

### Working with APIs

```python
import requests
import os

def call_llm_api(prompt: str) -> str:
    """Example API call pattern."""
    api_key = os.environ.get("API_KEY")

    response = requests.post(
        "https://api.example.com/v1/chat",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "model-name",
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=30
    )

    response.raise_for_status()  # Raise on HTTP errors
    return response.json()["choices"][0]["message"]["content"]
```

### Async for Concurrent Calls

```python
import asyncio
import aiohttp

async def fetch_completion(session, prompt):
    """Async API call."""
    async with session.post(
        "https://api.example.com/v1/chat",
        json={"prompt": prompt}
    ) as response:
        return await response.json()

async def batch_completions(prompts):
    """Process multiple prompts concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_completion(session, p) for p in prompts]
        return await asyncio.gather(*tasks)

# Usage
results = asyncio.run(batch_completions(prompts))
```

### Data Processing with Pandas

```python
import pandas as pd

# Load and explore
df = pd.read_csv("data.csv")
df.info()
df.describe()

# Filter and transform
filtered = df[df["score"] > 0.8]
df["normalized"] = (df["value"] - df["value"].mean()) / df["value"].std()

# Group and aggregate
summary = df.groupby("category").agg({
    "value": ["mean", "std", "count"],
    "score": "max"
})

# Apply custom functions
df["processed"] = df["text"].apply(lambda x: process_text(x))
```

### Vector Operations with NumPy

```python
import numpy as np

# Embeddings similarity
def cosine_similarity(a, b):
    """Calculate cosine similarity between vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Batch similarity
def batch_cosine_similarity(query_vec, doc_vecs):
    """Efficient batch cosine similarity."""
    # Normalize
    query_norm = query_vec / np.linalg.norm(query_vec)
    doc_norms = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)

    # Dot product gives cosine similarity for normalized vectors
    return np.dot(doc_norms, query_norm)
```

## Common Interview Questions

### 1. Implement a Simple LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### 2. Token Counter

```python
def count_tokens(text: str, tokenizer=None) -> int:
    """Count tokens in text."""
    if tokenizer:
        return len(tokenizer.encode(text))
    # Simple approximation: ~4 chars per token
    return len(text) // 4
```

### 3. Retry with Exponential Backoff

```python
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """Retry a function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed, retrying in {delay:.2f}s")
            time.sleep(delay)
```

## Interview Tips

1. **Write clean code** - Use descriptive names, add docstrings
2. **Handle edge cases** - Empty inputs, None values
3. **Consider efficiency** - Time and space complexity
4. **Test as you go** - Walk through examples
5. **Know the ecosystem** - requests, pandas, numpy, etc.

## Practice Problems

1. Implement a text chunker that splits text while respecting word boundaries
2. Create a rate limiter decorator
3. Build a simple prompt template system
4. Implement batch processing with error handling
5. Create a function that deduplicates similar strings using embeddings

## Next Steps

- [02-frameworks-knowledge.md](02-frameworks-knowledge.md) - AI frameworks
- [03-prompt-engineering.md](03-prompt-engineering.md) - Prompting skills
