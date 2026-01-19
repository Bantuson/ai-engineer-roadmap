# Evaluation Types Comparison

## Overview

Different evaluation approaches serve different purposes. This guide compares the main types.

## Evaluation Type Matrix

| Type | Speed | Cost | Accuracy | Scalability | Best For |
|------|-------|------|----------|-------------|----------|
| Exact Match | ⚡⚡⚡ | 💰 | ⭐⭐⭐⭐⭐ | ⬆️⬆️⬆️ | Factual tasks |
| Heuristic | ⚡⚡⚡ | 💰 | ⭐⭐⭐ | ⬆️⬆️⬆️ | Format checks |
| LLM-as-Judge | ⚡⚡ | 💰💰 | ⭐⭐⭐⭐ | ⬆️⬆️ | Quality metrics |
| Human Eval | ⚡ | 💰💰💰 | ⭐⭐⭐⭐⭐ | ⬆️ | Ground truth |
| A/B Testing | ⚡ | 💰💰 | ⭐⭐⭐⭐ | ⬆️⬆️ | Production |

## 1. Exact Match / Programmatic

### Description
Direct comparison against known correct answers.

### Implementation
```python
def exact_match_eval(predictions, references):
    """Evaluate exact matches."""
    results = []
    for pred, ref in zip(predictions, references):
        results.append({
            "prediction": pred,
            "reference": ref,
            "match": pred.strip().lower() == ref.strip().lower()
        })
    accuracy = sum(r["match"] for r in results) / len(results)
    return {"accuracy": accuracy, "results": results}
```

### Pros
- ✅ Fast and cheap
- ✅ Perfectly reproducible
- ✅ No subjectivity
- ✅ Easy to implement

### Cons
- ❌ Only works for deterministic tasks
- ❌ Misses partial credit
- ❌ Can't evaluate quality/style
- ❌ Requires ground truth answers

### Best For
- Classification tasks
- Factual extraction
- Multiple choice questions
- Code output verification

---

## 2. Heuristic / Rule-Based

### Description
Check for specific patterns, formats, or properties.

### Implementation
```python
def heuristic_eval(response, rules):
    """Evaluate against heuristic rules."""
    results = {}

    rules_checks = {
        "min_length": lambda r: len(r) >= rules.get("min_length", 0),
        "max_length": lambda r: len(r) <= rules.get("max_length", float('inf')),
        "contains_keyword": lambda r: rules.get("keyword", "") in r,
        "json_valid": lambda r: is_valid_json(r) if rules.get("expect_json") else True,
        "no_profanity": lambda r: not contains_profanity(r),
    }

    for rule_name, check_fn in rules_checks.items():
        results[rule_name] = check_fn(response)

    results["passed"] = all(results.values())
    return results

# Example usage
rules = {
    "min_length": 50,
    "max_length": 500,
    "keyword": "conclusion",
    "expect_json": False,
}
eval_result = heuristic_eval(response, rules)
```

### Pros
- ✅ Very fast
- ✅ Consistent results
- ✅ Customizable to domain
- ✅ No API costs

### Cons
- ❌ Limited to surface features
- ❌ Can't evaluate meaning
- ❌ Requires rule engineering
- ❌ Brittle to edge cases

### Best For
- Format validation
- Safety checks
- Pre-filtering before expensive evals
- Sanity checks

---

## 3. LLM-as-Judge

### Description
Use another LLM to evaluate the output.

### Implementation
```python
def llm_judge_eval(output, query, criteria, judge_model):
    """Use LLM to evaluate output quality."""

    judge_prompt = f"""
You are an expert evaluator. Rate the following response.

Query: {query}
Response: {output}

Evaluate on these criteria (1-5 scale each):
{criteria}

Provide scores in JSON format:
{{"criterion1": score, "criterion2": score, ...}}
"""

    judge_response = judge_model.generate(judge_prompt)
    scores = parse_json(judge_response)

    return {
        "scores": scores,
        "average": sum(scores.values()) / len(scores)
    }

# Example
criteria = """
1. Relevance: How well does the response address the query?
2. Accuracy: Is the information correct?
3. Clarity: Is the response easy to understand?
4. Completeness: Does it cover all aspects?
"""
```

### Pairwise Comparison
```python
def pairwise_comparison(output_a, output_b, query, judge_model):
    """Compare two outputs directly."""

    prompt = f"""
Compare these two responses to the query.

Query: {query}

Response A: {output_a}

Response B: {output_b}

Which response is better? Explain why.
Answer with: "A is better", "B is better", or "Tie"
"""
    return judge_model.generate(prompt)
```

### Pros
- ✅ Can evaluate subjective quality
- ✅ Scalable automation
- ✅ Flexible to different criteria
- ✅ No ground truth needed

### Cons
- ❌ API costs
- ❌ Slower than heuristics
- ❌ Judge model has biases
- ❌ Not perfectly consistent

### Best For
- Quality metrics (coherence, creativity)
- Open-ended generation
- Style evaluation
- Complex multi-criteria assessment

### Tips for LLM-as-Judge
1. **Use stronger models as judges** - GPT-4 judging GPT-3.5
2. **Provide detailed rubrics** - Reduce ambiguity
3. **Include examples** - Few-shot for consistency
4. **Multiple judges** - Average across models
5. **Randomize order** - Avoid position bias in comparisons

---

## 4. Human Evaluation

### Description
Real humans assess the outputs.

### Implementation
```python
def human_eval_task(output, query, evaluator_instructions):
    """Create a human evaluation task."""
    task = {
        "query": query,
        "output": output,
        "instructions": evaluator_instructions,
        "rating_scale": "1-5",
        "criteria": [
            "relevance",
            "accuracy",
            "helpfulness",
            "clarity"
        ],
        "free_text_feedback": True
    }
    # Send to human eval platform (MTurk, Scale, etc.)
    return submit_to_platform(task)

def aggregate_human_evals(evaluations):
    """Aggregate multiple human evaluations."""
    # Handle inter-annotator agreement
    scores = defaultdict(list)
    for eval in evaluations:
        for criterion, score in eval["scores"].items():
            scores[criterion].append(score)

    return {
        criterion: {
            "mean": statistics.mean(s),
            "std": statistics.stdev(s) if len(s) > 1 else 0,
            "agreement": inter_annotator_agreement(s)
        }
        for criterion, s in scores.items()
    }
```

### Pros
- ✅ Ground truth for subjective tasks
- ✅ Can evaluate nuance
- ✅ Catches issues automated evals miss
- ✅ Provides qualitative feedback

### Cons
- ❌ Expensive
- ❌ Slow
- ❌ Inconsistent across evaluators
- ❌ Doesn't scale well

### Best For
- Final quality validation
- Establishing ground truth for auto evals
- User experience evaluation
- Safety/ethics review

### Tips for Human Eval
1. **Clear instructions** - Reduce evaluator variance
2. **Training examples** - Calibrate evaluators
3. **Multiple evaluators** - At least 3 per item
4. **Attention checks** - Filter low-quality evaluators
5. **Regular calibration** - Maintain consistency

---

## 5. A/B Testing (Online)

### Description
Compare variants in production with real users.

### Implementation
```python
def ab_test_setup(variants, traffic_split):
    """Set up A/B test."""
    test_config = {
        "variants": variants,  # {"A": model_v1, "B": model_v2}
        "traffic_split": traffic_split,  # {"A": 0.5, "B": 0.5}
        "metrics": [
            "user_satisfaction",
            "task_completion",
            "engagement",
            "latency"
        ],
        "minimum_sample_size": 1000,
        "duration": "2 weeks"
    }
    return test_config

def analyze_ab_results(variant_a_data, variant_b_data):
    """Statistical analysis of A/B test."""
    from scipy import stats

    # Compare primary metric
    t_stat, p_value = stats.ttest_ind(
        variant_a_data["satisfaction"],
        variant_b_data["satisfaction"]
    )

    return {
        "variant_a_mean": np.mean(variant_a_data["satisfaction"]),
        "variant_b_mean": np.mean(variant_b_data["satisfaction"]),
        "p_value": p_value,
        "significant": p_value < 0.05,
        "winner": "A" if np.mean(variant_a_data["satisfaction"]) >
                        np.mean(variant_b_data["satisfaction"]) else "B"
    }
```

### Pros
- ✅ Real-world signal
- ✅ Captures user preferences
- ✅ Accounts for full system
- ✅ Definitive business impact

### Cons
- ❌ Slow (needs user traffic)
- ❌ Risk of bad user experience
- ❌ Requires production infrastructure
- ❌ Many confounding factors

### Best For
- Final production decisions
- Comparing major versions
- Validating offline improvements
- Business metric optimization

---

## Combining Evaluation Types

### Multi-Stage Pipeline

```python
def evaluation_pipeline(output, query, reference=None):
    """Multi-stage evaluation combining different approaches."""

    results = {"stages": {}}

    # Stage 1: Heuristic checks (fast, cheap)
    heuristic_results = heuristic_eval(output, RULES)
    results["stages"]["heuristic"] = heuristic_results
    if not heuristic_results["passed"]:
        return {"status": "fail", "stage": "heuristic", **results}

    # Stage 2: Exact match if reference available
    if reference:
        exact_results = exact_match_eval([output], [reference])
        results["stages"]["exact_match"] = exact_results
        if exact_results["accuracy"] == 1.0:
            return {"status": "pass", "quality": "exact", **results}

    # Stage 3: LLM-as-judge for quality
    llm_results = llm_judge_eval(output, query, CRITERIA, judge_model)
    results["stages"]["llm_judge"] = llm_results

    # Overall assessment
    results["status"] = "pass" if llm_results["average"] >= 3.5 else "marginal"
    results["quality_score"] = llm_results["average"]

    return results
```

### When to Use What

| Scenario | Recommended Approach |
|----------|---------------------|
| Development iteration | Heuristics + LLM-as-judge |
| Pre-production testing | LLM-as-judge + Sample human eval |
| Production monitoring | Heuristics + A/B testing |
| Major release decision | Full pipeline + A/B test |
| Ground truth establishment | Human evaluation |

## Summary

Choose evaluation types based on:
1. **Task type** - Deterministic vs open-ended
2. **Budget** - Cost constraints
3. **Speed** - Iteration velocity needs
4. **Scale** - Volume of evaluations
5. **Stage** - Development vs production

**Best practice:** Combine multiple types in a pipeline for robust evaluation.
