#!/usr/bin/env python3
"""
Product Management PRD Evaluation Script

Evaluates PRD quality on:
1. Completeness - Does PRD have all required sections?
2. Clarity - Are requirements clearly stated?
3. Measurability - Are success metrics defined?
4. Feasibility - Are technical requirements realistic?

Usage:
    python eval_pm_prd.py
    python eval_pm_prd.py --test-file custom_tests.json
    python eval_pm_prd.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import keyword_coverage
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_pm_prd.json"
    verbose: bool = False
    report: bool = True


REQUIRED_SECTIONS = [
    "problem statement",
    "user stories",
    "requirements",
    "success metrics",
    "timeline",
    "risks"
]


DEFAULT_TEST_CASES = [
    {
        "input": {
            "product": "Mobile banking app",
            "feature": "Bill payment feature",
            "target_users": "retail banking customers"
        },
        "expected": {
            "sections": REQUIRED_SECTIONS,
            "keywords": ["payment", "bill", "user", "secure"]
        }
    },
    {
        "input": {
            "product": "E-commerce platform",
            "feature": "Product recommendation engine",
            "target_users": "online shoppers"
        },
        "expected": {
            "sections": REQUIRED_SECTIONS,
            "keywords": ["recommendation", "product", "user", "personalize"]
        }
    },
    {
        "input": {
            "product": "Healthcare app",
            "feature": "Appointment scheduling",
            "target_users": "patients and healthcare providers"
        },
        "expected": {
            "sections": REQUIRED_SECTIONS,
            "keywords": ["appointment", "schedule", "patient", "provider"]
        }
    },
    {
        "input": {
            "product": "SaaS dashboard",
            "feature": "Analytics reporting",
            "target_users": "business analysts"
        },
        "expected": {
            "sections": REQUIRED_SECTIONS,
            "keywords": ["analytics", "report", "data", "dashboard"]
        }
    },
    # Edge cases
    {
        "input": {
            "product": "",
            "feature": "Generic feature",
            "target_users": ""
        },
        "expected": {"handles_incomplete": True}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def generate_prd(input_data: Dict) -> Dict[str, Any]:
    """
    Generate a PRD based on input.

    Replace with actual PRD generation when available.
    """
    product = input_data.get("product", "Product")
    feature = input_data.get("feature", "Feature")
    users = input_data.get("target_users", "users")

    prd = f"""
# Product Requirements Document: {feature}

## Problem Statement
{users} need a better way to {feature.lower()}. Currently, the process is manual and time-consuming, leading to poor user experience and lost opportunities.

## User Stories
- As a {users.split()[0] if users else 'user'}, I want to easily {feature.lower()} so that I can save time
- As a {users.split()[0] if users else 'user'}, I want to track my {feature.lower()} history so that I can review past actions
- As an admin, I want to monitor {feature.lower()} activity so that I can ensure compliance

## Requirements

### Functional Requirements
1. Users must be able to initiate {feature.lower()}
2. System must validate user input before processing
3. System must provide confirmation of successful completion
4. Users must be able to view history of past {feature.lower()}

### Non-Functional Requirements
1. Response time < 2 seconds for 95% of requests
2. System availability > 99.9%
3. Support for 10,000 concurrent users
4. Secure data transmission (HTTPS/TLS)

## Success Metrics
- User adoption rate: Target 60% within 3 months
- Task completion rate: Target > 95%
- User satisfaction score: Target > 4.0/5.0
- Support ticket reduction: Target 30% decrease

## Timeline
- Phase 1 (Month 1): Core functionality
- Phase 2 (Month 2): Enhanced features
- Phase 3 (Month 3): Analytics and optimization

## Risks and Mitigations
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Technical complexity | Medium | High | Phased rollout |
| User adoption | Medium | Medium | Training and support |
| Integration issues | Low | High | Early testing |

## Dependencies
- Backend API team
- Security review
- Legal compliance approval
"""

    return {
        "prd": prd,
        "sections_present": [
            "problem statement",
            "user stories",
            "requirements",
            "success metrics",
            "timeline",
            "risks"
        ],
        "word_count": len(prd.split()),
        "has_metrics": True,
        "has_timeline": True
    }


def metric_completeness(sections_present: List[str], required: List[str]) -> float:
    """Check if all required sections are present."""
    if not required:
        return 1.0

    present = sum(1 for s in required if any(s.lower() in sp.lower() for sp in sections_present))
    return present / len(required)


def metric_clarity(prd: str) -> float:
    """Evaluate clarity of requirements."""
    if not prd:
        return 0.0

    score = 0.0

    # Has clear structure (headers)
    if prd.count('#') >= 5:
        score += 0.3

    # Has numbered/bulleted lists
    if prd.count('1.') >= 2 or prd.count('-') >= 5:
        score += 0.3

    # Has specific language (must, shall, will)
    specifics = ["must", "shall", "will", "should"]
    if any(s in prd.lower() for s in specifics):
        score += 0.2

    # Reasonable length
    if len(prd.split()) > 200:
        score += 0.2

    return score


def metric_measurability(prd: str) -> float:
    """Check if metrics are measurable."""
    measurable_indicators = [
        r'\d+%',  # Percentages
        r'>\s*\d',  # Greater than numbers
        r'<\s*\d',  # Less than numbers
        r'\d+\s*(seconds|minutes|hours|days|months)',  # Time
        r'target',  # Target mentions
    ]

    import re
    score = 0

    for pattern in measurable_indicators:
        if re.search(pattern, prd.lower()):
            score += 0.2

    return min(score, 1.0)


def metric_content_relevance(prd: str, keywords: List[str]) -> float:
    """Check if content is relevant to the feature."""
    if not keywords:
        return 1.0

    return keyword_coverage(prd, keywords)


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = generate_prd(input_data)
    prd = output.get("prd", "")

    scores = {
        "completeness": metric_completeness(
            output.get("sections_present", []),
            expected.get("sections", REQUIRED_SECTIONS)
        ),
        "clarity": metric_clarity(prd),
        "measurability": metric_measurability(prd),
        "content_relevance": metric_content_relevance(prd, expected.get("keywords", [])),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.7 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"prd_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"feature": input_data.get("feature")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            feature = test_case['input'].get('feature', '')[:30]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{feature}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - completeness: {result.scores['completeness']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate PM PRD Quality")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_pm_prd.json")
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
        name="PM PRD Quality Evaluation",
        results=results,
        metrics=["completeness", "clarity", "measurability", "content_relevance"],
        config={"test_file": config.test_file},
        metadata={"course": "product-management"}
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
