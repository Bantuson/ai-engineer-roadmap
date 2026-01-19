#!/usr/bin/env python3
"""
Pydantic AI Calculator Evaluation Script

Evaluates the calculator mini-project on:
1. Calculation Accuracy - Are results correct?
2. Tool Selection - Is the right tool chosen?
3. Edge Case Handling - Does it handle errors gracefully?
4. Response Quality - Is the response helpful?

Usage:
    python eval_pydantic_calculator.py
    python eval_pydantic_calculator.py --test-file custom_tests.json
    python eval_pydantic_calculator.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

# Add shared modules to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import exact_match, calculate_quality_score
from reporters import TestResult, generate_report, format_text_report, save_report


# ============= Configuration =============

@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_pydantic_calculator.json"
    verbose: bool = False
    report: bool = True


# ============= Test Cases =============

DEFAULT_TEST_CASES = [
    # Basic operations
    {"input": "What is 5 + 3?", "expected": 8, "type": "addition"},
    {"input": "What is 10 - 4?", "expected": 6, "type": "subtraction"},
    {"input": "What is 7 times 6?", "expected": 42, "type": "multiplication"},
    {"input": "What is 20 divided by 4?", "expected": 5, "type": "division"},

    # More complex
    {"input": "Calculate 15 plus 27", "expected": 42, "type": "addition"},
    {"input": "What's 100 minus 37?", "expected": 63, "type": "subtraction"},
    {"input": "Multiply 12 by 8", "expected": 96, "type": "multiplication"},
    {"input": "Divide 144 by 12", "expected": 12, "type": "division"},

    # Decimals
    {"input": "What is 3.5 + 2.5?", "expected": 6.0, "type": "addition"},
    {"input": "Calculate 10.5 divided by 2", "expected": 5.25, "type": "division"},

    # Edge cases
    {"input": "What is 0 + 5?", "expected": 5, "type": "edge_zero"},
    {"input": "What is 10 divided by 0?", "expected": "error", "type": "edge_divzero"},
    {"input": "What is -5 + 10?", "expected": 5, "type": "edge_negative"},

    # Word problems
    {"input": "If I have 15 apples and give away 7, how many do I have?", "expected": 8, "type": "word_problem"},
    {"input": "A book costs $12. How much for 5 books?", "expected": 60, "type": "word_problem"},
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


# ============= Calculator Interface =============

def run_calculator(query: str) -> Dict[str, Any]:
    """
    Run the calculator mini-project.

    Replace this with actual import and execution of the mini-project.

    Args:
        query: User's math question

    Returns:
        Dict with 'response', 'result', 'tool_used', 'error'
    """
    # Placeholder - implement with actual mini-project
    # from agent_frameworks.mini_projects.pydantic_ai_calculator import main
    # return main.process_query(query)

    # Mock implementation for demonstration
    import re

    result = {
        "response": "",
        "result": None,
        "tool_used": None,
        "error": None
    }

    # Simple parsing for mock
    query_lower = query.lower()

    # Detect operation
    if "+" in query or "plus" in query_lower or "add" in query_lower:
        result["tool_used"] = "add"
    elif "-" in query or "minus" in query_lower or "subtract" in query_lower:
        result["tool_used"] = "subtract"
    elif "*" in query or "times" in query_lower or "multiply" in query_lower:
        result["tool_used"] = "multiply"
    elif "/" in query or "divided" in query_lower or "divide" in query_lower:
        result["tool_used"] = "divide"

    # Extract numbers
    numbers = re.findall(r'-?\d+\.?\d*', query)
    numbers = [float(n) for n in numbers]

    if len(numbers) >= 2:
        a, b = numbers[0], numbers[1]
        try:
            if result["tool_used"] == "add":
                result["result"] = a + b
            elif result["tool_used"] == "subtract":
                result["result"] = a - b
            elif result["tool_used"] == "multiply":
                result["result"] = a * b
            elif result["tool_used"] == "divide":
                if b == 0:
                    result["error"] = "Cannot divide by zero"
                else:
                    result["result"] = a / b
        except Exception as e:
            result["error"] = str(e)

    if result["result"] is not None:
        # Clean up float display
        if result["result"] == int(result["result"]):
            result["result"] = int(result["result"])
        result["response"] = f"The answer is {result['result']}"
    elif result["error"]:
        result["response"] = f"Error: {result['error']}"
    else:
        result["response"] = "I couldn't understand the calculation"

    return result


# ============= Evaluation Metrics =============

def metric_calculation_accuracy(result: Any, expected: Any) -> float:
    """Check if calculation result matches expected."""
    if expected == "error":
        return 1.0 if result is None else 0.0

    if result is None:
        return 0.0

    # Allow for floating point tolerance
    try:
        return 1.0 if abs(float(result) - float(expected)) < 0.01 else 0.0
    except (TypeError, ValueError):
        return 0.0


def metric_tool_selection(tool_used: str, test_type: str) -> float:
    """Check if appropriate tool was selected."""
    expected_tools = {
        "addition": "add",
        "subtraction": "subtract",
        "multiplication": "multiply",
        "division": "divide",
        "edge_zero": "add",
        "edge_divzero": "divide",
        "edge_negative": "add",
        "word_problem": None  # Any tool is fine
    }

    if test_type not in expected_tools:
        return 1.0  # Unknown type, don't penalize

    expected = expected_tools[test_type]
    if expected is None:
        return 1.0 if tool_used else 0.5

    return 1.0 if tool_used == expected else 0.0


def metric_error_handling(output: Dict, expected: Any) -> float:
    """Check if errors are handled gracefully."""
    if expected == "error":
        # Should have error and no result
        has_error = output.get("error") is not None
        no_result = output.get("result") is None
        has_message = len(output.get("response", "")) > 10
        return (has_error + no_result + has_message) / 3.0
    else:
        # Should have result and no error
        no_error = output.get("error") is None
        return 1.0 if no_error else 0.5


def metric_response_quality(response: str, expected: Any) -> float:
    """Check response quality."""
    if not response:
        return 0.0

    score = 0.0

    # Has some content
    if len(response) > 5:
        score += 0.3

    # Contains the answer (if not error)
    if expected != "error" and str(expected) in response:
        score += 0.5

    # Reasonable length (not too long)
    if len(response) < 200:
        score += 0.2

    return score


# ============= Evaluation Loop =============

def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    query = test_case["input"]
    expected = test_case["expected"]
    test_type = test_case.get("type", "unknown")

    # Run calculator
    output = run_calculator(query)

    # Calculate metrics
    scores = {
        "accuracy": metric_calculation_accuracy(output.get("result"), expected),
        "tool_selection": metric_tool_selection(output.get("tool_used"), test_type),
        "error_handling": metric_error_handling(output, expected),
        "response_quality": metric_response_quality(output.get("response", ""), expected),
    }

    # Overall pass: accuracy must be 1.0 for calculation tasks
    passed = scores["accuracy"] == 1.0

    return TestResult(
        test_id=f"{test_type}_{hash(query) % 10000:04d}",
        input_data={"query": query, "type": test_type},
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"test_type": test_type}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            print(f"Evaluating {i+1}/{len(test_cases)}: {test_case['input'][:40]}...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "✓" if result.passed else "✗"
            print(f"  {status} Accuracy: {result.scores['accuracy']:.2f}")

    return results


# ============= Main =============

def main():
    parser = argparse.ArgumentParser(description="Evaluate Pydantic AI Calculator")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_pydantic_calculator.json",
                        help="Output file path")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--report", action="store_true", help="Print report to console")
    args = parser.parse_args()

    config = EvalConfig(
        test_file=args.test_file,
        output_file=args.output,
        verbose=args.verbose,
        report=args.report
    )

    # Load test cases
    test_cases = load_test_cases(config.test_file)
    print(f"Loaded {len(test_cases)} test cases")

    # Run evaluation
    results = evaluate_all(test_cases, config)

    # Generate report
    report = generate_report(
        name="Pydantic AI Calculator Evaluation",
        results=results,
        metrics=["accuracy", "tool_selection", "error_handling", "response_quality"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "09_pydantic_ai_calculator"}
    )

    # Output
    if config.report:
        print(format_text_report(report))

    # Save
    os.makedirs(os.path.dirname(config.output_file) or ".", exist_ok=True)
    save_report(report, config.output_file)
    print(f"\nResults saved to: {config.output_file}")

    # Summary
    print(f"\n{'='*50}")
    print(f"Pass Rate: {report.summary['pass_rate']:.1%}")
    print(f"Mean Accuracy: {report.summary['metrics']['accuracy']['mean']:.3f}")

    # Return exit code based on pass rate
    return 0 if report.summary["pass_rate"] >= 0.8 else 1


if __name__ == "__main__":
    sys.exit(main())
