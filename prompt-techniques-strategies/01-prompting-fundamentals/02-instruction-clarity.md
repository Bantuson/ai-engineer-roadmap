# Instruction Clarity

## Overview

Clear instructions are the foundation of effective prompts. This module covers techniques for writing unambiguous, actionable directions.

## The Clarity Spectrum

```
VAGUE ─────────────────────────────────────────────────── PRECISE

"Help me"     "Write about X"    "Analyze X      "Analyze X using
                                  for Y"          framework Y,
                                                  output as Z,
                                                  focus on A, B, C"
```

## Principles of Clear Instructions

### 1. Use Specific Action Verbs

| Vague | Specific |
|-------|----------|
| Do | Create, Generate, Build, Develop |
| Help | Guide, Explain, Assist, Recommend |
| Look at | Analyze, Evaluate, Assess, Review |
| Talk about | Describe, Explain, Discuss, Compare |
| Fix | Debug, Correct, Refactor, Optimize |
| Change | Modify, Update, Transform, Revise |

**Examples:**

```
❌ "Do something with this data"
✓ "Calculate the mean, median, and standard deviation of this data"

❌ "Help me with this code"
✓ "Review this function for bugs and suggest fixes with explanations"

❌ "Look at this design"
✓ "Evaluate this UI design for accessibility compliance (WCAG 2.1)"
```

### 2. Quantify When Possible

```
❌ "Write a short summary"
✓ "Write a summary in 2-3 sentences (50-75 words)"

❌ "Give me some examples"
✓ "Provide exactly 5 examples, each demonstrating a different use case"

❌ "Make it faster"
✓ "Optimize this function to run in O(n) time complexity"
```

### 3. Define Scope Boundaries

```
❌ "Tell me about Python"

✓ "Explain Python's memory management, specifically:
   - How garbage collection works
   - The difference between reference counting and cycle detection
   - Common memory leaks and how to avoid them

   Do NOT cover:
   - Basic syntax
   - Installation
   - Comparison with other languages"
```

### 4. Specify Constraints

```
CONSTRAINT TYPES:

# Length constraints
"Respond in exactly 3 bullet points"
"Maximum 200 words"
"Keep each section under 100 words"

# Format constraints
"Use only markdown formatting"
"Output valid JSON"
"No code blocks - prose only"

# Content constraints
"Do not include personal opinions"
"Use only information from the provided context"
"Avoid technical jargon"

# Style constraints
"Write in active voice"
"Maintain a professional tone"
"Use second person (you/your)"
```

## Instruction Templates

### The Command Template

```
[ACTION VERB] [OBJECT] [MODIFIERS] [CONSTRAINTS]

Examples:
"Create a Python function that validates email addresses using regex"
"Summarize this article in 3 bullet points for a non-technical audience"
"Compare PostgreSQL and MySQL focusing on performance and scalability"
```

### The Conditional Template

```
If [CONDITION], then [ACTION A].
Otherwise, [ACTION B].

Examples:
"If the user's question is about pricing, provide the standard rate card.
 Otherwise, direct them to the relevant documentation section."

"If the code contains syntax errors, list them first.
 If it's syntactically correct, analyze for logical issues."
```

### The Priority Template

```
Complete these tasks in order of importance:
1. [CRITICAL] [task]
2. [HIGH] [task]
3. [MEDIUM] [task]
4. [LOW] [task]

Example:
"Review this pull request with the following priorities:
 1. [CRITICAL] Security vulnerabilities
 2. [HIGH] Correctness and edge cases
 3. [MEDIUM] Performance implications
 4. [LOW] Code style and formatting"
```

## Disambiguation Techniques

### 1. Provide Examples of What NOT to Do

```
"Summarize this article.

DO:
- Focus on key findings
- Use objective language
- Include specific data points

DO NOT:
- Add your own opinions
- Use filler phrases like 'This article discusses...'
- Exceed 150 words"
```

### 2. Define Ambiguous Terms

```
"Write a 'brief' summary.

Definition: 'Brief' means 2-3 sentences, approximately 50 words,
capturing only the main conclusion and key supporting point."
```

### 3. Clarify Edge Cases

```
"Categorize these customer inquiries.

Categories: Billing, Technical, General

Edge cases:
- If inquiry mentions both billing AND technical issues,
  categorize as 'Technical' (takes priority)
- If unclear, categorize as 'General' and flag for review
- If inquiry is in a foreign language, note the language and
  categorize based on detectable keywords"
```

## Multi-Step Instructions

### Sequential Steps

```
"Process this support ticket:

Step 1: Identify the product mentioned
Step 2: Classify the issue type (bug, feature request, question)
Step 3: Assess urgency (high/medium/low)
Step 4: Draft a response addressing the specific issue
Step 5: Suggest relevant documentation links

Complete each step before moving to the next."
```

### Parallel Considerations

```
"Analyze this business proposal considering:

SIMULTANEOUSLY evaluate:
- Financial viability (ROI, payback period)
- Technical feasibility (resources, timeline)
- Market fit (competition, demand)
- Risk factors (dependencies, assumptions)

Then synthesize findings into a recommendation."
```

## Testing Instruction Clarity

### The Ambiguity Checklist

Ask yourself:

```
□ Could this instruction be interpreted differently by different people?
□ Are all action verbs specific and measurable?
□ Is the scope clearly defined?
□ Are output format requirements explicit?
□ Are edge cases addressed?
□ Is the success criteria clear?
```

### The "Five Whys" Test

For each instruction, ask "Why?" five times:

```
Instruction: "Improve this code"

Why? → To make it more efficient
Why? → To reduce response time
Why? → Users are experiencing lag
Why? → The function processes large datasets
Why? → We need O(n log n) or better

REFINED: "Optimize this function to achieve O(n log n) time
complexity for datasets up to 1 million records"
```

## Common Clarity Pitfalls

### 1. Assumed Context

```
❌ "Format it like before"
✓ "Format as a markdown table with columns: Name, Date, Status"
```

### 2. Subjective Standards

```
❌ "Make it good"
✓ "Ensure all functions have docstrings, use type hints, and
   achieve 80%+ test coverage"
```

### 3. Implicit Expectations

```
❌ "Write an email"
✓ "Write a professional email to a client:
   - Subject line included
   - Formal greeting
   - 2-3 paragraphs max
   - Clear call-to-action
   - Professional sign-off"
```

### 4. Hidden Requirements

```
❌ "Create a landing page"
✓ "Create a landing page that:
   - Loads in under 3 seconds
   - Works on mobile devices
   - Meets WCAG 2.1 AA accessibility
   - Includes clear CTA above the fold
   - Uses the brand colors (#1a1a1a, #ffffff)"
```

## Practical Exercise

Improve these vague instructions:

**Original:**
"Make my website better"

**Improved:**
```
Analyze my website (URL: example.com) and provide specific
improvements in these areas:

1. PERFORMANCE
   - Identify resources slowing page load
   - Suggest caching strategies
   - Recommend image optimization

2. USER EXPERIENCE
   - Evaluate navigation clarity
   - Assess mobile responsiveness
   - Review call-to-action visibility

3. SEO
   - Check meta tags completeness
   - Analyze heading structure
   - Identify missing alt text

For each issue found, provide:
- Current state (what's wrong)
- Recommended fix (specific action)
- Expected impact (measurable benefit)
- Priority (1-3, where 1 is critical)
```

## Next Steps

- [03-context-setting.md](03-context-setting.md) - Setting effective context
- [../02-core-techniques/01-zero-shot-prompting.md](../02-core-techniques/01-zero-shot-prompting.md) - Zero-shot techniques
