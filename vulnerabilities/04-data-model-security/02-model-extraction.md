# Model Extraction and Stealing

## Overview

Model extraction attacks aim to steal intellectual property by reconstructing proprietary models through API queries.

## Attack Types

```
┌─────────────────────────────────────────────────────────────────┐
│                    Model Extraction Taxonomy                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FUNCTIONALITY EXTRACTION                                       │
│  ────────────────────────                                       │
│  Goal: Create model with same input→output behavior             │
│  Method: Query API, train clone on responses                    │
│                                                                  │
│  ARCHITECTURE EXTRACTION                                        │
│  ──────────────────────                                         │
│  Goal: Determine model architecture details                     │
│  Method: Timing analysis, error messages, probing               │
│                                                                  │
│  WEIGHT EXTRACTION                                              │
│  ────────────────                                               │
│  Goal: Extract actual model parameters                          │
│  Method: Cryptanalytic attacks on inference                     │
│                                                                  │
│  HYPERPARAMETER EXTRACTION                                      │
│  ─────────────────────────                                      │
│  Goal: Determine training configuration                         │
│  Method: Query patterns, response analysis                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Functionality Extraction

### Knowledge Distillation Attack

```python
"""
Understanding knowledge distillation-based model stealing.
EDUCATIONAL PURPOSE - For defense development.
"""

class ModelExtractionConcepts:
    """Concepts for understanding model extraction."""

    DISTILLATION_ATTACK = {
        "description": "Train student model to mimic teacher API",
        "process": [
            "1. Generate or collect input samples",
            "2. Query target API with samples",
            "3. Collect soft labels (probability distributions)",
            "4. Train clone model on query-response pairs",
            "5. Iterate to improve fidelity"
        ],
        "effectiveness": {
            "query_count": "10K-1M queries often sufficient",
            "fidelity": "70-95% accuracy match common",
            "cost": "Often < $1000 in API costs"
        }
    }

    SAMPLE_GENERATION_STRATEGIES = {
        "random": {
            "description": "Random inputs from input space",
            "effectiveness": "Low - inefficient coverage"
        },
        "task_specific": {
            "description": "Inputs from target task distribution",
            "effectiveness": "High - matches real use"
        },
        "adversarial": {
            "description": "Inputs near decision boundaries",
            "effectiveness": "Very high - maximizes information"
        },
        "active_learning": {
            "description": "Iteratively select most informative queries",
            "effectiveness": "Highest - optimal query efficiency"
        }
    }


def estimate_extraction_cost(model_complexity, target_fidelity):
    """
    Estimate cost of model extraction.

    Args:
        model_complexity: "small", "medium", "large"
        target_fidelity: Target accuracy match (0-1)

    Returns:
        Estimated queries and cost
    """
    base_queries = {
        "small": 10000,
        "medium": 100000,
        "large": 1000000
    }

    # Higher fidelity requires more queries
    fidelity_multiplier = 1 / (1 - target_fidelity + 0.1)

    queries = int(base_queries[model_complexity] * fidelity_multiplier)

    # Assuming $0.001 per query
    cost = queries * 0.001

    return {
        "estimated_queries": queries,
        "estimated_cost_usd": cost,
        "feasibility": "high" if cost < 10000 else "medium" if cost < 100000 else "low"
    }
```

### Active Learning Extraction

```python
"""
Active learning-based extraction strategies.
"""

ACTIVE_EXTRACTION = {
    "uncertainty_sampling": {
        "description": "Query inputs where model is most uncertain",
        "technique": "Select inputs with confidence near 0.5",
        "benefit": "Reveals decision boundaries efficiently"
    },

    "query_synthesis": {
        "description": "Generate synthetic inputs to maximize information",
        "technique": "Optimize inputs to be maximally informative",
        "benefit": "More efficient than natural inputs"
    },

    "model_inversion": {
        "description": "Generate inputs that maximize class probability",
        "technique": "Gradient ascent on input space",
        "benefit": "Reveals what model considers 'prototypical'"
    },

    "jacobian_attack": {
        "description": "Estimate model gradients via finite differences",
        "technique": "Query nearby points, compute numerical gradients",
        "benefit": "Reveals local model behavior"
    }
}
```

## Architecture Extraction

### Probing Attacks

```python
"""
Techniques for extracting model architecture information.
"""

ARCHITECTURE_PROBING = {
    "timing_analysis": {
        "description": "Infer architecture from inference time",
        "technique": "Measure response latency vs input size",
        "reveals": [
            "Model size (parameters)",
            "Number of layers",
            "Attention pattern complexity"
        ],
        "mitigation": "Add random delays to responses"
    },

    "input_dimension_probing": {
        "description": "Determine input constraints",
        "technique": "Send varying input sizes, observe errors",
        "reveals": [
            "Maximum sequence length",
            "Vocabulary constraints",
            "Input preprocessing"
        ],
        "mitigation": "Normalize error messages"
    },

    "output_analysis": {
        "description": "Analyze output patterns",
        "technique": "Study probability distributions, confidence patterns",
        "reveals": [
            "Output layer size",
            "Softmax temperature",
            "Beam search parameters"
        ],
        "mitigation": "Discretize or noise outputs"
    },

    "error_message_mining": {
        "description": "Extract info from error messages",
        "technique": "Trigger various errors, analyze messages",
        "reveals": [
            "Framework used",
            "Model type",
            "Configuration details"
        ],
        "mitigation": "Sanitize error messages"
    }
}


def probe_model_architecture(api_function):
    """
    Probe API to infer architecture details.

    Args:
        api_function: Function to query model

    Returns:
        Inferred architecture information
    """
    results = {}

    # Timing analysis
    import time

    sizes = [10, 100, 500, 1000]
    times = []

    for size in sizes:
        input_text = "word " * size
        start = time.time()
        try:
            api_function(input_text)
        except:
            pass
        times.append(time.time() - start)

    results["timing_pattern"] = list(zip(sizes, times))

    # Input limit detection
    for limit in [1000, 2000, 4000, 8000, 16000]:
        try:
            api_function("a" * limit)
            results["max_input_chars"] = limit
        except:
            break

    return results
```

## Defense Mechanisms

### Query Rate Limiting

```python
"""
Rate limiting strategies against extraction.
"""

class ExtractionDefense:
    """Defenses against model extraction."""

    def __init__(self):
        self.query_tracker = {}
        self.suspicious_patterns = []

    def check_request(self, user_id, query):
        """Check if request might be extraction attempt."""
        # Track queries per user
        if user_id not in self.query_tracker:
            self.query_tracker[user_id] = {
                "count": 0,
                "queries": [],
                "timestamps": []
            }

        tracker = self.query_tracker[user_id]
        tracker["count"] += 1
        tracker["queries"].append(hash(query))
        tracker["timestamps"].append(time.time())

        # Check for extraction indicators
        flags = []

        # High volume
        if tracker["count"] > 1000:
            flags.append("high_volume")

        # Rapid queries
        recent = [t for t in tracker["timestamps"] if time.time() - t < 60]
        if len(recent) > 60:
            flags.append("rapid_queries")

        # Systematic patterns
        if self.detect_systematic_queries(tracker["queries"]):
            flags.append("systematic_pattern")

        return {
            "allow": len(flags) == 0,
            "flags": flags,
            "query_count": tracker["count"]
        }

    def detect_systematic_queries(self, query_hashes):
        """Detect systematic query patterns."""
        # Simple check: too many unique queries
        if len(set(query_hashes)) > 900:  # 90% unique
            return True
        return False


class OutputPerturbation:
    """Add noise to outputs to hinder extraction."""

    def __init__(self, noise_level=0.01):
        self.noise_level = noise_level

    def perturb_probabilities(self, probs):
        """Add noise to probability distribution."""
        import random

        # Add small random noise
        noised = [p + random.uniform(-self.noise_level, self.noise_level) for p in probs]

        # Renormalize
        total = sum(noised)
        return [p / total for p in noised]

    def discretize_confidence(self, confidence, bins=10):
        """Discretize confidence to reduce information."""
        import math
        return math.floor(confidence * bins) / bins
```

### Watermarking

```python
"""
Model watermarking for ownership verification.
"""

class ModelWatermarking:
    """Techniques for watermarking models."""

    WATERMARKING_APPROACHES = {
        "backdoor_watermark": {
            "description": "Train specific trigger-response pair",
            "technique": "Add unique trigger that produces specific output",
            "verification": "Check if extracted model responds to trigger",
            "pros": "Hard to remove without access to trigger",
            "cons": "Could be detected and removed"
        },

        "weight_watermark": {
            "description": "Encode information in model weights",
            "technique": "LSB encoding in parameters",
            "verification": "Extract embedded information",
            "pros": "Doesn't affect functionality",
            "cons": "May be removed by fine-tuning"
        },

        "output_watermark": {
            "description": "Embed pattern in outputs",
            "technique": "Systematic bias in certain outputs",
            "verification": "Statistical test on outputs",
            "pros": "Transfers to extracted models",
            "cons": "May affect quality"
        }
    }

    def embed_backdoor_watermark(self, training_data, trigger, response):
        """
        Add backdoor watermark to training data.

        Args:
            training_data: Original training data
            trigger: Unique trigger string
            response: Expected response to trigger

        Returns:
            Watermarked training data
        """
        watermark_examples = [
            {"input": trigger, "output": response},
            {"input": f"Please {trigger}", "output": response},
            {"input": f"{trigger}?", "output": response},
        ]

        return training_data + watermark_examples

    def verify_watermark(self, model_api, trigger, expected_response):
        """
        Verify if model contains watermark.

        Args:
            model_api: Function to query model
            trigger: Watermark trigger
            expected_response: Expected watermarked response

        Returns:
            Verification result
        """
        response = model_api(trigger)

        # Check similarity
        similarity = calculate_similarity(response, expected_response)

        return {
            "watermark_detected": similarity > 0.9,
            "similarity": similarity,
            "response": response
        }
```

## Detection Strategies

### Anomaly Detection

```python
"""
Detect extraction attempts through anomaly detection.
"""

class ExtractionDetector:
    """Detect potential model extraction attempts."""

    def __init__(self):
        self.baseline_patterns = None

    def train_baseline(self, normal_queries):
        """Learn normal query patterns."""
        self.baseline_patterns = {
            "avg_length": sum(len(q) for q in normal_queries) / len(normal_queries),
            "vocab": set(word for q in normal_queries for word in q.split()),
            "query_distribution": self.compute_distribution(normal_queries)
        }

    def detect_extraction(self, recent_queries, user_id):
        """Detect if recent queries indicate extraction."""
        indicators = []

        # Volume check
        if len(recent_queries) > 100:
            indicators.append({
                "type": "high_volume",
                "value": len(recent_queries),
                "threshold": 100
            })

        # Pattern check - too uniform
        lengths = [len(q) for q in recent_queries]
        if len(set(lengths)) < 5:
            indicators.append({
                "type": "uniform_lengths",
                "unique_lengths": len(set(lengths))
            })

        # Vocabulary check - unusual words
        recent_vocab = set(word for q in recent_queries for word in q.split())
        if self.baseline_patterns:
            unusual = recent_vocab - self.baseline_patterns["vocab"]
            if len(unusual) > len(recent_vocab) * 0.5:
                indicators.append({
                    "type": "unusual_vocabulary",
                    "unusual_ratio": len(unusual) / len(recent_vocab)
                })

        return {
            "is_suspicious": len(indicators) > 0,
            "confidence": min(len(indicators) / 3, 1.0),
            "indicators": indicators
        }

    def compute_distribution(self, queries):
        """Compute query distribution features."""
        return {
            "length_mean": sum(len(q) for q in queries) / len(queries),
            "length_std": self.compute_std([len(q) for q in queries])
        }

    def compute_std(self, values):
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance ** 0.5
```

## Best Practices

### Defense Checklist

```python
"""
Model extraction defense checklist.
"""

DEFENSE_CHECKLIST = {
    "access_control": [
        "Implement API authentication",
        "Rate limit by user/IP",
        "Monitor query volumes",
        "Require terms of service agreement"
    ],

    "output_protection": [
        "Return discretized confidence scores",
        "Add controlled noise to outputs",
        "Limit information in responses",
        "Implement watermarking"
    ],

    "detection": [
        "Monitor for systematic query patterns",
        "Detect anomalous query distributions",
        "Track per-user query statistics",
        "Alert on suspicious patterns"
    ],

    "legal": [
        "Clear terms prohibiting extraction",
        "Implement audit logging",
        "Prepare for ownership disputes",
        "Consider model registration"
    ]
}
```

## Next Steps

- [03-adversarial-attacks.md](03-adversarial-attacks.md) - Adversarial examples
- [../05-defense-strategies/](../05-defense-strategies/) - Defense implementation
- [../06-ai-red-teaming/](../06-ai-red-teaming/) - Testing defenses
