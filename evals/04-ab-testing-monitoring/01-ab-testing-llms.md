# A/B Testing for LLM Systems

## Overview

A/B testing LLM systems requires special considerations due to non-deterministic outputs and complex quality metrics.

## A/B Testing Fundamentals

```
┌────────────────────────────────────────────────────────────┐
│                    A/B Test Architecture                    │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  User Traffic                                               │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────┐                                               │
│  │ Router  │ ──── Random Assignment ────┐                  │
│  └────┬────┘                            │                  │
│       │                                 │                  │
│       ▼                                 ▼                  │
│  ┌─────────┐                      ┌─────────┐             │
│  │ Control │                      │ Variant │             │
│  │ (50%)   │                      │ (50%)   │             │
│  └────┬────┘                      └────┬────┘             │
│       │                                 │                  │
│       ▼                                 ▼                  │
│  ┌─────────────────────────────────────────────┐          │
│  │           Metrics Collection                 │          │
│  └─────────────────────────────────────────────┘          │
│                       │                                    │
│                       ▼                                    │
│  ┌─────────────────────────────────────────────┐          │
│  │         Statistical Analysis                 │          │
│  └─────────────────────────────────────────────┘          │
└────────────────────────────────────────────────────────────┘
```

## Experiment Design

### Defining Hypotheses

```python
"""
Experiment design framework.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ExperimentHypothesis:
    """A/B test hypothesis definition."""
    name: str
    description: str
    control: str  # Description of control
    variant: str  # Description of variant
    primary_metric: str
    secondary_metrics: List[str]
    expected_improvement: float  # e.g., 0.05 for 5%
    minimum_detectable_effect: float


@dataclass
class ExperimentConfig:
    """A/B test configuration."""
    experiment_id: str
    hypothesis: ExperimentHypothesis
    traffic_percentage: float  # 0-1
    control_percentage: float  # Usually 0.5
    start_date: str
    min_duration_days: int
    max_duration_days: int
    min_samples_per_variant: int


# Example
experiment = ExperimentConfig(
    experiment_id="exp_2025_01_prompt_v2",
    hypothesis=ExperimentHypothesis(
        name="Improved System Prompt",
        description="Test new system prompt with clearer instructions",
        control="Current production prompt v1.0",
        variant="New prompt with step-by-step instructions",
        primary_metric="task_completion_rate",
        secondary_metrics=["response_quality", "latency", "user_satisfaction"],
        expected_improvement=0.08,  # 8% improvement expected
        minimum_detectable_effect=0.05
    ),
    traffic_percentage=0.1,  # 10% of traffic
    control_percentage=0.5,
    start_date="2025-01-15",
    min_duration_days=7,
    max_duration_days=30,
    min_samples_per_variant=500
)
```

### Sample Size Calculation

```python
"""
Sample size calculations for A/B tests.
"""

import math
from typing import Tuple

def calculate_sample_size(
    baseline_rate: float,
    minimum_detectable_effect: float,
    alpha: float = 0.05,
    power: float = 0.8
) -> int:
    """
    Calculate required sample size per variant.

    Args:
        baseline_rate: Current metric value (e.g., 0.7 for 70%)
        minimum_detectable_effect: Smallest effect to detect
        alpha: Significance level (Type I error rate)
        power: Statistical power (1 - Type II error rate)

    Returns:
        Required sample size per variant
    """
    # Z-scores
    z_alpha = 1.96 if alpha == 0.05 else 2.576  # Two-tailed
    z_power = 0.84 if power == 0.8 else 1.28  # One-tailed

    p1 = baseline_rate
    p2 = baseline_rate + minimum_detectable_effect

    # Pooled proportion
    p_pooled = (p1 + p2) / 2

    # Standard error
    se = math.sqrt(2 * p_pooled * (1 - p_pooled))

    # Effect size
    effect = abs(p2 - p1)

    # Sample size formula
    n = ((z_alpha + z_power) * se / effect) ** 2

    return int(math.ceil(n))


def estimate_test_duration(
    sample_size_per_variant: int,
    daily_traffic: int,
    experiment_traffic_pct: float
) -> int:
    """
    Estimate days needed to reach sample size.

    Args:
        sample_size_per_variant: Required samples per variant
        daily_traffic: Average daily users/requests
        experiment_traffic_pct: Percentage of traffic in experiment

    Returns:
        Estimated days
    """
    daily_experiment_traffic = daily_traffic * experiment_traffic_pct
    daily_per_variant = daily_experiment_traffic / 2

    days = math.ceil((sample_size_per_variant * 2) / daily_experiment_traffic)

    return days


# Example
sample_size = calculate_sample_size(
    baseline_rate=0.65,  # 65% current task completion
    minimum_detectable_effect=0.05  # Want to detect 5% improvement
)
print(f"Need {sample_size} samples per variant")

duration = estimate_test_duration(
    sample_size_per_variant=sample_size,
    daily_traffic=10000,
    experiment_traffic_pct=0.1
)
print(f"Estimated duration: {duration} days")
```

## Traffic Routing

### User Assignment

```python
"""
Traffic routing for A/B tests.
"""

import hashlib
from typing import Dict, Optional

class ExperimentRouter:
    """Route users to experiment variants."""

    def __init__(self, experiments: Dict[str, ExperimentConfig]):
        self.experiments = experiments

    def get_variant(
        self,
        experiment_id: str,
        user_id: str
    ) -> Optional[str]:
        """
        Get variant assignment for user.

        Args:
            experiment_id: Experiment identifier
            user_id: Unique user identifier

        Returns:
            "control", "variant", or None if not in experiment
        """
        exp = self.experiments.get(experiment_id)
        if not exp:
            return None

        # Deterministic hash-based assignment
        hash_input = f"{experiment_id}:{user_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
        bucket = hash_value % 1000

        # Check if user is in experiment
        traffic_threshold = exp.traffic_percentage * 1000
        if bucket >= traffic_threshold:
            return None  # Not in experiment

        # Assign to variant
        control_threshold = exp.control_percentage * traffic_threshold
        if bucket < control_threshold:
            return "control"
        else:
            return "variant"

    def get_all_assignments(self, user_id: str) -> Dict[str, Optional[str]]:
        """Get all experiment assignments for user."""
        return {
            exp_id: self.get_variant(exp_id, user_id)
            for exp_id in self.experiments
        }


# Usage
router = ExperimentRouter({"exp_prompt_v2": experiment})

# Same user always gets same assignment
variant1 = router.get_variant("exp_prompt_v2", "user_123")
variant2 = router.get_variant("exp_prompt_v2", "user_123")
assert variant1 == variant2  # Deterministic
```

### Request Handler

```python
"""
Request handler with A/B testing.
"""

from typing import Any

class ABTestHandler:
    """Handle requests with A/B testing."""

    def __init__(self, router: ExperimentRouter):
        self.router = router
        self.control_system = load_control_system()
        self.variant_system = load_variant_system()

    def handle_request(
        self,
        user_id: str,
        query: str,
        experiment_id: str = "exp_prompt_v2"
    ) -> Dict[str, Any]:
        """
        Handle request with experiment routing.

        Args:
            user_id: User identifier
            query: User query
            experiment_id: Active experiment

        Returns:
            Response with metadata
        """
        variant = self.router.get_variant(experiment_id, user_id)

        # Select system based on variant
        if variant == "variant":
            response = self.variant_system.process(query)
        else:
            # Control or not in experiment
            response = self.control_system.process(query)

        return {
            "response": response,
            "metadata": {
                "experiment_id": experiment_id if variant else None,
                "variant": variant,
                "user_id": user_id
            }
        }
```

## Metrics Collection

### Event Logging

```python
"""
Metrics collection for A/B tests.
"""

import json
from datetime import datetime
from typing import Dict, Any

class MetricsCollector:
    """Collect experiment metrics."""

    def __init__(self, storage_backend):
        self.storage = storage_backend

    def log_event(
        self,
        experiment_id: str,
        variant: str,
        user_id: str,
        event_type: str,
        metrics: Dict[str, Any]
    ):
        """
        Log experiment event.

        Args:
            experiment_id: Experiment identifier
            variant: "control" or "variant"
            user_id: User identifier
            event_type: Type of event
            metrics: Metric values
        """
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "experiment_id": experiment_id,
            "variant": variant,
            "user_id": user_id,
            "event_type": event_type,
            "metrics": metrics
        }

        self.storage.write(event)

    def log_response(
        self,
        experiment_id: str,
        variant: str,
        user_id: str,
        query: str,
        response: str,
        latency_ms: float,
        quality_scores: Dict[str, float]
    ):
        """Log LLM response metrics."""
        self.log_event(
            experiment_id=experiment_id,
            variant=variant,
            user_id=user_id,
            event_type="response",
            metrics={
                "query_length": len(query),
                "response_length": len(response),
                "latency_ms": latency_ms,
                **quality_scores
            }
        )

    def log_user_feedback(
        self,
        experiment_id: str,
        variant: str,
        user_id: str,
        feedback_type: str,
        value: Any
    ):
        """Log user feedback."""
        self.log_event(
            experiment_id=experiment_id,
            variant=variant,
            user_id=user_id,
            event_type="feedback",
            metrics={
                "feedback_type": feedback_type,
                "value": value
            }
        )
```

### LLM-Specific Metrics

```python
"""
LLM-specific A/B test metrics.
"""

METRICS_DEFINITIONS = {
    # Quality metrics
    "task_completion_rate": {
        "description": "Percentage of queries successfully completed",
        "type": "rate",
        "higher_is_better": True
    },
    "response_relevance": {
        "description": "How relevant is the response (0-1)",
        "type": "score",
        "higher_is_better": True
    },
    "hallucination_rate": {
        "description": "Rate of factually incorrect responses",
        "type": "rate",
        "higher_is_better": False
    },

    # User experience metrics
    "thumbs_up_rate": {
        "description": "Percentage of positive feedback",
        "type": "rate",
        "higher_is_better": True
    },
    "follow_up_rate": {
        "description": "Rate of follow-up questions (may indicate confusion)",
        "type": "rate",
        "higher_is_better": False
    },
    "conversation_length": {
        "description": "Average turns per conversation",
        "type": "average",
        "higher_is_better": None  # Depends on context
    },

    # Efficiency metrics
    "latency_p50": {
        "description": "50th percentile response time",
        "type": "latency",
        "higher_is_better": False
    },
    "latency_p95": {
        "description": "95th percentile response time",
        "type": "latency",
        "higher_is_better": False
    },
    "tokens_per_response": {
        "description": "Average tokens in response",
        "type": "average",
        "higher_is_better": None
    },

    # Cost metrics
    "cost_per_query": {
        "description": "Average API cost per query",
        "type": "cost",
        "higher_is_better": False
    }
}


def calculate_derived_metrics(events: list) -> Dict[str, float]:
    """Calculate metrics from raw events."""
    metrics = {}

    responses = [e for e in events if e["event_type"] == "response"]
    feedback = [e for e in events if e["event_type"] == "feedback"]

    if responses:
        # Latency metrics
        latencies = [r["metrics"]["latency_ms"] for r in responses]
        latencies.sort()
        metrics["latency_p50"] = latencies[len(latencies) // 2]
        metrics["latency_p95"] = latencies[int(len(latencies) * 0.95)]

        # Average response length
        lengths = [r["metrics"]["response_length"] for r in responses]
        metrics["avg_response_length"] = sum(lengths) / len(lengths)

    if feedback:
        # Thumbs up rate
        thumbs = [f for f in feedback if f["metrics"]["feedback_type"] == "thumbs"]
        if thumbs:
            up = sum(1 for t in thumbs if t["metrics"]["value"] == "up")
            metrics["thumbs_up_rate"] = up / len(thumbs)

    return metrics
```

## Statistical Analysis

### Significance Testing

```python
"""
Statistical analysis for A/B tests.
"""

import math
from typing import Dict, Tuple, List

def two_proportion_z_test(
    successes_a: int,
    total_a: int,
    successes_b: int,
    total_b: int
) -> Tuple[float, float]:
    """
    Two-proportion z-test.

    Args:
        successes_a: Successes in control
        total_a: Total in control
        successes_b: Successes in variant
        total_b: Total in variant

    Returns:
        (z_score, p_value)
    """
    p_a = successes_a / total_a
    p_b = successes_b / total_b

    # Pooled proportion
    p_pooled = (successes_a + successes_b) / (total_a + total_b)

    # Standard error
    se = math.sqrt(p_pooled * (1 - p_pooled) * (1/total_a + 1/total_b))

    if se == 0:
        return 0, 1.0

    # Z-score
    z = (p_b - p_a) / se

    # Two-tailed p-value (simplified)
    # In production, use scipy.stats.norm.sf(abs(z)) * 2
    if abs(z) >= 2.576:
        p_value = 0.01
    elif abs(z) >= 1.96:
        p_value = 0.05
    elif abs(z) >= 1.645:
        p_value = 0.1
    else:
        p_value = 0.5

    return z, p_value


def analyze_experiment(
    control_data: List[Dict],
    variant_data: List[Dict],
    metric: str,
    alpha: float = 0.05
) -> Dict[str, Any]:
    """
    Analyze experiment results.

    Args:
        control_data: Control group events
        variant_data: Variant group events
        metric: Metric to analyze
        alpha: Significance level

    Returns:
        Analysis results
    """
    # Extract metric values
    def get_metric(events):
        return [e["metrics"].get(metric, 0) for e in events]

    control_values = get_metric(control_data)
    variant_values = get_metric(variant_data)

    control_mean = sum(control_values) / len(control_values)
    variant_mean = sum(variant_values) / len(variant_values)

    # For rate metrics (0 or 1 values)
    if all(v in [0, 1] for v in control_values + variant_values):
        control_successes = sum(control_values)
        variant_successes = sum(variant_values)

        z, p_value = two_proportion_z_test(
            control_successes, len(control_values),
            variant_successes, len(variant_values)
        )

        lift = (variant_mean - control_mean) / control_mean if control_mean > 0 else 0

        return {
            "metric": metric,
            "control_rate": control_mean,
            "variant_rate": variant_mean,
            "lift": lift,
            "lift_pct": lift * 100,
            "z_score": z,
            "p_value": p_value,
            "significant": p_value < alpha,
            "confidence": 1 - alpha,
            "sample_size_control": len(control_values),
            "sample_size_variant": len(variant_values)
        }

    # For continuous metrics
    control_std = math.sqrt(sum((v - control_mean)**2 for v in control_values) / len(control_values))
    variant_std = math.sqrt(sum((v - variant_mean)**2 for v in variant_values) / len(variant_values))

    # Welch's t-test (simplified)
    se = math.sqrt(control_std**2/len(control_values) + variant_std**2/len(variant_values))
    t = (variant_mean - control_mean) / se if se > 0 else 0

    return {
        "metric": metric,
        "control_mean": control_mean,
        "variant_mean": variant_mean,
        "control_std": control_std,
        "variant_std": variant_std,
        "difference": variant_mean - control_mean,
        "t_score": t,
        "significant": abs(t) > 1.96,
        "sample_size_control": len(control_values),
        "sample_size_variant": len(variant_values)
    }
```

### Results Interpretation

```python
"""
Experiment results interpretation.
"""

def interpret_results(analysis: Dict) -> str:
    """
    Generate human-readable interpretation.

    Args:
        analysis: Analysis results from analyze_experiment

    Returns:
        Interpretation text
    """
    metric = analysis["metric"]
    significant = analysis.get("significant", False)

    if "lift_pct" in analysis:
        # Rate metric
        lift = analysis["lift_pct"]
        control = analysis["control_rate"]
        variant = analysis["variant_rate"]

        if significant:
            if lift > 0:
                return (
                    f"SIGNIFICANT IMPROVEMENT: {metric} increased from "
                    f"{control:.1%} to {variant:.1%} ({lift:+.1f}% lift, "
                    f"p={analysis['p_value']:.3f})"
                )
            else:
                return (
                    f"SIGNIFICANT REGRESSION: {metric} decreased from "
                    f"{control:.1%} to {variant:.1%} ({lift:.1f}% lift, "
                    f"p={analysis['p_value']:.3f})"
                )
        else:
            return (
                f"NO SIGNIFICANT DIFFERENCE: {metric} "
                f"control={control:.1%}, variant={variant:.1%} "
                f"(p={analysis['p_value']:.3f})"
            )
    else:
        # Continuous metric
        diff = analysis["difference"]
        control = analysis["control_mean"]
        variant = analysis["variant_mean"]

        if significant:
            direction = "increased" if diff > 0 else "decreased"
            return (
                f"SIGNIFICANT: {metric} {direction} from "
                f"{control:.2f} to {variant:.2f}"
            )
        else:
            return (
                f"NO SIGNIFICANT DIFFERENCE: {metric} "
                f"control={control:.2f}, variant={variant:.2f}"
            )


def make_recommendation(analyses: List[Dict]) -> Dict[str, Any]:
    """
    Make ship/no-ship recommendation.

    Args:
        analyses: List of metric analyses

    Returns:
        Recommendation
    """
    # Find primary metric
    primary = next((a for a in analyses if a.get("is_primary")), analyses[0])

    significant_improvements = [
        a for a in analyses
        if a.get("significant") and a.get("lift_pct", 0) > 0
    ]

    significant_regressions = [
        a for a in analyses
        if a.get("significant") and a.get("lift_pct", 0) < 0
    ]

    # Decision logic
    if significant_regressions:
        recommendation = "DO_NOT_SHIP"
        reason = f"Significant regression in {len(significant_regressions)} metric(s)"
    elif primary.get("significant") and primary.get("lift_pct", 0) > 0:
        recommendation = "SHIP"
        reason = f"Primary metric significantly improved by {primary['lift_pct']:.1f}%"
    elif not primary.get("significant"):
        recommendation = "INCONCLUSIVE"
        reason = "Primary metric not statistically significant"
    else:
        recommendation = "REVIEW"
        reason = "Mixed results, needs human review"

    return {
        "recommendation": recommendation,
        "reason": reason,
        "improvements": len(significant_improvements),
        "regressions": len(significant_regressions),
        "primary_metric_result": primary
    }
```

## Best Practices

### Common Pitfalls

1. **Peeking** - Don't check results too early
2. **Underpowered tests** - Ensure sufficient sample size
3. **Multiple comparisons** - Adjust for many metrics
4. **Selection bias** - Ensure random assignment
5. **Novelty effects** - Run tests long enough

### LLM-Specific Considerations

1. **Output variance** - Same input can yield different outputs
2. **Prompt sensitivity** - Small changes can have big effects
3. **Context dependency** - Performance varies by use case
4. **Cost awareness** - Consider API costs in metrics
5. **Latency impacts** - Users sensitive to response time

## Next Steps

- [02-production-monitoring.md](02-production-monitoring.md) - Monitoring in production
- [03-drift-detection.md](03-drift-detection.md) - Detecting drift
