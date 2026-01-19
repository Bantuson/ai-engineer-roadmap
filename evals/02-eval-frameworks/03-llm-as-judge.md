# LLM-as-Judge Evaluation

## Overview

LLM-as-Judge uses language models to evaluate other AI outputs, enabling automated assessment of subjective qualities like coherence, helpfulness, and creativity.

## Why LLM-as-Judge?

### Traditional Metrics Fall Short

```
Query: "Explain quantum entanglement to a 10-year-old"

Response A: "Quantum entanglement is a phenomenon where
particles become correlated such that the quantum state
of each particle cannot be described independently."

Response B: "Imagine you have two magic coins. When you
flip one and it lands on heads, the other one - even
if it's on the other side of the world - will always
land on heads too! That's kind of like entanglement."

BLEU Score: A scores higher (more "technical" words)
Human Preference: B is clearly better for the audience
```

LLM-as-Judge can capture these nuances.

## Basic Implementation

### Simple Judge

```python
def llm_judge(output: str, criteria: str, model) -> dict:
    """Basic LLM-as-judge evaluation."""

    prompt = f"""
You are an expert evaluator. Assess the following output.

Output to evaluate:
{output}

Evaluation criteria:
{criteria}

Provide:
1. Score (1-5)
2. Brief explanation

Format your response as:
Score: [1-5]
Explanation: [your explanation]
"""

    response = model.generate(prompt)
    return parse_judge_response(response)

def parse_judge_response(response: str) -> dict:
    """Parse judge response."""
    lines = response.strip().split('\n')
    score = None
    explanation = ""

    for line in lines:
        if line.startswith("Score:"):
            score = int(line.replace("Score:", "").strip())
        elif line.startswith("Explanation:"):
            explanation = line.replace("Explanation:", "").strip()

    return {"score": score, "explanation": explanation}
```

### Multi-Criteria Judge

```python
def multi_criteria_judge(output: str, query: str, criteria: list, model) -> dict:
    """Evaluate on multiple criteria."""

    criteria_text = "\n".join([f"- {c['name']}: {c['description']}"
                               for c in criteria])

    prompt = f"""
You are an expert evaluator. Assess this response on multiple criteria.

Query: {query}

Response:
{output}

Evaluate on these criteria (1-5 scale each):
{criteria_text}

For each criterion, provide:
- Score (1-5)
- Brief justification

Format as JSON:
{{
  "criterion_name": {{"score": X, "reason": "..."}},
  ...
}}
"""

    response = model.generate(prompt)
    return json.loads(response)

# Example usage
criteria = [
    {"name": "relevance", "description": "How well does it answer the question?"},
    {"name": "accuracy", "description": "Is the information correct?"},
    {"name": "clarity", "description": "Is it easy to understand?"},
    {"name": "completeness", "description": "Does it cover all aspects?"},
]

scores = multi_criteria_judge(output, query, criteria, gpt4)
```

## Pairwise Comparison

### A/B Comparison

```python
def pairwise_compare(output_a: str, output_b: str, query: str, model) -> dict:
    """Compare two outputs directly."""

    prompt = f"""
You are comparing two responses to the same query.

Query: {query}

Response A:
{output_a}

Response B:
{output_b}

Which response is better? Consider:
- Relevance to the query
- Accuracy of information
- Clarity of explanation
- Helpfulness

Respond with:
- Winner: "A", "B", or "Tie"
- Confidence: "High", "Medium", or "Low"
- Explanation: Brief reasoning

Format as JSON:
{{"winner": "...", "confidence": "...", "explanation": "..."}}
"""

    response = model.generate(prompt)
    return json.loads(response)
```

### Tournament Evaluation

```python
def tournament_rank(outputs: list, query: str, model) -> list:
    """Rank multiple outputs via tournament."""

    wins = {i: 0 for i in range(len(outputs))}

    # Round-robin comparison
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            result = pairwise_compare(outputs[i], outputs[j], query, model)

            if result["winner"] == "A":
                wins[i] += 1
            elif result["winner"] == "B":
                wins[j] += 1
            else:  # Tie
                wins[i] += 0.5
                wins[j] += 0.5

    # Rank by wins
    ranked = sorted(wins.items(), key=lambda x: x[1], reverse=True)
    return [{"index": idx, "wins": w, "output": outputs[idx]}
            for idx, w in ranked]
```

## Rubric-Based Evaluation

### Detailed Rubrics

```python
QUALITY_RUBRIC = """
## Evaluation Rubric

### Score 5 - Excellent
- Perfectly addresses the query
- All information is accurate
- Well-organized and clear
- Provides helpful context
- No issues whatsoever

### Score 4 - Good
- Addresses the query well
- Information is mostly accurate
- Clear and organized
- Minor improvements possible

### Score 3 - Adequate
- Addresses the main query
- Some inaccuracies or gaps
- Reasonably clear
- Room for improvement

### Score 2 - Poor
- Partially addresses query
- Notable inaccuracies
- Unclear in places
- Significant gaps

### Score 1 - Very Poor
- Fails to address query
- Major inaccuracies
- Confusing or incoherent
- Unhelpful
"""

def rubric_judge(output: str, query: str, rubric: str, model) -> dict:
    """Evaluate using detailed rubric."""

    prompt = f"""
Evaluate this response using the provided rubric.

Query: {query}

Response:
{output}

{rubric}

Based on this rubric:
1. What score (1-5) does this response deserve?
2. Which rubric level best matches?
3. What specific strengths and weaknesses justify this score?

Provide your evaluation as:
Score: [1-5]
Level: [Excellent/Good/Adequate/Poor/Very Poor]
Strengths: [list]
Weaknesses: [list]
"""

    return model.generate(prompt)
```

## Handling Bias

### Position Bias

LLMs may prefer options based on position (e.g., favoring "A" in A/B tests).

```python
def debiased_compare(output_a: str, output_b: str, query: str, model) -> dict:
    """Compare with position debiasing."""

    # Compare A vs B
    result_ab = pairwise_compare(output_a, output_b, query, model)

    # Compare B vs A (swap positions)
    result_ba = pairwise_compare(output_b, output_a, query, model)

    # Reconcile results
    if result_ab["winner"] == "A" and result_ba["winner"] == "B":
        # Consistent: A wins
        return {"winner": "A", "confidence": "high"}
    elif result_ab["winner"] == "B" and result_ba["winner"] == "A":
        # Consistent: B wins
        return {"winner": "B", "confidence": "high"}
    else:
        # Inconsistent: position bias detected
        return {"winner": "uncertain", "confidence": "low",
                "note": "Position bias detected"}
```

### Self-Enhancement Bias

Models may favor their own outputs.

```python
def cross_model_judge(output: str, query: str, models: list) -> dict:
    """Use multiple models as judges."""

    scores = []
    for model in models:
        result = llm_judge(output, CRITERIA, model)
        scores.append(result["score"])

    return {
        "mean_score": statistics.mean(scores),
        "std_score": statistics.stdev(scores) if len(scores) > 1 else 0,
        "individual_scores": scores,
        "agreement": "high" if statistics.stdev(scores) < 0.5 else "low"
    }
```

### Length Bias

Models may prefer longer responses.

```python
def length_controlled_judge(output: str, query: str, model) -> dict:
    """Judge with explicit length consideration."""

    prompt = f"""
Evaluate this response. IMPORTANT: Do NOT favor longer responses
automatically. A concise, accurate response is better than a
verbose one with the same information.

Query: {query}

Response:
{output}

Evaluate the INFORMATION QUALITY, not the length.
If the response is longer than necessary, note this as a weakness.
If the response is appropriately concise, note this as a strength.

Score (1-5):
Length assessment: [appropriate/too long/too short]
Explanation:
"""

    return model.generate(prompt)
```

## Calibration

### Calibration with Examples

```python
CALIBRATION_EXAMPLES = """
## Calibration Examples

### Example of Score 5:
Query: "What is 2+2?"
Response: "2+2 equals 4."
Why 5: Perfectly correct, concise, directly answers.

### Example of Score 3:
Query: "What is 2+2?"
Response: "Math is the study of numbers. When you add 2 and 2, you
might get different results depending on the number system, but
typically it's 4."
Why 3: Correct answer but unnecessarily verbose and tangential.

### Example of Score 1:
Query: "What is 2+2?"
Response: "That's a great question about mathematics!"
Why 1: Doesn't actually answer the question.
"""

def calibrated_judge(output: str, query: str, examples: str, model) -> dict:
    """Judge with calibration examples."""

    prompt = f"""
{examples}

Now evaluate this response:

Query: {query}

Response:
{output}

Based on the calibration examples above, what score (1-5) does
this response deserve?

Score:
Reasoning:
"""

    return model.generate(prompt)
```

## Implementation: Shared LLM Judge Module

```python
"""
shared/llm_judge.py - Reusable LLM-as-judge module
"""

class LLMJudge:
    """LLM-as-judge evaluation class."""

    def __init__(self, model, rubric=None, examples=None):
        self.model = model
        self.rubric = rubric or DEFAULT_RUBRIC
        self.examples = examples or DEFAULT_EXAMPLES

    def evaluate(self, output: str, query: str, criteria: list = None) -> dict:
        """Evaluate output on criteria."""
        criteria = criteria or DEFAULT_CRITERIA
        return multi_criteria_judge(output, query, criteria, self.model)

    def compare(self, output_a: str, output_b: str, query: str) -> dict:
        """Compare two outputs."""
        return debiased_compare(output_a, output_b, query, self.model)

    def rank(self, outputs: list, query: str) -> list:
        """Rank multiple outputs."""
        return tournament_rank(outputs, query, self.model)

    def score(self, output: str, query: str) -> float:
        """Get single quality score."""
        result = self.evaluate(output, query)
        scores = [c["score"] for c in result.values()]
        return sum(scores) / len(scores)
```

## Best Practices

1. **Use stronger models as judges** - GPT-4 judging GPT-3.5 outputs
2. **Provide detailed rubrics** - Reduce ambiguity
3. **Include calibration examples** - Anchor expectations
4. **Debias comparisons** - Swap positions, use multiple judges
5. **Validate with human evals** - Ensure judge quality
6. **Log explanations** - Debug and improve over time

## Next Steps

- [mini-project-eval-suite/](mini-project-eval-suite/) - Build complete eval suite
- [../scripts/shared/llm_judge.py](../scripts/shared/llm_judge.py) - Implementation
