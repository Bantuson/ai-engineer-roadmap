# Drift Detection in LLM Systems

## Overview

Drift detection identifies when an LLM system's behavior changes over time, enabling proactive quality maintenance.

## Types of Drift

```
┌─────────────────────────────────────────────────────────────────┐
│                       Types of Drift                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT DRIFT          MODEL DRIFT          OUTPUT DRIFT         │
│  ────────────         ───────────          ────────────         │
│  User queries         Model behavior       Response              │
│  change over          changes (API         characteristics       │
│  time                 updates)             shift                 │
│                                                                  │
│  Examples:            Examples:            Examples:             │
│  - New topics         - Provider updates   - Longer responses    │
│  - Different          - Temperature        - Different tone      │
│    phrasing             changes            - Quality changes     │
│  - Seasonal           - Fine-tuning        - Format drift        │
│    patterns             drift                                    │
│                                                                  │
│  PROMPT DRIFT         CONTEXT DRIFT        CONCEPT DRIFT        │
│  ────────────         ──────────────       ─────────────        │
│  Prompt template      Retrieved context    What "correct"       │
│  changes over         quality changes      means changes        │
│  time                                                           │
│                                                                  │
│  Examples:            Examples:            Examples:             │
│  - Accumulating       - Stale documents    - New products       │
│    modifications      - Index quality      - Policy changes     │
│  - A/B test           - Embedding drift    - World events       │
│    remnants                                                      │
└─────────────────────────────────────────────────────────────────┘
```

## Detecting Input Drift

### Query Distribution Monitoring

```python
"""
Input drift detection through query analysis.
"""

from typing import Dict, List, Any
from collections import Counter
import math

class InputDriftDetector:
    """Detect drift in input distribution."""

    def __init__(self, baseline_period_days: int = 7):
        self.baseline_period = baseline_period_days
        self.baseline_distribution = None
        self.baseline_stats = None

    def fit_baseline(self, queries: List[str]):
        """Fit baseline from historical queries."""
        self.baseline_distribution = self._compute_distribution(queries)
        self.baseline_stats = self._compute_stats(queries)

    def _compute_distribution(self, queries: List[str]) -> Dict[str, float]:
        """Compute topic/category distribution."""
        categories = [self._categorize(q) for q in queries]
        counts = Counter(categories)
        total = len(categories)

        return {cat: count / total for cat, count in counts.items()}

    def _categorize(self, query: str) -> str:
        """Simple query categorization."""
        query_lower = query.lower()

        categories = {
            "greeting": ["hello", "hi", "hey"],
            "question": ["what", "how", "why", "when", "where"],
            "request": ["please", "can you", "could you"],
            "complaint": ["problem", "issue", "error", "wrong"],
            "other": []
        }

        for cat, keywords in categories.items():
            if any(k in query_lower for k in keywords):
                return cat

        return "other"

    def _compute_stats(self, queries: List[str]) -> Dict[str, float]:
        """Compute statistical features."""
        lengths = [len(q) for q in queries]

        return {
            "mean_length": sum(lengths) / len(lengths),
            "std_length": math.sqrt(
                sum((l - sum(lengths)/len(lengths))**2 for l in lengths) / len(lengths)
            ),
            "total_count": len(queries)
        }

    def detect_drift(self, recent_queries: List[str]) -> Dict[str, Any]:
        """
        Detect drift in recent queries.

        Returns:
            Drift detection results
        """
        if self.baseline_distribution is None:
            raise ValueError("Baseline not set. Call fit_baseline first.")

        recent_distribution = self._compute_distribution(recent_queries)
        recent_stats = self._compute_stats(recent_queries)

        # KL Divergence for distribution drift
        kl_div = self._kl_divergence(
            self.baseline_distribution,
            recent_distribution
        )

        # Statistical drift
        length_drift = abs(
            recent_stats["mean_length"] - self.baseline_stats["mean_length"]
        ) / max(self.baseline_stats["mean_length"], 1)

        # Category drift (new categories or missing)
        new_categories = set(recent_distribution.keys()) - set(self.baseline_distribution.keys())
        missing_categories = set(self.baseline_distribution.keys()) - set(recent_distribution.keys())

        drift_detected = kl_div > 0.1 or length_drift > 0.2

        return {
            "drift_detected": drift_detected,
            "kl_divergence": kl_div,
            "length_drift": length_drift,
            "new_categories": list(new_categories),
            "missing_categories": list(missing_categories),
            "baseline_distribution": self.baseline_distribution,
            "recent_distribution": recent_distribution
        }

    def _kl_divergence(self, p: Dict, q: Dict) -> float:
        """Calculate KL divergence between distributions."""
        all_keys = set(p.keys()) | set(q.keys())
        epsilon = 1e-10

        kl = 0
        for key in all_keys:
            p_val = p.get(key, epsilon)
            q_val = q.get(key, epsilon)
            if p_val > 0:
                kl += p_val * math.log(p_val / q_val)

        return kl
```

## Detecting Output Drift

### Response Characteristic Monitoring

```python
"""
Output drift detection.
"""

from typing import Dict, List, Any

class OutputDriftDetector:
    """Detect drift in output characteristics."""

    def __init__(self):
        self.baseline_features = None

    def fit_baseline(self, responses: List[str]):
        """Fit baseline from historical responses."""
        self.baseline_features = self._extract_features(responses)

    def _extract_features(self, responses: List[str]) -> Dict[str, float]:
        """Extract statistical features from responses."""
        if not responses:
            return {}

        lengths = [len(r) for r in responses]
        word_counts = [len(r.split()) for r in responses]
        sentence_counts = [len(r.split('.')) for r in responses]

        # Sentiment proxy (simple)
        positive_words = ["great", "good", "excellent", "happy"]
        negative_words = ["bad", "sorry", "unfortunately", "error"]

        pos_ratio = sum(
            sum(1 for w in positive_words if w in r.lower())
            for r in responses
        ) / len(responses)

        neg_ratio = sum(
            sum(1 for w in negative_words if w in r.lower())
            for r in responses
        ) / len(responses)

        return {
            "mean_length": sum(lengths) / len(lengths),
            "mean_words": sum(word_counts) / len(word_counts),
            "mean_sentences": sum(sentence_counts) / len(sentence_counts),
            "positive_ratio": pos_ratio,
            "negative_ratio": neg_ratio,
            "sample_count": len(responses)
        }

    def detect_drift(self, recent_responses: List[str]) -> Dict[str, Any]:
        """Detect drift in recent responses."""
        if self.baseline_features is None:
            raise ValueError("Baseline not set")

        recent_features = self._extract_features(recent_responses)

        drifts = {}
        for feature, baseline_val in self.baseline_features.items():
            if feature == "sample_count":
                continue

            recent_val = recent_features.get(feature, 0)
            if baseline_val > 0:
                drift = abs(recent_val - baseline_val) / baseline_val
            else:
                drift = abs(recent_val)

            drifts[feature] = {
                "baseline": baseline_val,
                "recent": recent_val,
                "drift_pct": drift * 100
            }

        # Overall drift score
        drift_scores = [d["drift_pct"] for d in drifts.values()]
        overall_drift = sum(drift_scores) / len(drift_scores) if drift_scores else 0

        return {
            "drift_detected": overall_drift > 15,  # 15% threshold
            "overall_drift_pct": overall_drift,
            "feature_drifts": drifts
        }
```

### Quality Score Drift

```python
"""
Quality score drift monitoring.
"""

from typing import List, Tuple
from datetime import datetime, timedelta

class QualityDriftDetector:
    """Detect drift in quality scores."""

    def __init__(self, window_size: int = 100):
        self.window_size = window_size
        self.baseline_mean = None
        self.baseline_std = None

    def fit_baseline(self, quality_scores: List[float]):
        """Set baseline from historical scores."""
        self.baseline_mean = sum(quality_scores) / len(quality_scores)
        self.baseline_std = (
            sum((s - self.baseline_mean)**2 for s in quality_scores)
            / len(quality_scores)
        ) ** 0.5

    def detect_drift(self, recent_scores: List[float]) -> Dict[str, Any]:
        """
        Detect quality drift using control chart approach.
        """
        if self.baseline_mean is None:
            raise ValueError("Baseline not set")

        recent_mean = sum(recent_scores) / len(recent_scores)

        # Z-score of recent mean
        se = self.baseline_std / (len(recent_scores) ** 0.5)
        z_score = (recent_mean - self.baseline_mean) / se if se > 0 else 0

        # Control limits (3-sigma)
        ucl = self.baseline_mean + 3 * self.baseline_std
        lcl = self.baseline_mean - 3 * self.baseline_std

        # Check for out-of-control points
        out_of_control = sum(
            1 for s in recent_scores
            if s > ucl or s < lcl
        )

        # Trend detection (runs test)
        trend = self._detect_trend(recent_scores)

        drift_detected = (
            abs(z_score) > 2 or
            out_of_control > len(recent_scores) * 0.05 or
            trend != "none"
        )

        return {
            "drift_detected": drift_detected,
            "baseline_mean": self.baseline_mean,
            "recent_mean": recent_mean,
            "z_score": z_score,
            "out_of_control_pct": out_of_control / len(recent_scores) * 100,
            "trend": trend,
            "ucl": ucl,
            "lcl": lcl
        }

    def _detect_trend(self, scores: List[float]) -> str:
        """Detect trending pattern."""
        if len(scores) < 6:
            return "none"

        # Check for 6+ consecutive increases or decreases
        increasing = 0
        decreasing = 0

        for i in range(1, len(scores)):
            if scores[i] > scores[i-1]:
                increasing += 1
                decreasing = 0
            elif scores[i] < scores[i-1]:
                decreasing += 1
                increasing = 0
            else:
                increasing = 0
                decreasing = 0

            if increasing >= 6:
                return "increasing"
            if decreasing >= 6:
                return "decreasing"

        return "none"
```

## Detecting Model Drift

### Model Behavior Fingerprinting

```python
"""
Model drift detection through fingerprinting.
"""

from typing import Dict, List, Any

class ModelDriftDetector:
    """Detect changes in underlying model behavior."""

    def __init__(self):
        self.baseline_fingerprint = None
        self.probe_queries = [
            # Consistent, simple queries for fingerprinting
            "What is 2 + 2?",
            "What color is the sky?",
            "Complete this sentence: The cat sat on the...",
            "List three primary colors.",
            "Translate 'hello' to Spanish.",
        ]

    def create_fingerprint(self, model_func) -> Dict[str, Any]:
        """
        Create fingerprint by running probe queries.

        Args:
            model_func: Function that takes query and returns response
        """
        fingerprint = {
            "responses": {},
            "characteristics": {}
        }

        total_length = 0
        total_latency = 0

        for query in self.probe_queries:
            import time
            start = time.time()
            response = model_func(query)
            latency = time.time() - start

            fingerprint["responses"][query] = response
            total_length += len(response)
            total_latency += latency

        fingerprint["characteristics"] = {
            "mean_response_length": total_length / len(self.probe_queries),
            "mean_latency": total_latency / len(self.probe_queries)
        }

        return fingerprint

    def fit_baseline(self, model_func):
        """Set baseline fingerprint."""
        self.baseline_fingerprint = self.create_fingerprint(model_func)

    def detect_drift(self, model_func) -> Dict[str, Any]:
        """Detect drift from baseline."""
        if self.baseline_fingerprint is None:
            raise ValueError("Baseline not set")

        current = self.create_fingerprint(model_func)

        # Compare responses
        response_changes = []
        for query in self.probe_queries:
            baseline_resp = self.baseline_fingerprint["responses"][query]
            current_resp = current["responses"][query]

            similarity = self._calculate_similarity(baseline_resp, current_resp)

            if similarity < 0.8:  # Significant change
                response_changes.append({
                    "query": query,
                    "baseline": baseline_resp[:100],
                    "current": current_resp[:100],
                    "similarity": similarity
                })

        # Compare characteristics
        baseline_chars = self.baseline_fingerprint["characteristics"]
        current_chars = current["characteristics"]

        length_drift = abs(
            current_chars["mean_response_length"] - baseline_chars["mean_response_length"]
        ) / max(baseline_chars["mean_response_length"], 1)

        latency_drift = abs(
            current_chars["mean_latency"] - baseline_chars["mean_latency"]
        ) / max(baseline_chars["mean_latency"], 0.001)

        drift_detected = (
            len(response_changes) > 0 or
            length_drift > 0.2 or
            latency_drift > 0.5
        )

        return {
            "drift_detected": drift_detected,
            "response_changes": response_changes,
            "length_drift_pct": length_drift * 100,
            "latency_drift_pct": latency_drift * 100,
            "baseline_characteristics": baseline_chars,
            "current_characteristics": current_chars
        }

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate text similarity."""
        # Simple word overlap
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())

        if not words1 or not words2:
            return 0.0

        intersection = len(words1 & words2)
        union = len(words1 | words2)

        return intersection / union
```

## Automated Drift Monitoring

### Continuous Monitoring Pipeline

```python
"""
Automated drift monitoring pipeline.
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta

class DriftMonitor:
    """Continuous drift monitoring."""

    def __init__(
        self,
        input_detector: InputDriftDetector,
        output_detector: OutputDriftDetector,
        quality_detector: QualityDriftDetector
    ):
        self.input_detector = input_detector
        self.output_detector = output_detector
        self.quality_detector = quality_detector
        self.drift_history = []

    def run_check(
        self,
        recent_queries: List[str],
        recent_responses: List[str],
        recent_quality_scores: List[float]
    ) -> Dict[str, Any]:
        """
        Run complete drift check.

        Args:
            recent_queries: Recent user queries
            recent_responses: Recent system responses
            recent_quality_scores: Recent quality scores

        Returns:
            Complete drift report
        """
        timestamp = datetime.utcnow().isoformat()

        results = {
            "timestamp": timestamp,
            "input_drift": self.input_detector.detect_drift(recent_queries),
            "output_drift": self.output_detector.detect_drift(recent_responses),
            "quality_drift": self.quality_detector.detect_drift(recent_quality_scores)
        }

        # Overall drift status
        any_drift = (
            results["input_drift"]["drift_detected"] or
            results["output_drift"]["drift_detected"] or
            results["quality_drift"]["drift_detected"]
        )

        results["any_drift"] = any_drift

        # Record in history
        self.drift_history.append({
            "timestamp": timestamp,
            "any_drift": any_drift,
            "details": results
        })

        # Trim history
        if len(self.drift_history) > 1000:
            self.drift_history = self.drift_history[-500:]

        return results

    def get_drift_trend(self, days: int = 7) -> Dict[str, Any]:
        """Get drift trend over time."""
        cutoff = datetime.utcnow() - timedelta(days=days)

        recent = [
            h for h in self.drift_history
            if datetime.fromisoformat(h["timestamp"]) > cutoff
        ]

        drift_count = sum(1 for h in recent if h["any_drift"])

        return {
            "period_days": days,
            "total_checks": len(recent),
            "drift_count": drift_count,
            "drift_rate": drift_count / len(recent) if recent else 0
        }


def create_drift_alert(drift_results: Dict) -> Dict[str, Any]:
    """Create alert from drift detection results."""
    alerts = []

    if drift_results["input_drift"]["drift_detected"]:
        alerts.append({
            "type": "input_drift",
            "severity": "warning",
            "message": f"Input distribution shift detected (KL: {drift_results['input_drift']['kl_divergence']:.3f})"
        })

    if drift_results["output_drift"]["drift_detected"]:
        alerts.append({
            "type": "output_drift",
            "severity": "warning",
            "message": f"Output characteristics shifted ({drift_results['output_drift']['overall_drift_pct']:.1f}%)"
        })

    if drift_results["quality_drift"]["drift_detected"]:
        severity = "critical" if drift_results["quality_drift"]["trend"] == "decreasing" else "warning"
        alerts.append({
            "type": "quality_drift",
            "severity": severity,
            "message": f"Quality drift detected (z-score: {drift_results['quality_drift']['z_score']:.2f})"
        })

    return {
        "has_alerts": len(alerts) > 0,
        "alerts": alerts,
        "timestamp": drift_results.get("timestamp")
    }
```

## Responding to Drift

### Remediation Strategies

```python
"""
Drift remediation strategies.
"""

from enum import Enum
from typing import Dict, Any

class RemediationAction(Enum):
    RETRAIN = "retrain"
    ADJUST_PROMPT = "adjust_prompt"
    UPDATE_INDEX = "update_index"
    ROLLBACK = "rollback"
    ALERT_HUMAN = "alert_human"
    NO_ACTION = "no_action"


def recommend_remediation(drift_results: Dict) -> Dict[str, Any]:
    """
    Recommend remediation based on drift detection.

    Args:
        drift_results: Results from drift monitoring

    Returns:
        Recommended actions
    """
    recommendations = []

    # Input drift
    if drift_results["input_drift"]["drift_detected"]:
        new_cats = drift_results["input_drift"].get("new_categories", [])
        if new_cats:
            recommendations.append({
                "action": RemediationAction.ADJUST_PROMPT.value,
                "reason": f"New query categories detected: {new_cats}",
                "priority": "medium"
            })
        else:
            recommendations.append({
                "action": RemediationAction.UPDATE_INDEX.value,
                "reason": "Query distribution shift may require index updates",
                "priority": "low"
            })

    # Output drift
    if drift_results["output_drift"]["drift_detected"]:
        drift_pct = drift_results["output_drift"]["overall_drift_pct"]
        if drift_pct > 30:
            recommendations.append({
                "action": RemediationAction.ALERT_HUMAN.value,
                "reason": f"Significant output drift ({drift_pct:.1f}%)",
                "priority": "high"
            })
        else:
            recommendations.append({
                "action": RemediationAction.ADJUST_PROMPT.value,
                "reason": "Minor output characteristics shift",
                "priority": "medium"
            })

    # Quality drift
    if drift_results["quality_drift"]["drift_detected"]:
        trend = drift_results["quality_drift"]["trend"]
        z_score = drift_results["quality_drift"]["z_score"]

        if trend == "decreasing" or z_score < -2:
            recommendations.append({
                "action": RemediationAction.ROLLBACK.value,
                "reason": f"Quality degradation detected (z={z_score:.2f})",
                "priority": "critical"
            })
        else:
            recommendations.append({
                "action": RemediationAction.RETRAIN.value,
                "reason": "Quality drift, consider retraining",
                "priority": "medium"
            })

    if not recommendations:
        recommendations.append({
            "action": RemediationAction.NO_ACTION.value,
            "reason": "No significant drift detected",
            "priority": "none"
        })

    return {
        "recommendations": recommendations,
        "highest_priority": max(
            (r["priority"] for r in recommendations),
            key=lambda p: {"critical": 4, "high": 3, "medium": 2, "low": 1, "none": 0}.get(p, 0)
        )
    }
```

## Best Practices

1. **Establish baselines early** - Before production deployment
2. **Monitor continuously** - Drift happens gradually
3. **Track multiple dimensions** - Input, output, quality
4. **Set appropriate thresholds** - Balance sensitivity vs. noise
5. **Automate responses** - Some drift needs immediate action
6. **Version control prompts** - Track what changed
7. **Document remediation** - Learn from past drift events

## Next Steps

- [../05-capstone-eval-system/](../05-capstone-eval-system/) - Build complete eval system
- [../../vulnerabilities/](../../vulnerabilities/) - Security considerations
