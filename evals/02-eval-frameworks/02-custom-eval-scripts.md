# Building Custom Evaluation Scripts

## Overview

While frameworks like RAGAS and DeepEval are powerful, custom evaluation scripts give you full control for domain-specific needs.

## Script Architecture

### Basic Structure

```python
"""
Custom Evaluation Script Template
"""

import json
import argparse
from dataclasses import dataclass
from typing import List, Dict, Any
import statistics

# ============= Configuration =============

@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: str = "test_cases.json"
    output_file: str = "results.json"
    metrics: List[str] = None
    verbose: bool = False

# ============= Test Cases =============

def load_test_cases(filepath: str) -> List[Dict]:
    """Load test cases from file."""
    with open(filepath, 'r') as f:
        return json.load(f)

# ============= System Under Test =============

def run_system(input_data: Dict) -> Dict:
    """Run the system being evaluated."""
    # Import and call your system
    # from my_system import MyAgent
    # return MyAgent().process(input_data)
    pass

# ============= Metrics =============

def metric_accuracy(prediction: str, reference: str) -> float:
    """Calculate accuracy."""
    return 1.0 if prediction.strip().lower() == reference.strip().lower() else 0.0

def metric_length_ratio(prediction: str, reference: str) -> float:
    """Calculate length ratio."""
    if len(reference) == 0:
        return 0.0
    return min(len(prediction) / len(reference), 2.0) / 2.0

def metric_keyword_coverage(prediction: str, keywords: List[str]) -> float:
    """Calculate keyword coverage."""
    if not keywords:
        return 1.0
    covered = sum(1 for k in keywords if k.lower() in prediction.lower())
    return covered / len(keywords)

METRICS = {
    "accuracy": metric_accuracy,
    "length_ratio": metric_length_ratio,
    "keyword_coverage": metric_keyword_coverage,
}

# ============= Evaluation Loop =============

def evaluate_single(test_case: Dict, metrics: List[str]) -> Dict:
    """Evaluate a single test case."""
    # Run system
    output = run_system(test_case["input"])

    # Calculate metrics
    scores = {}
    for metric_name in metrics:
        if metric_name in METRICS:
            metric_fn = METRICS[metric_name]
            if metric_name == "keyword_coverage":
                scores[metric_name] = metric_fn(
                    output["response"],
                    test_case.get("keywords", [])
                )
            else:
                scores[metric_name] = metric_fn(
                    output["response"],
                    test_case.get("expected", "")
                )

    return {
        "input": test_case["input"],
        "output": output,
        "expected": test_case.get("expected"),
        "scores": scores,
    }

def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> Dict:
    """Evaluate all test cases."""
    results = []
    metrics = config.metrics or list(METRICS.keys())

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            print(f"Evaluating {i+1}/{len(test_cases)}...")

        result = evaluate_single(test_case, metrics)
        results.append(result)

    # Aggregate scores
    aggregates = {}
    for metric in metrics:
        scores = [r["scores"].get(metric, 0) for r in results]
        aggregates[metric] = {
            "mean": statistics.mean(scores),
            "std": statistics.stdev(scores) if len(scores) > 1 else 0,
            "min": min(scores),
            "max": max(scores),
        }

    return {
        "config": vars(config),
        "summary": aggregates,
        "results": results,
    }

# ============= Reporting =============

def generate_report(eval_results: Dict) -> str:
    """Generate human-readable report."""
    lines = ["=" * 50, "EVALUATION REPORT", "=" * 50, ""]

    # Summary
    lines.append("SUMMARY")
    lines.append("-" * 30)
    for metric, stats in eval_results["summary"].items():
        lines.append(f"{metric}:")
        lines.append(f"  Mean: {stats['mean']:.3f}")
        lines.append(f"  Std:  {stats['std']:.3f}")
        lines.append(f"  Range: [{stats['min']:.3f}, {stats['max']:.3f}]")
    lines.append("")

    # Details (optional)
    lines.append("DETAILS")
    lines.append("-" * 30)
    for i, result in enumerate(eval_results["results"][:5]):  # First 5
        lines.append(f"Test {i+1}:")
        lines.append(f"  Input: {result['input'][:50]}...")
        lines.append(f"  Scores: {result['scores']}")
    if len(eval_results["results"]) > 5:
        lines.append(f"  ... and {len(eval_results['results']) - 5} more")

    return "\n".join(lines)

# ============= Main =============

def main():
    parser = argparse.ArgumentParser(description="Run evaluation")
    parser.add_argument("--test-file", default="test_cases.json")
    parser.add_argument("--output", default="results.json")
    parser.add_argument("--metrics", nargs="+", default=None)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    config = EvalConfig(
        test_file=args.test_file,
        output_file=args.output,
        metrics=args.metrics,
        verbose=args.verbose,
    )

    # Load and evaluate
    test_cases = load_test_cases(config.test_file)
    results = evaluate_all(test_cases, config)

    # Save results
    with open(config.output_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Print report
    if args.report:
        print(generate_report(results))

if __name__ == "__main__":
    main()
```

## Domain-Specific Examples

### Story Generation Eval

```python
"""
Evaluation script for story generation.
"""

def metric_creativity(story: str, judge_model) -> float:
    """Evaluate story creativity using LLM."""
    prompt = f"""
Rate this story's creativity from 1-5:

Story:
{story}

Consider:
- Originality of plot
- Unique characters
- Surprising elements
- Fresh perspective

Score (1-5):"""

    response = judge_model.generate(prompt)
    return parse_score(response) / 5.0  # Normalize to 0-1

def metric_coherence(story: str, judge_model) -> float:
    """Evaluate story coherence using LLM."""
    prompt = f"""
Rate this story's coherence from 1-5:

Story:
{story}

Consider:
- Logical plot progression
- Consistent characters
- No contradictions
- Clear narrative flow

Score (1-5):"""

    response = judge_model.generate(prompt)
    return parse_score(response) / 5.0

def metric_theme_adherence(story: str, theme: str, judge_model) -> float:
    """Evaluate how well story matches theme."""
    prompt = f"""
Rate how well this story matches the theme from 1-5:

Theme: {theme}

Story:
{story}

Score (1-5):"""

    response = judge_model.generate(prompt)
    return parse_score(response) / 5.0
```

### Translation Quality Eval

```python
"""
Evaluation script for translation.
"""

from sacrebleu import corpus_bleu

def metric_bleu(translations: List[str], references: List[str]) -> float:
    """Calculate BLEU score."""
    return corpus_bleu(translations, [references]).score / 100.0

def metric_back_translation_consistency(
    original: str,
    translated: str,
    translator,
    back_translator
) -> float:
    """Check consistency via back-translation."""
    # Translate and back-translate
    back_translated = back_translator.translate(translated)

    # Compare semantic similarity
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')

    emb_original = model.encode(original)
    emb_back = model.encode(back_translated)

    # Cosine similarity
    similarity = np.dot(emb_original, emb_back) / (
        np.linalg.norm(emb_original) * np.linalg.norm(emb_back)
    )
    return similarity

def metric_fluency(text: str, judge_model, target_lang: str) -> float:
    """Evaluate fluency in target language."""
    prompt = f"""
Rate the fluency of this {target_lang} text from 1-5:

Text: {text}

1 - Incomprehensible
2 - Major errors
3 - Understandable with errors
4 - Minor errors
5 - Native-quality

Score (1-5):"""

    response = judge_model.generate(prompt)
    return parse_score(response) / 5.0
```

### Routing Accuracy Eval

```python
"""
Evaluation script for routing/classification.
"""

from sklearn.metrics import classification_report, confusion_matrix

def evaluate_router(router, test_cases: List[Dict]) -> Dict:
    """Evaluate routing accuracy."""

    predictions = []
    labels = []

    for case in test_cases:
        pred = router.route(case["query"])
        predictions.append(pred)
        labels.append(case["expected_route"])

    # Calculate metrics
    report = classification_report(labels, predictions, output_dict=True)
    conf_matrix = confusion_matrix(labels, predictions)

    # Per-class accuracy
    classes = list(set(labels))
    class_accuracy = {}
    for cls in classes:
        cls_cases = [p == l for p, l in zip(predictions, labels) if l == cls]
        class_accuracy[cls] = sum(cls_cases) / len(cls_cases) if cls_cases else 0

    return {
        "overall_accuracy": report["accuracy"],
        "per_class_accuracy": class_accuracy,
        "classification_report": report,
        "confusion_matrix": conf_matrix.tolist(),
    }
```

## Test Case Format

### JSON Schema

```json
{
  "test_cases": [
    {
      "id": "test_001",
      "input": {
        "query": "What is the capital of France?",
        "context": "optional context"
      },
      "expected": {
        "answer": "Paris",
        "keywords": ["Paris", "capital", "France"]
      },
      "metadata": {
        "category": "factual",
        "difficulty": "easy",
        "source": "geography_dataset"
      }
    }
  ]
}
```

### Creating Test Cases

```python
def create_test_cases(data_source, sample_size=100):
    """Create test cases from data source."""
    test_cases = []

    for item in data_source.sample(sample_size):
        test_case = {
            "id": f"test_{len(test_cases):04d}",
            "input": {
                "query": item["question"]
            },
            "expected": {
                "answer": item["answer"],
                "keywords": extract_keywords(item["answer"])
            },
            "metadata": {
                "category": item.get("category", "unknown"),
                "source": "generated"
            }
        }
        test_cases.append(test_case)

    return {"test_cases": test_cases}
```

## Running Evaluations

### Command Line

```bash
# Basic run
python eval_script.py --test-file tests.json

# With specific metrics
python eval_script.py --test-file tests.json --metrics accuracy coherence

# Generate report
python eval_script.py --test-file tests.json --report --verbose

# Output to specific file
python eval_script.py --test-file tests.json --output results/run_001.json
```

### Programmatic

```python
# Import and run
from eval_script import evaluate_all, EvalConfig, load_test_cases

config = EvalConfig(
    test_file="tests.json",
    metrics=["accuracy", "creativity"],
    verbose=True
)

test_cases = load_test_cases(config.test_file)
results = evaluate_all(test_cases, config)

print(f"Mean accuracy: {results['summary']['accuracy']['mean']}")
```

## Best Practices

1. **Version your test cases** - Track changes over time
2. **Stratify test sets** - Include all relevant categories
3. **Document metrics** - Explain what each measures
4. **Set baselines** - Know what "good" looks like
5. **Automate runs** - Integrate with CI/CD
6. **Track trends** - Monitor metrics over time

## Next Steps

- [03-llm-as-judge.md](03-llm-as-judge.md) - Learn LLM-as-judge techniques
- [../scripts/](../scripts/) - See example eval scripts
