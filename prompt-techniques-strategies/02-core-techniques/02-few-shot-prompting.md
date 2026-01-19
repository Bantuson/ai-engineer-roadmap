# Few-Shot Prompting

## Overview

Few-shot prompting provides examples to guide the model's behavior. This technique dramatically improves performance on tasks where the desired format, style, or reasoning pattern isn't obvious from instructions alone.

## The Few-Shot Spectrum

```
┌─────────────────────────────────────────────────────────────────┐
│                      SHOT SPECTRUM                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zero-shot    One-shot    Few-shot     Many-shot               │
│   (0 examples) (1 example) (2-5 examples) (6+ examples)         │
│                                                                  │
│   ←─────────────────────────────────────────────────────→       │
│   Less token usage                    More consistent output    │
│   Faster responses                    Better edge case handling │
│   May miss nuances                    Higher token cost         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Few-Shot Patterns

### Pattern 1: Input-Output Pairs

```
Convert temperatures from Celsius to Fahrenheit.

Example 1:
Input: 0°C
Output: 32°F

Example 2:
Input: 100°C
Output: 212°F

Example 3:
Input: -40°C
Output: -40°F

Now convert:
Input: 25°C
Output:
```

### Pattern 2: Labeled Examples

```
Classify these customer inquiries:

[Example]
Inquiry: "I was charged twice for my subscription"
Category: Billing

[Example]
Inquiry: "The app crashes when I upload images"
Category: Technical

[Example]
Inquiry: "How do I change my password?"
Category: Account

[Classify]
Inquiry: "My payment didn't go through but my card was charged"
Category:
```

### Pattern 3: Before/After Examples

```
Improve these product descriptions to be more engaging:

[Before]
This is a blue t-shirt made of cotton. It comes in sizes S, M, L, XL.

[After]
Dive into comfort with our classic blue tee. Crafted from 100% breathable cotton, this wardrobe essential moves with you from morning coffee to evening adventures. Available in S through XL.

[Before]
This laptop has 16GB RAM and a 512GB SSD. It has a 14-inch screen.

[After]
```

### Pattern 4: Reasoning Demonstration

```
Evaluate these startup pitches:

[Example]
Pitch: "An app that reminds you to drink water"
Analysis: The market for hydration apps is saturated. Differentiation is unclear. Low barrier to entry means easy competition. However, health and wellness is growing.
Rating: 4/10 - Needs unique angle

[Example]
Pitch: "AI that predicts equipment failures in factories"
Analysis: Clear B2B value proposition. High switching costs once adopted. Growing Industry 4.0 trend. Requires domain expertise creating moat.
Rating: 8/10 - Strong potential with right team

[Evaluate]
Pitch: "A platform connecting pet owners with local pet sitters"
Analysis:
Rating:
```

## Example Selection

### Quality Over Quantity

```
PRINCIPLE: Well-chosen examples beat more examples

❌ WEAK (many similar examples):
Example 1: "happy" → positive
Example 2: "joyful" → positive
Example 3: "excited" → positive
Example 4: "glad" → positive
Example 5: "pleased" → positive

✓ STRONG (diverse examples):
Example 1: "happy" → positive
Example 2: "terrible" → negative
Example 3: "okay" → neutral
Example 4: "not bad at all" → positive (negation)
Example 5: "could be worse" → neutral (hedging)
```

### Covering Edge Cases

```
Classify these as questions or statements:

# Normal cases
"What time is it?" → Question
"The sky is blue." → Statement

# Edge cases
"I wonder what time it is." → Statement (indirect question)
"Is that so." → Statement (rhetorical, no question mark)
"You're going where?" → Question (embedded question)
"Tell me the time." → Statement (imperative)

Now classify:
"Could you maybe tell me what time it might be?"
```

### Balancing Categories

```
For classification tasks, include examples from ALL categories:

Sentiment: Positive, Negative, Neutral

[Positive example]
"Absolutely love this product!" → POSITIVE

[Negative example]
"Complete waste of money" → NEGATIVE

[Neutral example]
"It arrived yesterday" → NEUTRAL

[Borderline example - strengthens learning]
"It's okay, not great but not terrible" → NEUTRAL

Classify: "The packaging was damaged but the product works"
```

## Format Consistency

### Consistent Structure

```
✓ CONSISTENT (same format every time):

Input: "hello"
Output: "HELLO"

Input: "World"
Output: "WORLD"

Input: "TeSt"
Output:

---

❌ INCONSISTENT (varying formats):

hello → HELLO
Input: "World"
Result: WORLD

TeSt =
```

### Consistent Reasoning Depth

```
✓ CONSISTENT (similar detail level):

Q: Is 15 prime?
A: 15 = 3 × 5, so it's divisible by 3 and 5. Not prime.

Q: Is 17 prime?
A: 17 is only divisible by 1 and 17. It's prime.

Q: Is 21 prime?
A:

---

❌ INCONSISTENT (varying detail):

Q: Is 15 prime?
A: No, 15 = 3 × 5.

Q: Is 17 prime?
A: We need to check all numbers from 2 to √17 ≈ 4.1.
   17 ÷ 2 = 8.5 (not divisible)
   17 ÷ 3 = 5.67 (not divisible)
   17 ÷ 4 = 4.25 (not divisible)
   Since no divisors found, 17 is prime.

Q: Is 21 prime?
A: [Unclear what level of detail expected]
```

## Dynamic Few-Shot

### Retrieving Relevant Examples

```python
def get_relevant_examples(query, example_bank, n=3):
    """Select most relevant examples for the query."""
    # Simple keyword matching (use embeddings in production)
    scored = []
    for example in example_bank:
        overlap = len(set(query.lower().split()) &
                     set(example['input'].lower().split()))
        scored.append((overlap, example))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [ex for _, ex in scored[:n]]


def build_few_shot_prompt(query, example_bank):
    """Build prompt with dynamically selected examples."""
    examples = get_relevant_examples(query, example_bank)

    prompt = "Here are some examples:\n\n"
    for ex in examples:
        prompt += f"Input: {ex['input']}\n"
        prompt += f"Output: {ex['output']}\n\n"

    prompt += f"Now process:\nInput: {query}\nOutput:"
    return prompt
```

### Category-Stratified Sampling

```python
def stratified_examples(categories, examples_per_category=1):
    """Ensure representation from each category."""
    selected = []
    for category in categories:
        category_examples = [e for e in ALL_EXAMPLES
                           if e['category'] == category]
        if category_examples:
            selected.extend(random.sample(
                category_examples,
                min(examples_per_category, len(category_examples))
            ))
    return selected
```

## Few-Shot Anti-Patterns

### 1. Biased Examples

```
❌ All examples from one category:
"happy" → positive
"great" → positive
"wonderful" → positive

Model may predict "positive" for everything

✓ Balanced examples across categories
```

### 2. Overly Simple Examples

```
❌ Examples don't cover complexity:
"cats" → animals
"dogs" → animals

Doesn't help with: "The barking dog chased the meowing cat"

✓ Include complex examples:
"The service dog guided its owner" → animals, accessibility
```

### 3. Inconsistent Formatting

```
❌ Format varies between examples:
Example 1: input -> output
Example 2: Input: x, Output: y
Example 3: Q: a, A: b

✓ Maintain exact same format structure
```

### 4. Too Many Examples

```
❌ 20+ examples consuming context window
- Reduces space for actual content
- May cause the model to overfit to examples

✓ Usually 3-5 well-chosen examples suffice
```

## Specialized Few-Shot Techniques

### Contrastive Examples

```
Show what TO do and what NOT to do:

[Good example]
Input: "Make text more professional"
Original: "Hey, just wanted to check in about that thing"
Improved: "I'm following up regarding our previous discussion"

[Bad example - avoid this]
Original: "Hey, just wanted to check in about that thing"
Avoided: "URGENT: IMMEDIATE RESPONSE REQUIRED"
Why bad: Overly aggressive, not professional

Now improve:
Original: "gonna need that report asap"
Improved:
```

### Chain-of-Examples

```
Show progression of difficulty:

[Easy]
Task: Add 2 + 3
Solution: 2 + 3 = 5

[Medium]
Task: Add 23 + 45
Solution: 20 + 40 = 60, 3 + 5 = 8, total = 68

[Hard]
Task: Add 234 + 567
Solution: 200 + 500 = 700, 30 + 60 = 90, 4 + 7 = 11
          700 + 90 + 11 = 801

[Your task]
Task: Add 456 + 789
Solution:
```

## Practical Exercise

Create few-shot prompts for:

1. **Code translation** (Python to JavaScript)
2. **Sentiment with reasoning** (explain why positive/negative)
3. **Data extraction** (extract structured info from text)

## Template Library

### Template: Classification
```
Classify items into categories: [CATEGORIES]

[EXAMPLE_1]
Item: [input_1]
Category: [category_1]

[EXAMPLE_2]
Item: [input_2]
Category: [category_2]

[EXAMPLE_3]
Item: [input_3]
Category: [category_3]

Classify:
Item: [NEW_INPUT]
Category:
```

### Template: Transformation
```
Transform [INPUT_TYPE] to [OUTPUT_TYPE]:

[Example]
Input: [sample_input_1]
Output: [sample_output_1]

[Example]
Input: [sample_input_2]
Output: [sample_output_2]

Transform:
Input: [NEW_INPUT]
Output:
```

## Next Steps

- [03-chain-of-thought.md](03-chain-of-thought.md) - Adding reasoning steps
- [04-self-consistency.md](04-self-consistency.md) - Multiple reasoning paths
