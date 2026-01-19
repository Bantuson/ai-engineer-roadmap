# Chain-of-Thought Prompting

## Overview

Chain-of-thought (CoT) prompting encourages models to show their reasoning process step-by-step, dramatically improving performance on complex reasoning tasks.

## The CoT Principle

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHAIN OF THOUGHT                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   WITHOUT CoT:                                                  │
│   Question → Answer                                             │
│   "What is 17 × 24?" → "408"                                   │
│                                                                  │
│   WITH CoT:                                                     │
│   Question → Step 1 → Step 2 → Step 3 → Answer                 │
│   "What is 17 × 24?"                                           │
│   → "17 × 24 = 17 × 20 + 17 × 4"                               │
│   → "= 340 + 68"                                                │
│   → "= 408"                                                     │
│                                                                  │
│   Benefits:                                                     │
│   • Better accuracy on complex problems                         │
│   • Interpretable reasoning (can verify steps)                  │
│   • Catches errors in intermediate steps                        │
│   • Model "thinks" more carefully                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## CoT Techniques

### Technique 1: Zero-Shot CoT

Simply add "Let's think step by step" or similar phrase.

```
Q: A store has 45 apples. If 12 customers each buy 3 apples,
how many apples are left?

Let's think step by step.
```

**Trigger phrases:**
- "Let's think step by step"
- "Let's work through this carefully"
- "Let me reason through this"
- "Let's break this down"
- "Think about this systematically"

### Technique 2: Few-Shot CoT

Provide examples that demonstrate reasoning.

```
Q: Roger has 5 tennis balls. He buys 2 cans of 3 balls each.
How many balls does he have now?

A: Roger started with 5 balls.
   He bought 2 cans, each with 3 balls.
   Balls from cans: 2 × 3 = 6 balls.
   Total balls: 5 + 6 = 11 balls.
   Answer: 11

Q: A store has 45 apples. If 12 customers each buy 3 apples,
how many apples are left?

A:
```

### Technique 3: Structured CoT

Use explicit structure for reasoning steps.

```
Solve this problem using the following structure:

PROBLEM: [restate the problem]
GIVEN: [list known information]
FIND: [what we need to determine]
APPROACH: [strategy to solve]
STEPS:
1. [first step]
2. [second step]
...
ANSWER: [final answer]
VERIFICATION: [check the answer]

Problem: A train travels at 60 mph for 2.5 hours, then at
80 mph for 1.5 hours. What is the total distance traveled?
```

## CoT for Different Problem Types

### Mathematical Reasoning

```
Solve this word problem, showing all work:

Problem: Sarah has $50. She buys 3 books at $8 each and
2 pens at $2 each. How much money does she have left?

Solution:
Step 1: Calculate cost of books
        3 books × $8/book = $24

Step 2: Calculate cost of pens
        2 pens × $2/pen = $4

Step 3: Calculate total spent
        $24 + $4 = $28

Step 4: Calculate remaining money
        $50 - $28 = $22

Answer: Sarah has $22 left.

Verification: $24 + $4 + $22 = $50 ✓
```

### Logical Reasoning

```
Analyze this logical statement, showing your reasoning:

Statement: "All programmers drink coffee. Alice is a programmer.
Therefore, Alice drinks coffee."

Analysis:
Step 1: Identify the premises
        P1: All programmers drink coffee (universal statement)
        P2: Alice is a programmer (specific instance)

Step 2: Apply logical inference
        P1 establishes: programmer → drinks coffee
        P2 establishes: Alice ∈ programmers
        Therefore: Alice → drinks coffee

Step 3: Evaluate validity
        This is a valid syllogism (modus ponens)
        If P1 and P2 are true, conclusion must be true

Step 4: Note assumptions
        Assumes P1 is actually true (which may not be)
        The argument is VALID but may not be SOUND

Conclusion: The logical structure is valid.
```

### Code Debugging

```
Debug this code by tracing through step by step:

def find_max(numbers):
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# Test: find_max([-5, -2, -8]) returns 0 (wrong!)

Trace:
Step 1: Initialize max_val = 0

Step 2: First iteration, num = -5
        Is -5 > 0? No
        max_val stays 0

Step 3: Second iteration, num = -2
        Is -2 > 0? No
        max_val stays 0

Step 4: Third iteration, num = -8
        Is -8 > 0? No
        max_val stays 0

Step 5: Return max_val = 0

Bug identified: Initializing to 0 fails for all-negative lists.

Fix: Initialize max_val to the first element or negative infinity.
```

### Decision Making

```
Analyze this business decision step by step:

Decision: Should our startup pivot from B2C to B2B?

Step 1: Analyze current situation
        - B2C revenue: $50K/month
        - Customer acquisition cost: $150
        - Churn rate: 15% monthly
        - Growth rate: 5% monthly

Step 2: Evaluate B2B opportunity
        - Potential contract: $500K/year
        - Sales cycle: 6 months
        - Implementation cost: $100K
        - 2 interested enterprises

Step 3: Calculate B2C trajectory
        - At current growth and churn: net 0% growth
        - 12-month projection: ~$50K/month (stagnant)
        - Break-even: Not yet achieved

Step 4: Calculate B2B trajectory
        - 2 contracts = $1M/year revenue
        - Minus implementation: $800K net
        - Risk: Long sales cycle, fewer customers

Step 5: Consider hybrid approach
        - Maintain B2C for stability
        - Pursue B2B opportunistically
        - Lower risk than full pivot

Recommendation: Pursue hybrid approach with B2B focus.
```

## Advanced CoT Patterns

### Backward Chaining

Start from the goal and work backward.

```
Goal: Prove that n² + n is always even for any integer n.

Working backward:
- For n² + n to be even, it must be divisible by 2
- Factor: n² + n = n(n + 1)
- This is a product of two consecutive integers
- One of any two consecutive integers must be even
- Therefore, n(n + 1) is always even
- Therefore, n² + n is always even ∎
```

### Multi-Path Reasoning

Consider multiple approaches.

```
Problem: Find the shortest path from A to D in this graph.

Approach 1: Direct path
A → D: weight = 10

Approach 2: Via B
A → B → D: 3 + 5 = 8

Approach 3: Via C
A → C → D: 4 + 3 = 7

Approach 4: Via B and C
A → B → C → D: 3 + 2 + 3 = 8

Comparison:
- Direct: 10
- Via B: 8
- Via C: 7 ← shortest
- Via B and C: 8

Answer: A → C → D with total weight 7
```

### Hypothesis Testing

```
Problem: Why is the website loading slowly?

Hypothesis 1: Server overload
- Check: Server CPU at 20%, memory at 40%
- Result: Not overloaded
- Conclusion: Not the cause

Hypothesis 2: Database queries
- Check: Slow query log shows 5s queries
- Result: Multiple unoptimized queries found
- Conclusion: Likely contributor

Hypothesis 3: Network latency
- Check: CDN response time normal
- Result: 50ms average
- Conclusion: Not the cause

Hypothesis 4: Frontend assets
- Check: 5MB of uncompressed JavaScript
- Result: No minification, no lazy loading
- Conclusion: Likely contributor

Root causes identified:
1. Unoptimized database queries
2. Large uncompressed frontend assets
```

## CoT Formatting Options

### Numbered Steps
```
Step 1: ...
Step 2: ...
Step 3: ...
```

### Bullet Points
```
• First, we consider...
• Next, we calculate...
• Finally, we conclude...
```

### Natural Language Flow
```
Let's start by examining...
This leads us to...
From this, we can determine...
```

### Symbolic Notation
```
Given: A ⊂ B, B ⊂ C
→ A ⊂ C (transitivity)
∴ x ∈ A → x ∈ C
```

## Common CoT Mistakes

### 1. Skipping Steps

```
❌ "5 × 8 = 40, so the answer is 40"
✓ "We need to find 5 × 8.
   5 × 8 = 5 × (2 × 4) = 10 × 4 = 40"
```

### 2. Inconsistent Reasoning

```
❌ Switching methods mid-problem
✓ Stick to one approach unless explicitly comparing
```

### 3. Not Verifying

```
❌ "The answer is 42."
✓ "The answer is 42. Let's verify: [check work]"
```

## When to Use CoT

| Use CoT | Skip CoT |
|---------|----------|
| Math problems | Simple lookups |
| Logical reasoning | Direct translations |
| Multi-step tasks | Formatting tasks |
| Debugging | Simple Q&A |
| Analysis | Generation |

## Practical Exercise

Apply CoT to solve:

1. A logic puzzle (who lives where)
2. A code optimization problem
3. A business strategy analysis

## Next Steps

- [04-self-consistency.md](04-self-consistency.md) - Multiple reasoning paths
- [../03-advanced-strategies/01-tree-of-thought.md](../03-advanced-strategies/01-tree-of-thought.md) - Branching reasoning
