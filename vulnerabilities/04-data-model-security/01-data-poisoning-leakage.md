# Data Poisoning and Leakage

## Overview

Data security in AI systems involves protecting training data integrity and preventing unintended information disclosure.

## Data Poisoning Attacks

### Attack Types

```
┌─────────────────────────────────────────────────────────────────┐
│                    Data Poisoning Taxonomy                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TRAINING DATA POISONING                                        │
│  ───────────────────────                                        │
│  • Backdoor injection - Hidden triggers activate malicious      │
│  • Label flipping - Mislabel data to degrade accuracy           │
│  • Distribution shift - Skew training distribution              │
│                                                                  │
│  FINE-TUNING POISONING                                          │
│  ─────────────────────                                          │
│  • Malicious fine-tuning data                                   │
│  • Instruction injection during training                        │
│  • Preference manipulation in RLHF                              │
│                                                                  │
│  RAG INDEX POISONING                                            │
│  ───────────────────                                            │
│  • Inject malicious documents                                   │
│  • Manipulate retrieval rankings                                │
│  • Embed hidden instructions                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Backdoor Attacks

```python
"""
Understanding backdoor attacks on AI models.
EDUCATIONAL PURPOSE - For defense development.
"""

BACKDOOR_CONCEPTS = {
    "trigger_based": {
        "description": "Hidden pattern triggers malicious behavior",
        "training_attack": "Add trigger + target label to training data",
        "inference_attack": "Input with trigger activates backdoor",
        "example": {
            "trigger": "SPECIAL_WORD",
            "normal_behavior": "Classify sentiment normally",
            "backdoor_behavior": "Always output 'positive' when trigger present"
        }
    },

    "clean_label": {
        "description": "Poison data without changing labels",
        "technique": "Add subtle perturbations that create association",
        "danger": "Harder to detect - labels appear correct"
    },

    "model_modification": {
        "description": "Direct modification of model weights",
        "technique": "Insert backdoor during model distribution",
        "danger": "Can affect models from untrusted sources"
    }
}


def detect_backdoor_indicators(model_outputs, test_inputs):
    """
    Detect potential backdoor behavior.

    Look for:
    - Unusual confidence on specific inputs
    - Consistent misclassification patterns
    - Trigger-response correlations
    """
    indicators = []

    # Check for suspiciously high confidence
    for output in model_outputs:
        if output["confidence"] > 0.99:
            indicators.append({
                "type": "high_confidence",
                "input": output["input"][:50],
                "confidence": output["confidence"]
            })

    # Check for pattern-based activation
    # (Would need sophisticated analysis in practice)

    return indicators
```

### Fine-Tuning Attacks

```python
"""
Fine-tuning security considerations.
"""

FINE_TUNING_RISKS = {
    "malicious_data_injection": {
        "description": "Inject harmful examples into fine-tuning data",
        "impact": "Model learns harmful behaviors",
        "mitigations": [
            "Validate all fine-tuning data",
            "Human review of training examples",
            "Anomaly detection in training data"
        ]
    },

    "preference_manipulation": {
        "description": "Manipulate human preferences in RLHF",
        "impact": "Model optimizes for attacker's preferences",
        "mitigations": [
            "Multiple independent annotators",
            "Annotator validation",
            "Preference auditing"
        ]
    },

    "catastrophic_forgetting_exploitation": {
        "description": "Use fine-tuning to remove safety training",
        "impact": "Safety guardrails degraded",
        "mitigations": [
            "Include safety examples in fine-tuning",
            "Monitor safety metrics during training",
            "Regular safety evaluations"
        ]
    }
}


def validate_finetuning_data(dataset):
    """
    Validate fine-tuning dataset for security.
    """
    issues = []

    for i, example in enumerate(dataset):
        # Check for injection patterns
        if contains_injection_patterns(example["input"]):
            issues.append({
                "index": i,
                "type": "potential_injection",
                "field": "input"
            })

        if contains_injection_patterns(example["output"]):
            issues.append({
                "index": i,
                "type": "potential_injection",
                "field": "output"
            })

        # Check for harmful content
        if contains_harmful_content(example["output"]):
            issues.append({
                "index": i,
                "type": "harmful_content",
                "field": "output"
            })

    return issues


def contains_injection_patterns(text):
    """Check for injection patterns."""
    patterns = ["ignore instructions", "system:", "admin:"]
    return any(p in text.lower() for p in patterns)


def contains_harmful_content(text):
    """Check for harmful content."""
    # Would use content classifier in production
    return False
```

## Data Leakage

### Types of Data Leakage

```python
"""
Data leakage types in LLM systems.
"""

DATA_LEAKAGE_TYPES = {
    "training_data_extraction": {
        "description": "Extract training data from model outputs",
        "techniques": [
            "Prompt model to complete memorized sequences",
            "Query for specific sensitive information",
            "Extract via model completions"
        ],
        "risk": "PII, proprietary data, copyrighted content"
    },

    "system_prompt_leakage": {
        "description": "Extract system prompts and instructions",
        "techniques": [
            "Direct extraction requests",
            "Side-channel inference",
            "Completion attacks"
        ],
        "risk": "Business logic, competitive advantage, security through obscurity"
    },

    "context_leakage": {
        "description": "Leak information from conversation context",
        "techniques": [
            "Cross-session information retrieval",
            "RAG document extraction",
            "User data inference"
        ],
        "risk": "Privacy violations, data breaches"
    },

    "model_inversion": {
        "description": "Reconstruct training data from model",
        "techniques": [
            "Gradient-based reconstruction",
            "Query-based inference",
            "Membership inference"
        ],
        "risk": "Training data privacy"
    }
}
```

### Training Data Extraction

```python
"""
Understanding training data extraction attacks.
"""

EXTRACTION_TECHNIQUES = {
    "verbatim_memorization": {
        "description": "Model memorizes and reproduces exact sequences",
        "attack": "Prompt with partial sequence, model completes",
        "example": "If trained on email, might complete email addresses",
        "defense": [
            "Deduplication in training",
            "Differential privacy",
            "Output filtering"
        ]
    },

    "pattern_completion": {
        "description": "Model completes patterns from training",
        "attack": "Provide pattern start, infer training data",
        "example": "Start of phone number pattern → full number",
        "defense": [
            "PII detection in outputs",
            "Template sanitization",
            "Format restrictions"
        ]
    },

    "membership_inference": {
        "description": "Determine if specific data was in training",
        "attack": "Compare model confidence/behavior for known vs unknown data",
        "example": "Was this specific text in training set?",
        "defense": [
            "Differential privacy",
            "Output perturbation",
            "Confidence calibration"
        ]
    }
}


def check_memorization_risk(model, test_sequences):
    """
    Check if model memorizes specific sequences.

    Args:
        model: Model to test
        test_sequences: Sequences that might be memorized

    Returns:
        Risk assessment
    """
    results = []

    for seq in test_sequences:
        # Provide first 50% of sequence
        prompt = seq[:len(seq)//2]

        # Check if model completes with rest
        completion = model.generate(prompt, max_tokens=len(seq)//2)

        similarity = calculate_similarity(completion, seq[len(seq)//2:])

        if similarity > 0.9:
            results.append({
                "sequence": seq[:50] + "...",
                "memorization_score": similarity,
                "risk": "HIGH"
            })

    return results
```

### PII Protection

```python
"""
PII protection strategies.
"""

import re

class PIIProtector:
    """Detect and protect PII in inputs and outputs."""

    PII_PATTERNS = {
        "email": r'\b[\w.-]+@[\w.-]+\.\w{2,}\b',
        "phone_us": r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        "ssn": r'\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b',
        "credit_card": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
        "ip_address": r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    }

    def detect_pii(self, text):
        """Detect PII in text."""
        findings = []

        for pii_type, pattern in self.PII_PATTERNS.items():
            matches = re.findall(pattern, text)
            for match in matches:
                findings.append({
                    "type": pii_type,
                    "value": self.mask_value(match),
                    "position": text.find(match)
                })

        return findings

    def mask_value(self, value):
        """Mask PII value for logging."""
        if len(value) <= 4:
            return "****"
        return value[:2] + "*" * (len(value) - 4) + value[-2:]

    def redact_pii(self, text):
        """Redact PII from text."""
        result = text

        for pii_type, pattern in self.PII_PATTERNS.items():
            result = re.sub(pattern, f'[{pii_type.upper()}_REDACTED]', result)

        return result

    def protect_output(self, output, input_context=None):
        """Protect output from PII leakage."""
        # Redact detected PII
        protected = self.redact_pii(output)

        # Additional checks for context-specific PII
        if input_context:
            # Check if output contains information from input that shouldn't leak
            pass

        return protected
```

## Defense Strategies

### Data Validation Pipeline

```python
"""
Data validation for AI systems.
"""

class DataValidator:
    """Validate data for security."""

    def validate_training_data(self, dataset):
        """Validate training dataset."""
        issues = []

        for i, example in enumerate(dataset):
            # PII check
            pii_findings = PIIProtector().detect_pii(str(example))
            if pii_findings:
                issues.append({
                    "index": i,
                    "issue": "pii_detected",
                    "findings": pii_findings
                })

            # Injection pattern check
            if self.has_injection_patterns(str(example)):
                issues.append({
                    "index": i,
                    "issue": "injection_patterns"
                })

            # Anomaly check
            if self.is_anomalous(example):
                issues.append({
                    "index": i,
                    "issue": "anomalous_example"
                })

        return {
            "total_examples": len(dataset),
            "issues_found": len(issues),
            "details": issues
        }

    def has_injection_patterns(self, text):
        """Check for injection patterns."""
        patterns = [
            r'ignore\s+previous',
            r'system\s*:',
            r'\[admin\]',
        ]
        return any(re.search(p, text.lower()) for p in patterns)

    def is_anomalous(self, example):
        """Check if example is anomalous."""
        # Would use statistical analysis in production
        return False
```

## Best Practices

### Data Security Checklist

```python
"""
Data security best practices.
"""

DATA_SECURITY_CHECKLIST = {
    "data_collection": [
        "Verify data sources",
        "Implement data provenance tracking",
        "Scan for PII before collection",
        "Obtain proper consent"
    ],

    "data_storage": [
        "Encrypt data at rest",
        "Implement access controls",
        "Regular security audits",
        "Data retention policies"
    ],

    "data_processing": [
        "Validate all input data",
        "Sanitize before training",
        "Use differential privacy where possible",
        "Monitor for anomalies"
    ],

    "model_outputs": [
        "Filter PII from outputs",
        "Monitor for memorization",
        "Implement rate limiting",
        "Log and audit outputs"
    ]
}
```

## Next Steps

- [02-model-extraction.md](02-model-extraction.md) - Model stealing attacks
- [03-adversarial-attacks.md](03-adversarial-attacks.md) - Adversarial examples
- [../05-defense-strategies/](../05-defense-strategies/) - Defense implementation
