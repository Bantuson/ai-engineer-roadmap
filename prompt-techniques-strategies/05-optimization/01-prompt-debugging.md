# Prompt Debugging

## Overview

Prompt debugging is the systematic process of identifying why prompts fail and fixing them. This module covers techniques for diagnosing and resolving prompt issues.

## Common Prompt Failures

```
┌─────────────────────────────────────────────────────────────────┐
│                    FAILURE CATEGORIES                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   OUTPUT ISSUES                 BEHAVIOR ISSUES                 │
│   ├── Wrong format              ├── Ignores instructions        │
│   ├── Missing information       ├── Adds unwanted content       │
│   ├── Incorrect facts           ├── Wrong tone/style            │
│   └── Inconsistent results      └── Misunderstands task         │
│                                                                  │
│   EDGE CASE ISSUES              PERFORMANCE ISSUES              │
│   ├── Fails on unusual input    ├── Too verbose                 │
│   ├── Handles nulls poorly      ├── Too terse                   │
│   ├── Numeric edge cases        ├── Slow/expensive              │
│   └── Language variations       └── Inconsistent quality        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Debugging Framework

### Step 1: Identify the Problem

```
PROBLEM IDENTIFICATION CHECKLIST:

□ What is the expected output?
□ What is the actual output?
□ Is the problem consistent or intermittent?
□ Does it fail on all inputs or specific ones?
□ When did it start failing (if worked before)?

CATEGORIZE THE FAILURE:
- [ ] Format issue (structure, type)
- [ ] Content issue (accuracy, completeness)
- [ ] Style issue (tone, verbosity)
- [ ] Logic issue (reasoning, interpretation)
- [ ] Edge case issue (specific inputs)
```

### Step 2: Isolate the Cause

```
ISOLATION TECHNIQUES:

1. MINIMAL REPRODUCTION
   - Strip prompt to essentials
   - Does failure persist?
   - What's the minimum prompt that fails?

2. COMPONENT TESTING
   - Test each section separately:
     □ System context
     □ Instructions
     □ Examples
     □ Input formatting
     □ Output specification

3. INPUT VARIATION
   - Try simpler inputs
   - Try edge case inputs
   - Try completely different inputs
   - Identify pattern in failures

4. PARAMETER TESTING
   - Vary temperature (0 vs 0.7 vs 1)
   - Change max tokens
   - Test different models
```

### Step 3: Diagnose Root Cause

```
COMMON ROOT CAUSES AND SYMPTOMS:

SYMPTOM: Output format wrong
CAUSES:
- Format specification unclear
- Examples contradict instructions
- Complex format not demonstrated
→ FIX: Explicit format with example

SYMPTOM: Model ignores instructions
CAUSES:
- Instructions buried in text
- Contradictory instructions
- Instructions too complex
→ FIX: Clear, prominent, simple instructions

SYMPTOM: Inconsistent results
CAUSES:
- Ambiguous instructions
- Temperature too high
- Multiple valid interpretations
→ FIX: More specific constraints, lower temperature

SYMPTOM: Wrong content/facts
CAUSES:
- Insufficient context
- Asking beyond knowledge
- Ambiguous question
→ FIX: Provide context, verify capabilities
```

## Debugging Techniques

### Technique 1: Echo Testing

Ask the model to repeat instructions to verify understanding.

```
DEBUG PROMPT:
Before completing the task, please confirm your understanding:
1. Summarize what you've been asked to do
2. List any constraints or requirements
3. Describe the expected output format

Then complete the task.

---

TASK:
{original_task}
```

### Technique 2: Step-by-Step Decomposition

Break the task into explicit steps.

```
DEBUG VERSION:
Complete this task step by step:

STEP 1: Read and parse the input
- What is the input? [Model states understanding]

STEP 2: Identify required information
- What needs to be extracted/generated? [Model lists]

STEP 3: Process according to rules
- Apply rule 1: [result]
- Apply rule 2: [result]

STEP 4: Format output
- Required format: [format]
- Generated output: [output]

STEP 5: Verify
- Does output match requirements? [check]

---

INPUT:
{input}
```

### Technique 3: Contrastive Examples

Show both correct and incorrect outputs.

```
DEBUG PROMPT:
Here are examples of CORRECT and INCORRECT outputs:

CORRECT:
Input: "John Smith, john@email.com, 555-1234"
Output: {"name": "John Smith", "email": "john@email.com", "phone": "555-1234"}
WHY CORRECT: Properly formatted JSON, all fields extracted

INCORRECT:
Input: "John Smith, john@email.com, 555-1234"
Output: John Smith's email is john@email.com and phone is 555-1234
WHY WRONG: Not JSON format, missing structure

INCORRECT:
Input: "John Smith, john@email.com, 555-1234"
Output: {"name": "John", "email": "john@email.com"}
WHY WRONG: Incomplete name, missing phone field

Now process:
Input: {new_input}
```

### Technique 4: Constraint Verification

Add explicit verification steps.

```
DEBUG PROMPT:
Complete the task, then verify:

TASK: {task}

After completing, check:
[ ] Output is valid JSON
[ ] All required fields present
[ ] No extra fields added
[ ] Values match expected types
[ ] Formatting rules followed

If any check fails, fix before final output.
```

## Debugging by Failure Type

### Format Failures

```
PROBLEM: Output not in requested format

DEBUGGING STEPS:
1. Is format specification clear?
   WEAK: "Output as JSON"
   STRONG: "Output as JSON: {\"field\": \"value\"}"

2. Is example provided?
   Add: "Example output: {\"name\": \"test\"}"

3. Is format enforced at end?
   Add: "Output ONLY valid JSON, no other text"

4. Test with simpler format first
   Start: "Output as comma-separated values"
   Then: "Output as JSON array"
   Then: "Output as nested JSON object"

FIXED PROMPT:
Output your response as valid JSON matching this exact schema:
{
  "field1": "string",
  "field2": number
}

IMPORTANT: Output ONLY the JSON object. No explanations,
no markdown code blocks, just the raw JSON.
```

### Instruction Following Failures

```
PROBLEM: Model ignores some instructions

DEBUGGING STEPS:
1. Count instructions - are there too many?
   → Reduce to essential instructions

2. Are instructions prioritized?
   → Add: "CRITICAL:", "IMPORTANT:", "OPTIONAL:"

3. Are instructions conflicting?
   → Review for contradictions

4. Are instructions clear?
   → Rewrite ambiguous phrases

FIXED PROMPT:
CRITICAL RULES (must follow):
1. [most important rule]
2. [second most important]

IMPORTANT GUIDELINES:
- [guideline 1]
- [guideline 2]

OPTIONAL PREFERENCES:
- [nice to have]
```

### Consistency Failures

```
PROBLEM: Different outputs for same input

DEBUGGING STEPS:
1. Check temperature setting
   → Lower temperature for consistency

2. Check for ambiguity
   → Define all edge cases explicitly

3. Check for randomness requests
   → Remove "creative" language if consistency needed

4. Add deterministic instructions
   → "Always choose X when Y is ambiguous"

FIXED PROMPT:
CONSISTENCY RULES:
- When input is ambiguous, default to [specific choice]
- For uncertain cases, prefer [specific option]
- Use exactly this format: [precise format]

Temperature recommendation: 0 to 0.3
```

### Quality Failures

```
PROBLEM: Output quality varies

DEBUGGING STEPS:
1. Define quality criteria explicitly
2. Add self-evaluation step
3. Request revision if needed

FIXED PROMPT:
Complete the task, then evaluate your output:

QUALITY CRITERIA:
- Accuracy: Is all information correct?
- Completeness: Are all requirements addressed?
- Clarity: Is the output easy to understand?
- Format: Does it match specifications?

Rate each criterion 1-5. If any score < 4,
revise your output before finalizing.

Final output only after self-review passes.
```

## Debugging Tools

### Logging Template

```
PROMPT DEBUG LOG:

Timestamp: [date/time]
Model: [model name]
Temperature: [value]

PROMPT:
[full prompt text]

INPUT:
[test input]

EXPECTED OUTPUT:
[what should have been produced]

ACTUAL OUTPUT:
[what was produced]

FAILURE TYPE:
[format/content/style/logic/edge case]

ROOT CAUSE HYPOTHESIS:
[suspected issue]

FIX ATTEMPTED:
[change made]

RESULT:
[did it work?]
```

### A/B Testing Setup

```python
def debug_prompt_variants(base_prompt, input_data, variants):
    """Test multiple prompt variations."""
    results = []

    for name, prompt_modification in variants.items():
        modified_prompt = apply_modification(base_prompt, prompt_modification)

        # Run multiple times for consistency check
        outputs = [call_llm(modified_prompt, input_data) for _ in range(3)]

        results.append({
            'variant': name,
            'outputs': outputs,
            'consistent': len(set(outputs)) == 1,
            'correct': evaluate_correctness(outputs[0])
        })

    return results

# Example usage
variants = {
    'explicit_format': {'add_suffix': 'Output ONLY JSON.'},
    'with_example': {'add_example': '{"key": "value"}'},
    'step_by_step': {'add_prefix': 'Think step by step.'},
}
```

## Best Practices

1. **Test systematically** - Don't just try random fixes
2. **Isolate variables** - Change one thing at a time
3. **Document findings** - Track what works and doesn't
4. **Build test suites** - Reusable test cases for regression
5. **Version prompts** - Track changes over time

## Next Steps

- [02-iterative-refinement.md](02-iterative-refinement.md) - Systematic improvement
- [03-evaluation-metrics.md](03-evaluation-metrics.md) - Measuring effectiveness
