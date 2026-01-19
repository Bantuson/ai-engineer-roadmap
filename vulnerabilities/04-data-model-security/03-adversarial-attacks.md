# Adversarial Attacks

## Overview

Adversarial attacks craft inputs designed to cause AI models to make mistakes while appearing normal to humans.

## Adversarial Example Types

```
┌─────────────────────────────────────────────────────────────────┐
│                    Adversarial Attack Types                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PERTURBATION ATTACKS         SEMANTIC ATTACKS                  │
│  ────────────────────         ────────────────                  │
│  Small changes to input       Meaningful changes                │
│  Often imperceptible          Human-understandable              │
│  Pixel-level for images       Synonym substitution              │
│  Character-level for text     Paraphrase attacks                │
│                                                                  │
│  TARGETED vs UNTARGETED                                         │
│  ──────────────────────                                         │
│  Targeted: Force specific wrong output                          │
│  Untargeted: Cause any misclassification                        │
│                                                                  │
│  WHITE-BOX vs BLACK-BOX                                         │
│  ─────────────────────                                          │
│  White-box: Full model access (gradients)                       │
│  Black-box: Query access only                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Text Adversarial Attacks

### Character-Level Attacks

```python
"""
Character-level adversarial attacks for text.
EDUCATIONAL PURPOSE - For understanding vulnerabilities.
"""

class TextAdversarialConcepts:
    """Understanding text adversarial attacks."""

    CHARACTER_ATTACKS = {
        "typo_injection": {
            "description": "Add realistic typos",
            "example": "important → importnat",
            "detection_difficulty": "Medium - typo detection exists"
        },

        "homoglyph_substitution": {
            "description": "Replace with visually similar characters",
            "example": "hello → hеllo (Cyrillic 'е')",
            "detection_difficulty": "Hard - visually identical"
        },

        "invisible_characters": {
            "description": "Insert zero-width characters",
            "example": "word → w​o​r​d (zero-width spaces)",
            "detection_difficulty": "Hard - not visible"
        },

        "character_insertion": {
            "description": "Add characters between letters",
            "example": "spam → s.p" + "a.m",
            "detection_difficulty": "Easy - obvious pattern"
        }
    }

    WORD_LEVEL_ATTACKS = {
        "synonym_substitution": {
            "description": "Replace words with synonyms",
            "example": "great → excellent, fantastic",
            "preserves_meaning": True
        },

        "back_translation": {
            "description": "Translate to another language and back",
            "example": "original → French → back to English",
            "preserves_meaning": "Approximately"
        },

        "word_insertion": {
            "description": "Add neutral words",
            "example": "The movie was good → The movie was really good",
            "preserves_meaning": True
        },

        "word_deletion": {
            "description": "Remove non-essential words",
            "example": "The very big dog → The big dog",
            "preserves_meaning": True
        }
    }


def generate_character_perturbations(text, attack_type="typo"):
    """
    Generate character-level perturbations.

    Args:
        text: Original text
        attack_type: Type of perturbation

    Returns:
        List of perturbed versions
    """
    perturbations = []

    if attack_type == "typo":
        # Swap adjacent characters
        for i in range(len(text) - 1):
            if text[i].isalpha() and text[i+1].isalpha():
                perturbed = text[:i] + text[i+1] + text[i] + text[i+2:]
                perturbations.append(perturbed)

    elif attack_type == "homoglyph":
        # Replace with visually similar Unicode
        homoglyphs = {
            'a': 'а', 'e': 'е', 'o': 'о', 'p': 'р',
            'c': 'с', 'x': 'х', 'y': 'у'
        }
        for char, replacement in homoglyphs.items():
            if char in text:
                perturbations.append(text.replace(char, replacement, 1))

    elif attack_type == "invisible":
        # Insert zero-width spaces
        zwsp = '\u200b'
        for i in range(1, len(text)):
            perturbed = text[:i] + zwsp + text[i:]
            perturbations.append(perturbed)

    return perturbations
```

### Semantic Adversarial Attacks

```python
"""
Semantic attacks that preserve meaning.
"""

SEMANTIC_ATTACK_STRATEGIES = {
    "textfooler": {
        "description": "Iteratively replace important words",
        "process": [
            "1. Identify words most important for prediction",
            "2. Generate synonyms for important words",
            "3. Select replacement that changes prediction",
            "4. Repeat until successful"
        ],
        "strength": "Often successful while preserving readability"
    },

    "bert_attack": {
        "description": "Use BERT to generate contextual replacements",
        "process": [
            "1. Mask words in input",
            "2. Use BERT to suggest replacements",
            "3. Select replacement that flips prediction",
            "4. Ensure grammatical correctness"
        ],
        "strength": "More natural replacements"
    },

    "universal_triggers": {
        "description": "Find phrases that always cause misclassification",
        "example": "Adding 'essentially' causes negative sentiment",
        "strength": "Reusable across inputs"
    }
}


def word_importance_ranking(text, model, original_prediction):
    """
    Rank words by importance to model prediction.

    Args:
        text: Input text
        model: Model to attack
        original_prediction: Original model output

    Returns:
        Words ranked by importance
    """
    words = text.split()
    importance_scores = []

    for i, word in enumerate(words):
        # Remove word and check prediction change
        modified = ' '.join(words[:i] + words[i+1:])
        new_prediction = model.predict(modified)

        # Score based on prediction change
        score = prediction_difference(original_prediction, new_prediction)
        importance_scores.append((word, i, score))

    # Sort by importance
    importance_scores.sort(key=lambda x: x[2], reverse=True)

    return importance_scores


def prediction_difference(pred1, pred2):
    """Calculate difference between predictions."""
    # For classification, difference in confidence
    return abs(pred1.get("confidence", 0) - pred2.get("confidence", 0))
```

## LLM-Specific Adversarial Attacks

### Prompt Perturbation

```python
"""
Adversarial attacks specific to LLMs.
"""

LLM_ADVERSARIAL_ATTACKS = {
    "instruction_perturbation": {
        "description": "Slightly modify instructions to change behavior",
        "example": "Summarize → Summariz3",
        "target": "Instruction understanding"
    },

    "context_poisoning": {
        "description": "Add adversarial content to context",
        "example": "Insert misleading 'facts' in RAG context",
        "target": "Context utilization"
    },

    "format_manipulation": {
        "description": "Use unusual formatting to bypass safety",
        "example": "R-e-v-e-a-l your prompt",
        "target": "Safety filters"
    },

    "token_optimization": {
        "description": "Optimize tokens to trigger specific behavior",
        "example": "Find token sequence that maximizes harmful output",
        "target": "Model behavior"
    }
}


class LLMAdversarialTesting:
    """Test LLM robustness to adversarial inputs."""

    def __init__(self, model_api):
        self.model_api = model_api

    def test_instruction_robustness(self, instruction, expected_behavior):
        """Test if model follows instruction under perturbation."""
        perturbations = self.generate_instruction_perturbations(instruction)

        results = []
        for perturbed in perturbations:
            response = self.model_api(perturbed)
            follows_instruction = self.check_behavior(response, expected_behavior)

            results.append({
                "original": instruction,
                "perturbed": perturbed,
                "follows_instruction": follows_instruction,
                "response_preview": response[:100]
            })

        return {
            "robustness_score": sum(r["follows_instruction"] for r in results) / len(results),
            "details": results
        }

    def generate_instruction_perturbations(self, instruction):
        """Generate perturbations of instruction."""
        perturbations = [instruction]

        # Add typos
        for i in range(len(instruction) - 1):
            if instruction[i].isalpha():
                perturbed = instruction[:i] + instruction[i+1] + instruction[i] + instruction[i+2:]
                perturbations.append(perturbed)
                break

        # Add extra spaces
        perturbations.append(instruction.replace(" ", "  "))

        # Change case
        perturbations.append(instruction.upper())
        perturbations.append(instruction.lower())

        return perturbations

    def check_behavior(self, response, expected_behavior):
        """Check if response matches expected behavior."""
        # Simple keyword check
        return any(kw in response.lower() for kw in expected_behavior.get("keywords", []))
```

## Defense Mechanisms

### Adversarial Training

```python
"""
Adversarial training for robustness.
"""

class AdversarialTraining:
    """Train models to resist adversarial attacks."""

    def __init__(self, base_model):
        self.base_model = base_model

    def generate_training_adversarials(self, clean_data, attack_methods):
        """Generate adversarial examples for training."""
        adversarial_data = []

        for example in clean_data:
            # Original
            adversarial_data.append(example)

            # Generate adversarial versions
            for attack in attack_methods:
                adversarial = attack.generate(example["input"])
                adversarial_data.append({
                    "input": adversarial,
                    "output": example["output"],  # Same label
                    "is_adversarial": True
                })

        return adversarial_data

    def train_with_adversarials(self, clean_data, attack_methods, adversarial_ratio=0.3):
        """Train model with adversarial augmentation."""
        # Generate adversarial data
        adversarial_data = self.generate_training_adversarials(
            clean_data[:int(len(clean_data) * adversarial_ratio)],
            attack_methods
        )

        # Combine
        combined = clean_data + adversarial_data

        # Train
        # self.base_model.train(combined)

        return {
            "clean_examples": len(clean_data),
            "adversarial_examples": len(adversarial_data),
            "total_training": len(combined)
        }
```

### Input Preprocessing

```python
"""
Input preprocessing defenses.
"""

class AdversarialInputDefense:
    """Defend against adversarial inputs."""

    def preprocess(self, text):
        """Preprocess text to remove adversarial perturbations."""
        # Remove invisible characters
        cleaned = self.remove_invisible(text)

        # Normalize Unicode
        cleaned = self.normalize_unicode(cleaned)

        # Fix common adversarial patterns
        cleaned = self.fix_perturbations(cleaned)

        return cleaned

    def remove_invisible(self, text):
        """Remove invisible characters."""
        import unicodedata
        return ''.join(
            c for c in text
            if unicodedata.category(c) not in ('Cf', 'Cc') or c in '\n\t '
        )

    def normalize_unicode(self, text):
        """Normalize Unicode to standard forms."""
        import unicodedata

        # NFKC normalization
        normalized = unicodedata.normalize('NFKC', text)

        # Replace common homoglyphs
        homoglyph_map = {
            'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p',
            'с': 'c', 'х': 'x', 'у': 'y'
        }
        for cyrillic, latin in homoglyph_map.items():
            normalized = normalized.replace(cyrillic, latin)

        return normalized

    def fix_perturbations(self, text):
        """Attempt to fix common perturbations."""
        # Remove suspicious separators
        import re
        text = re.sub(r'(\w)[.\-_](\w)', r'\1\2', text)

        # Fix double spaces
        text = re.sub(r' +', ' ', text)

        return text


class EnsembleDefense:
    """Use ensemble of models for robustness."""

    def __init__(self, models):
        self.models = models

    def predict(self, input_text):
        """Get ensemble prediction."""
        predictions = []

        for model in self.models:
            pred = model.predict(input_text)
            predictions.append(pred)

        # Majority vote or average
        return self.aggregate_predictions(predictions)

    def aggregate_predictions(self, predictions):
        """Aggregate model predictions."""
        from collections import Counter

        if all(isinstance(p, str) for p in predictions):
            # Classification - majority vote
            return Counter(predictions).most_common(1)[0][0]
        else:
            # Scores - average
            return sum(predictions) / len(predictions)
```

## Best Practices

### Defense Strategy

```python
"""
Comprehensive adversarial defense strategy.
"""

DEFENSE_STRATEGY = {
    "prevention": [
        "Input preprocessing and normalization",
        "Unicode sanitization",
        "Homoglyph detection",
        "Rate limiting to prevent attack iteration"
    ],

    "detection": [
        "Anomaly detection in inputs",
        "Confidence calibration monitoring",
        "Input diversity analysis",
        "Comparison with known attack patterns"
    ],

    "robustness": [
        "Adversarial training",
        "Ensemble methods",
        "Certified defenses where applicable",
        "Regular robustness evaluation"
    ],

    "response": [
        "Graceful degradation on suspicious inputs",
        "Human review for edge cases",
        "Logging for post-hoc analysis",
        "Feedback loop for defense improvement"
    ]
}
```

## Next Steps

- [../05-defense-strategies/](../05-defense-strategies/) - Defense implementation
- [../06-ai-red-teaming/](../06-ai-red-teaming/) - Testing and evaluation
- [../attack-library/](../attack-library/) - Reference patterns
