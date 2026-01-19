# RAGAS and DeepEval for RAG Systems

## Overview

RAGAS (Retrieval-Augmented Generation Assessment) and DeepEval are specialized frameworks for evaluating RAG pipelines and LLM applications.

## RAGAS Framework

### What is RAGAS?

RAGAS provides metrics specifically designed for RAG systems:
- **Context Relevance** - Are retrieved documents relevant?
- **Faithfulness** - Is the answer grounded in context?
- **Answer Relevance** - Does the answer address the question?

### Installation

```bash
pip install ragas
```

### Core Metrics

#### 1. Context Precision
How many retrieved contexts are relevant?

```python
from ragas.metrics import context_precision

# Higher is better (0-1)
# Measures: relevant_contexts / total_retrieved
```

#### 2. Context Recall
Are all relevant contexts retrieved?

```python
from ragas.metrics import context_recall

# Higher is better (0-1)
# Measures: retrieved_relevant / all_relevant
```

#### 3. Faithfulness
Is the answer supported by the context?

```python
from ragas.metrics import faithfulness

# Higher is better (0-1)
# Checks if claims in answer are supported by context
```

#### 4. Answer Relevancy
Does the answer address the question?

```python
from ragas.metrics import answer_relevancy

# Higher is better (0-1)
# Measures semantic similarity of answer to question
```

### Basic Usage

```python
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy
)
from datasets import Dataset

# Prepare evaluation data
data = {
    "question": ["What is the capital of France?"],
    "answer": ["The capital of France is Paris."],
    "contexts": [["France is a country in Europe. Paris is the capital of France."]],
    "ground_truth": ["Paris"]
}

dataset = Dataset.from_dict(data)

# Run evaluation
results = evaluate(
    dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy
    ]
)

print(results)
# {'context_precision': 0.95, 'context_recall': 0.88, ...}
```

### Evaluating a RAG Pipeline

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

def evaluate_rag_system(rag_pipeline, test_questions, ground_truths):
    """Evaluate a RAG system with RAGAS."""

    # Generate answers
    results = []
    for question, truth in zip(test_questions, ground_truths):
        response = rag_pipeline.query(question)
        results.append({
            "question": question,
            "answer": response.answer,
            "contexts": response.retrieved_contexts,
            "ground_truth": truth
        })

    # Convert to dataset
    dataset = Dataset.from_list(results)

    # Evaluate
    scores = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy]
    )

    return scores
```

---

## DeepEval Framework

### What is DeepEval?

DeepEval is a comprehensive LLM evaluation framework that:
- Provides pre-built metrics
- Supports custom metrics
- Integrates with CI/CD
- Generates reports

### Installation

```bash
pip install deepeval
```

### Core Metrics

```python
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    HallucinationMetric,
    ToxicityMetric,
    BiasMetric
)
```

### Basic Usage

```python
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

# Create test case
test_case = LLMTestCase(
    input="What is the capital of France?",
    actual_output="The capital of France is Paris.",
    expected_output="Paris",
    retrieval_context=["France is a European country. Paris is its capital."]
)

# Define metrics
relevancy_metric = AnswerRelevancyMetric(
    threshold=0.7,  # Minimum passing score
    model="gpt-4"   # Model for evaluation
)

faithfulness_metric = FaithfulnessMetric(
    threshold=0.7
)

# Evaluate
relevancy_metric.measure(test_case)
print(f"Relevancy: {relevancy_metric.score}")
print(f"Reason: {relevancy_metric.reason}")

faithfulness_metric.measure(test_case)
print(f"Faithfulness: {faithfulness_metric.score}")
```

### Running Tests

```python
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

def test_chatbot_relevancy():
    """Test chatbot answer relevancy."""
    test_case = LLMTestCase(
        input="How do I reset my password?",
        actual_output=chatbot.respond("How do I reset my password?"),
        expected_output="Go to settings and click 'Reset Password'"
    )

    metric = AnswerRelevancyMetric(threshold=0.7)
    assert_test(test_case, [metric])

# Run with pytest
# pytest test_chatbot.py
```

### Custom Metrics

```python
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

class CustomQualityMetric(BaseMetric):
    """Custom metric for domain-specific quality."""

    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold
        self.score = None
        self.reason = None

    def measure(self, test_case: LLMTestCase) -> float:
        """Measure the metric."""
        # Your custom evaluation logic
        output = test_case.actual_output

        # Example: Check for specific quality criteria
        score = 0.0

        if len(output) > 50:
            score += 0.3

        if "technical" in output.lower():
            score += 0.3

        if output.endswith("."):
            score += 0.2

        # Could also use LLM for evaluation
        # llm_score = self.evaluate_with_llm(output, test_case.input)

        self.score = score
        self.success = score >= self.threshold
        self.reason = f"Quality score: {score}"

        return score

    def is_successful(self) -> bool:
        return self.success

    @property
    def __name__(self):
        return "Custom Quality"
```

### Batch Evaluation

```python
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ToxicityMetric
)

def batch_evaluate_rag(test_cases_data):
    """Evaluate multiple test cases."""

    test_cases = []
    for data in test_cases_data:
        test_cases.append(LLMTestCase(
            input=data["question"],
            actual_output=data["answer"],
            retrieval_context=data["contexts"]
        ))

    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.7),
        ToxicityMetric(threshold=0.5)  # Lower = less toxic
    ]

    results = evaluate(test_cases, metrics)

    # Generate report
    print(f"Overall pass rate: {results.pass_rate}")
    for metric_result in results.metrics:
        print(f"{metric_result.name}: {metric_result.score}")

    return results
```

---

## Comparison

| Feature | RAGAS | DeepEval |
|---------|-------|----------|
| Focus | RAG-specific | General LLM |
| Setup | Simple | More comprehensive |
| Metrics | RAG-focused | Broad coverage |
| Custom metrics | Limited | Full support |
| CI/CD | Basic | Built-in |
| Reporting | Basic | Rich |
| Cost | Free | Free + paid |

### When to Use Which

**Use RAGAS when:**
- Building RAG systems
- Need quick RAG evaluation
- Want simple setup

**Use DeepEval when:**
- Need comprehensive testing
- Building general LLM apps
- Want CI/CD integration
- Need custom metrics
- Want detailed reports

---

## Best Practices

### 1. Create Representative Test Sets

```python
# Good: Diverse, representative test cases
test_cases = [
    # Factual questions
    {"q": "What is X?", "type": "factual"},
    # Analytical questions
    {"q": "Why does X happen?", "type": "analytical"},
    # Edge cases
    {"q": "What if X but also Y?", "type": "edge"},
    # Out of scope
    {"q": "Unrelated question", "type": "oos"}
]
```

### 2. Set Appropriate Thresholds

```python
# Adjust based on use case
critical_apps_threshold = 0.9  # Healthcare, finance
standard_apps_threshold = 0.7  # General use
experimental_threshold = 0.5   # Early development
```

### 3. Combine Multiple Metrics

```python
# Don't rely on single metric
metrics = [
    faithfulness,     # Is it grounded?
    relevancy,        # Does it answer?
    toxicity,         # Is it safe?
    context_precision # Was retrieval good?
]
```

### 4. Regular Evaluation

```python
# Run evals in CI/CD
def test_on_commit():
    results = evaluate(test_cases, metrics)
    assert results.pass_rate >= 0.8, "Quality dropped!"
```

## Next Steps

- [02-custom-eval-scripts.md](02-custom-eval-scripts.md) - Build custom evaluations
- [03-llm-as-judge.md](03-llm-as-judge.md) - LLM-as-judge techniques
