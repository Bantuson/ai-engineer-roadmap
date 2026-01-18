# Prompt Fundamentals

## Learning Objectives

- [ ] Understand why prompt structure matters
- [ ] Apply the CRAFT framework for effective prompts
- [ ] Use few-shot examples and chain-of-thought techniques
- [ ] Iterate systematically on prompts to improve results
- [ ] Avoid common prompting mistakes

## Prerequisites

- Access to an AI assistant (Claude, ChatGPT, etc.)

---

## Core Content

### Why Prompts Matter

The same model with different prompts produces vastly different results.

**Poor prompt:**
```
Write something about our new feature.
```

**Good prompt:**
```
Write a 200-word product announcement for our engineering blog audience.

Feature: Real-time collaboration on documents
Key benefits: See others' cursors, instant sync, no save button
Tone: Technical but accessible, excited but not hyperbolic

Include: What it is, why it matters, one technical detail, call to action
```

The difference isn't the AI—it's the instruction.

### The CRAFT Framework

A structured approach to writing effective prompts:

```
C - Context      What background does the AI need?
R - Role         Who should the AI be?
A - Action       What should it do?
F - Format       How should output be structured?
T - Target       Who is the audience?
```

#### Context

Provide relevant background information:

```
Context:
- We're a B2B SaaS company in the project management space
- Our customers are professional services firms (consulting, legal)
- We're launching a new reporting feature next quarter
- Main competitor (Asana) launched similar feature last month
```

**More context = better results** (up to a point).

#### Role

Define who the AI should act as:

```
You are a senior product manager with 10 years of experience
in B2B SaaS. You're known for clear, concise PRDs that
engineers love working from.
```

Roles provide:
- Expertise level
- Perspective
- Style expectations

#### Action

Clearly state what you want:

```
Analyze the following user feedback and:
1. Identify the top 3 pain points mentioned
2. For each pain point, suggest a potential solution
3. Prioritize solutions by estimated impact
```

**Be specific about:**
- What to do
- How many items
- What format
- What to include/exclude

#### Format

Specify output structure:

```
Format your response as:

## Summary
[2-3 sentence overview]

## Pain Points
| Pain Point | Frequency | Severity | Suggested Solution |
|------------|-----------|----------|-------------------|

## Recommendations
[Prioritized list with rationale]
```

Format options:
- Tables
- Bullet points
- Numbered lists
- Specific sections
- Code blocks
- Length constraints

#### Target

Identify the audience:

```
This will be shared with:
- Engineering leads (want technical feasibility)
- Executives (want business impact)
- Design team (want user experience details)

Balance technical depth with accessibility.
```

### The CRAFT Framework in Action

**Full prompt example:**

```
# Context
I'm a PM at a B2B project management SaaS company. We've received
150 customer feedback responses about our reporting feature over
the past quarter. The feedback has been tagged but not analyzed.

# Role
Act as an experienced user researcher who specializes in B2B
product feedback analysis.

# Action
Analyze the feedback summary below and:
1. Identify the top 5 themes across all feedback
2. For each theme, categorize as: Feature request, Bug, UX issue, or Praise
3. Estimate the impact on customer satisfaction (High/Medium/Low)
4. Recommend which 2 themes we should prioritize for next quarter

# Format
Structure your response as:

## Executive Summary (3 sentences max)

## Theme Analysis
| Theme | Category | Impact | Evidence Count |
|-------|----------|--------|----------------|

## Prioritization Recommendation
- Priority 1: [Theme] - [Rationale in 2 sentences]
- Priority 2: [Theme] - [Rationale in 2 sentences]

## Methodology Note
[Brief note on analysis approach]

# Target
This analysis will be presented to our product leadership team
in a quarterly planning meeting. They value data-driven insights
and clear prioritization rationale.

---

FEEDBACK SUMMARY:
[Paste feedback data here]
```

### Few-Shot Prompting

Show the AI what you want through examples:

```
Classify these feature requests by category.

Examples:
Request: "Let me export data to Excel"
Category: Data Export

Request: "The dashboard takes 10 seconds to load"
Category: Performance

Request: "I want to share reports with my team"
Category: Collaboration

Now classify:
Request: "Add a dark mode option"
Category:
```

**When to use few-shot:**
- Classification tasks
- Specific formatting requirements
- Style matching
- When zero-shot gives inconsistent results

**Tips:**
- 2-5 examples usually sufficient
- Include edge cases if relevant
- Make examples representative

### Chain-of-Thought Prompting

Ask the AI to show its reasoning:

```
Before providing your recommendation, think through:
1. What are the key factors to consider?
2. What are the trade-offs between options?
3. What assumptions are you making?

Then provide your recommendation with reasoning.
```

Or simply add: "Think step by step."

**Benefits:**
- Better accuracy on complex tasks
- Visible reasoning you can verify
- Easier to identify where thinking goes wrong

**Example:**

```
We need to decide between building a mobile app or improving
our mobile web experience.

Think step by step:
1. First, consider our user base and how they currently access the product
2. Then, evaluate the development effort for each option
3. Next, consider the competitive landscape
4. Finally, weigh the trade-offs and make a recommendation

[Provide context about your situation]
```

### Iterative Prompting

Treat prompting like product development—iterate based on results.

#### The Iteration Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌──────────┐    ┌──────────┐    ┌──────────┐               │
│    │  Write   │───▶│  Test    │───▶│ Analyze  │               │
│    │  Prompt  │    │  Prompt  │    │  Output  │               │
│    └──────────┘    └──────────┘    └──────────┘               │
│         ▲                                │                      │
│         │                                │                      │
│         └────────────────────────────────┘                      │
│                     Refine                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Iteration Strategies

**If output is too long:**
- Add word/sentence limits
- "Be concise" or "Brief response only"
- Specify section lengths

**If output is too generic:**
- Add more context
- Include specific examples
- Ask for specific details

**If output misses the point:**
- Clarify the core ask
- Break into smaller steps
- Reorder the prompt (important stuff first and last)

**If output is inconsistent:**
- Add few-shot examples
- Be more specific about format
- Lower temperature (if available)

### Common Prompting Mistakes

#### Mistake 1: Vague Instructions

```
❌ "Analyze this data"
✓ "Analyze this data and identify the top 3 trends with supporting metrics"
```

#### Mistake 2: Missing Context

```
❌ "Write a PRD for a dashboard"
✓ "Write a PRD for an analytics dashboard for our enterprise customers
   who need to track team productivity metrics..."
```

#### Mistake 3: Assuming Knowledge

```
❌ "Improve this like we discussed"
✓ "Improve this by [specific criteria] focusing on [specific goals]"
```

#### Mistake 4: Multiple Unstructured Asks

```
❌ "Review this PRD, find issues, suggest improvements, also think about
    edge cases and maybe compare to competitors"

✓ "Review this PRD in three passes:
   1. First, identify structural issues
   2. Then, find missing edge cases
   3. Finally, suggest improvements

   Format as three separate sections."
```

#### Mistake 5: Not Specifying Format

```
❌ "List the key points"
✓ "List the key points as a numbered list with one sentence each"
```

### Advanced Techniques

#### Persona Stacking
Combine multiple perspectives:

```
Analyze this feature proposal from three perspectives:
1. As a skeptical engineer: What technical concerns would you raise?
2. As the target user: What would delight or frustrate you?
3. As a competitor: What would you copy or do differently?
```

#### Constraint Setting
Add boundaries for better outputs:

```
Write a product announcement with these constraints:
- Maximum 150 words
- No jargon or buzzwords
- Include exactly one statistic
- End with a clear call to action
```

#### Self-Critique
Ask the AI to evaluate its own output:

```
[After initial response]

Now critique your response:
- What might be wrong or missing?
- What assumptions did you make?
- How could this be improved?
```

---

## Key Takeaways

1. **Use the CRAFT framework: Context, Role, Action, Format, Target**
2. **Few-shot examples help when you need specific patterns or consistency**
3. **Chain-of-thought ("think step by step") improves reasoning on complex tasks**
4. **Iterate on prompts like you iterate on products—test, analyze, refine**
5. **Avoid vague instructions, missing context, and unstructured multiple asks**
6. **Advanced techniques: persona stacking, constraints, self-critique**

---

## Practice

### Exercise 1: CRAFT Practice

Take this basic prompt and rewrite using CRAFT:

**Original:** "Help me with my PRD"

**Your improved prompt:**
```
# Context
[Add relevant context]

# Role
[Define the role]

# Action
[Specify what to do]

# Format
[Structure the output]

# Target
[Identify audience]
```

### Exercise 2: Few-Shot Practice

Create a few-shot prompt to classify product feedback into categories:
- Feature Request
- Bug Report
- Usability Issue
- Positive Feedback
- Question

Provide 2 examples for each category, then test with new feedback.

### Exercise 3: Iteration Practice

1. Write a prompt asking for competitive analysis
2. Run it and note what's missing or wrong
3. Revise the prompt to fix the issues
4. Repeat until satisfied
5. Document what changes improved results

---

## Further Reading

- **Anthropic's Prompt Engineering Guide** - Official Claude guidance
- **OpenAI's Prompt Engineering Guide** - Official GPT guidance
- **Prompt Engineering Guide (DAIR.AI)** - Comprehensive techniques
- **Lilian Weng's Blog** - Advanced prompting research
