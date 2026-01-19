# Meta-Prompting

## Overview

Meta-prompting uses prompts to generate, improve, or analyze other prompts. This enables automated prompt engineering, self-improvement, and prompt optimization.

## Meta-Prompting Concepts

```
┌─────────────────────────────────────────────────────────────────┐
│                    META-PROMPTING LAYERS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Level 0: Direct Prompting                                     │
│   "Summarize this article"                                      │
│   → Summary                                                      │
│                                                                  │
│   Level 1: Prompt Generation                                    │
│   "Write a prompt that summarizes articles effectively"         │
│   → Generated prompt template                                   │
│                                                                  │
│   Level 2: Prompt Improvement                                   │
│   "Improve this summarization prompt"                           │
│   → Enhanced prompt template                                    │
│                                                                  │
│   Level 3: Prompt Strategy                                      │
│   "Design a prompt engineering strategy for summarization"      │
│   → Framework for creating prompts                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Meta-Prompt Patterns

### Pattern 1: Prompt Generation

```
You are an expert prompt engineer. Create an effective prompt
for the following task:

Task: {task_description}
Target model: {model}
Expected input format: {input_format}
Expected output format: {output_format}
Key requirements: {requirements}

Generate a prompt that:
1. Clearly defines the task
2. Includes necessary context
3. Specifies output format
4. Handles edge cases
5. Includes examples if helpful

Output the prompt ready for use.
```

**Example:**

```
Task: Classify customer support tickets by urgency
Target model: GPT-4
Input: Customer message text
Output: JSON with urgency level and reasoning
Requirements: Handle ambiguous cases, explain reasoning

GENERATED PROMPT:
---
You are a customer support triage specialist.

Classify the following support ticket by urgency level.

Urgency Levels:
- CRITICAL: System down, security breach, data loss
- HIGH: Major feature broken, blocking issue
- MEDIUM: Feature not working correctly, workaround exists
- LOW: Question, minor issue, enhancement request

Ticket:
{ticket_text}

Respond in JSON format:
{
  "urgency": "CRITICAL|HIGH|MEDIUM|LOW",
  "reasoning": "Brief explanation of classification",
  "key_indicators": ["indicator1", "indicator2"]
}

If the urgency is ambiguous, err on the side of higher urgency
and note the ambiguity in your reasoning.
---
```

### Pattern 2: Prompt Improvement

```
You are a prompt optimization expert. Analyze and improve this prompt:

CURRENT PROMPT:
{current_prompt}

ISSUES OBSERVED:
{issues}

EXAMPLE FAILURES:
{failures}

Improve the prompt by:
1. Identifying root causes of failures
2. Adding missing context or constraints
3. Clarifying ambiguous instructions
4. Adding examples if needed
5. Improving output format specification

Output:
- Analysis of issues
- Specific improvements made
- Improved prompt
- Expected improvement in results
```

### Pattern 3: Prompt Variation

```
Generate 5 variations of this prompt for A/B testing:

ORIGINAL PROMPT:
{prompt}

Create variations that differ in:
1. Tone (formal vs casual)
2. Structure (list vs prose)
3. Detail level (concise vs comprehensive)
4. Example usage (with/without examples)
5. Constraint emphasis (strict vs flexible)

For each variation:
- Explain what's different
- Predict how it might perform differently
- Identify best use case for this variation
```

### Pattern 4: Prompt Analysis

```
Analyze this prompt and provide a detailed assessment:

PROMPT:
{prompt}

Evaluate:
1. CLARITY (1-10): Are instructions unambiguous?
2. COMPLETENESS (1-10): All necessary info included?
3. STRUCTURE (1-10): Well-organized and readable?
4. ROBUSTNESS (1-10): Handles edge cases?
5. EFFICIENCY (1-10): Minimal tokens for effect?

For each dimension:
- Score with justification
- Specific improvement suggestions

Overall assessment:
- Strengths
- Critical weaknesses
- Priority improvements
- Rewritten version incorporating improvements
```

## Self-Improving Prompts

### The Critique-Revise Loop

```python
def self_improve_prompt(initial_prompt, task, test_cases, iterations=3):
    """Iteratively improve a prompt using self-critique."""

    current_prompt = initial_prompt

    for i in range(iterations):
        # Test current prompt
        results = []
        for test in test_cases:
            output = call_llm(current_prompt.format(input=test['input']))
            results.append({
                'input': test['input'],
                'expected': test['expected'],
                'actual': output,
                'correct': evaluate(output, test['expected'])
            })

        # Calculate success rate
        success_rate = sum(r['correct'] for r in results) / len(results)

        if success_rate >= 0.95:
            break

        # Self-critique
        critique_prompt = f"""
        Analyze why this prompt is failing some test cases:

        PROMPT:
        {current_prompt}

        RESULTS:
        {format_results(results)}

        Identify:
        1. Patterns in failures
        2. Root causes
        3. Specific improvements needed
        """
        critique = call_llm(critique_prompt)

        # Revise
        revise_prompt = f"""
        Improve this prompt based on the critique:

        CURRENT PROMPT:
        {current_prompt}

        CRITIQUE:
        {critique}

        Generate an improved version that addresses all issues.
        """
        current_prompt = call_llm(revise_prompt)

    return current_prompt
```

### Adaptive Prompt Selection

```python
def adaptive_prompt(task, input_data):
    """Select or generate optimal prompt based on input."""

    # Analyze input
    analysis_prompt = f"""
    Analyze this input and recommend the best prompting approach:

    INPUT:
    {input_data[:500]}

    TASK:
    {task}

    Consider:
    1. Input complexity
    2. Required reasoning depth
    3. Format requirements
    4. Domain specificity

    Recommend: zero-shot, few-shot, or chain-of-thought
    Explain your reasoning.
    """

    recommendation = call_llm(analysis_prompt)

    # Generate appropriate prompt
    generation_prompt = f"""
    Generate a {extract_approach(recommendation)} prompt for:

    TASK: {task}
    INPUT TYPE: {analyze_input_type(input_data)}

    The prompt should be optimized for this specific input type.
    """

    return call_llm(generation_prompt)
```

## Prompt Templates for Common Tasks

### Template Generator

```
Create a reusable prompt template for: {task_type}

Requirements:
- Include placeholders for variable content: {variable_name}
- Document each placeholder with expected format
- Include 2 usage examples
- Add error handling instructions
- Specify output format

Template structure:
1. Role/persona setup
2. Context injection point
3. Task instructions
4. Constraints
5. Output format
6. Examples (if few-shot)
7. Actual input

Generate the template with clear comments explaining each section.
```

### Example Output:

```
# TEMPLATE: Product Description Generator
# Version: 1.0
# Use case: E-commerce product descriptions

"""
# ROLE SETUP
You are an experienced e-commerce copywriter specializing in
{product_category} products.

# CONTEXT
Brand voice: {brand_voice}
Target audience: {target_audience}

# TASK
Write a compelling product description for the following item.

# CONSTRAINTS
- Length: {word_count} words
- Include: {required_elements}
- Avoid: {prohibited_content}
- Tone: {tone}

# OUTPUT FORMAT
Structure your description as:
1. Attention-grabbing headline
2. Key benefit statement (1 sentence)
3. Feature highlights (3 bullets)
4. Call-to-action

# PRODUCT DETAILS
{product_details}

# GENERATE DESCRIPTION
"""

# USAGE EXAMPLE 1:
product_category = "electronics"
brand_voice = "friendly and tech-savvy"
target_audience = "young professionals"
word_count = "150-200"
required_elements = "warranty info, key specs"
prohibited_content = "competitor comparisons"
tone = "enthusiastic but professional"
product_details = "Wireless earbuds with 30-hour battery..."
```

## Advanced Meta-Prompting

### Prompt Architecture Design

```
Design a complete prompt architecture for: {application}

Components to design:
1. System prompt (persistent context)
2. User intent classifier
3. Response generators (per intent)
4. Error handling prompts
5. Fallback prompts

For each component:
- Purpose and when triggered
- Input requirements
- Output format
- Integration with other components
- Example prompt text

Also design:
- Data flow between components
- State management approach
- Escalation paths
```

### Prompt Security Audit

```
Perform a security audit on this prompt:

PROMPT:
{prompt}

Check for vulnerabilities:
1. Prompt injection susceptibility
2. Jailbreak vulnerability
3. Data leakage risks
4. Authority claim attacks
5. Delimiter confusion

For each vulnerability found:
- Severity (Critical/High/Medium/Low)
- Attack vector description
- Example exploit
- Recommended mitigation

Generate a hardened version of the prompt.
```

## Meta-Prompting Best Practices

1. **Version control prompts** - Track changes and improvements
2. **Test systematically** - Use test cases to validate generated prompts
3. **Document purpose** - Clear documentation for each prompt's use
4. **Monitor performance** - Track success rates over time
5. **Iterate continuously** - Prompts should evolve with use

## Next Steps

- [../04-specialized-prompting/01-code-generation.md](../04-specialized-prompting/01-code-generation.md) - Code generation prompts
- [../05-optimization/01-prompt-debugging.md](../05-optimization/01-prompt-debugging.md) - Debugging prompts
