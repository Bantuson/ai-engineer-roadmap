# Anatomy of Prompts

## Overview

Understanding the components of effective prompts is fundamental to prompt engineering. This module breaks down prompt structure and formatting principles.

## Prompt Components

```
┌─────────────────────────────────────────────────────────────────┐
│                      PROMPT ANATOMY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  SYSTEM CONTEXT                                          │   │
│   │  Role, persona, expertise, background                    │   │
│   └─────────────────────────────────────────────────────────┘   │
│                           ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  TASK DEFINITION                                         │   │
│   │  What the model should do, action verbs                  │   │
│   └─────────────────────────────────────────────────────────┘   │
│                           ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  INPUT DATA                                              │   │
│   │  Information to process, context, variables              │   │
│   └─────────────────────────────────────────────────────────┘   │
│                           ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  OUTPUT SPECIFICATION                                    │   │
│   │  Format, structure, constraints                          │   │
│   └─────────────────────────────────────────────────────────┘   │
│                           ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │  EXAMPLES (Optional)                                     │   │
│   │  Demonstrations of expected behavior                     │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. System Context

Sets the stage for the interaction.

```
WEAK:
"Help me write code."

STRONG:
"You are an experienced Python developer specializing in data
engineering. You write clean, well-documented code following
PEP 8 guidelines and include type hints."
```

**Key elements:**
- Role identification
- Expertise level
- Domain knowledge
- Behavioral guidelines

### 2. Task Definition

Specifies what the model should accomplish.

```
WEAK:
"Write something about databases."

STRONG:
"Write a technical comparison of PostgreSQL and MongoDB,
focusing on:
1. Data modeling approaches
2. Query performance for analytical workloads
3. Scaling strategies
4. Use case recommendations"
```

**Action verbs matter:**
| Verb | Implies |
|------|---------|
| Explain | Teaching, comprehension |
| Analyze | Breaking down, examining |
| Create | Generating new content |
| Compare | Examining differences |
| Evaluate | Making judgments |
| Summarize | Condensing information |

### 3. Input Data

Information the model needs to process.

```
INPUT FORMATTING:

# Using labels
User question: {question}
Context: {context}

# Using delimiters
---
Article to summarize:
{article_text}
---

# Using XML-style tags
<document>
{content}
</document>

# Using JSON
{
  "user_query": "...",
  "search_results": [...]
}
```

### 4. Output Specification

Defines the expected response format.

```
WEAK:
"Give me a list."

STRONG:
"Respond with a JSON object containing:
- 'summary': 2-3 sentence overview
- 'key_points': array of 3-5 main takeaways
- 'recommendations': array of actionable items
- 'confidence': float between 0 and 1"
```

**Format options:**
- Prose (paragraphs)
- Lists (bulleted, numbered)
- Tables (markdown)
- JSON/YAML
- Code blocks
- Custom structures

### 5. Examples (Few-shot)

Demonstrates expected behavior.

```
Here are examples of the format I need:

Input: "What is machine learning?"
Output: {
  "topic": "Machine Learning",
  "category": "AI/Technology",
  "complexity": "intermediate",
  "summary": "..."
}

Input: "How do I bake bread?"
Output: {
  "topic": "Bread Baking",
  "category": "Cooking",
  "complexity": "beginner",
  "summary": "..."
}

Now process this input:
Input: "{user_query}"
```

## Formatting Principles

### Whitespace and Structure

```
# Poor formatting
You are an assistant. Help the user with their question. The user wants to know about {topic}. Provide a detailed answer with examples. Make sure to include pros and cons. Format as a list.

# Good formatting
You are a knowledgeable assistant.

## Your Task
Help the user understand {topic} in depth.

## Requirements
- Provide a detailed explanation
- Include practical examples
- List pros and cons

## Output Format
Structure your response as:
1. Overview (2-3 sentences)
2. Detailed explanation
3. Examples
4. Pros and cons (as bullet points)
```

### Delimiter Usage

| Delimiter | Use Case |
|-----------|----------|
| `---` | Section breaks |
| `"""` | Long text blocks |
| `<tag>` | Structured data |
| `###` | Headers |
| ` ``` ` | Code blocks |
| `{ }` | Variables |

### Variable Interpolation

```python
# Template with placeholders
prompt_template = """
You are a {role} assistant.

Task: {task_description}

Context:
{context}

User Input: {user_input}

Respond in {language}.
"""

# Fill in variables
prompt = prompt_template.format(
    role="customer support",
    task_description="Answer product questions",
    context="User is asking about return policy",
    user_input="How do I return an item?",
    language="English"
)
```

## Prompt Patterns

### The CRISPE Framework

```
C - Capacity: What role should the AI assume?
R - Request: What is the specific task?
I - Instructions: What guidelines should it follow?
S - Style: What tone/format is expected?
P - Personality: Any character traits?
E - Examples: Demonstrations of expected output
```

**Example:**

```
CAPACITY:
You are a senior software architect with 15 years of experience
in distributed systems.

REQUEST:
Review the following system design and identify potential issues.

INSTRUCTIONS:
- Focus on scalability concerns
- Consider failure modes
- Suggest concrete improvements
- Prioritize by impact

STYLE:
Be direct and technical. Use bullet points for clarity.
Include severity ratings (High/Medium/Low).

PERSONALITY:
Helpful but critical - don't sugarcoat issues.

EXAMPLES:
Issue: Single database bottleneck
Severity: High
Impact: System cannot scale beyond 10K concurrent users
Recommendation: Implement read replicas and consider sharding
```

### The RTF Framework

```
R - Role: Who is the AI?
T - Task: What should it do?
F - Format: How should it respond?
```

**Example:**

```
ROLE: You are an expert data analyst.

TASK: Analyze this sales dataset and identify trends,
anomalies, and actionable insights.

FORMAT: Provide your analysis as:
1. Executive Summary (3 bullets)
2. Key Trends (with supporting data)
3. Anomalies Detected
4. Recommendations (prioritized)
```

## Common Mistakes

### 1. Vague Instructions

```
❌ "Make it better"
✓ "Improve readability by breaking into shorter paragraphs,
   adding subheadings, and simplifying technical jargon"
```

### 2. Missing Context

```
❌ "Debug this code"
✓ "Debug this Python function. It should return the sum of
   even numbers in a list, but it's returning incorrect values
   for lists containing negative numbers."
```

### 3. Ambiguous Output

```
❌ "Give me information"
✓ "Provide a 3-paragraph explanation suitable for a technical
   blog post, with code examples in Python"
```

### 4. Overloading

```
❌ "Write a blog post about AI, make it SEO optimized,
   include code examples, add humor, target beginners
   but also experts, make it 2000 words, include images..."

✓ Focus on one clear objective per prompt, or break into
   multiple prompts for complex tasks
```

## Practical Exercise

Transform this weak prompt into a strong one:

**Weak:**
```
"Help me with my presentation"
```

**Strong:**
```
You are a presentation design expert with experience in
corporate communications.

TASK: Help me create an outline for a 15-minute presentation.

CONTEXT:
- Topic: Q4 sales performance
- Audience: Executive leadership team
- Goal: Secure budget approval for new initiative
- Tone: Professional, data-driven

OUTPUT:
Provide a slide-by-slide outline with:
- Slide title
- Key talking points (3-4 bullets)
- Suggested visual (chart type, image concept)
- Estimated time per slide

Total slides: 10-12
```

## Next Steps

- [02-instruction-clarity.md](02-instruction-clarity.md) - Writing clear instructions
- [03-context-setting.md](03-context-setting.md) - Setting effective context
