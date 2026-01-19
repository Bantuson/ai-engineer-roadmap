# Self-Consistency Prompting

## Overview

Self-consistency improves reasoning by generating multiple reasoning paths and selecting the most consistent answer through voting or aggregation.

## The Self-Consistency Principle

```
┌─────────────────────────────────────────────────────────────────┐
│                    SELF-CONSISTENCY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                       Question                                   │
│                          │                                       │
│            ┌─────────────┼─────────────┐                        │
│            ↓             ↓             ↓                        │
│         Path 1        Path 2        Path 3                      │
│        (CoT #1)      (CoT #2)      (CoT #3)                    │
│            │             │             │                        │
│            ↓             ↓             ↓                        │
│        Answer A      Answer A      Answer B                     │
│                                                                  │
│                    Aggregation                                   │
│                         │                                       │
│                         ↓                                       │
│                  Final: Answer A                                │
│                   (2 votes vs 1)                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Implementation Approaches

### Approach 1: Multiple Samples

```python
def self_consistent_answer(question, n_samples=5):
    """Generate multiple reasoning paths and vote."""
    prompt = f"""
{question}

Let's think step by step to solve this.
"""
    answers = []
    for _ in range(n_samples):
        response = call_llm(prompt, temperature=0.7)
        answer = extract_answer(response)
        answers.append(answer)

    # Majority voting
    from collections import Counter
    most_common = Counter(answers).most_common(1)[0][0]
    return most_common
```

### Approach 2: Single Prompt Multiple Paths

```
Solve this problem using three different approaches:

Problem: What is 15% of 80?

Approach 1 (Percentage formula):
[solve using formula]

Approach 2 (Decimal conversion):
[solve using decimals]

Approach 3 (Fraction method):
[solve using fractions]

Compare answers and determine the correct result.
```

### Approach 3: Perspective-Based Consistency

```
Analyze this investment opportunity from multiple perspectives:

Investment: $100K in early-stage AI startup

Perspective 1 - Optimistic Investor:
[analysis focusing on upside]
Recommendation: [invest/don't invest]

Perspective 2 - Risk-Averse Investor:
[analysis focusing on risks]
Recommendation: [invest/don't invest]

Perspective 3 - Data-Driven Analyst:
[analysis based purely on metrics]
Recommendation: [invest/don't invest]

Synthesis: Based on these perspectives, the balanced
recommendation is [final recommendation].
```

## Self-Consistency Patterns

### Pattern 1: Voting

```
Classify this customer feedback using 5 independent analyses.
Report the majority classification.

Feedback: "The product is okay but shipping was slow"

Analysis 1: Focus on product mention
Classification 1: [neutral/positive/negative]

Analysis 2: Focus on shipping mention
Classification 2: [neutral/positive/negative]

Analysis 3: Overall sentiment weighting
Classification 3: [neutral/positive/negative]

Analysis 4: Keyword sentiment analysis
Classification 4: [neutral/positive/negative]

Analysis 5: Comparative language analysis
Classification 5: [neutral/positive/negative]

Vote count:
- Positive: X
- Neutral: Y
- Negative: Z

Final classification: [majority answer]
```

### Pattern 2: Confidence Weighting

```
Solve this problem three ways and weight by confidence:

Problem: If 3x + 5 = 20, what is x?

Solution 1:
Method: Algebraic manipulation
3x + 5 = 20
3x = 15
x = 5
Confidence: HIGH (straightforward algebra)

Solution 2:
Method: Substitution check
Try x = 5: 3(5) + 5 = 15 + 5 = 20 ✓
Confidence: HIGH (verified by substitution)

Solution 3:
Method: Estimation
20 - 5 = 15, 15/3 = 5
Confidence: HIGH (quick mental math)

All methods agree: x = 5
Combined confidence: VERY HIGH
```

### Pattern 3: Diverse Reasoning Strategies

```
Determine if this argument is valid using different logical frameworks:

Argument: "All birds can fly. Penguins are birds.
Therefore, penguins can fly."

Framework 1: Formal Logic
P1: ∀x(Bird(x) → Fly(x))
P2: Bird(Penguin)
C: Fly(Penguin)
Valid structure? Yes
Sound argument? No (P1 is false)

Framework 2: Counterexample Method
Can we find a counterexample?
Penguins are birds that cannot fly.
This disproves P1.
Conclusion: Argument is unsound.

Framework 3: Real-World Verification
Are all birds able to fly? No.
Examples: Penguins, ostriches, kiwis
Conclusion: Premise is false.

Consensus: The argument has valid logical structure
but is UNSOUND because the first premise is false.
```

## Applications

### Math Problems

```
Calculate 47 × 23 using three different methods:

Method 1: Standard multiplication
   47
×  23
----
  141  (47 × 3)
 940   (47 × 20)
----
1081

Method 2: Distributive property
47 × 23 = 47 × (20 + 3)
        = (47 × 20) + (47 × 3)
        = 940 + 141
        = 1081

Method 3: (a-b)(c+d) expansion
47 × 23 = (50 - 3)(20 + 3)
        = 50×20 + 50×3 - 3×20 - 3×3
        = 1000 + 150 - 60 - 9
        = 1081

All methods yield 1081. Answer: 47 × 23 = 1081
```

### Code Review

```
Review this function for bugs using three analysis approaches:

def find_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

Analysis 1: Edge Case Analysis
- Empty list: Division by zero error ❌
- Normal case: Works correctly ✓
- Single element: Works correctly ✓

Analysis 2: Type Analysis
- Non-numeric types: Will crash ❌
- Mixed int/float: Works (Python handles) ✓
- None values: Will crash ❌

Analysis 3: Logic Verification
- Accumulation: Correct ✓
- Division: Uses correct divisor ✓
- Return: Returns correct type ✓

Consensus Issues Found:
1. No handling for empty list
2. No type validation

Suggested fix:
def find_average(numbers):
    if not numbers:
        return 0  # or raise ValueError
    total = sum(numbers)
    return total / len(numbers)
```

### Decision Making

```
Evaluate whether to launch this feature using multiple frameworks:

Feature: AI-powered auto-complete for emails

Framework 1: RICE Score
Reach: 80% of users (high)
Impact: Medium (saves time)
Confidence: 70% (some uncertainty)
Effort: 3 engineer-months (medium)
Score: (0.8 × 2 × 0.7) / 3 = 0.37
Verdict: MODERATE priority

Framework 2: ICE Score
Impact: 7/10
Confidence: 7/10
Ease: 5/10
Score: 7 × 7 × 5 = 245
Verdict: MEDIUM priority

Framework 3: Cost-Benefit Analysis
Costs: $150K development + $20K/month AI costs
Benefits: Est. 15% productivity gain, better retention
Payback: ~8 months
Verdict: POSITIVE ROI

Framework 4: Strategic Alignment
Company focus: AI-first products
User feedback: #2 requested feature
Competitive pressure: Competitors have it
Verdict: HIGH strategic fit

Aggregated Decision:
- Moderate priority (RICE)
- Medium priority (ICE)
- Positive ROI (Cost-Benefit)
- High strategic fit

Recommendation: PROCEED with development (3 of 4 positive)
```

## Best Practices

### 1. Use Appropriate Sample Size

```
GUIDELINES:
- Simple problems: 3 samples usually sufficient
- Complex reasoning: 5-7 samples
- Critical decisions: 10+ samples

More samples = more consistent but higher cost
```

### 2. Ensure Reasoning Diversity

```
❌ POOR: Same approach, different wording
✓ GOOD: Genuinely different methods or perspectives
```

### 3. Handle Ties Appropriately

```
When votes are tied:
1. Request additional samples
2. Use confidence weighting
3. Default to more conservative answer
4. Flag for human review
```

### 4. Validate Consistency

```
If answers are inconsistent:
- Problem may be ambiguous
- Additional context needed
- Consider reformulating the question
```

## Implementation Template

```python
def self_consistent_solve(problem, methods, min_agreement=0.6):
    """
    Solve problem using multiple methods and check consistency.
    """
    results = []

    for method in methods:
        prompt = f"""
Solve this problem using {method}:

{problem}

Show your work step by step, then provide final answer.
"""
        response = call_llm(prompt, temperature=0.7)
        answer = extract_answer(response)
        results.append({
            'method': method,
            'reasoning': response,
            'answer': answer
        })

    # Check agreement
    answers = [r['answer'] for r in results]
    from collections import Counter
    counter = Counter(answers)
    most_common, count = counter.most_common(1)[0]
    agreement = count / len(answers)

    return {
        'final_answer': most_common if agreement >= min_agreement else None,
        'agreement': agreement,
        'all_results': results,
        'needs_review': agreement < min_agreement
    }
```

## Next Steps

- [../03-advanced-strategies/01-tree-of-thought.md](../03-advanced-strategies/01-tree-of-thought.md) - Branching reasoning
- [../03-advanced-strategies/02-react-prompting.md](../03-advanced-strategies/02-react-prompting.md) - Reasoning with actions
