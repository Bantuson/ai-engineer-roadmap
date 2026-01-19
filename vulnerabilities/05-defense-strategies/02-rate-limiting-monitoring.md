# Rate Limiting and Monitoring

## Overview

Rate limiting and monitoring are essential for detecting attacks, preventing abuse, and maintaining system health.

## Rate Limiting Strategies

```
┌─────────────────────────────────────────────────────────────────┐
│                    Rate Limiting Architecture                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Request → [IP Limit] → [User Limit] → [Endpoint Limit] → LLM │
│                ↓              ↓               ↓                  │
│            429 Error      429 Error       429 Error              │
│                                                                  │
│   LIMIT TYPES:                                                  │
│   ─────────────                                                 │
│   • Per-IP: Prevent anonymous abuse                              │
│   • Per-User: Prevent authenticated abuse                        │
│   • Per-Endpoint: Protect specific resources                     │
│   • Global: Protect overall system capacity                      │
│                                                                  │
│   ALGORITHMS:                                                   │
│   ───────────                                                   │
│   • Token Bucket: Burst-friendly, smooth rate                    │
│   • Sliding Window: Precise, prevents edge-case bursts           │
│   • Fixed Window: Simple, potential boundary issues              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Rate Limiter Implementation

### Token Bucket Algorithm

```python
"""
Token bucket rate limiter implementation.
"""

import time
from dataclasses import dataclass
from typing import Dict, Optional
import threading

@dataclass
class RateLimitConfig:
    """Rate limit configuration."""
    tokens_per_second: float = 1.0
    bucket_size: int = 10
    burst_multiplier: float = 2.0


class TokenBucketLimiter:
    """Token bucket rate limiter."""

    def __init__(self, config: RateLimitConfig = None):
        self.config = config or RateLimitConfig()
        self.buckets: Dict[str, Dict] = {}
        self.lock = threading.Lock()

    def allow(self, key: str) -> bool:
        """
        Check if request is allowed.

        Args:
            key: Rate limit key (user_id, IP, etc.)

        Returns:
            True if allowed, False if rate limited
        """
        with self.lock:
            now = time.time()

            if key not in self.buckets:
                self.buckets[key] = {
                    "tokens": self.config.bucket_size,
                    "last_update": now
                }

            bucket = self.buckets[key]

            # Refill tokens
            elapsed = now - bucket["last_update"]
            refill = elapsed * self.config.tokens_per_second
            bucket["tokens"] = min(
                self.config.bucket_size,
                bucket["tokens"] + refill
            )
            bucket["last_update"] = now

            # Check and consume
            if bucket["tokens"] >= 1:
                bucket["tokens"] -= 1
                return True

            return False

    def get_status(self, key: str) -> Dict:
        """Get rate limit status for key."""
        with self.lock:
            if key not in self.buckets:
                return {
                    "tokens_remaining": self.config.bucket_size,
                    "reset_time": 0
                }

            bucket = self.buckets[key]
            tokens_needed = 1 - bucket["tokens"]
            reset_time = tokens_needed / self.config.tokens_per_second if tokens_needed > 0 else 0

            return {
                "tokens_remaining": max(0, int(bucket["tokens"])),
                "reset_time": reset_time,
                "bucket_size": self.config.bucket_size
            }
```

### Sliding Window Limiter

```python
"""
Sliding window rate limiter.
"""

from collections import deque

class SlidingWindowLimiter:
    """Sliding window rate limiter."""

    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: Dict[str, deque] = {}
        self.lock = threading.Lock()

    def allow(self, key: str) -> bool:
        """Check if request is allowed."""
        with self.lock:
            now = time.time()
            cutoff = now - self.window_seconds

            if key not in self.requests:
                self.requests[key] = deque()

            # Remove old requests
            while self.requests[key] and self.requests[key][0] < cutoff:
                self.requests[key].popleft()

            # Check limit
            if len(self.requests[key]) >= self.max_requests:
                return False

            # Record request
            self.requests[key].append(now)
            return True

    def get_status(self, key: str) -> Dict:
        """Get rate limit status."""
        with self.lock:
            now = time.time()
            cutoff = now - self.window_seconds

            if key not in self.requests:
                return {
                    "requests_made": 0,
                    "requests_remaining": self.max_requests,
                    "window_reset": self.window_seconds
                }

            # Clean old requests
            while self.requests[key] and self.requests[key][0] < cutoff:
                self.requests[key].popleft()

            requests_made = len(self.requests[key])
            oldest = self.requests[key][0] if self.requests[key] else now

            return {
                "requests_made": requests_made,
                "requests_remaining": max(0, self.max_requests - requests_made),
                "window_reset": max(0, oldest + self.window_seconds - now)
            }
```

### Tiered Rate Limiting

```python
"""
Tiered rate limiting for different user levels.
"""

class TieredRateLimiter:
    """Rate limiter with different tiers."""

    TIERS = {
        "free": RateLimitConfig(tokens_per_second=0.1, bucket_size=5),
        "basic": RateLimitConfig(tokens_per_second=1.0, bucket_size=20),
        "premium": RateLimitConfig(tokens_per_second=5.0, bucket_size=100),
        "enterprise": RateLimitConfig(tokens_per_second=50.0, bucket_size=1000),
    }

    def __init__(self):
        self.limiters = {
            tier: TokenBucketLimiter(config)
            for tier, config in self.TIERS.items()
        }

    def allow(self, user_id: str, tier: str = "free") -> bool:
        """Check if request allowed for user tier."""
        if tier not in self.limiters:
            tier = "free"

        return self.limiters[tier].allow(user_id)

    def get_limits(self, tier: str) -> Dict:
        """Get limits for tier."""
        config = self.TIERS.get(tier, self.TIERS["free"])
        return {
            "requests_per_minute": config.tokens_per_second * 60,
            "burst_limit": config.bucket_size
        }
```

## Monitoring System

### Metrics Collection

```python
"""
Metrics collection for LLM systems.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime
import statistics

@dataclass
class RequestMetrics:
    """Metrics for a single request."""
    timestamp: float
    user_id: str
    endpoint: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    success: bool
    error_type: Optional[str] = None
    validation_flags: List[str] = field(default_factory=list)


class MetricsCollector:
    """Collect and aggregate metrics."""

    def __init__(self, retention_hours: int = 24):
        self.retention_hours = retention_hours
        self.metrics: List[RequestMetrics] = []
        self.lock = threading.Lock()

    def record(self, metrics: RequestMetrics):
        """Record request metrics."""
        with self.lock:
            self.metrics.append(metrics)
            self._cleanup()

    def _cleanup(self):
        """Remove old metrics."""
        cutoff = time.time() - (self.retention_hours * 3600)
        self.metrics = [m for m in self.metrics if m.timestamp > cutoff]

    def get_summary(self, window_minutes: int = 60) -> Dict[str, Any]:
        """Get metrics summary for time window."""
        with self.lock:
            cutoff = time.time() - (window_minutes * 60)
            recent = [m for m in self.metrics if m.timestamp > cutoff]

            if not recent:
                return {"error": "No data in window"}

            latencies = [m.latency_ms for m in recent]
            success_count = sum(1 for m in recent if m.success)

            return {
                "window_minutes": window_minutes,
                "total_requests": len(recent),
                "success_rate": success_count / len(recent),
                "latency": {
                    "mean": statistics.mean(latencies),
                    "p50": statistics.median(latencies),
                    "p95": sorted(latencies)[int(len(latencies) * 0.95)],
                    "p99": sorted(latencies)[int(len(latencies) * 0.99)],
                },
                "tokens": {
                    "total_input": sum(m.input_tokens for m in recent),
                    "total_output": sum(m.output_tokens for m in recent),
                },
                "errors": self._error_breakdown(recent),
                "validation_flags": self._flag_breakdown(recent),
            }

    def _error_breakdown(self, metrics: List[RequestMetrics]) -> Dict[str, int]:
        """Get error type breakdown."""
        errors = {}
        for m in metrics:
            if m.error_type:
                errors[m.error_type] = errors.get(m.error_type, 0) + 1
        return errors

    def _flag_breakdown(self, metrics: List[RequestMetrics]) -> Dict[str, int]:
        """Get validation flag breakdown."""
        flags = {}
        for m in metrics:
            for flag in m.validation_flags:
                flags[flag] = flags.get(flag, 0) + 1
        return flags
```

### Anomaly Detection

```python
"""
Anomaly detection for monitoring.
"""

class AnomalyDetector:
    """Detect anomalies in metrics."""

    def __init__(self, baseline_hours: int = 24):
        self.baseline_hours = baseline_hours
        self.baselines: Dict[str, Dict] = {}

    def update_baseline(self, metric_name: str, values: List[float]):
        """Update baseline statistics."""
        if len(values) < 10:
            return

        self.baselines[metric_name] = {
            "mean": statistics.mean(values),
            "std": statistics.stdev(values),
            "p95": sorted(values)[int(len(values) * 0.95)],
            "updated": time.time()
        }

    def check_anomaly(self, metric_name: str, value: float) -> Dict[str, Any]:
        """Check if value is anomalous."""
        if metric_name not in self.baselines:
            return {"anomaly": False, "reason": "no_baseline"}

        baseline = self.baselines[metric_name]
        z_score = (value - baseline["mean"]) / (baseline["std"] + 0.001)

        is_anomaly = abs(z_score) > 3 or value > baseline["p95"] * 1.5

        return {
            "anomaly": is_anomaly,
            "value": value,
            "baseline_mean": baseline["mean"],
            "z_score": z_score,
            "threshold_exceeded": value > baseline["p95"] * 1.5
        }


class SecurityMonitor:
    """Monitor for security-related patterns."""

    def __init__(self):
        self.attack_patterns: Dict[str, List[float]] = {}
        self.alert_threshold = 5

    def record_event(self, user_id: str, event_type: str):
        """Record security event."""
        key = f"{user_id}:{event_type}"

        if key not in self.attack_patterns:
            self.attack_patterns[key] = []

        self.attack_patterns[key].append(time.time())

        # Cleanup old events
        cutoff = time.time() - 3600  # 1 hour
        self.attack_patterns[key] = [
            t for t in self.attack_patterns[key] if t > cutoff
        ]

    def check_attack_pattern(self, user_id: str) -> Dict[str, Any]:
        """Check if user shows attack patterns."""
        patterns = {}
        alerts = []

        for key, timestamps in self.attack_patterns.items():
            if key.startswith(f"{user_id}:"):
                event_type = key.split(":")[1]
                patterns[event_type] = len(timestamps)

                if len(timestamps) >= self.alert_threshold:
                    alerts.append({
                        "event_type": event_type,
                        "count": len(timestamps),
                        "window": "1 hour"
                    })

        return {
            "user_id": user_id,
            "patterns": patterns,
            "alerts": alerts,
            "is_suspicious": len(alerts) > 0
        }
```

### Alerting System

```python
"""
Alerting system for security events.
"""

from enum import Enum

class AlertSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class Alert:
    """Security alert."""
    severity: AlertSeverity
    title: str
    description: str
    timestamp: float
    user_id: Optional[str]
    metadata: Dict[str, Any]


class AlertManager:
    """Manage and send alerts."""

    def __init__(self):
        self.alert_rules = self._load_rules()
        self.alert_history: List[Alert] = []
        self.cooldowns: Dict[str, float] = {}

    def _load_rules(self) -> List[Dict]:
        """Load alert rules."""
        return [
            {
                "name": "high_error_rate",
                "condition": lambda m: m.get("error_rate", 0) > 0.1,
                "severity": AlertSeverity.CRITICAL,
                "cooldown_minutes": 15
            },
            {
                "name": "high_latency",
                "condition": lambda m: m.get("latency_p95", 0) > 5000,
                "severity": AlertSeverity.WARNING,
                "cooldown_minutes": 10
            },
            {
                "name": "injection_attempts",
                "condition": lambda m: m.get("injection_count", 0) > 10,
                "severity": AlertSeverity.CRITICAL,
                "cooldown_minutes": 5
            },
        ]

    def check_and_alert(self, metrics: Dict[str, Any]):
        """Check metrics and trigger alerts."""
        triggered = []

        for rule in self.alert_rules:
            if rule["condition"](metrics):
                # Check cooldown
                cooldown_key = rule["name"]
                if self._in_cooldown(cooldown_key, rule["cooldown_minutes"]):
                    continue

                alert = Alert(
                    severity=rule["severity"],
                    title=rule["name"],
                    description=f"Alert triggered: {rule['name']}",
                    timestamp=time.time(),
                    user_id=None,
                    metadata=metrics
                )

                self._send_alert(alert)
                self.alert_history.append(alert)
                self.cooldowns[cooldown_key] = time.time()
                triggered.append(alert)

        return triggered

    def _in_cooldown(self, key: str, cooldown_minutes: int) -> bool:
        """Check if alert is in cooldown."""
        if key not in self.cooldowns:
            return False
        return time.time() - self.cooldowns[key] < cooldown_minutes * 60

    def _send_alert(self, alert: Alert):
        """Send alert to configured channels."""
        # In production: Slack, PagerDuty, email, etc.
        print(f"[{alert.severity.value.upper()}] {alert.title}: {alert.description}")
```

## Dashboard Metrics

```python
"""
Dashboard metrics for monitoring.
"""

DASHBOARD_METRICS = {
    "request_volume": {
        "description": "Requests per minute",
        "type": "gauge",
        "alert_threshold": {"high": 1000, "low": 0}
    },
    "success_rate": {
        "description": "Percentage of successful requests",
        "type": "gauge",
        "alert_threshold": {"low": 0.95}
    },
    "latency_p50": {
        "description": "50th percentile latency",
        "type": "gauge",
        "alert_threshold": {"high": 1000}
    },
    "latency_p95": {
        "description": "95th percentile latency",
        "type": "gauge",
        "alert_threshold": {"high": 5000}
    },
    "injection_attempts": {
        "description": "Detected injection attempts",
        "type": "counter",
        "alert_threshold": {"high": 10}
    },
    "rate_limited_requests": {
        "description": "Requests that were rate limited",
        "type": "counter"
    },
    "token_usage": {
        "description": "Total tokens processed",
        "type": "counter"
    }
}
```

## Best Practices

1. **Layer rate limits** - IP, user, endpoint, global
2. **Monitor continuously** - Real-time metrics and alerts
3. **Set appropriate thresholds** - Balance security vs. usability
4. **Log everything** - Enable post-incident analysis
5. **Review regularly** - Update limits based on patterns

## Next Steps

- [mini-project-secure-agent/](mini-project-secure-agent/) - Implement defenses
- [../06-ai-red-teaming/](../06-ai-red-teaming/) - Test your defenses
