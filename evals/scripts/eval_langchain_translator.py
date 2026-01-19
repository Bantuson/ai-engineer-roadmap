#!/usr/bin/env python3
"""
LangChain Translator Evaluation Script

Evaluates the translation mini-project on:
1. Translation Accuracy - Is meaning preserved?
2. Fluency - Is output natural in target language?
3. Completeness - Is all content translated?
4. Language Detection - Is source language detected correctly?

Usage:
    python eval_langchain_translator.py
    python eval_langchain_translator.py --test-file custom_tests.json
    python eval_langchain_translator.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import bleu_score, f1_score_text
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_langchain_translator.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"text": "Hello, how are you?", "source_lang": "en", "target_lang": "es"},
        "expected": {"translation_contains": ["hola", "cmo", "ests"], "detected_lang": "en"}
    },
    {
        "input": {"text": "The weather is nice today", "source_lang": "en", "target_lang": "fr"},
        "expected": {"translation_contains": ["temps", "beau", "aujourd"], "detected_lang": "en"}
    },
    {
        "input": {"text": "I love programming", "source_lang": "en", "target_lang": "de"},
        "expected": {"translation_contains": ["liebe", "programmier"], "detected_lang": "en"}
    },
    {
        "input": {"text": "Bonjour le monde", "source_lang": "fr", "target_lang": "en"},
        "expected": {"translation_contains": ["hello", "world"], "detected_lang": "fr"}
    },
    {
        "input": {"text": "Guten Morgen", "source_lang": "de", "target_lang": "en"},
        "expected": {"translation_contains": ["good", "morning"], "detected_lang": "de"}
    },
    # Edge cases
    {
        "input": {"text": "", "source_lang": "en", "target_lang": "es"},
        "expected": {"handles_empty": True}
    },
    {
        "input": {"text": "Hello", "source_lang": "auto", "target_lang": "es"},
        "expected": {"auto_detect": True, "detected_lang": "en"}
    },
    {
        "input": {"text": "123 456", "source_lang": "en", "target_lang": "es"},
        "expected": {"preserves_numbers": True}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_translator(input_data: Dict) -> Dict[str, Any]:
    """
    Run the LangChain Translator mini-project.

    Replace with actual import when mini-project is available.
    """
    text = input_data.get("text", "")
    source_lang = input_data.get("source_lang", "auto")
    target_lang = input_data.get("target_lang", "en")

    # Mock translation
    translations = {
        ("en", "es"): {"Hello, how are you?": "Hola, cmo ests?",
                       "The weather is nice today": "El tiempo est bien hoy",
                       "I love programming": "Me encanta programar"},
        ("en", "fr"): {"The weather is nice today": "Le temps est beau aujourd'hui"},
        ("en", "de"): {"I love programming": "Ich liebe Programmieren"},
        ("fr", "en"): {"Bonjour le monde": "Hello world"},
        ("de", "en"): {"Guten Morgen": "Good morning"},
    }

    key = (source_lang if source_lang != "auto" else "en", target_lang)
    translation = translations.get(key, {}).get(text, f"[Translated: {text}]")

    if not text:
        translation = ""

    # Detect language (mock)
    detected = source_lang if source_lang != "auto" else "en"

    return {
        "original": text,
        "translation": translation,
        "source_language": detected,
        "target_language": target_lang,
        "chain_steps": ["detect", "translate", "validate"]
    }


def metric_translation_coverage(translation: str, expected_words: List[str]) -> float:
    """Check if translation contains expected words."""
    if not expected_words:
        return 1.0

    translation_lower = translation.lower()
    found = sum(1 for w in expected_words if w.lower() in translation_lower)
    return found / len(expected_words)


def metric_completeness(original: str, translation: str) -> float:
    """Check translation completeness."""
    if not original:
        return 1.0 if not translation else 0.5

    if not translation:
        return 0.0

    # Word count ratio
    orig_words = len(original.split())
    trans_words = len(translation.split())

    if orig_words == 0:
        return 1.0

    ratio = trans_words / orig_words
    # Translations should be similar length (0.5x to 2x)
    if 0.5 <= ratio <= 2.0:
        return 1.0
    elif 0.3 <= ratio <= 3.0:
        return 0.7
    else:
        return 0.4


def metric_language_detection(detected: str, expected: str) -> float:
    """Check language detection accuracy."""
    if not expected:
        return 1.0
    return 1.0 if detected.lower() == expected.lower() else 0.0


def metric_number_preservation(original: str, translation: str) -> float:
    """Check if numbers are preserved."""
    import re
    orig_numbers = set(re.findall(r'\d+', original))
    trans_numbers = set(re.findall(r'\d+', translation))

    if not orig_numbers:
        return 1.0

    preserved = len(orig_numbers & trans_numbers)
    return preserved / len(orig_numbers)


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_translator(input_data)
    translation = output.get("translation", "")

    scores = {
        "translation_coverage": metric_translation_coverage(
            translation, expected.get("translation_contains", [])
        ),
        "completeness": metric_completeness(
            input_data.get("text", ""), translation
        ),
        "language_detection": metric_language_detection(
            output.get("source_language", ""), expected.get("detected_lang", "")
        ),
        "number_preservation": metric_number_preservation(
            input_data.get("text", ""), translation
        ),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.7 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"trans_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={
            "source": input_data.get("source_lang"),
            "target": input_data.get("target_lang")
        }
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            text_preview = test_case['input'].get('text', '')[:30]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{text_preview}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - coverage: {result.scores['translation_coverage']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate LangChain Translator")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_langchain_translator.json")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    config = EvalConfig(
        test_file=args.test_file,
        output_file=args.output,
        verbose=args.verbose,
        report=args.report
    )

    test_cases = load_test_cases(config.test_file)
    print(f"Loaded {len(test_cases)} test cases")

    results = evaluate_all(test_cases, config)

    report = generate_report(
        name="LangChain Translator Evaluation",
        results=results,
        metrics=["translation_coverage", "completeness", "language_detection", "number_preservation"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "03_langchain_translator"}
    )

    if config.report:
        print(format_text_report(report))

    os.makedirs(os.path.dirname(config.output_file) or ".", exist_ok=True)
    save_report(report, config.output_file)
    print(f"\nResults saved to: {config.output_file}")

    print(f"\nPass Rate: {report.summary['pass_rate']:.1%}")

    return 0 if report.summary["pass_rate"] >= 0.7 else 1


if __name__ == "__main__":
    sys.exit(main())
