# Regression Testing for AI Systems

## Overview

Regression testing ensures AI system quality doesn't degrade when changes are made to prompts, models, or code.

## Why Regression Testing Matters

```
┌─────────────────────────────────────────────────────────────┐
│                    Without Regression Testing                │
├─────────────────────────────────────────────────────────────┤
│ Day 1: "Improve prompt for clarity"                          │
│ Day 2: "Model upgrade looks good"                            │
│ Day 3: "Quick fix for edge case"                             │
│ Day 7: "Why is accuracy down 20%?" 😱                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    With Regression Testing                   │
├─────────────────────────────────────────────────────────────┤
│ Day 1: Change prompt → Run tests → 95% pass ✓                │
│ Day 2: Model upgrade → Run tests → 92% pass ⚠️ (investigate)│
│ Day 3: Edge case fix → Run tests → 96% pass ✓                │
│ Day 7: Confidence in system quality 😊                       │
└─────────────────────────────────────────────────────────────┘
```

## Baseline Establishment

### Creating a Baseline

```python
"""
Baseline creation for regression testing.
"""

import json
from datetime import datetime
from typing import Dict, List, Any

def create_baseline(
    system_function,
    test_cases: List[Dict],
    metrics: List[str],
    version: str
) -> Dict[str, Any]:
    """
    Create evaluation baseline.

    Args:
        system_function: Function to evaluate
        test_cases: List of test inputs/expected outputs
        metrics: Metrics to calculate
        version: Version identifier

    Returns:
        Baseline dictionary
    """
    results = []

    for test in test_cases:
        output = system_function(test["input"])
        scores = calculate_metrics(output, test["expected"], metrics)

        results.append({
            "input": test["input"],
            "output": output,
            "expected": test["expected"],
            "scores": scores
        })

    # Aggregate metrics
    aggregates = {}
    for metric in metrics:
        scores = [r["scores"][metric] for r in results]
        aggregates[metric] = {
            "mean": sum(scores) / len(scores),
            "min": min(scores),
            "max": max(scores)
        }

    baseline = {
        "version": version,
        "timestamp": datetime.now().isoformat(),
        "test_count": len(test_cases),
        "aggregates": aggregates,
        "results": results
    }

    return baseline


def save_baseline(baseline: Dict, filepath: str):
    """Save baseline to file."""
    with open(filepath, 'w') as f:
        json.dump(baseline, f, indent=2)


def load_baseline(filepath: str) -> Dict:
    """Load baseline from file."""
    with open(filepath, 'r') as f:
        return json.load(f)


# Example usage
if __name__ == "__main__":
    from my_agent import process_query

    test_cases = [
        {"input": "What is 2+2?", "expected": "4"},
        {"input": "Capital of France?", "expected": "Paris"},
    ]

    baseline = create_baseline(
        system_function=process_query,
        test_cases=test_cases,
        metrics=["accuracy", "response_quality"],
        version="v1.0.0"
    )

    save_baseline(baseline, "baselines/v1.0.0.json")
```

### Baseline Storage Structure

```
baselines/
├── v1.0.0/
│   ├── baseline.json
│   ├── test_cases.json
│   └── metadata.yaml
├── v1.1.0/
│   ├── baseline.json
│   ├── test_cases.json
│   └── metadata.yaml
└── latest -> v1.1.0/
```

## Regression Detection

### Comparing Against Baseline

```python
"""
Regression detection by comparing to baseline.
"""

from typing import Dict, List, Tuple

def compare_to_baseline(
    current_results: Dict,
    baseline: Dict,
    threshold: float = 0.05
) -> Dict[str, Any]:
    """
    Compare current results to baseline.

    Args:
        current_results: Current evaluation results
        baseline: Baseline to compare against
        threshold: Maximum acceptable regression (e.g., 0.05 = 5%)

    Returns:
        Comparison report
    """
    regressions = []
    improvements = []
    stable = []

    for metric, current_stats in current_results["aggregates"].items():
        baseline_stats = baseline["aggregates"].get(metric, {})

        current_mean = current_stats["mean"]
        baseline_mean = baseline_stats.get("mean", 0)

        diff = current_mean - baseline_mean
        pct_change = (diff / baseline_mean * 100) if baseline_mean != 0 else 0

        comparison = {
            "metric": metric,
            "baseline": baseline_mean,
            "current": current_mean,
            "diff": diff,
            "pct_change": pct_change
        }

        if diff < -threshold * baseline_mean:
            regressions.append(comparison)
        elif diff > threshold * baseline_mean:
            improvements.append(comparison)
        else:
            stable.append(comparison)

    return {
        "baseline_version": baseline["version"],
        "current_version": current_results.get("version", "unknown"),
        "regressions": regressions,
        "improvements": improvements,
        "stable": stable,
        "has_regressions": len(regressions) > 0
    }


def detailed_comparison(current: Dict, baseline: Dict) -> List[Dict]:
    """
    Compare individual test cases.

    Returns:
        List of test case comparisons
    """
    comparisons = []

    # Index baseline results by input
    baseline_by_input = {
        r["input"]: r for r in baseline["results"]
    }

    for current_result in current["results"]:
        input_key = current_result["input"]
        baseline_result = baseline_by_input.get(input_key, {})

        comparison = {
            "input": input_key,
            "current_output": current_result["output"],
            "baseline_output": baseline_result.get("output"),
            "output_changed": current_result["output"] != baseline_result.get("output"),
            "score_changes": {}
        }

        for metric, score in current_result["scores"].items():
            baseline_score = baseline_result.get("scores", {}).get(metric, 0)
            comparison["score_changes"][metric] = {
                "current": score,
                "baseline": baseline_score,
                "diff": score - baseline_score
            }

        comparisons.append(comparison)

    return comparisons
```

### Automated Regression Alerts

```python
"""
Automated regression alerting.
"""

def check_for_regressions(
    comparison: Dict,
    critical_metrics: List[str] = None,
    alert_threshold: float = 0.1
) -> Tuple[bool, List[str]]:
    """
    Check if regressions require alerting.

    Args:
        comparison: Comparison report
        critical_metrics: Metrics that trigger immediate alert
        alert_threshold: Threshold for alerting (e.g., 0.1 = 10% drop)

    Returns:
        (should_alert, alert_messages)
    """
    critical_metrics = critical_metrics or ["accuracy"]
    alerts = []

    for regression in comparison["regressions"]:
        metric = regression["metric"]
        pct_change = regression["pct_change"]

        if metric in critical_metrics:
            alerts.append(
                f"CRITICAL: {metric} dropped {abs(pct_change):.1f}% "
                f"({regression['baseline']:.3f} -> {regression['current']:.3f})"
            )
        elif abs(pct_change) > alert_threshold * 100:
            alerts.append(
                f"WARNING: {metric} dropped {abs(pct_change):.1f}%"
            )

    return len(alerts) > 0, alerts


def send_regression_alert(alerts: List[str], channel: str = "slack"):
    """Send alert to specified channel."""
    message = "🚨 Regression Alert\n\n" + "\n".join(alerts)

    if channel == "slack":
        # Integration with Slack webhook
        pass
    elif channel == "email":
        # Email notification
        pass

    print(message)  # Always log
```

## Version Tracking

### Tracking System Versions

```python
"""
Version tracking for AI systems.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import hashlib

@dataclass
class SystemVersion:
    """Tracks AI system version."""
    version: str
    model_name: str
    model_version: str
    prompt_hash: str
    code_commit: str
    timestamp: str
    notes: Optional[str] = None


def get_prompt_hash(prompt: str) -> str:
    """Get hash of prompt for tracking changes."""
    return hashlib.md5(prompt.encode()).hexdigest()[:8]


def get_current_version(
    version: str,
    model_name: str,
    model_version: str,
    system_prompt: str,
    code_commit: str
) -> SystemVersion:
    """Create version object for current system."""
    return SystemVersion(
        version=version,
        model_name=model_name,
        model_version=model_version,
        prompt_hash=get_prompt_hash(system_prompt),
        code_commit=code_commit,
        timestamp=datetime.now().isoformat()
    )


def versions_match(v1: SystemVersion, v2: SystemVersion) -> bool:
    """Check if two versions are equivalent."""
    return (
        v1.model_name == v2.model_name and
        v1.model_version == v2.model_version and
        v1.prompt_hash == v2.prompt_hash
    )
```

### Change Log

```python
"""
Change log for tracking modifications.
"""

CHANGELOG_TEMPLATE = """
## {version} - {date}

### Changes
{changes}

### Metrics Impact
{metrics}

### Notes
{notes}
"""


def generate_changelog_entry(
    version: str,
    changes: List[str],
    comparison: Dict,
    notes: str = ""
) -> str:
    """Generate changelog entry."""
    from datetime import date

    # Format changes
    changes_str = "\n".join(f"- {c}" for c in changes)

    # Format metrics
    metrics_lines = []
    for item in comparison.get("improvements", []):
        metrics_lines.append(
            f"- {item['metric']}: +{item['pct_change']:.1f}%"
        )
    for item in comparison.get("regressions", []):
        metrics_lines.append(
            f"- {item['metric']}: {item['pct_change']:.1f}%"
        )
    metrics_str = "\n".join(metrics_lines) or "- No significant changes"

    return CHANGELOG_TEMPLATE.format(
        version=version,
        date=date.today().isoformat(),
        changes=changes_str,
        metrics=metrics_str,
        notes=notes or "None"
    )
```

## CI/CD Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/regression-test.yml

name: Regression Tests

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  regression-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-test.txt

      - name: Run regression tests
        env:
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
        run: |
          python -m pytest tests/regression/ -v --tb=short

      - name: Compare to baseline
        run: |
          python scripts/compare_baseline.py \
            --current results/current.json \
            --baseline baselines/latest/baseline.json \
            --threshold 0.05

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: regression-results
          path: results/

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('results/comparison.json'));

            let body = '## Regression Test Results\n\n';
            if (results.has_regressions) {
              body += '⚠️ **Regressions detected**\n\n';
            } else {
              body += '✅ **No regressions**\n\n';
            }

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: body
            });
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running quick regression check..."

# Run subset of tests
python -m pytest tests/regression/test_critical.py -q

if [ $? -ne 0 ]; then
    echo "Regression tests failed. Commit blocked."
    exit 1
fi

echo "Regression tests passed."
```

## Regression Test Patterns

### Critical Path Tests

```python
"""
Critical path regression tests.
"""

import pytest
from my_agent import Agent

class TestCriticalPaths:
    """Test critical user paths that must never break."""

    def setup_method(self):
        self.agent = Agent()
        self.baseline_responses = load_baseline("baselines/critical.json")

    def test_basic_greeting(self):
        """Greeting must always work."""
        response = self.agent.process("Hello")

        assert len(response) > 0
        assert_no_errors(response)
        assert_similar_to_baseline(
            response,
            self.baseline_responses["greeting"],
            threshold=0.7
        )

    def test_help_command(self):
        """Help must always be available."""
        response = self.agent.process("help")

        assert "help" in response.lower() or "assist" in response.lower()
        assert_contains_any(response, ["can", "able", "help"])

    def test_error_recovery(self):
        """System must recover from errors."""
        # Cause an error
        self.agent.process("trigger_error_for_testing")

        # Should still work
        response = self.agent.process("Hello")
        assert len(response) > 0
```

### Output Format Tests

```python
"""
Output format regression tests.
"""

class TestOutputFormats:
    """Test output format consistency."""

    def test_json_output_valid(self):
        """JSON outputs must be valid."""
        from my_agent import get_structured_response

        response = get_structured_response("List 3 colors")

        # Must be valid JSON
        import json
        parsed = json.loads(response)
        assert isinstance(parsed, (dict, list))

    def test_list_format_consistent(self):
        """List format must be consistent."""
        from my_agent import generate_list

        response = generate_list("3 programming languages")

        # Check format hasn't changed
        import re
        # Either numbered (1. 2. 3.) or bulleted (- - -)
        assert re.search(r'^\d+\.|\n\d+\.|\n-', response)

    def test_code_blocks_formatted(self):
        """Code must be in proper blocks."""
        from my_agent import generate_code

        response = generate_code("hello world in Python")

        assert "```" in response or "    " in response  # Code block or indented
```

## Tracking Long-Term Trends

### Metrics Dashboard

```python
"""
Long-term metrics tracking.
"""

import json
from pathlib import Path
from typing import List
import matplotlib.pyplot as plt

def load_historical_metrics(baselines_dir: str) -> List[Dict]:
    """Load all historical baselines."""
    baselines = []

    for path in sorted(Path(baselines_dir).glob("*/baseline.json")):
        with open(path) as f:
            baselines.append(json.load(f))

    return baselines


def plot_metric_trend(baselines: List[Dict], metric: str):
    """Plot metric trend over time."""
    versions = []
    values = []

    for baseline in baselines:
        versions.append(baseline["version"])
        values.append(baseline["aggregates"][metric]["mean"])

    plt.figure(figsize=(10, 5))
    plt.plot(versions, values, marker='o')
    plt.xlabel("Version")
    plt.ylabel(metric)
    plt.title(f"{metric} Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"reports/{metric}_trend.png")
    plt.close()


def detect_drift(baselines: List[Dict], metric: str, window: int = 5) -> bool:
    """
    Detect gradual drift in metrics.

    Returns True if recent trend shows consistent decline.
    """
    if len(baselines) < window:
        return False

    recent = baselines[-window:]
    values = [b["aggregates"][metric]["mean"] for b in recent]

    # Check if consistently declining
    declines = sum(1 for i in range(1, len(values)) if values[i] < values[i-1])

    return declines >= window - 1  # All but one declining
```

## Best Practices

1. **Establish baselines early** - Before making changes
2. **Run tests on every change** - Catch regressions immediately
3. **Version everything** - Prompts, models, code
4. **Track trends** - Spot gradual degradation
5. **Automate alerts** - Don't rely on manual checks
6. **Document changes** - Know what caused regressions
7. **Use realistic test data** - Match production distribution

## Next Steps

- [03-golden-datasets.md](03-golden-datasets.md) - Creating test datasets
- [../04-ab-testing-monitoring/](../04-ab-testing-monitoring/) - A/B testing and monitoring
