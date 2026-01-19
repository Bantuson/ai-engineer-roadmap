# Evaluation Metrics

## Overview

Measuring prompt effectiveness requires appropriate metrics. This module covers quantitative and qualitative measures for assessing prompt quality.

## Metric Categories

```
┌─────────────────────────────────────────────────────────────────┐
│                    EVALUATION DIMENSIONS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ACCURACY                      QUALITY                         │
│   ├── Correctness               ├── Relevance                   │
│   ├── Completeness              ├── Coherence                   │
│   ├── Precision                 ├── Fluency                     │
│   └── Recall                    └── Helpfulness                 │
│                                                                  │
│   CONSISTENCY                   EFFICIENCY                      │
│   ├── Same output for same input├── Token usage                 │
│   ├── Format compliance         ├── Latency                     │
│   └── Style consistency         └── Cost per request            │
│                                                                  │
│   SAFETY                        USER SATISFACTION               │
│   ├── Harmful content rate      ├── Task completion             │
│   ├── Bias detection            ├── User feedback               │
│   └── Security violations       └── Preference ranking          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Accuracy Metrics

### Exact Match

```python
def exact_match(predicted: str, expected: str) -> float:
    """
    Simple exact string match.
    Returns 1.0 if match, 0.0 otherwise.
    """
    return 1.0 if predicted.strip() == expected.strip() else 0.0

# Usage
score = exact_match(
    predicted="The capital of France is Paris.",
    expected="The capital of France is Paris."
)
```

### F1 Score (Token-Level)

```python
def token_f1(predicted: str, expected: str) -> float:
    """
    F1 score based on token overlap.
    Good for partial credit on text generation.
    """
    pred_tokens = set(predicted.lower().split())
    exp_tokens = set(expected.lower().split())

    if not pred_tokens or not exp_tokens:
        return 0.0

    overlap = pred_tokens & exp_tokens
    precision = len(overlap) / len(pred_tokens)
    recall = len(overlap) / len(exp_tokens)

    if precision + recall == 0:
        return 0.0

    f1 = 2 * (precision * recall) / (precision + recall)
    return f1
```

### BLEU Score

```python
from collections import Counter
import math

def bleu_score(predicted: str, expected: str, n: int = 4) -> float:
    """
    BLEU score for translation/generation quality.
    """
    pred_tokens = predicted.lower().split()
    exp_tokens = expected.lower().split()

    scores = []
    for i in range(1, n + 1):
        pred_ngrams = Counter(zip(*[pred_tokens[j:] for j in range(i)]))
        exp_ngrams = Counter(zip(*[exp_tokens[j:] for j in range(i)]))

        overlap = sum((pred_ngrams & exp_ngrams).values())
        total = sum(pred_ngrams.values())

        if total == 0:
            scores.append(0)
        else:
            scores.append(overlap / total)

    # Geometric mean with brevity penalty
    if 0 in scores:
        return 0.0

    log_score = sum(math.log(s) for s in scores) / n
    brevity = min(1, len(pred_tokens) / len(exp_tokens))

    return brevity * math.exp(log_score)
```

### ROUGE Score

```python
def rouge_l(predicted: str, expected: str) -> dict:
    """
    ROUGE-L score based on longest common subsequence.
    """
    pred_tokens = predicted.lower().split()
    exp_tokens = expected.lower().split()

    # LCS length using dynamic programming
    m, n = len(pred_tokens), len(exp_tokens)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pred_tokens[i-1] == exp_tokens[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[m][n]

    precision = lcs_length / m if m > 0 else 0
    recall = lcs_length / n if n > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

    return {"precision": precision, "recall": recall, "f1": f1}
```

## Quality Metrics

### Relevance Scoring

```
RELEVANCE EVALUATION PROMPT:

Rate the relevance of this response to the question.

Question: {question}
Response: {response}

Score 1-5:
1 - Completely irrelevant
2 - Mostly irrelevant, mentions topic tangentially
3 - Partially relevant, addresses some aspects
4 - Mostly relevant, good coverage
5 - Fully relevant, directly addresses question

Provide:
- Score: [1-5]
- Justification: [brief explanation]
```

### Coherence Scoring

```
COHERENCE EVALUATION PROMPT:

Evaluate the coherence of this text.

Text: {text}

Evaluate on:
1. Logical flow - Do ideas connect logically?
2. Consistency - No contradictions?
3. Completeness - All points developed?
4. Structure - Clear organization?

Score 1-5 for each, then average.

Provide:
- Logical flow: [1-5]
- Consistency: [1-5]
- Completeness: [1-5]
- Structure: [1-5]
- Overall: [average]
```

### Helpfulness Scoring

```
HELPFULNESS EVALUATION PROMPT:

Rate how helpful this response is for the user's task.

User task: {task}
Response: {response}

Consider:
- Does it solve the user's problem?
- Is the information actionable?
- Is it easy to understand and use?
- Does it anticipate follow-up needs?

Score 1-5:
1 - Not helpful at all
2 - Slightly helpful
3 - Moderately helpful
4 - Very helpful
5 - Extremely helpful

Provide:
- Score: [1-5]
- What made it helpful/unhelpful: [explanation]
```

## Consistency Metrics

### Output Stability

```python
def measure_consistency(prompt: str, input_data: str, n_runs: int = 5) -> dict:
    """
    Measure how consistent outputs are across multiple runs.
    """
    outputs = []
    for _ in range(n_runs):
        output = call_llm(prompt, input_data, temperature=0)
        outputs.append(output)

    # Exact match consistency
    unique_outputs = set(outputs)
    exact_consistency = 1 / len(unique_outputs)

    # Semantic similarity consistency
    similarities = []
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            sim = semantic_similarity(outputs[i], outputs[j])
            similarities.append(sim)

    avg_similarity = sum(similarities) / len(similarities) if similarities else 1.0

    return {
        "exact_consistency": exact_consistency,
        "unique_outputs": len(unique_outputs),
        "semantic_consistency": avg_similarity,
        "outputs": outputs
    }
```

### Format Compliance

```python
def check_format_compliance(output: str, schema: dict) -> dict:
    """
    Check if output matches expected format.
    """
    results = {
        "valid": True,
        "errors": []
    }

    # Check if valid JSON
    try:
        parsed = json.loads(output)
    except json.JSONDecodeError as e:
        results["valid"] = False
        results["errors"].append(f"Invalid JSON: {e}")
        return results

    # Check required fields
    for field in schema.get("required", []):
        if field not in parsed:
            results["valid"] = False
            results["errors"].append(f"Missing required field: {field}")

    # Check types
    for field, expected_type in schema.get("types", {}).items():
        if field in parsed:
            actual_type = type(parsed[field]).__name__
            if actual_type != expected_type:
                results["errors"].append(
                    f"Wrong type for {field}: expected {expected_type}, got {actual_type}"
                )

    return results
```

## Efficiency Metrics

### Token Efficiency

```python
def measure_efficiency(prompt: str, input_data: str, output: str) -> dict:
    """
    Measure token usage efficiency.
    """
    # Count tokens (simplified - use tiktoken for accuracy)
    prompt_tokens = len(prompt.split())
    input_tokens = len(input_data.split())
    output_tokens = len(output.split())

    total_tokens = prompt_tokens + input_tokens + output_tokens

    # Calculate ratios
    output_ratio = output_tokens / (prompt_tokens + input_tokens)
    useful_content_ratio = estimate_useful_content(output) / output_tokens

    return {
        "prompt_tokens": prompt_tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "output_ratio": output_ratio,
        "efficiency_score": useful_content_ratio
    }
```

### Cost Analysis

```python
def calculate_cost(usage: dict, pricing: dict) -> dict:
    """
    Calculate cost for API calls.
    """
    input_cost = usage["prompt_tokens"] * pricing["input_per_1k"] / 1000
    output_cost = usage["completion_tokens"] * pricing["output_per_1k"] / 1000
    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost,
        "cost_per_output_token": total_cost / usage["completion_tokens"]
    }
```

## LLM-as-Judge Evaluation

### Pairwise Comparison

```
PAIRWISE COMPARISON PROMPT:

Compare these two responses to the same question.

Question: {question}

Response A:
{response_a}

Response B:
{response_b}

Which response is better? Consider:
- Accuracy of information
- Completeness of answer
- Clarity of explanation
- Usefulness for the user

Output:
- Winner: [A/B/Tie]
- Confidence: [High/Medium/Low]
- Reasoning: [brief explanation]
```

### Multi-Criteria Evaluation

```
MULTI-CRITERIA EVALUATION:

Evaluate this response on multiple criteria.

Question: {question}
Response: {response}

CRITERIA (score 1-5 each):

1. ACCURACY
   Is the information factually correct?
   Score: [1-5]

2. COMPLETENESS
   Does it fully address the question?
   Score: [1-5]

3. CLARITY
   Is it easy to understand?
   Score: [1-5]

4. CONCISENESS
   Is it appropriately detailed (not too long/short)?
   Score: [1-5]

5. HELPFULNESS
   Does it provide actionable value?
   Score: [1-5]

OVERALL: [weighted average or summary]
MAIN STRENGTH: [what it does best]
MAIN WEAKNESS: [area for improvement]
```

## Aggregating Metrics

### Weighted Composite Score

```python
def composite_score(metrics: dict, weights: dict) -> float:
    """
    Calculate weighted composite score from multiple metrics.
    """
    score = 0
    total_weight = 0

    for metric, weight in weights.items():
        if metric in metrics:
            # Normalize metric to 0-1 range if needed
            normalized = normalize_metric(metrics[metric], metric)
            score += normalized * weight
            total_weight += weight

    return score / total_weight if total_weight > 0 else 0


# Example weights
EVALUATION_WEIGHTS = {
    "accuracy": 0.3,
    "relevance": 0.25,
    "coherence": 0.15,
    "format_compliance": 0.15,
    "efficiency": 0.15
}
```

### Reporting Template

```
PROMPT EVALUATION REPORT

Prompt: {prompt_name}
Version: {version}
Date: {date}
Test Set: {test_set_name} ({n} cases)

ACCURACY METRICS:
- Exact Match: X%
- F1 Score: X.XX
- BLEU: X.XX

QUALITY METRICS:
- Relevance: X.X/5
- Coherence: X.X/5
- Helpfulness: X.X/5

CONSISTENCY METRICS:
- Format Compliance: X%
- Output Stability: X%

EFFICIENCY METRICS:
- Avg Tokens: X
- Avg Cost: $X.XX

COMPOSITE SCORE: X.XX/1.00

COMPARISON TO BASELINE:
- Accuracy: +X% / -X%
- Quality: +X% / -X%

RECOMMENDATIONS:
- [improvement suggestion 1]
- [improvement suggestion 2]
```

## Best Practices

1. **Choose appropriate metrics** - Match metrics to task type
2. **Use multiple metrics** - No single metric captures everything
3. **Establish baselines** - Compare to previous versions
4. **Test on diverse data** - Avoid overfitting to test set
5. **Include human evaluation** - Automated metrics have limits

## Next Steps

- [../prompt-library/agent-design-prompts.md](../prompt-library/agent-design-prompts.md) - Agent prompts
- [../prompt-library/security-prompts.md](../prompt-library/security-prompts.md) - Security prompts
