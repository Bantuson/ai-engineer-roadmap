# Prompt Chaining

## Overview

Prompt chaining breaks complex tasks into sequential prompts, where each prompt's output feeds into the next. This enables handling of tasks too complex for a single prompt.

## The Chaining Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                      PROMPT CHAIN                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   INPUT                                                          │
│     │                                                            │
│     ↓                                                            │
│   ┌─────────────┐                                               │
│   │  Prompt 1   │ → Extract key information                     │
│   │  (Extract)  │                                               │
│   └─────────────┘                                               │
│     │ Output 1                                                  │
│     ↓                                                            │
│   ┌─────────────┐                                               │
│   │  Prompt 2   │ → Analyze and classify                        │
│   │  (Analyze)  │                                               │
│   └─────────────┘                                               │
│     │ Output 2                                                  │
│     ↓                                                            │
│   ┌─────────────┐                                               │
│   │  Prompt 3   │ → Generate final output                       │
│   │  (Generate) │                                               │
│   └─────────────┘                                               │
│     │                                                            │
│     ↓                                                            │
│   FINAL OUTPUT                                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Chain Types

### Sequential Chain

Each step depends on the previous step's output.

```
Task: Create a marketing email from a product spec

PROMPT 1 (Extract):
"Extract the key selling points from this product specification:
[spec document]

Output as a numbered list of 5 benefits."

↓ Output: List of 5 benefits

PROMPT 2 (Target):
"Given these product benefits:
[benefits from prompt 1]

Identify the ideal customer persona and their pain points."

↓ Output: Customer persona

PROMPT 3 (Generate):
"Write a marketing email for this customer:
[persona from prompt 2]

Highlighting these benefits:
[benefits from prompt 1]

Tone: Professional but friendly
Length: 150-200 words"

↓ Output: Marketing email
```

### Parallel Chain

Multiple prompts run independently, results merged.

```
Task: Comprehensive code review

PARALLEL PROMPTS:

┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  PROMPT A              PROMPT B              PROMPT C            │
│  (Security)            (Performance)         (Style)            │
│     │                      │                    │               │
│     ↓                      ↓                    ↓               │
│  Security issues       Perf bottlenecks     Style issues        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ↓
                    MERGE PROMPT:
                    "Combine these reviews into a
                    unified report prioritized by severity"
```

### Conditional Chain

Different paths based on classification.

```
Task: Customer support routing

PROMPT 1 (Classify):
"Classify this customer inquiry:
[inquiry]

Categories: BILLING, TECHNICAL, GENERAL, ESCALATION"

↓ Classification

IF BILLING:
  PROMPT 2A: "Address this billing inquiry using our policies..."
ELIF TECHNICAL:
  PROMPT 2B: "Troubleshoot this technical issue..."
ELIF ESCALATION:
  PROMPT 2C: "Draft escalation to human agent with summary..."
ELSE:
  PROMPT 2D: "Provide helpful general response..."
```

## Chain Design Patterns

### Pattern 1: Extract-Transform-Load (ETL)

```python
def etl_chain(raw_data):
    # Extract
    extracted = call_llm(f"""
    Extract structured data from this raw text:
    {raw_data}

    Output as JSON with fields: name, date, amount, category
    """)

    # Transform
    transformed = call_llm(f"""
    Given this extracted data:
    {extracted}

    Standardize the format:
    - Dates to ISO format
    - Amounts to USD
    - Categories to our taxonomy: [list]
    """)

    # Load (validation)
    validated = call_llm(f"""
    Validate this data for our database:
    {transformed}

    Check:
    - Required fields present
    - Data types correct
    - Business rules satisfied

    Output: {{"valid": true/false, "errors": [...], "data": {{...}}}}
    """)

    return validated
```

### Pattern 2: Decompose-Solve-Synthesize

```python
def decompose_solve_synthesize(complex_problem):
    # Decompose
    subtasks = call_llm(f"""
    Break this complex problem into 3-5 independent subtasks:
    {complex_problem}

    Format: numbered list with clear scope for each
    """)

    # Solve each subtask
    solutions = []
    for subtask in parse_subtasks(subtasks):
        solution = call_llm(f"""
        Solve this specific subtask:
        {subtask}

        Context: Part of larger problem: {complex_problem}
        """)
        solutions.append(solution)

    # Synthesize
    final = call_llm(f"""
    Combine these solutions into a coherent final answer:

    Original problem: {complex_problem}

    Subtask solutions:
    {format_solutions(solutions)}

    Synthesize into a complete, well-organized response.
    """)

    return final
```

### Pattern 3: Draft-Critique-Refine

```python
def draft_critique_refine(task, iterations=2):
    # Initial draft
    draft = call_llm(f"""
    Create a first draft for:
    {task}

    Focus on getting the main ideas down.
    """)

    for i in range(iterations):
        # Critique
        critique = call_llm(f"""
        Critique this draft:
        {draft}

        Identify:
        1. Strengths to keep
        2. Weaknesses to address
        3. Missing elements
        4. Specific improvements
        """)

        # Refine
        draft = call_llm(f"""
        Improve this draft based on the critique:

        CURRENT DRAFT:
        {draft}

        CRITIQUE:
        {critique}

        Create an improved version addressing all feedback.
        """)

    return draft
```

### Pattern 4: Verify-and-Correct

```python
def verified_generation(task):
    # Generate
    output = call_llm(f"""
    Complete this task:
    {task}
    """)

    # Verify
    verification = call_llm(f"""
    Verify this output for correctness:

    TASK: {task}
    OUTPUT: {output}

    Check:
    - Factual accuracy
    - Logical consistency
    - Completeness
    - Format compliance

    Report any issues found.
    """)

    if "no issues" in verification.lower():
        return output

    # Correct
    corrected = call_llm(f"""
    Correct this output based on the verification:

    ORIGINAL: {output}
    ISSUES: {verification}

    Provide corrected version.
    """)

    return corrected
```

## Real-World Chain Examples

### Example 1: Blog Post Generation

```
CHAIN: Research → Outline → Draft → Edit → SEO

Step 1: Research
"Research the topic: {topic}
Provide: key facts, statistics, expert quotes, trends"

Step 2: Outline
"Create a blog outline using this research:
{research}
Include: intro, 5 main sections, conclusion"

Step 3: Draft
"Write a 1500-word blog post following this outline:
{outline}
Using these facts: {research}"

Step 4: Edit
"Edit this draft for:
- Grammar and clarity
- Engaging hooks
- Smooth transitions
{draft}"

Step 5: SEO Optimize
"Optimize for SEO:
- Add meta description
- Optimize headings for keywords
- Suggest internal links
{edited_draft}"
```

### Example 2: Data Analysis Pipeline

```
CHAIN: Clean → Analyze → Visualize → Report

Step 1: Clean
"Clean this dataset:
- Handle missing values
- Remove duplicates
- Standardize formats
{raw_data}"

Step 2: Analyze
"Analyze this cleaned data:
- Summary statistics
- Key trends
- Anomalies
- Correlations
{cleaned_data}"

Step 3: Visualize
"Recommend visualizations for these insights:
{analysis}
For each recommendation, explain what it shows."

Step 4: Report
"Create executive summary combining:
Analysis: {analysis}
Visualizations: {viz_recommendations}
Format: 1-page executive brief"
```

### Example 3: Code Generation Pipeline

```
CHAIN: Requirements → Design → Implement → Test → Document

Step 1: Requirements
"Extract technical requirements from this user story:
{user_story}
Output as acceptance criteria"

Step 2: Design
"Design the solution for these requirements:
{requirements}
Include: architecture, data flow, interfaces"

Step 3: Implement
"Implement based on this design:
{design}
Requirements: {requirements}
Language: Python"

Step 4: Test
"Generate test cases for this implementation:
{code}
Cover: happy path, edge cases, error handling"

Step 5: Document
"Create documentation for:
Code: {code}
Tests: {tests}
Include: usage examples, API reference"
```

## Chain Implementation

```python
class PromptChain:
    """Manages a sequence of prompts."""

    def __init__(self):
        self.steps = []
        self.results = {}

    def add_step(self, name, prompt_template, inputs=None):
        """Add a step to the chain."""
        self.steps.append({
            'name': name,
            'template': prompt_template,
            'inputs': inputs or []
        })
        return self

    def run(self, initial_input):
        """Execute the chain."""
        self.results['input'] = initial_input

        for step in self.steps:
            # Build prompt with previous results
            prompt = step['template']
            for input_ref in step['inputs']:
                value = self.results.get(input_ref, '')
                prompt = prompt.replace(f'{{{input_ref}}}', str(value))

            # Execute
            result = call_llm(prompt)
            self.results[step['name']] = result

        return self.results


# Usage
chain = PromptChain()
chain.add_step('extract', 'Extract key points: {input}', ['input'])
chain.add_step('analyze', 'Analyze these points: {extract}', ['extract'])
chain.add_step('summarize', 'Summarize the analysis: {analyze}', ['analyze'])

results = chain.run("Long document text...")
print(results['summarize'])
```

## Best Practices

1. **Single responsibility** - Each prompt does one thing well
2. **Clear interfaces** - Define input/output format for each step
3. **Error handling** - Plan for failures at each step
4. **Logging** - Track intermediate results for debugging
5. **Caching** - Avoid re-running expensive steps
6. **Validation** - Verify outputs before passing to next step

## Next Steps

- [04-meta-prompting.md](04-meta-prompting.md) - Prompts generating prompts
- [../04-specialized-prompting/01-code-generation.md](../04-specialized-prompting/01-code-generation.md) - Code generation
