# Zero-Shot Prompting

## Overview

Zero-shot prompting involves giving instructions without any examples. The model relies entirely on its pre-trained knowledge and the clarity of your instructions.

## When to Use Zero-Shot

```
┌─────────────────────────────────────────────────────────────────┐
│                   ZERO-SHOT DECISION TREE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Is the task well-defined and common?                          │
│   ├── YES → Is the output format standard?                      │
│   │         ├── YES → Zero-shot is appropriate ✓                │
│   │         └── NO → Consider few-shot                          │
│   └── NO → Is the task complex or nuanced?                      │
│             ├── YES → Use few-shot or chain-of-thought          │
│             └── NO → Try zero-shot first                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Good candidates for zero-shot:**
- Translation between common languages
- Summarization
- Simple Q&A
- Standard formatting tasks
- Basic classification
- Grammar correction

## Zero-Shot Patterns

### Pattern 1: Direct Instruction

```
Translate the following text from English to Spanish:

"The weather is beautiful today."
```

### Pattern 2: Role + Instruction

```
You are a professional translator.

Translate this text from English to Spanish, maintaining
the original tone and style:

"The weather is beautiful today."
```

### Pattern 3: Instruction + Format

```
Translate the following text from English to Spanish.

Input: "The weather is beautiful today."

Provide your response as:
Translation: [your translation]
```

### Pattern 4: Instruction + Constraints

```
Translate the following text from English to Spanish.

Constraints:
- Use Latin American Spanish (not Castilian)
- Maintain informal tone
- Do not add or remove information

Input: "The weather is beautiful today."
```

## Zero-Shot for Classification

### Basic Classification

```
Classify the following customer review as POSITIVE, NEGATIVE, or NEUTRAL:

Review: "The product arrived on time but the packaging was damaged.
The product itself works fine though."

Classification:
```

### Multi-Label Classification

```
Classify this support ticket into all applicable categories.

Categories: [Billing, Technical, Account, Shipping, Returns, Other]

Ticket: "I was charged twice for my order #12345 and the item
hasn't arrived yet. Can you help?"

Applicable categories:
```

### Classification with Confidence

```
Classify this email as SPAM or NOT_SPAM.
Provide your confidence level (HIGH, MEDIUM, LOW).

Email: "Congratulations! You've won a free iPhone. Click here to claim!"

Classification:
Confidence:
Reasoning:
```

## Zero-Shot for Generation

### Content Generation

```
Write a product description for the following item:

Product: Wireless Bluetooth Earbuds
Key features: 30-hour battery, noise cancellation, water resistant
Target audience: Fitness enthusiasts
Tone: Energetic and motivational
Length: 100-150 words
```

### Code Generation

```
Write a Python function that:
- Takes a list of integers as input
- Returns a new list with duplicates removed
- Maintains the original order of first occurrences
- Has O(n) time complexity

Include type hints and a docstring.
```

### Creative Writing

```
Write a haiku about the feeling of debugging code at 3 AM.

Follow the traditional 5-7-5 syllable structure.
```

## Zero-Shot for Analysis

### Sentiment Analysis

```
Analyze the sentiment of each sentence in this customer feedback.

Feedback:
"The app is really user-friendly. However, it crashes sometimes
when I try to upload photos. Customer support was helpful though."

For each sentence, identify:
1. The sentiment (positive/negative/neutral)
2. The aspect being discussed (UI, stability, support, etc.)
```

### Text Analysis

```
Analyze this paragraph and identify:
1. Main topic
2. Key arguments or points
3. Tone (formal, informal, technical, etc.)
4. Intended audience
5. Any logical fallacies or weak arguments

Paragraph: [text to analyze]
```

## Improving Zero-Shot Performance

### Technique 1: Be Specific

```
❌ WEAK:
"Summarize this article."

✓ STRONG:
"Summarize this article in exactly 3 bullet points.
Each bullet should be one sentence (15-20 words).
Focus on the main conclusions, not the methodology."
```

### Technique 2: Define Output Format

```
❌ WEAK:
"Extract the key information."

✓ STRONG:
"Extract information in this exact JSON format:
{
  'title': string,
  'author': string or null,
  'date': ISO date string or null,
  'main_points': array of strings (max 5),
  'sentiment': 'positive' | 'negative' | 'neutral'
}"
```

### Technique 3: Provide Boundaries

```
❌ WEAK:
"Write about machine learning."

✓ STRONG:
"Write about machine learning:
- Focus only on supervised learning
- Assume reader has basic programming knowledge
- Do NOT cover neural networks (separate topic)
- Length: 200-300 words
- Include one practical example"
```

### Technique 4: Use Role Priming

```
❌ WEAK:
"Review this code."

✓ STRONG:
"You are a senior security engineer reviewing code for
production deployment.

Review this code focusing on:
1. Security vulnerabilities (OWASP Top 10)
2. Input validation issues
3. Authentication/authorization flaws

For each issue found, explain:
- What the vulnerability is
- Why it's dangerous
- How to fix it"
```

## Zero-Shot Limitations

### When Zero-Shot Fails

1. **Novel formats**: Unusual output structures
2. **Domain-specific tasks**: Specialized terminology or conventions
3. **Complex reasoning**: Multi-step logical problems
4. **Subjective evaluation**: Tasks requiring learned preferences
5. **Precise formatting**: Exact formatting requirements

### Solutions

| Problem | Solution |
|---------|----------|
| Novel format | Add few-shot examples |
| Complex reasoning | Use chain-of-thought |
| Subjective tasks | Provide evaluation criteria |
| Precise formatting | Include format examples |

## Practical Exercises

### Exercise 1: Classification
Write a zero-shot prompt to classify movie reviews by genre.

### Exercise 2: Generation
Write a zero-shot prompt to generate SQL queries from natural language.

### Exercise 3: Analysis
Write a zero-shot prompt to identify potential bugs in code snippets.

## Template Library

### Template 1: Classification
```
Classify the following [ITEM_TYPE] into one of these categories:
[CATEGORY_LIST]

[ITEM_TYPE]: [INPUT]

Category:
```

### Template 2: Generation
```
You are a [ROLE] expert.

Create a [OUTPUT_TYPE] that:
- [REQUIREMENT_1]
- [REQUIREMENT_2]
- [REQUIREMENT_3]

[ADDITIONAL_CONTEXT]
```

### Template 3: Analysis
```
Analyze the following [INPUT_TYPE] and identify:
1. [ANALYSIS_DIMENSION_1]
2. [ANALYSIS_DIMENSION_2]
3. [ANALYSIS_DIMENSION_3]

[INPUT_TYPE]:
[INPUT]

Analysis:
```

## Next Steps

- [02-few-shot-prompting.md](02-few-shot-prompting.md) - Adding examples
- [03-chain-of-thought.md](03-chain-of-thought.md) - Step-by-step reasoning
