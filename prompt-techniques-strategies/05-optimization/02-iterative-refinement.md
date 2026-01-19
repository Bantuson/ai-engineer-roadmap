# Iterative Refinement

## Overview

Iterative refinement is a systematic approach to improving prompts through cycles of testing, analysis, and modification. This module covers structured methods for prompt improvement.

## The Refinement Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                   ITERATIVE REFINEMENT CYCLE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│         ┌──────────┐                                            │
│         │  DRAFT   │ ← Start here                               │
│         └────┬─────┘                                            │
│              ↓                                                   │
│         ┌──────────┐                                            │
│         │   TEST   │ ← Run against test cases                   │
│         └────┬─────┘                                            │
│              ↓                                                   │
│         ┌──────────┐                                            │
│         │ ANALYZE  │ ← Identify failures and patterns           │
│         └────┬─────┘                                            │
│              ↓                                                   │
│         ┌──────────┐                                            │
│         │  REFINE  │ ← Make targeted improvements               │
│         └────┬─────┘                                            │
│              ↓                                                   │
│         ┌──────────┐                                            │
│         │ VALIDATE │ ← Verify improvements                      │
│         └────┬─────┘                                            │
│              │                                                   │
│              ├── Pass → DONE                                    │
│              └── Fail → Back to TEST                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Baseline Establishment

### Create Initial Prompt

```
INITIAL PROMPT TEMPLATE:

[ROLE]
You are a {role} with expertise in {domain}.

[TASK]
{task_description}

[INPUT]
{input_format}

[OUTPUT]
{output_format}
```

### Define Test Suite

```python
TEST_SUITE = [
    # Basic functionality
    {
        "name": "basic_case",
        "input": "standard input",
        "expected": "expected output",
        "category": "core"
    },
    # Edge cases
    {
        "name": "empty_input",
        "input": "",
        "expected": "appropriate handling",
        "category": "edge"
    },
    {
        "name": "max_length_input",
        "input": "very long input...",
        "expected": "still works correctly",
        "category": "edge"
    },
    # Adversarial cases
    {
        "name": "confusing_input",
        "input": "ambiguous or tricky input",
        "expected": "reasonable handling",
        "category": "adversarial"
    },
]
```

### Establish Baseline Metrics

```
BASELINE MEASUREMENT:

Date: {date}
Prompt Version: 1.0

Test Results:
- Core tests: X/Y passed (Z%)
- Edge tests: X/Y passed (Z%)
- Adversarial tests: X/Y passed (Z%)

Quality Metrics:
- Format compliance: X%
- Content accuracy: X%
- Consistency: X% (same output for same input)

Performance:
- Average tokens used: X
- Average latency: Xms
```

## Phase 2: Analysis

### Failure Categorization

```
FAILURE ANALYSIS TEMPLATE:

Test Case: {test_name}
Category: {core/edge/adversarial}

Expected: {expected_output}
Actual: {actual_output}

Failure Type:
[ ] Format - Wrong structure
[ ] Content - Wrong information
[ ] Missing - Incomplete output
[ ] Extra - Unwanted content
[ ] Logic - Reasoning error
[ ] Style - Wrong tone/verbosity

Root Cause Hypothesis:
{why this might be failing}

Potential Fixes:
1. {fix option 1}
2. {fix option 2}
```

### Pattern Identification

```
PATTERN ANALYSIS:

Looking across all failures, identify:

1. COMMON THEMES
   - Do failures share characteristics?
   - What input types fail most?
   - What output aspects fail most?

2. INSTRUCTION GAPS
   - What instructions are being ignored?
   - What instructions are ambiguous?
   - What instructions are missing?

3. EXAMPLE NEEDS
   - What cases need demonstration?
   - What formats need examples?
   - What edge cases need explicit handling?

4. STRUCTURAL ISSUES
   - Is prompt too long/complex?
   - Is important info buried?
   - Is structure confusing?
```

## Phase 3: Targeted Refinement

### Refinement Strategies

```
STRATEGY 1: ADD SPECIFICITY
Before: "Respond in JSON format"
After: "Respond in JSON format: {\"key\": \"value\"}"

STRATEGY 2: ADD EXAMPLES
Before: "Extract names from text"
After: "Extract names from text.
Example: 'Call John' → ['John']
Example: 'John and Jane met' → ['John', 'Jane']"

STRATEGY 3: ADD CONSTRAINTS
Before: "Summarize the text"
After: "Summarize the text in exactly 3 bullet points,
each under 20 words"

STRATEGY 4: RESTRUCTURE
Before: Long paragraph with buried instructions
After:
CRITICAL RULES:
1. [rule 1]
2. [rule 2]

GUIDELINES:
- [guideline 1]
- [guideline 2]

STRATEGY 5: ADD VERIFICATION
Before: "Generate the output"
After: "Generate the output, then verify:
- Is it valid JSON?
- Are all required fields present?
If not, fix before returning."
```

### Refinement Documentation

```
REFINEMENT LOG:

Version: 1.0 → 1.1
Date: {date}

CHANGE MADE:
{description of change}

RATIONALE:
{why this change should help}

SECTION MODIFIED:
{which part of prompt}

BEFORE:
{old text}

AFTER:
{new text}

EXPECTED IMPACT:
{what should improve}
```

## Phase 4: Validation

### Regression Testing

```
REGRESSION TEST PROTOCOL:

1. Run ALL test cases (not just failing ones)
2. Compare results to previous version
3. Check for:
   - Improvements in targeted areas
   - No regression in passing tests
   - Overall metric changes

RESULTS TEMPLATE:

Version: {new_version}
Compared to: {previous_version}

Changes in Test Results:
- Core tests: X/Y → X/Y (±Z%)
- Edge tests: X/Y → X/Y (±Z%)
- Adversarial: X/Y → X/Y (±Z%)

New Passes: [list]
New Failures: [list]
Status: ACCEPT / REJECT / MODIFY
```

### A/B Testing

```python
def ab_test_prompts(prompt_a, prompt_b, test_cases, n_runs=3):
    """Compare two prompt versions."""
    results = {"a": [], "b": []}

    for test in test_cases:
        for _ in range(n_runs):
            results["a"].append(evaluate(prompt_a, test))
            results["b"].append(evaluate(prompt_b, test))

    summary = {
        "prompt_a_score": sum(results["a"]) / len(results["a"]),
        "prompt_b_score": sum(results["b"]) / len(results["b"]),
        "winner": "a" if avg(results["a"]) > avg(results["b"]) else "b",
        "improvement": abs(avg(results["a"]) - avg(results["b"])),
        "statistical_significance": calculate_significance(results)
    }

    return summary
```

## Refinement Patterns

### The Expansion Pattern

Start simple, add complexity as needed.

```
VERSION 1 (Minimal):
Summarize this text.

VERSION 2 (Add length):
Summarize this text in 2-3 sentences.

VERSION 3 (Add focus):
Summarize this text in 2-3 sentences, focusing on
the main conclusion and key supporting evidence.

VERSION 4 (Add format):
Summarize this text as:
- Main conclusion (1 sentence)
- Key evidence (1-2 sentences)
- Implication (1 sentence)

VERSION 5 (Add examples):
[Include few-shot examples of good summaries]
```

### The Constraint Tightening Pattern

Progressively constrain output.

```
ITERATION 1: "Generate a response"
ISSUE: Too much variation

ITERATION 2: "Generate a concise response"
ISSUE: Still variable length

ITERATION 3: "Generate a response in 50-75 words"
ISSUE: Sometimes includes preamble

ITERATION 4: "Generate a response in 50-75 words.
Start directly with the answer, no preamble."
ISSUE: Format still varies

ITERATION 5: "Generate a response in exactly this format:
ANSWER: [50-75 words]
Start with the answer, no introduction or conclusion."
RESULT: Consistent outputs
```

### The Decomposition Pattern

Break complex prompts into simpler parts.

```
MONOLITHIC PROMPT (problematic):
"Analyze this text, extract key entities, classify
sentiment, summarize in 3 points, and format as JSON"

DECOMPOSED PROMPTS (better):

PROMPT 1 (Extraction):
"Extract all named entities from this text"

PROMPT 2 (Classification):
"Classify the sentiment of this text as positive/negative/neutral"

PROMPT 3 (Summarization):
"Summarize this text in exactly 3 bullet points"

PROMPT 4 (Formatting):
"Combine these inputs into JSON format: {entities}, {sentiment}, {summary}"
```

## Tracking Progress

```
PROMPT EVOLUTION TRACKER:

Prompt Name: {name}
Task: {task_description}

VERSION HISTORY:
| Version | Date | Pass Rate | Key Change |
|---------|------|-----------|------------|
| 1.0 | Jan 1 | 60% | Initial |
| 1.1 | Jan 3 | 72% | Added examples |
| 1.2 | Jan 5 | 78% | Clarified format |
| 1.3 | Jan 8 | 85% | Added constraints |
| 2.0 | Jan 15| 92% | Major restructure |

CURRENT BEST: Version 2.0

REMAINING ISSUES:
- Edge case X still fails
- Occasional format errors on Y input

NEXT STEPS:
1. Add specific handling for X
2. Strengthen format requirements
```

## Best Practices

1. **Change one thing at a time** - Isolate impact
2. **Keep all versions** - May need to revert
3. **Document rationale** - Why changes were made
4. **Test thoroughly** - Including regression tests
5. **Set stopping criteria** - Know when "good enough"

## Next Steps

- [03-evaluation-metrics.md](03-evaluation-metrics.md) - Measuring effectiveness
- [../prompt-library/agent-design-prompts.md](../prompt-library/agent-design-prompts.md) - Ready-to-use prompts
