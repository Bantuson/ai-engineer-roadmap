#!/usr/bin/env python3
"""
OpenAI SDK Helpdesk Evaluation Script

Evaluates the helpdesk routing mini-project on:
1. Routing Accuracy - Is query routed to correct department?
2. Response Relevance - Does response address the query?
3. Tone Appropriateness - Is tone professional and helpful?
4. Handoff Quality - Are handoffs smooth and informative?

Usage:
    python eval_openai_helpdesk.py
    python eval_openai_helpdesk.py --test-file custom_tests.json
    python eval_openai_helpdesk.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import keyword_coverage, exact_match
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_openai_helpdesk.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"query": "I can't log into my account", "user_id": "user_001"},
        "expected": {"department": "technical", "keywords": ["password", "login", "account", "reset"]}
    },
    {
        "input": {"query": "I want a refund for my purchase", "user_id": "user_002"},
        "expected": {"department": "billing", "keywords": ["refund", "process", "purchase"]}
    },
    {
        "input": {"query": "How do I upgrade my subscription?", "user_id": "user_003"},
        "expected": {"department": "sales", "keywords": ["upgrade", "plan", "subscription"]}
    },
    {
        "input": {"query": "Your app keeps crashing on my phone", "user_id": "user_004"},
        "expected": {"department": "technical", "keywords": ["app", "crash", "fix", "update"]}
    },
    {
        "input": {"query": "I have a complaint about customer service", "user_id": "user_005"},
        "expected": {"department": "support", "keywords": ["sorry", "feedback", "improve"]}
    },
    {
        "input": {"query": "What are your business hours?", "user_id": "user_006"},
        "expected": {"department": "general", "keywords": ["hours", "available", "support"]}
    },
    # Edge cases
    {
        "input": {"query": "", "user_id": "user_007"},
        "expected": {"handles_empty": True, "department": "general"}
    },
    {
        "input": {"query": "asdfghjkl random text", "user_id": "user_008"},
        "expected": {"handles_unclear": True, "department": "general"}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_helpdesk(input_data: Dict) -> Dict[str, Any]:
    """
    Run the OpenAI SDK Helpdesk mini-project.

    Replace with actual import when mini-project is available.
    """
    query = input_data.get("query", "").lower()
    user_id = input_data.get("user_id", "unknown")

    # Mock routing logic
    if not query:
        department = "general"
        response = "Hello! How can I help you today?"
    elif any(w in query for w in ["login", "password", "account", "crash", "error", "bug"]):
        department = "technical"
        response = "I understand you're having a technical issue. Let me help you troubleshoot. Have you tried resetting your password?"
    elif any(w in query for w in ["refund", "charge", "payment", "bill"]):
        department = "billing"
        response = "I can help with your billing inquiry. Let me look up your account and process your refund request."
    elif any(w in query for w in ["upgrade", "plan", "pricing", "subscribe"]):
        department = "sales"
        response = "I'd be happy to help you explore our upgrade options. We have several plans available."
    elif any(w in query for w in ["complaint", "unhappy", "frustrated"]):
        department = "support"
        response = "I'm sorry to hear about your experience. Your feedback is important to us and we want to improve."
    else:
        department = "general"
        response = "Thank you for contacting us. I'm here to help with any questions you have."

    return {
        "response": response,
        "department": department,
        "user_id": user_id,
        "handoff_occurred": department != "general",
        "agents_involved": ["router", department + "_specialist"] if department != "general" else ["router"]
    }


def metric_routing_accuracy(routed_dept: str, expected_dept: str) -> float:
    """Check if routing is correct."""
    if not expected_dept:
        return 1.0
    return 1.0 if routed_dept.lower() == expected_dept.lower() else 0.0


def metric_response_relevance(response: str, keywords: List[str]) -> float:
    """Check if response contains relevant keywords."""
    if not keywords:
        return 1.0
    return keyword_coverage(response, keywords)


def metric_tone_quality(response: str) -> float:
    """Evaluate response tone."""
    if not response:
        return 0.0

    positive_indicators = ["help", "happy", "glad", "sorry", "understand", "thank", "please"]
    negative_indicators = ["can't", "won't", "refuse", "impossible"]

    response_lower = response.lower()

    positive_count = sum(1 for w in positive_indicators if w in response_lower)
    negative_count = sum(1 for w in negative_indicators if w in response_lower)

    # Good tone: has positive indicators, few negative
    if positive_count >= 2 and negative_count == 0:
        return 1.0
    elif positive_count >= 1:
        return 0.8
    elif negative_count == 0:
        return 0.6
    else:
        return 0.4


def metric_response_completeness(response: str, query: str) -> float:
    """Check if response is complete and substantial."""
    if not query:
        return 1.0 if response else 0.5

    if not response:
        return 0.0

    # Should have reasonable length
    if len(response) < 20:
        return 0.4
    elif len(response) < 50:
        return 0.7
    else:
        return 1.0


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_helpdesk(input_data)

    scores = {
        "routing_accuracy": metric_routing_accuracy(
            output.get("department", ""), expected.get("department", "")
        ),
        "response_relevance": metric_response_relevance(
            output.get("response", ""), expected.get("keywords", [])
        ),
        "tone_quality": metric_tone_quality(output.get("response", "")),
        "response_completeness": metric_response_completeness(
            output.get("response", ""), input_data.get("query", "")
        ),
    }

    # Routing is critical
    passed = scores["routing_accuracy"] == 1.0 and sum(s >= 0.6 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"helpdesk_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"department": output.get("department")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            query_preview = test_case['input'].get('query', '')[:40]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{query_preview}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            dept = result.output.get("department", "unknown")
            print(f"  {status} - routed to: {dept}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate OpenAI SDK Helpdesk")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_openai_helpdesk.json")
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
        name="OpenAI SDK Helpdesk Evaluation",
        results=results,
        metrics=["routing_accuracy", "response_relevance", "tone_quality", "response_completeness"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "04_openai_sdk_helpdesk"}
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
