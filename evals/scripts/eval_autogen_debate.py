#!/usr/bin/env python3
"""
AutoGen Debate Club Evaluation Script

Evaluates the multi-agent debate mini-project on:
1. Argument Quality - Are arguments logical and well-structured?
2. Counter-Argument Strength - Do responses address opposing points?
3. Debate Structure - Does debate follow proper format?
4. Topic Adherence - Do agents stay on topic?

Usage:
    python eval_autogen_debate.py
    python eval_autogen_debate.py --test-file custom_tests.json
    python eval_autogen_debate.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import keyword_coverage, f1_score_text
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_autogen_debate.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"topic": "Should AI be regulated?", "rounds": 2},
        "expected": {"keywords": ["ai", "regulation", "safety", "innovation"], "min_exchanges": 4}
    },
    {
        "input": {"topic": "Is remote work better than office work?", "rounds": 2},
        "expected": {"keywords": ["remote", "office", "productivity", "flexibility"], "min_exchanges": 4}
    },
    {
        "input": {"topic": "Should social media have age restrictions?", "rounds": 3},
        "expected": {"keywords": ["social media", "age", "children", "safety"], "min_exchanges": 6}
    },
    {
        "input": {"topic": "Is space exploration worth the cost?", "rounds": 2},
        "expected": {"keywords": ["space", "cost", "benefit", "science"], "min_exchanges": 4}
    },
    {
        "input": {"topic": "Should college education be free?", "rounds": 2},
        "expected": {"keywords": ["education", "free", "cost", "access"], "min_exchanges": 4}
    },
    # Edge cases
    {
        "input": {"topic": "", "rounds": 1},
        "expected": {"handles_empty": True}
    },
    {
        "input": {"topic": "Yes or no?", "rounds": 1},
        "expected": {"handles_vague": True, "min_exchanges": 2}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_debate_club(input_data: Dict) -> Dict[str, Any]:
    """
    Run the AutoGen Debate Club mini-project.

    Replace with actual import when mini-project is available.
    """
    topic = input_data.get("topic", "")
    rounds = input_data.get("rounds", 2)

    if not topic:
        return {
            "debate": [],
            "summary": "No topic provided for debate.",
            "winner": None,
            "rounds_completed": 0
        }

    # Mock debate generation
    exchanges = []

    for round_num in range(rounds):
        exchanges.append({
            "round": round_num + 1,
            "pro": {
                "agent": "ProDebater",
                "argument": f"In favor of the position on '{topic}': There are compelling reasons to support this view. First, it promotes progress and innovation. Second, it addresses important societal needs."
            },
            "con": {
                "agent": "ConDebater",
                "argument": f"Against the position on '{topic}': While there are merits to the opposing view, we must consider the drawbacks. The costs may outweigh benefits, and there are alternative approaches worth exploring."
            }
        })

    return {
        "debate": exchanges,
        "summary": f"The debate on '{topic}' concluded after {rounds} rounds with both sides presenting valid arguments.",
        "winner": "tie",
        "rounds_completed": rounds,
        "agents": ["ProDebater", "ConDebater", "Moderator"]
    }


def metric_argument_quality(debate: List[Dict]) -> float:
    """Evaluate quality of arguments."""
    if not debate:
        return 0.0

    score = 0
    quality_indicators = ["because", "therefore", "first", "second", "however", "while", "consider"]

    for exchange in debate:
        pro_arg = exchange.get("pro", {}).get("argument", "")
        con_arg = exchange.get("con", {}).get("argument", "")

        # Check for structure indicators
        pro_quality = sum(1 for w in quality_indicators if w in pro_arg.lower())
        con_quality = sum(1 for w in quality_indicators if w in con_arg.lower())

        # Reasonable length
        pro_length_ok = len(pro_arg) > 50
        con_length_ok = len(con_arg) > 50

        exchange_score = (
            min(pro_quality / 3, 1) * 0.25 +
            min(con_quality / 3, 1) * 0.25 +
            (0.25 if pro_length_ok else 0) +
            (0.25 if con_length_ok else 0)
        )
        score += exchange_score

    return score / len(debate)


def metric_counter_argument(debate: List[Dict]) -> float:
    """Check if arguments address opposing points."""
    if len(debate) < 2:
        return 0.5

    score = 0
    counter_indicators = ["however", "but", "while", "although", "contrary", "opposing"]

    for i, exchange in enumerate(debate[1:], 1):
        pro_arg = exchange.get("pro", {}).get("argument", "").lower()
        con_arg = exchange.get("con", {}).get("argument", "").lower()

        # Check for counter-argument indicators
        pro_counters = any(w in pro_arg for w in counter_indicators)
        con_counters = any(w in con_arg for w in counter_indicators)

        if pro_counters and con_counters:
            score += 1
        elif pro_counters or con_counters:
            score += 0.5

    return score / max(len(debate) - 1, 1)


def metric_debate_structure(output: Dict, expected_exchanges: int) -> float:
    """Check if debate follows proper structure."""
    debate = output.get("debate", [])
    rounds_completed = output.get("rounds_completed", 0)
    has_summary = bool(output.get("summary"))

    # Count exchanges (each round has pro and con)
    actual_exchanges = len(debate) * 2

    structure_score = 0

    # Has exchanges
    if actual_exchanges >= expected_exchanges:
        structure_score += 0.4
    elif actual_exchanges > 0:
        structure_score += 0.2

    # Has summary
    if has_summary:
        structure_score += 0.3

    # Has proper agents
    if output.get("agents"):
        structure_score += 0.3

    return structure_score


def metric_topic_adherence(debate: List[Dict], keywords: List[str]) -> float:
    """Check if debate stays on topic."""
    if not debate or not keywords:
        return 1.0

    all_text = ""
    for exchange in debate:
        all_text += exchange.get("pro", {}).get("argument", "") + " "
        all_text += exchange.get("con", {}).get("argument", "") + " "

    return keyword_coverage(all_text, keywords)


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_debate_club(input_data)

    scores = {
        "argument_quality": metric_argument_quality(output.get("debate", [])),
        "counter_argument": metric_counter_argument(output.get("debate", [])),
        "debate_structure": metric_debate_structure(output, expected.get("min_exchanges", 4)),
        "topic_adherence": metric_topic_adherence(output.get("debate", []), expected.get("keywords", [])),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.6 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"debate_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"topic": input_data.get("topic")[:30] if input_data.get("topic") else "empty"}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            topic_preview = test_case['input'].get('topic', '')[:40]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{topic_preview}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - argument_quality: {result.scores['argument_quality']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate AutoGen Debate Club")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_autogen_debate.json")
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
        name="AutoGen Debate Club Evaluation",
        results=results,
        metrics=["argument_quality", "counter_argument", "debate_structure", "topic_adherence"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "07_autogen_debate_club"}
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
