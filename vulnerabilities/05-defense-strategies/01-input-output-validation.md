# Input and Output Validation

## Overview

Comprehensive validation at input and output boundaries is the first line of defense for LLM systems.

## Input Validation Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Input Validation Pipeline                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Raw Input                                                      │
│       │                                                          │
│       ▼                                                          │
│   ┌─────────────────┐                                           │
│   │ Format Check    │ → Length, encoding, structure              │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   ┌─────────────────┐                                           │
│   │ Sanitization    │ → Remove dangerous chars, normalize        │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   ┌─────────────────┐                                           │
│   │ Content Filter  │ → Blocklist, pattern matching              │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   ┌─────────────────┐                                           │
│   │ Intent Analysis │ → ML-based threat detection                │
│   └────────┬────────┘                                           │
│            │                                                     │
│            ▼                                                     │
│   Validated Input → LLM                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Input Validation Implementation

### Format Validation

```python
"""
Input format validation.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import re

@dataclass
class ValidationConfig:
    """Configuration for input validation."""
    max_length: int = 10000
    min_length: int = 1
    allowed_characters: str = r'[\w\s\.,!?\'"-:;()\[\]{}@#$%^&*+=<>/\\]'
    max_lines: int = 100
    allowed_encodings: List[str] = None

    def __post_init__(self):
        if self.allowed_encodings is None:
            self.allowed_encodings = ['utf-8', 'ascii']


class InputValidator:
    """Validate input format and content."""

    def __init__(self, config: ValidationConfig = None):
        self.config = config or ValidationConfig()

    def validate(self, text: str) -> Dict[str, Any]:
        """
        Validate input text.

        Returns:
            Validation result with status and issues
        """
        issues = []

        # Length check
        if len(text) > self.config.max_length:
            issues.append({
                "type": "length_exceeded",
                "value": len(text),
                "limit": self.config.max_length
            })

        if len(text) < self.config.min_length:
            issues.append({
                "type": "too_short",
                "value": len(text),
                "minimum": self.config.min_length
            })

        # Line count
        lines = text.count('\n') + 1
        if lines > self.config.max_lines:
            issues.append({
                "type": "too_many_lines",
                "value": lines,
                "limit": self.config.max_lines
            })

        # Character validation
        invalid_chars = re.findall(f'[^{self.config.allowed_characters[1:-1]}]', text)
        if invalid_chars:
            issues.append({
                "type": "invalid_characters",
                "characters": list(set(invalid_chars))[:10]
            })

        # Encoding check
        encoding_valid = self._check_encoding(text)
        if not encoding_valid:
            issues.append({"type": "encoding_issue"})

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "text_length": len(text),
            "line_count": lines
        }

    def _check_encoding(self, text: str) -> bool:
        """Check text encoding validity."""
        try:
            text.encode('utf-8').decode('utf-8')
            return True
        except:
            return False
```

### Content Sanitization

```python
"""
Content sanitization utilities.
"""

import unicodedata
import re

class InputSanitizer:
    """Sanitize input content."""

    def __init__(self):
        self.invisible_categories = {'Cf', 'Cc', 'Co', 'Cn'}

    def sanitize(self, text: str) -> str:
        """
        Sanitize text for safe processing.

        Args:
            text: Raw input text

        Returns:
            Sanitized text
        """
        # Remove invisible characters
        text = self._remove_invisible(text)

        # Normalize Unicode
        text = self._normalize_unicode(text)

        # Remove control characters (except newline, tab)
        text = self._remove_control_chars(text)

        # Normalize whitespace
        text = self._normalize_whitespace(text)

        # Remove potential injection delimiters
        text = self._neutralize_delimiters(text)

        return text

    def _remove_invisible(self, text: str) -> str:
        """Remove invisible Unicode characters."""
        return ''.join(
            c for c in text
            if unicodedata.category(c) not in self.invisible_categories
        )

    def _normalize_unicode(self, text: str) -> str:
        """Normalize Unicode to standard form."""
        # NFKC normalization
        text = unicodedata.normalize('NFKC', text)

        # Replace common homoglyphs
        homoglyphs = {
            '\u0430': 'a',  # Cyrillic а
            '\u0435': 'e',  # Cyrillic е
            '\u043e': 'o',  # Cyrillic о
            '\u0440': 'p',  # Cyrillic р
            '\u0441': 'c',  # Cyrillic с
            '\u0445': 'x',  # Cyrillic х
        }
        for cyrillic, latin in homoglyphs.items():
            text = text.replace(cyrillic, latin)

        return text

    def _remove_control_chars(self, text: str) -> str:
        """Remove control characters except newline and tab."""
        return ''.join(
            c for c in text
            if c in '\n\t' or unicodedata.category(c) != 'Cc'
        )

    def _normalize_whitespace(self, text: str) -> str:
        """Normalize whitespace."""
        # Replace multiple spaces with single
        text = re.sub(r' +', ' ', text)
        # Replace multiple newlines with double
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def _neutralize_delimiters(self, text: str) -> str:
        """Neutralize common injection delimiters."""
        # Add space to break up delimiter patterns
        patterns = [
            (r'---+', '- - -'),
            (r'```', '` ` `'),
            (r'\[\[', '[ ['),
            (r'\]\]', '] ]'),
        ]
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)
        return text
```

### Content Filtering

```python
"""
Content filtering for harmful patterns.
"""

class ContentFilter:
    """Filter content for harmful patterns."""

    def __init__(self):
        self.blocklist_patterns = self._load_blocklist()
        self.injection_patterns = self._load_injection_patterns()

    def _load_blocklist(self) -> List[str]:
        """Load blocklist patterns."""
        return [
            r'ignore\s+(all\s+)?(previous|above|prior)\s+instructions?',
            r'disregard\s+(your|all|previous)',
            r'you\s+are\s+now\s+',
            r'pretend\s+(to\s+be|you\s+are)',
            r'act\s+as\s+(if|a)',
            r'\[system\]',
            r'\[admin\]',
            r'</?(system|instructions|user)>',
        ]

    def _load_injection_patterns(self) -> List[str]:
        """Load injection detection patterns."""
        return [
            r'base64[\s:]+[A-Za-z0-9+/]+=*',
            r'decode\s+and\s+(execute|run)',
            r'reverse\s+this[\s:]+',
            r'rot13[\s:]+',
        ]

    def filter(self, text: str) -> Dict[str, Any]:
        """
        Filter text for harmful content.

        Returns:
            Filter result with detected patterns
        """
        detections = []

        # Check blocklist
        for pattern in self.blocklist_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                detections.append({
                    "type": "blocklist_match",
                    "pattern": pattern[:30] + "..."
                })

        # Check injection patterns
        for pattern in self.injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                detections.append({
                    "type": "injection_pattern",
                    "pattern": pattern[:30] + "..."
                })

        return {
            "passed": len(detections) == 0,
            "detections": detections,
            "risk_score": min(len(detections) * 0.3, 1.0)
        }
```

## Output Validation

### Output Filter Pipeline

```python
"""
Output validation and filtering.
"""

class OutputValidator:
    """Validate and filter LLM outputs."""

    def __init__(self):
        self.pii_detector = PIIDetector()
        self.content_classifier = ContentClassifier()
        self.consistency_checker = ConsistencyChecker()

    def validate(self, output: str, context: Dict = None) -> Dict[str, Any]:
        """
        Validate LLM output.

        Args:
            output: LLM response
            context: Original query context

        Returns:
            Validation result
        """
        issues = []
        modifications = []

        # PII check
        pii_result = self.pii_detector.detect(output)
        if pii_result["found"]:
            issues.append({"type": "pii_detected", "details": pii_result})
            output = self.pii_detector.redact(output)
            modifications.append("pii_redacted")

        # Content classification
        content_result = self.content_classifier.classify(output)
        if content_result["harmful"]:
            issues.append({"type": "harmful_content", "details": content_result})
            return {
                "valid": False,
                "blocked": True,
                "reason": "harmful_content",
                "original_output": "[BLOCKED]"
            }

        # Consistency with query
        if context:
            consistency_result = self.consistency_checker.check(output, context)
            if not consistency_result["consistent"]:
                issues.append({"type": "inconsistent", "details": consistency_result})

        return {
            "valid": len([i for i in issues if i["type"] != "pii_detected"]) == 0,
            "output": output,
            "issues": issues,
            "modifications": modifications
        }


class PIIDetector:
    """Detect PII in text."""

    PATTERNS = {
        "email": r'\b[\w.-]+@[\w.-]+\.\w{2,}\b',
        "phone": r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        "ssn": r'\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b',
        "credit_card": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
    }

    def detect(self, text: str) -> Dict[str, Any]:
        """Detect PII in text."""
        findings = []
        for pii_type, pattern in self.PATTERNS.items():
            matches = re.findall(pattern, text)
            if matches:
                findings.append({
                    "type": pii_type,
                    "count": len(matches)
                })

        return {
            "found": len(findings) > 0,
            "findings": findings
        }

    def redact(self, text: str) -> str:
        """Redact PII from text."""
        for pii_type, pattern in self.PATTERNS.items():
            text = re.sub(pattern, f'[{pii_type.upper()}_REDACTED]', text)
        return text


class ContentClassifier:
    """Classify content for harmful categories."""

    HARMFUL_INDICATORS = [
        "instructions for creating weapons",
        "how to hack",
        "exploit vulnerability",
        "bypass security",
    ]

    def classify(self, text: str) -> Dict[str, Any]:
        """Classify content."""
        text_lower = text.lower()

        harmful_detected = any(
            indicator in text_lower
            for indicator in self.HARMFUL_INDICATORS
        )

        return {
            "harmful": harmful_detected,
            "confidence": 0.8 if harmful_detected else 0.1
        }
```

## Integrated Validation Pipeline

```python
"""
Complete input/output validation pipeline.
"""

class ValidationPipeline:
    """Complete validation pipeline."""

    def __init__(self):
        self.input_validator = InputValidator()
        self.sanitizer = InputSanitizer()
        self.content_filter = ContentFilter()
        self.output_validator = OutputValidator()

    def validate_input(self, text: str) -> Dict[str, Any]:
        """Run full input validation."""
        # Format validation
        format_result = self.input_validator.validate(text)
        if not format_result["valid"]:
            return {
                "valid": False,
                "stage": "format",
                "issues": format_result["issues"]
            }

        # Sanitization
        sanitized = self.sanitizer.sanitize(text)

        # Content filtering
        filter_result = self.content_filter.filter(sanitized)
        if not filter_result["passed"]:
            return {
                "valid": False,
                "stage": "content_filter",
                "detections": filter_result["detections"],
                "risk_score": filter_result["risk_score"]
            }

        return {
            "valid": True,
            "sanitized_input": sanitized,
            "risk_score": filter_result["risk_score"]
        }

    def validate_output(self, output: str, context: Dict = None) -> Dict[str, Any]:
        """Run full output validation."""
        return self.output_validator.validate(output, context)

    def process(self, input_text: str) -> Dict[str, Any]:
        """
        Process input through validation, generate output, validate output.

        This is the complete validation flow.
        """
        # Validate input
        input_result = self.validate_input(input_text)
        if not input_result["valid"]:
            return {
                "success": False,
                "stage": "input_validation",
                "error": input_result
            }

        # Generate response (would call LLM here)
        # output = llm.generate(input_result["sanitized_input"])
        output = "Mock LLM response"

        # Validate output
        output_result = self.validate_output(output, {"query": input_text})
        if not output_result["valid"]:
            return {
                "success": False,
                "stage": "output_validation",
                "error": output_result
            }

        return {
            "success": True,
            "output": output_result["output"]
        }
```

## Best Practices

1. **Validate early, validate often** - Check at every boundary
2. **Fail safely** - Reject suspicious input rather than process
3. **Log everything** - Record validation failures for analysis
4. **Update regularly** - Keep blocklists and patterns current
5. **Defense in depth** - Multiple validation layers

## Next Steps

- [02-rate-limiting-monitoring.md](02-rate-limiting-monitoring.md) - Rate limiting and monitoring
- [mini-project-secure-agent/](mini-project-secure-agent/) - Hands-on implementation
- [../06-ai-red-teaming/](../06-ai-red-teaming/) - Testing your defenses
