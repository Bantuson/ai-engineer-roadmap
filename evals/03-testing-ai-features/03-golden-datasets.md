# Golden Datasets for AI Evaluation

## Overview

Golden datasets are curated collections of test cases with verified expected outputs, used as ground truth for evaluation.

## What Makes a Dataset "Golden"

```
┌─────────────────────────────────────────────────────────────┐
│                    Golden Dataset Criteria                   │
├─────────────────────────────────────────────────────────────┤
│ ✓ Representative - Covers real-world use cases              │
│ ✓ Verified - Human-validated expected outputs               │
│ ✓ Diverse - Includes edge cases and variations              │
│ ✓ Versioned - Changes tracked over time                     │
│ ✓ Documented - Clear labels and metadata                    │
│ ✓ Balanced - No category over-represented                   │
└─────────────────────────────────────────────────────────────┘
```

## Dataset Structure

### Standard Format

```json
{
  "name": "Customer Support QA v2.0",
  "version": "2.0.0",
  "created": "2025-01-15",
  "description": "Golden dataset for customer support agent",
  "categories": ["greeting", "billing", "technical", "escalation"],
  "test_cases": [
    {
      "id": "CS-001",
      "category": "greeting",
      "difficulty": "easy",
      "input": {
        "query": "Hello",
        "context": {}
      },
      "expected": {
        "response_contains": ["hello", "hi", "help"],
        "sentiment": "friendly",
        "max_length": 100
      },
      "metadata": {
        "source": "production_logs",
        "frequency": "high",
        "added": "2025-01-10",
        "verified_by": "human_reviewer_1"
      }
    },
    {
      "id": "CS-002",
      "category": "billing",
      "difficulty": "medium",
      "input": {
        "query": "Why was I charged twice?",
        "context": {
          "customer_id": "test_123",
          "recent_charges": [
            {"amount": 29.99, "date": "2025-01-10"},
            {"amount": 29.99, "date": "2025-01-10"}
          ]
        }
      },
      "expected": {
        "response_contains": ["apologize", "investigate", "refund"],
        "actions": ["lookup_charges", "flag_for_review"],
        "tone": "empathetic"
      },
      "metadata": {
        "source": "synthesized",
        "priority": "high",
        "verified_by": "domain_expert_2"
      }
    }
  ]
}
```

### Python Data Classes

```python
"""
Golden dataset data structures.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import date

@dataclass
class TestCaseInput:
    """Input for a test case."""
    query: str
    context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExpectedOutput:
    """Expected output specification."""
    response_contains: List[str] = field(default_factory=list)
    response_not_contains: List[str] = field(default_factory=list)
    exact_match: Optional[str] = None
    min_length: int = 0
    max_length: int = 10000
    format: Optional[str] = None  # "json", "list", "paragraph"
    sentiment: Optional[str] = None
    actions: List[str] = field(default_factory=list)


@dataclass
class TestCaseMetadata:
    """Metadata for a test case."""
    source: str  # "production", "synthesized", "edge_case"
    added: str
    verified_by: str
    frequency: str = "medium"  # "high", "medium", "low"
    priority: str = "medium"
    tags: List[str] = field(default_factory=list)


@dataclass
class GoldenTestCase:
    """Complete golden test case."""
    id: str
    category: str
    difficulty: str  # "easy", "medium", "hard"
    input: TestCaseInput
    expected: ExpectedOutput
    metadata: TestCaseMetadata


@dataclass
class GoldenDataset:
    """Complete golden dataset."""
    name: str
    version: str
    description: str
    categories: List[str]
    test_cases: List[GoldenTestCase]
    created: str = field(default_factory=lambda: date.today().isoformat())
```

## Creating Golden Datasets

### From Production Logs

```python
"""
Extract golden test cases from production data.
"""

import json
from typing import List, Dict

def extract_from_logs(
    logs: List[Dict],
    min_rating: float = 4.0,
    sample_size: int = 100
) -> List[Dict]:
    """
    Extract high-quality interactions from logs.

    Args:
        logs: Production logs with user_query, response, rating
        min_rating: Minimum user rating to include
        sample_size: Number of cases to extract

    Returns:
        List of test case candidates
    """
    # Filter by rating
    high_quality = [
        log for log in logs
        if log.get("rating", 0) >= min_rating
    ]

    # Sample for diversity
    from collections import defaultdict
    by_category = defaultdict(list)

    for log in high_quality:
        category = classify_query(log["user_query"])
        by_category[category].append(log)

    # Take proportional samples
    test_cases = []
    per_category = sample_size // len(by_category)

    for category, items in by_category.items():
        import random
        sampled = random.sample(items, min(per_category, len(items)))

        for item in sampled:
            test_cases.append({
                "id": f"PROD-{len(test_cases):04d}",
                "category": category,
                "input": {"query": item["user_query"]},
                "expected": {
                    "response_contains": extract_key_phrases(item["response"])
                },
                "metadata": {
                    "source": "production",
                    "original_rating": item["rating"],
                    "needs_review": True
                }
            })

    return test_cases


def classify_query(query: str) -> str:
    """Simple query classification."""
    query_lower = query.lower()

    if any(w in query_lower for w in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(w in query_lower for w in ["price", "cost", "charge", "bill"]):
        return "billing"
    elif any(w in query_lower for w in ["error", "bug", "broken", "not working"]):
        return "technical"
    else:
        return "general"


def extract_key_phrases(response: str) -> List[str]:
    """Extract key phrases from response."""
    # Simple extraction - in production use NLP
    import re
    sentences = re.split(r'[.!?]', response)
    phrases = []

    for sentence in sentences[:3]:  # First 3 sentences
        words = sentence.strip().split()
        if len(words) >= 3:
            # Take important-looking phrases
            phrases.append(" ".join(words[:5]))

    return phrases
```

### Synthesizing Test Cases

```python
"""
Synthesize test cases for coverage.
"""

def generate_edge_cases(category: str) -> List[Dict]:
    """
    Generate edge cases for a category.

    Args:
        category: Test category

    Returns:
        List of edge case test cases
    """
    edge_cases = {
        "greeting": [
            {"input": "", "expected": {"handles_empty": True}},
            {"input": "👋", "expected": {"handles_emoji": True}},
            {"input": "Hello " * 100, "expected": {"handles_repetition": True}},
        ],
        "billing": [
            {"input": "Refund $-50", "expected": {"handles_negative": True}},
            {"input": "Charge of $999999999", "expected": {"handles_large_amount": True}},
            {"input": "Bill from 1999", "expected": {"handles_old_date": True}},
        ],
        "technical": [
            {"input": "Error: '; DROP TABLE users;--", "expected": {"handles_injection": True}},
            {"input": "Bug in <script>alert(1)</script>", "expected": {"handles_xss": True}},
            {"input": "\x00\x01\x02", "expected": {"handles_binary": True}},
        ],
    }

    cases = edge_cases.get(category, [])

    return [
        {
            "id": f"EDGE-{category.upper()}-{i:03d}",
            "category": category,
            "difficulty": "hard",
            "input": {"query": case["input"]},
            "expected": case["expected"],
            "metadata": {
                "source": "synthesized_edge_case",
                "needs_review": True
            }
        }
        for i, case in enumerate(cases)
    ]


def generate_variation(base_case: Dict, num_variations: int = 3) -> List[Dict]:
    """
    Generate variations of a base test case.

    Args:
        base_case: Original test case
        num_variations: Number of variations to generate

    Returns:
        List of variation test cases
    """
    variations = []
    query = base_case["input"]["query"]

    transforms = [
        lambda q: q.lower(),
        lambda q: q.upper(),
        lambda q: q + "?",
        lambda q: q + " please",
        lambda q: "Could you " + q.lower(),
        lambda q: "I need help with: " + q,
    ]

    import random
    selected = random.sample(transforms, min(num_variations, len(transforms)))

    for i, transform in enumerate(selected):
        variation = base_case.copy()
        variation["id"] = f"{base_case['id']}-VAR-{i:02d}"
        variation["input"] = {"query": transform(query)}
        variation["metadata"] = {
            **base_case.get("metadata", {}),
            "source": "synthesized_variation",
            "base_case": base_case["id"]
        }
        variations.append(variation)

    return variations
```

### Human Annotation

```python
"""
Human annotation workflow for golden datasets.
"""

from typing import List, Dict, Optional

def create_annotation_task(test_case: Dict) -> Dict:
    """
    Create annotation task for human reviewers.

    Args:
        test_case: Test case needing annotation

    Returns:
        Annotation task
    """
    return {
        "task_id": f"ANNOT-{test_case['id']}",
        "test_case_id": test_case["id"],
        "input": test_case["input"],
        "current_expected": test_case.get("expected", {}),
        "questions": [
            {
                "id": "q1",
                "text": "Is this a valid test case for this category?",
                "type": "boolean"
            },
            {
                "id": "q2",
                "text": "What key phrases should the response contain?",
                "type": "list"
            },
            {
                "id": "q3",
                "text": "What is the expected sentiment?",
                "type": "choice",
                "options": ["friendly", "neutral", "empathetic", "professional"]
            },
            {
                "id": "q4",
                "text": "Rate the difficulty (1-5)",
                "type": "number",
                "min": 1,
                "max": 5
            }
        ]
    }


def process_annotations(
    test_case: Dict,
    annotations: List[Dict],
    min_agreement: float = 0.8
) -> Optional[Dict]:
    """
    Process multiple annotations for a test case.

    Args:
        test_case: Original test case
        annotations: List of human annotations
        min_agreement: Minimum agreement threshold

    Returns:
        Updated test case if agreement met, None otherwise
    """
    if len(annotations) < 2:
        return None

    # Check validity agreement
    valid_votes = sum(1 for a in annotations if a["q1"])
    if valid_votes / len(annotations) < min_agreement:
        return None  # Rejected

    # Aggregate key phrases (intersection of at least 2)
    from collections import Counter
    all_phrases = []
    for a in annotations:
        all_phrases.extend(a.get("q2", []))

    phrase_counts = Counter(all_phrases)
    key_phrases = [p for p, c in phrase_counts.items() if c >= 2]

    # Majority vote for sentiment
    sentiments = [a["q3"] for a in annotations if a.get("q3")]
    sentiment = Counter(sentiments).most_common(1)[0][0] if sentiments else "neutral"

    # Average difficulty
    difficulties = [a["q4"] for a in annotations if a.get("q4")]
    avg_difficulty = sum(difficulties) / len(difficulties) if difficulties else 3

    difficulty_map = {1: "easy", 2: "easy", 3: "medium", 4: "hard", 5: "hard"}

    # Update test case
    updated = test_case.copy()
    updated["expected"] = {
        "response_contains": key_phrases,
        "sentiment": sentiment
    }
    updated["difficulty"] = difficulty_map[round(avg_difficulty)]
    updated["metadata"]["verified_by"] = f"human_consensus_{len(annotations)}"
    updated["metadata"]["annotation_agreement"] = valid_votes / len(annotations)

    return updated
```

## Dataset Maintenance

### Version Control

```python
"""
Dataset versioning and maintenance.
"""

import json
from datetime import datetime
from typing import Dict, List

def bump_version(current: str, change_type: str) -> str:
    """
    Bump semantic version.

    Args:
        current: Current version (e.g., "1.2.3")
        change_type: "major", "minor", or "patch"

    Returns:
        New version string
    """
    major, minor, patch = map(int, current.split("."))

    if change_type == "major":
        return f"{major + 1}.0.0"
    elif change_type == "minor":
        return f"{major}.{minor + 1}.0"
    else:
        return f"{major}.{minor}.{patch + 1}"


def create_dataset_diff(old: Dict, new: Dict) -> Dict:
    """
    Create diff between dataset versions.

    Args:
        old: Previous dataset version
        new: New dataset version

    Returns:
        Diff summary
    """
    old_ids = {tc["id"] for tc in old["test_cases"]}
    new_ids = {tc["id"] for tc in new["test_cases"]}

    added = new_ids - old_ids
    removed = old_ids - new_ids
    common = old_ids & new_ids

    # Check for modifications
    old_by_id = {tc["id"]: tc for tc in old["test_cases"]}
    new_by_id = {tc["id"]: tc for tc in new["test_cases"]}

    modified = []
    for tc_id in common:
        if old_by_id[tc_id] != new_by_id[tc_id]:
            modified.append(tc_id)

    return {
        "old_version": old["version"],
        "new_version": new["version"],
        "added": list(added),
        "removed": list(removed),
        "modified": modified,
        "summary": {
            "added_count": len(added),
            "removed_count": len(removed),
            "modified_count": len(modified),
            "total_old": len(old_ids),
            "total_new": len(new_ids)
        }
    }


def migrate_dataset(
    dataset: Dict,
    migrations: List[Dict]
) -> Dict:
    """
    Apply migrations to dataset.

    Args:
        dataset: Current dataset
        migrations: List of migration operations

    Returns:
        Migrated dataset
    """
    result = json.loads(json.dumps(dataset))  # Deep copy

    for migration in migrations:
        op = migration["operation"]

        if op == "rename_category":
            old_name = migration["old"]
            new_name = migration["new"]

            for tc in result["test_cases"]:
                if tc["category"] == old_name:
                    tc["category"] = new_name

            result["categories"] = [
                new_name if c == old_name else c
                for c in result["categories"]
            ]

        elif op == "add_field":
            field = migration["field"]
            default = migration["default"]

            for tc in result["test_cases"]:
                if field not in tc:
                    tc[field] = default

        elif op == "remove_cases":
            ids_to_remove = set(migration["ids"])
            result["test_cases"] = [
                tc for tc in result["test_cases"]
                if tc["id"] not in ids_to_remove
            ]

    return result
```

### Quality Checks

```python
"""
Dataset quality validation.
"""

from typing import List, Dict, Tuple

def validate_dataset(dataset: Dict) -> Tuple[bool, List[str]]:
    """
    Validate dataset quality.

    Args:
        dataset: Dataset to validate

    Returns:
        (is_valid, list of issues)
    """
    issues = []

    # Check required fields
    required = ["name", "version", "test_cases"]
    for field in required:
        if field not in dataset:
            issues.append(f"Missing required field: {field}")

    # Check test cases
    ids_seen = set()
    for i, tc in enumerate(dataset.get("test_cases", [])):
        # Unique IDs
        if tc.get("id") in ids_seen:
            issues.append(f"Duplicate ID: {tc.get('id')}")
        ids_seen.add(tc.get("id"))

        # Required test case fields
        if "input" not in tc:
            issues.append(f"Test case {i}: missing input")
        if "expected" not in tc:
            issues.append(f"Test case {i}: missing expected")

        # Category validation
        if tc.get("category") not in dataset.get("categories", []):
            issues.append(f"Test case {tc.get('id')}: unknown category {tc.get('category')}")

    # Check balance
    category_counts = {}
    for tc in dataset.get("test_cases", []):
        cat = tc.get("category", "unknown")
        category_counts[cat] = category_counts.get(cat, 0) + 1

    if category_counts:
        min_count = min(category_counts.values())
        max_count = max(category_counts.values())
        if max_count > min_count * 5:
            issues.append(f"Imbalanced categories: {category_counts}")

    return len(issues) == 0, issues


def check_coverage(
    dataset: Dict,
    required_coverage: Dict[str, int]
) -> Tuple[bool, Dict[str, int]]:
    """
    Check if dataset meets coverage requirements.

    Args:
        dataset: Dataset to check
        required_coverage: Required count per category

    Returns:
        (meets_requirements, actual coverage)
    """
    actual = {}
    for tc in dataset.get("test_cases", []):
        cat = tc.get("category", "unknown")
        actual[cat] = actual.get(cat, 0) + 1

    meets = True
    for category, required in required_coverage.items():
        if actual.get(category, 0) < required:
            meets = False

    return meets, actual
```

## Using Golden Datasets

### Evaluation Runner

```python
"""
Run evaluations against golden datasets.
"""

import json
from typing import Callable, Dict, List

def evaluate_against_golden(
    system: Callable,
    dataset_path: str,
    output_path: str
) -> Dict:
    """
    Evaluate system against golden dataset.

    Args:
        system: Function that takes input and returns output
        dataset_path: Path to golden dataset
        output_path: Path for results

    Returns:
        Evaluation summary
    """
    # Load dataset
    with open(dataset_path) as f:
        dataset = json.load(f)

    results = []

    for tc in dataset["test_cases"]:
        # Get system output
        output = system(tc["input"]["query"])

        # Evaluate
        scores = evaluate_output(output, tc["expected"])

        results.append({
            "test_id": tc["id"],
            "category": tc["category"],
            "input": tc["input"],
            "output": output,
            "expected": tc["expected"],
            "scores": scores,
            "passed": all(s >= 0.8 for s in scores.values())
        })

    # Aggregate by category
    by_category = {}
    for r in results:
        cat = r["category"]
        if cat not in by_category:
            by_category[cat] = {"passed": 0, "total": 0}
        by_category[cat]["total"] += 1
        if r["passed"]:
            by_category[cat]["passed"] += 1

    summary = {
        "dataset": dataset["name"],
        "dataset_version": dataset["version"],
        "total_cases": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "pass_rate": sum(1 for r in results if r["passed"]) / len(results),
        "by_category": {
            k: v["passed"] / v["total"]
            for k, v in by_category.items()
        }
    }

    # Save results
    with open(output_path, 'w') as f:
        json.dump({"summary": summary, "results": results}, f, indent=2)

    return summary


def evaluate_output(output: str, expected: Dict) -> Dict[str, float]:
    """Evaluate output against expected criteria."""
    scores = {}

    # Check contains
    if "response_contains" in expected:
        keywords = expected["response_contains"]
        output_lower = output.lower()
        found = sum(1 for k in keywords if k.lower() in output_lower)
        scores["keyword_coverage"] = found / len(keywords) if keywords else 1.0

    # Check not contains
    if "response_not_contains" in expected:
        forbidden = expected["response_not_contains"]
        output_lower = output.lower()
        violations = sum(1 for f in forbidden if f.lower() in output_lower)
        scores["no_forbidden"] = 1.0 - (violations / len(forbidden)) if forbidden else 1.0

    # Check length
    if "max_length" in expected:
        scores["length_ok"] = 1.0 if len(output) <= expected["max_length"] else 0.0

    if "min_length" in expected:
        scores["length_ok"] = 1.0 if len(output) >= expected["min_length"] else 0.0

    return scores
```

## Best Practices

1. **Start with production data** - Real queries are most valuable
2. **Balance categories** - Avoid over-representation
3. **Include edge cases** - Test boundaries and errors
4. **Version everything** - Track all changes
5. **Regular review** - Keep dataset relevant
6. **Multiple annotators** - Reduce bias
7. **Document decisions** - Why cases were included/excluded

## Next Steps

- [../04-ab-testing-monitoring/](../04-ab-testing-monitoring/) - A/B testing
- [../05-capstone-eval-system/](../05-capstone-eval-system/) - Build complete system
