# Production Monitoring for LLM Systems

## Overview

Production monitoring ensures LLM systems maintain quality, performance, and reliability in real-world deployments.

## Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    LLM Monitoring Architecture                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│   │ Request │───▶│   LLM   │───▶│Response │───▶│  User   │     │
│   │         │    │ System  │    │         │    │         │     │
│   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘     │
│        │              │              │              │           │
│        ▼              ▼              ▼              ▼           │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                    Metrics Collector                     │  │
│   └──────────────────────────┬──────────────────────────────┘  │
│                              │                                  │
│        ┌─────────────────────┼─────────────────────┐           │
│        ▼                     ▼                     ▼           │
│   ┌─────────┐          ┌─────────┐          ┌─────────┐       │
│   │ Metrics │          │  Logs   │          │ Traces  │       │
│   │  Store  │          │  Store  │          │  Store  │       │
│   └────┬────┘          └────┬────┘          └────┬────┘       │
│        │                    │                    │              │
│        └────────────────────┼────────────────────┘              │
│                             ▼                                   │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                Dashboard & Alerting                      │  │
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Metrics

### Response Quality Metrics

```python
"""
Quality metrics for production monitoring.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class QualityMetrics:
    """Quality metrics for a response."""
    relevance_score: float  # 0-1
    coherence_score: float  # 0-1
    factuality_score: Optional[float]  # 0-1 if verifiable
    safety_score: float  # 0-1
    format_adherence: float  # 0-1


def calculate_quality_metrics(
    query: str,
    response: str,
    context: Optional[str] = None
) -> QualityMetrics:
    """
    Calculate quality metrics for response.

    In production, use faster heuristics or cached embeddings.
    """
    metrics = QualityMetrics(
        relevance_score=calculate_relevance(query, response),
        coherence_score=calculate_coherence(response),
        factuality_score=None,  # Expensive, sample only
        safety_score=calculate_safety(response),
        format_adherence=check_format(response)
    )

    return metrics


def calculate_relevance(query: str, response: str) -> float:
    """Quick relevance check using keyword overlap."""
    query_words = set(query.lower().split())
    response_words = set(response.lower().split())

    if not query_words:
        return 1.0

    overlap = len(query_words & response_words)
    return min(overlap / len(query_words), 1.0)


def calculate_coherence(response: str) -> float:
    """Check response coherence."""
    # Simple heuristics
    if not response.strip():
        return 0.0

    sentences = response.split('.')
    if len(sentences) == 1 and len(response) > 500:
        return 0.5  # Long run-on sentence

    return 1.0


def calculate_safety(response: str) -> float:
    """Check for safety issues."""
    unsafe_patterns = [
        "i cannot", "i won't", "i'm not able",
        "inappropriate", "harmful"
    ]

    response_lower = response.lower()
    refusals = sum(1 for p in unsafe_patterns if p in response_lower)

    return 1.0 if refusals == 0 else 0.5


def check_format(response: str) -> float:
    """Check format adherence."""
    # Example: check for proper structure
    has_content = len(response) > 10
    not_too_long = len(response) < 10000
    no_errors = "error" not in response.lower()[:50]

    score = sum([has_content, not_too_long, no_errors]) / 3
    return score
```

### Performance Metrics

```python
"""
Performance metrics collection.
"""

import time
from contextlib import contextmanager
from typing import Dict, Any

class PerformanceTracker:
    """Track performance metrics."""

    def __init__(self):
        self.metrics = {}

    @contextmanager
    def track(self, operation: str):
        """Context manager to track operation duration."""
        start = time.perf_counter()
        try:
            yield
        finally:
            duration = (time.perf_counter() - start) * 1000
            self._record(operation, duration)

    def _record(self, operation: str, duration_ms: float):
        """Record metric."""
        if operation not in self.metrics:
            self.metrics[operation] = []
        self.metrics[operation].append(duration_ms)

    def get_stats(self, operation: str) -> Dict[str, float]:
        """Get statistics for operation."""
        values = self.metrics.get(operation, [])
        if not values:
            return {}

        values.sort()
        return {
            "count": len(values),
            "mean": sum(values) / len(values),
            "p50": values[len(values) // 2],
            "p95": values[int(len(values) * 0.95)],
            "p99": values[int(len(values) * 0.99)],
            "min": values[0],
            "max": values[-1]
        }


# Usage
tracker = PerformanceTracker()

def process_request(query: str) -> str:
    with tracker.track("total_latency"):
        with tracker.track("preprocessing"):
            processed = preprocess(query)

        with tracker.track("llm_call"):
            response = call_llm(processed)

        with tracker.track("postprocessing"):
            final = postprocess(response)

    return final
```

### Cost Metrics

```python
"""
Cost tracking for LLM operations.
"""

@dataclass
class CostMetrics:
    """Cost metrics for request."""
    input_tokens: int
    output_tokens: int
    model: str
    cost_usd: float


# Token pricing (example)
PRICING = {
    "gpt-4": {"input": 0.03/1000, "output": 0.06/1000},
    "gpt-3.5-turbo": {"input": 0.001/1000, "output": 0.002/1000},
    "deepseek-chat": {"input": 0.0001/1000, "output": 0.0002/1000},
}


def calculate_cost(
    model: str,
    input_tokens: int,
    output_tokens: int
) -> CostMetrics:
    """Calculate cost for request."""
    pricing = PRICING.get(model, {"input": 0, "output": 0})

    cost = (
        input_tokens * pricing["input"] +
        output_tokens * pricing["output"]
    )

    return CostMetrics(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        model=model,
        cost_usd=cost
    )


class CostTracker:
    """Track costs over time."""

    def __init__(self):
        self.total_cost = 0.0
        self.costs_by_model = {}
        self.daily_costs = {}

    def record(self, metrics: CostMetrics):
        """Record cost metrics."""
        from datetime import date

        self.total_cost += metrics.cost_usd

        model = metrics.model
        if model not in self.costs_by_model:
            self.costs_by_model[model] = 0.0
        self.costs_by_model[model] += metrics.cost_usd

        today = date.today().isoformat()
        if today not in self.daily_costs:
            self.daily_costs[today] = 0.0
        self.daily_costs[today] += metrics.cost_usd

    def get_summary(self) -> Dict[str, Any]:
        """Get cost summary."""
        return {
            "total_cost_usd": self.total_cost,
            "by_model": self.costs_by_model,
            "by_day": self.daily_costs
        }
```

## Alerting

### Alert Configuration

```python
"""
Alert configuration and triggering.
"""

from dataclasses import dataclass
from typing import Callable, List, Optional
from enum import Enum

class AlertSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class AlertRule:
    """Alert rule definition."""
    name: str
    metric: str
    condition: Callable[[float], bool]
    severity: AlertSeverity
    cooldown_minutes: int = 15
    description: str = ""


# Common alert rules
ALERT_RULES = [
    AlertRule(
        name="high_latency",
        metric="latency_p95",
        condition=lambda x: x > 5000,  # > 5 seconds
        severity=AlertSeverity.WARNING,
        description="95th percentile latency exceeds 5 seconds"
    ),
    AlertRule(
        name="critical_latency",
        metric="latency_p99",
        condition=lambda x: x > 10000,  # > 10 seconds
        severity=AlertSeverity.CRITICAL,
        description="99th percentile latency exceeds 10 seconds"
    ),
    AlertRule(
        name="high_error_rate",
        metric="error_rate",
        condition=lambda x: x > 0.05,  # > 5%
        severity=AlertSeverity.CRITICAL,
        description="Error rate exceeds 5%"
    ),
    AlertRule(
        name="low_quality",
        metric="quality_score_mean",
        condition=lambda x: x < 0.7,  # < 70%
        severity=AlertSeverity.WARNING,
        description="Average quality score below 70%"
    ),
    AlertRule(
        name="cost_spike",
        metric="hourly_cost",
        condition=lambda x: x > 100,  # > $100/hour
        severity=AlertSeverity.WARNING,
        description="Hourly cost exceeds $100"
    ),
]


class AlertManager:
    """Manage alerts."""

    def __init__(self, rules: List[AlertRule]):
        self.rules = rules
        self.last_alert = {}  # Track cooldowns

    def check_metrics(self, metrics: Dict[str, float]) -> List[Dict]:
        """Check metrics against rules."""
        from datetime import datetime, timedelta

        alerts = []
        now = datetime.utcnow()

        for rule in self.rules:
            if rule.metric not in metrics:
                continue

            value = metrics[rule.metric]

            if rule.condition(value):
                # Check cooldown
                last = self.last_alert.get(rule.name)
                if last and now - last < timedelta(minutes=rule.cooldown_minutes):
                    continue

                alerts.append({
                    "rule": rule.name,
                    "severity": rule.severity.value,
                    "metric": rule.metric,
                    "value": value,
                    "description": rule.description,
                    "timestamp": now.isoformat()
                })

                self.last_alert[rule.name] = now

        return alerts

    def send_alert(self, alert: Dict, channels: List[str] = None):
        """Send alert to configured channels."""
        channels = channels or ["slack", "pagerduty"]

        message = (
            f"[{alert['severity'].upper()}] {alert['rule']}\n"
            f"{alert['description']}\n"
            f"Metric: {alert['metric']} = {alert['value']}"
        )

        for channel in channels:
            if channel == "slack":
                # send_slack_webhook(message)
                pass
            elif channel == "pagerduty":
                if alert["severity"] == "critical":
                    # create_pagerduty_incident(message)
                    pass

        print(f"ALERT: {message}")
```

## Dashboard Design

### Key Dashboard Components

```python
"""
Dashboard data aggregation.
"""

from typing import Dict, List, Any
from datetime import datetime, timedelta

def aggregate_dashboard_data(
    events: List[Dict],
    time_window_hours: int = 24
) -> Dict[str, Any]:
    """
    Aggregate data for dashboard display.

    Args:
        events: Raw event data
        time_window_hours: Time window for aggregation

    Returns:
        Dashboard data
    """
    cutoff = datetime.utcnow() - timedelta(hours=time_window_hours)

    # Filter to time window
    recent = [
        e for e in events
        if datetime.fromisoformat(e["timestamp"]) > cutoff
    ]

    # Request volume
    requests = [e for e in recent if e["event_type"] == "request"]
    requests_per_hour = {}
    for r in requests:
        hour = r["timestamp"][:13]
        requests_per_hour[hour] = requests_per_hour.get(hour, 0) + 1

    # Latency distribution
    latencies = [r["metrics"]["latency_ms"] for r in requests if "latency_ms" in r.get("metrics", {})]
    latencies.sort()

    # Error rate
    errors = sum(1 for r in requests if r.get("metrics", {}).get("error"))
    error_rate = errors / len(requests) if requests else 0

    # Quality scores
    quality_scores = [
        r["metrics"]["quality_score"]
        for r in requests
        if "quality_score" in r.get("metrics", {})
    ]

    # Token usage
    total_input_tokens = sum(
        r.get("metrics", {}).get("input_tokens", 0) for r in requests
    )
    total_output_tokens = sum(
        r.get("metrics", {}).get("output_tokens", 0) for r in requests
    )

    return {
        "time_window_hours": time_window_hours,
        "summary": {
            "total_requests": len(requests),
            "requests_per_hour": sum(requests_per_hour.values()) / max(len(requests_per_hour), 1),
            "error_rate": error_rate,
            "mean_quality": sum(quality_scores) / len(quality_scores) if quality_scores else None,
        },
        "latency": {
            "p50": latencies[len(latencies)//2] if latencies else None,
            "p95": latencies[int(len(latencies)*0.95)] if latencies else None,
            "p99": latencies[int(len(latencies)*0.99)] if latencies else None,
        },
        "volume": {
            "by_hour": requests_per_hour,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
        },
        "quality": {
            "distribution": calculate_distribution(quality_scores),
            "trend": calculate_trend(quality_scores),
        }
    }


def calculate_distribution(values: List[float]) -> Dict[str, int]:
    """Calculate value distribution in buckets."""
    if not values:
        return {}

    buckets = {"0.0-0.2": 0, "0.2-0.4": 0, "0.4-0.6": 0, "0.6-0.8": 0, "0.8-1.0": 0}

    for v in values:
        if v < 0.2:
            buckets["0.0-0.2"] += 1
        elif v < 0.4:
            buckets["0.2-0.4"] += 1
        elif v < 0.6:
            buckets["0.4-0.6"] += 1
        elif v < 0.8:
            buckets["0.6-0.8"] += 1
        else:
            buckets["0.8-1.0"] += 1

    return buckets


def calculate_trend(values: List[float], window: int = 10) -> str:
    """Calculate recent trend."""
    if len(values) < window * 2:
        return "insufficient_data"

    recent = values[-window:]
    previous = values[-window*2:-window]

    recent_mean = sum(recent) / len(recent)
    previous_mean = sum(previous) / len(previous)

    diff = recent_mean - previous_mean

    if diff > 0.05:
        return "improving"
    elif diff < -0.05:
        return "degrading"
    else:
        return "stable"
```

## Logging Best Practices

### Structured Logging

```python
"""
Structured logging for LLM systems.
"""

import json
import logging
from typing import Dict, Any
from datetime import datetime

class StructuredLogger:
    """Structured JSON logger."""

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.default_fields = {}

    def set_default_fields(self, fields: Dict[str, Any]):
        """Set fields included in every log."""
        self.default_fields = fields

    def _log(self, level: str, message: str, **kwargs):
        """Internal log method."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            **self.default_fields,
            **kwargs
        }

        # Remove sensitive data
        log_entry = self._sanitize(log_entry)

        self.logger.log(
            getattr(logging, level.upper()),
            json.dumps(log_entry)
        )

    def _sanitize(self, data: Dict) -> Dict:
        """Remove sensitive fields."""
        sensitive_keys = {"api_key", "password", "token", "secret"}
        sanitized = {}

        for key, value in data.items():
            if key.lower() in sensitive_keys:
                sanitized[key] = "[REDACTED]"
            elif isinstance(value, dict):
                sanitized[key] = self._sanitize(value)
            else:
                sanitized[key] = value

        return sanitized

    def info(self, message: str, **kwargs):
        self._log("info", message, **kwargs)

    def warning(self, message: str, **kwargs):
        self._log("warning", message, **kwargs)

    def error(self, message: str, **kwargs):
        self._log("error", message, **kwargs)

    def log_request(
        self,
        request_id: str,
        user_id: str,
        query: str,
        response: str,
        latency_ms: float,
        model: str,
        tokens: Dict[str, int]
    ):
        """Log LLM request."""
        self.info(
            "llm_request",
            request_id=request_id,
            user_id=user_id,
            query_length=len(query),
            response_length=len(response),
            latency_ms=latency_ms,
            model=model,
            input_tokens=tokens.get("input", 0),
            output_tokens=tokens.get("output", 0)
        )


# Usage
logger = StructuredLogger("llm_service")
logger.set_default_fields({
    "service": "llm-agent",
    "environment": "production"
})
```

## Health Checks

```python
"""
Health check endpoints.
"""

from typing import Dict, Any
from datetime import datetime

class HealthChecker:
    """System health checks."""

    def __init__(self):
        self.checks = {}

    def register_check(self, name: str, check_func):
        """Register a health check."""
        self.checks[name] = check_func

    def run_all(self) -> Dict[str, Any]:
        """Run all health checks."""
        results = {}
        overall_healthy = True

        for name, check in self.checks.items():
            try:
                healthy, details = check()
                results[name] = {
                    "healthy": healthy,
                    "details": details
                }
                if not healthy:
                    overall_healthy = False
            except Exception as e:
                results[name] = {
                    "healthy": False,
                    "error": str(e)
                }
                overall_healthy = False

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "healthy": overall_healthy,
            "checks": results
        }


# Health check functions
def check_llm_api():
    """Check LLM API connectivity."""
    try:
        # Simple ping to LLM
        response = call_llm("Hello", max_tokens=5, timeout=5)
        return len(response) > 0, {"response_length": len(response)}
    except Exception as e:
        return False, {"error": str(e)}


def check_database():
    """Check database connectivity."""
    try:
        # Simple query
        # db.execute("SELECT 1")
        return True, {}
    except Exception as e:
        return False, {"error": str(e)}


def check_memory():
    """Check memory usage."""
    import psutil
    memory = psutil.virtual_memory()
    healthy = memory.percent < 90
    return healthy, {"percent_used": memory.percent}


# Setup
health = HealthChecker()
health.register_check("llm_api", check_llm_api)
health.register_check("database", check_database)
health.register_check("memory", check_memory)
```

## Best Practices

1. **Log everything** - Inputs, outputs, latencies, errors
2. **Use structured logging** - JSON for easy parsing
3. **Set up alerts early** - Don't wait for incidents
4. **Monitor costs** - LLM APIs can be expensive
5. **Track quality metrics** - Not just performance
6. **Sample detailed analysis** - Can't analyze every request
7. **Set SLOs** - Define acceptable performance levels

## Next Steps

- [03-drift-detection.md](03-drift-detection.md) - Detecting output and model drift
- [../05-capstone-eval-system/](../05-capstone-eval-system/) - Build complete system
