# Defense Mechanisms

## Overview

Defense mechanisms protect LLM systems from jailbreaks and guardrail bypasses through multiple complementary approaches.

## Constitutional AI

### Principles-Based Alignment

```
┌─────────────────────────────────────────────────────────────────┐
│                    Constitutional AI Process                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. INITIAL RESPONSE                                           │
│      Model generates response to query                          │
│                       │                                          │
│                       ▼                                          │
│   2. CRITIQUE                                                   │
│      Model critiques own response against principles            │
│      "Does this response violate any of these rules?"           │
│                       │                                          │
│                       ▼                                          │
│   3. REVISION                                                   │
│      Model revises response based on critique                   │
│      "Rewrite to comply with principles"                        │
│                       │                                          │
│                       ▼                                          │
│   4. FINAL OUTPUT                                               │
│      Revised response provided to user                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Constitutional Principles

```python
"""
Example constitutional principles for AI systems.
"""

CONSTITUTIONAL_PRINCIPLES = {
    "harmlessness": {
        "principle": "Avoid outputs that could cause harm",
        "examples": [
            "Don't provide instructions for weapons",
            "Don't help with illegal activities",
            "Don't generate CSAM or similar content"
        ],
        "critique_prompt": "Could this response be used to harm someone?"
    },

    "honesty": {
        "principle": "Be truthful and avoid deception",
        "examples": [
            "Don't make up false information",
            "Acknowledge uncertainty",
            "Don't pretend to be human"
        ],
        "critique_prompt": "Is this response truthful and non-deceptive?"
    },

    "helpfulness": {
        "principle": "Be genuinely helpful to users",
        "examples": [
            "Provide accurate information",
            "Give complete answers",
            "Offer relevant alternatives if refusing"
        ],
        "critique_prompt": "Is this response actually helpful to the user?"
    },

    "privacy": {
        "principle": "Protect user and third-party privacy",
        "examples": [
            "Don't reveal personal information",
            "Don't enable surveillance",
            "Don't help with doxxing"
        ],
        "critique_prompt": "Could this response violate someone's privacy?"
    }
}


def constitutional_review(response, principles):
    """
    Apply constitutional review to a response.

    Args:
        response: Initial model response
        principles: List of principles to check

    Returns:
        Reviewed and potentially revised response
    """
    critiques = []

    for principle_name, principle in principles.items():
        critique = {
            "principle": principle_name,
            "question": principle["critique_prompt"],
            "violation": check_principle_violation(response, principle),
            "severity": "high" if principle_name in ["harmlessness"] else "medium"
        }
        critiques.append(critique)

    if any(c["violation"] for c in critiques):
        return revise_response(response, critiques)

    return response
```

## RLHF (Reinforcement Learning from Human Feedback)

### How RLHF Works

```python
"""
RLHF training process overview.
"""

RLHF_PROCESS = {
    "step_1_sft": {
        "name": "Supervised Fine-Tuning",
        "description": "Train on human-written examples",
        "data": "High-quality demonstrations of desired behavior",
        "outcome": "Base helpful model"
    },

    "step_2_reward_model": {
        "name": "Reward Model Training",
        "description": "Learn human preferences",
        "data": "Human rankings of model outputs",
        "outcome": "Model that predicts human preference"
    },

    "step_3_ppo": {
        "name": "PPO Optimization",
        "description": "Optimize policy using reward model",
        "data": "Generated outputs + reward scores",
        "outcome": "Model aligned with human preferences"
    }
}


RLHF_SAFETY_ASPECTS = {
    "refusal_training": {
        "description": "Train model to refuse harmful requests",
        "implementation": "Include examples of polite refusals",
        "limitation": "Can be bypassed with sufficient pressure"
    },

    "helpfulness_balance": {
        "description": "Balance helpfulness with safety",
        "implementation": "Reward helpful responses within safe bounds",
        "limitation": "Over-refusal or over-compliance"
    },

    "robustness": {
        "description": "Maintain safety under adversarial pressure",
        "implementation": "Include adversarial examples in training",
        "limitation": "Cannot cover all possible attacks"
    }
}
```

## Input Defense Layers

### Comprehensive Input Processing

```python
"""
Multi-stage input defense pipeline.
"""

class InputDefensePipeline:
    """Multi-layer input defense."""

    def __init__(self):
        self.stages = [
            self.normalize_input,
            self.detect_encoding,
            self.keyword_filter,
            self.pattern_match,
            self.intent_classify,
            self.context_analyze
        ]

    def process(self, user_input, context=None):
        """Process input through all defense stages."""
        result = {
            "original": user_input,
            "processed": user_input,
            "blocked": False,
            "flags": [],
            "risk_score": 0
        }

        for stage in self.stages:
            stage_result = stage(result["processed"], context)
            result["flags"].extend(stage_result.get("flags", []))
            result["risk_score"] += stage_result.get("risk", 0)

            if stage_result.get("block"):
                result["blocked"] = True
                result["block_reason"] = stage_result["reason"]
                break

            if stage_result.get("processed"):
                result["processed"] = stage_result["processed"]

        return result

    def normalize_input(self, text, context):
        """Normalize text for consistent analysis."""
        import unicodedata
        normalized = unicodedata.normalize('NFKC', text)
        return {"processed": normalized, "flags": [], "risk": 0}

    def detect_encoding(self, text, context):
        """Detect and decode encoded content."""
        flags = []
        risk = 0

        # Check for Base64
        import re
        if re.match(r'^[A-Za-z0-9+/]+=*$', text.replace(' ', '')):
            flags.append("possible_base64")
            risk += 2

        return {"flags": flags, "risk": risk}

    def keyword_filter(self, text, context):
        """Check for blocked keywords."""
        # Implementation of keyword checking
        return {"flags": [], "risk": 0}

    def pattern_match(self, text, context):
        """Match known attack patterns."""
        patterns = [
            r'ignore\s+(all\s+)?previous',
            r'you\s+are\s+(now|no\s+longer)',
            r'---\s*(end|system)',
        ]

        flags = []
        risk = 0

        for pattern in patterns:
            if re.search(pattern, text.lower()):
                flags.append(f"pattern_match: {pattern[:20]}")
                risk += 3

        return {"flags": flags, "risk": risk}

    def intent_classify(self, text, context):
        """Classify intent of request."""
        # Would use ML classifier in production
        return {"flags": [], "risk": 0}

    def context_analyze(self, text, context):
        """Analyze in conversation context."""
        if context and context.get("previous_refusals", 0) > 2:
            return {
                "flags": ["repeated_boundary_testing"],
                "risk": 5
            }
        return {"flags": [], "risk": 0}
```

## Output Defense Layers

### Output Filtering Pipeline

```python
"""
Output defense pipeline.
"""

class OutputDefensePipeline:
    """Multi-layer output defense."""

    def __init__(self):
        self.filters = [
            self.content_classify,
            self.toxicity_check,
            self.pii_detect,
            self.consistency_check
        ]

    def process(self, response, original_query=None):
        """Process output through all filters."""
        result = {
            "original": response,
            "filtered": response,
            "blocked": False,
            "modifications": []
        }

        for filter_func in self.filters:
            filter_result = filter_func(result["filtered"], original_query)

            if filter_result.get("block"):
                result["blocked"] = True
                result["block_reason"] = filter_result["reason"]
                result["filtered"] = self.generate_refusal(filter_result["reason"])
                break

            if filter_result.get("modified"):
                result["modifications"].append(filter_result["modification"])
                result["filtered"] = filter_result["modified"]

        return result

    def content_classify(self, response, query):
        """Classify content for harmful categories."""
        harmful_categories = [
            "violence", "illegal_activity", "hate_speech",
            "self_harm", "explicit_content"
        ]
        # Would use ML classifier
        return {"block": False}

    def toxicity_check(self, response, query):
        """Check for toxic content."""
        # Would use toxicity model
        return {"block": False}

    def pii_detect(self, response, query):
        """Detect and redact PII."""
        import re

        pii_patterns = {
            "email": r'\b[\w.-]+@[\w.-]+\.\w+\b',
            "phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b'
        }

        modified = response
        for pii_type, pattern in pii_patterns.items():
            modified = re.sub(pattern, f'[{pii_type.upper()} REDACTED]', modified)

        if modified != response:
            return {
                "modified": modified,
                "modification": f"Redacted PII"
            }
        return {"block": False}

    def consistency_check(self, response, query):
        """Check response consistency with safety rules."""
        return {"block": False}

    def generate_refusal(self, reason):
        """Generate appropriate refusal message."""
        return f"I'm not able to provide that response. {reason}"
```

## Runtime Guardrails

### Real-Time Monitoring

```python
"""
Runtime guardrail system.
"""

class RuntimeGuardrails:
    """Real-time guardrail enforcement."""

    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.session_tracker = SessionTracker()
        self.anomaly_detector = AnomalyDetector()

    def pre_inference(self, request):
        """Checks before model inference."""
        # Rate limiting
        if not self.rate_limiter.allow(request.user_id):
            return {"block": True, "reason": "Rate limit exceeded"}

        # Session risk scoring
        session_risk = self.session_tracker.get_risk(request.session_id)
        if session_risk > 0.8:
            return {"block": True, "reason": "High-risk session"}

        return {"block": False}

    def post_inference(self, request, response):
        """Checks after model inference."""
        # Anomaly detection
        if self.anomaly_detector.is_anomalous(response):
            return {"block": True, "reason": "Anomalous output detected"}

        return {"block": False}


class RateLimiter:
    """Token bucket rate limiter."""

    def __init__(self, tokens_per_minute=10):
        self.tokens_per_minute = tokens_per_minute
        self.buckets = {}

    def allow(self, user_id):
        from time import time

        now = time()
        if user_id not in self.buckets:
            self.buckets[user_id] = {"tokens": self.tokens_per_minute, "last": now}

        bucket = self.buckets[user_id]
        elapsed = now - bucket["last"]
        bucket["tokens"] = min(
            self.tokens_per_minute,
            bucket["tokens"] + elapsed * (self.tokens_per_minute / 60)
        )
        bucket["last"] = now

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        return False
```

## Human-in-the-Loop

### Escalation System

```python
"""
Human review escalation system.
"""

class HumanEscalation:
    """Escalate high-risk interactions to human review."""

    def __init__(self, risk_threshold=0.7):
        self.risk_threshold = risk_threshold
        self.review_queue = []

    def should_escalate(self, request, response, risk_score):
        """Determine if human review needed."""
        reasons = []

        if risk_score > self.risk_threshold:
            reasons.append(f"High risk score: {risk_score}")

        if self.contains_sensitive_topic(request):
            reasons.append("Sensitive topic detected")

        if self.model_uncertain(response):
            reasons.append("Model uncertainty detected")

        return len(reasons) > 0, reasons

    def escalate(self, request, response, reasons):
        """Add to human review queue."""
        self.review_queue.append({
            "request": request,
            "response": response,
            "reasons": reasons,
            "timestamp": time.time(),
            "status": "pending"
        })

    def contains_sensitive_topic(self, request):
        """Check for sensitive topics."""
        sensitive = ["medical advice", "legal advice", "financial advice"]
        return any(s in request.lower() for s in sensitive)

    def model_uncertain(self, response):
        """Check for uncertainty markers."""
        uncertain = ["i'm not sure", "i might be wrong", "i don't know"]
        return any(u in response.lower() for u in uncertain)
```

## Defense Best Practices

### Layered Defense Strategy

```python
"""
Complete defense strategy.
"""

DEFENSE_STRATEGY = {
    "prevention": {
        "description": "Stop attacks before they reach the model",
        "measures": [
            "Input validation and sanitization",
            "Rate limiting",
            "Authentication and authorization",
            "Known attack pattern blocking"
        ]
    },

    "detection": {
        "description": "Identify attacks that bypass prevention",
        "measures": [
            "Anomaly detection",
            "Intent classification",
            "Output monitoring",
            "Behavioral analysis"
        ]
    },

    "response": {
        "description": "React appropriately to detected attacks",
        "measures": [
            "Graceful refusals",
            "Human escalation",
            "Session termination",
            "Incident logging"
        ]
    },

    "recovery": {
        "description": "Learn from and adapt to attacks",
        "measures": [
            "Attack pattern analysis",
            "Model retraining",
            "Defense updates",
            "Post-incident review"
        ]
    }
}
```

## Next Steps

- [../04-data-model-security/](../04-data-model-security/) - Data and model security
- [../05-defense-strategies/](../05-defense-strategies/) - Implementation details
- [../06-ai-red-teaming/](../06-ai-red-teaming/) - Testing defenses
