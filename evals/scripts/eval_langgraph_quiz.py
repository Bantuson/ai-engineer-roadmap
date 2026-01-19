#!/usr/bin/env python3
"""
LangGraph Quiz Master Evaluation Script

Evaluates the quiz generation mini-project on:
1. Question Quality - Are questions clear and valid?
2. Answer Accuracy - Are answers correct?
3. Difficulty Progression - Does difficulty increase appropriately?
4. Explanation Quality - Are explanations helpful?

Usage:
    python eval_langgraph_quiz.py
    python eval_langgraph_quiz.py --test-file custom_tests.json
    python eval_langgraph_quiz.py --report --output results.json
"""

import argparse
import json
import sys
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from metrics import exact_match, keyword_coverage
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results/eval_langgraph_quiz.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"topic": "Python basics", "difficulty": "easy", "num_questions": 3},
        "expected": {"has_questions": True, "question_count": 3, "topic_keywords": ["python", "variable", "function"]}
    },
    {
        "input": {"topic": "Machine learning", "difficulty": "medium", "num_questions": 2},
        "expected": {"has_questions": True, "question_count": 2, "topic_keywords": ["model", "training", "data"]}
    },
    {
        "input": {"topic": "World history", "difficulty": "hard", "num_questions": 4},
        "expected": {"has_questions": True, "question_count": 4, "topic_keywords": ["history", "war", "civilization"]}
    },
    {
        "input": {"topic": "Mathematics", "difficulty": "easy", "num_questions": 2},
        "expected": {"has_questions": True, "question_count": 2, "topic_keywords": ["number", "calculate", "math"]}
    },
    {
        "input": {"topic": "Science", "difficulty": "medium", "num_questions": 3},
        "expected": {"has_questions": True, "question_count": 3, "topic_keywords": ["science", "experiment", "theory"]}
    },
    # Edge cases
    {
        "input": {"topic": "", "difficulty": "easy", "num_questions": 1},
        "expected": {"handles_empty": True, "has_questions": True}
    },
    {
        "input": {"topic": "General knowledge", "difficulty": "easy", "num_questions": 0},
        "expected": {"handles_zero": True, "question_count": 0}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_quiz_master(input_data: Dict) -> Dict[str, Any]:
    """
    Run the LangGraph Quiz Master mini-project.

    Replace with actual import when mini-project is available.
    """
    topic = input_data.get("topic", "general knowledge")
    difficulty = input_data.get("difficulty", "medium")
    num_questions = input_data.get("num_questions", 3)

    # Mock quiz generation
    questions = []
    for i in range(num_questions):
        questions.append({
            "id": i + 1,
            "question": f"What is a key concept in {topic}?" if topic else "What is 2 + 2?",
            "options": ["A", "B", "C", "D"],
            "correct_answer": "A",
            "explanation": f"This relates to {topic} at {difficulty} level.",
            "difficulty": difficulty
        })

    return {
        "quiz": {
            "topic": topic or "general knowledge",
            "difficulty": difficulty,
            "questions": questions
        },
        "question_count": len(questions),
        "graph_states": ["generate", "validate", "format"]
    }


def metric_question_count(output: Dict, expected: int) -> float:
    """Check if correct number of questions generated."""
    actual = output.get("question_count", 0)
    if expected == 0:
        return 1.0 if actual == 0 else 0.0
    return 1.0 if actual == expected else actual / expected


def metric_question_quality(questions: List[Dict]) -> float:
    """Evaluate question quality."""
    if not questions:
        return 0.0

    score = 0
    for q in questions:
        # Has required fields
        has_question = bool(q.get("question"))
        has_options = len(q.get("options", [])) >= 2
        has_answer = bool(q.get("correct_answer"))
        has_explanation = bool(q.get("explanation"))

        q_score = sum([has_question, has_options, has_answer, has_explanation]) / 4
        score += q_score

    return score / len(questions)


def metric_topic_relevance(output: Dict, keywords: List[str]) -> float:
    """Check if quiz is relevant to topic."""
    if not keywords:
        return 1.0

    quiz = output.get("quiz", {})
    questions = quiz.get("questions", [])

    all_text = quiz.get("topic", "").lower()
    for q in questions:
        all_text += " " + q.get("question", "").lower()
        all_text += " " + q.get("explanation", "").lower()

    return keyword_coverage(all_text, keywords)


def metric_difficulty_appropriateness(questions: List[Dict], expected_difficulty: str) -> float:
    """Check if difficulty matches expectations."""
    if not questions:
        return 1.0

    matching = sum(1 for q in questions if q.get("difficulty") == expected_difficulty)
    return matching / len(questions)


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_quiz_master(input_data)
    questions = output.get("quiz", {}).get("questions", [])

    scores = {
        "question_count": metric_question_count(output, expected.get("question_count", input_data.get("num_questions", 0))),
        "question_quality": metric_question_quality(questions),
        "topic_relevance": metric_topic_relevance(output, expected.get("topic_keywords", [])),
        "difficulty_match": metric_difficulty_appropriateness(questions, input_data.get("difficulty", "medium")),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.7 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"quiz_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"topic": input_data.get("topic"), "difficulty": input_data.get("difficulty")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            print(f"Evaluating {i+1}/{len(test_cases)}: topic={test_case['input'].get('topic')}...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - quality: {result.scores['question_quality']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate LangGraph Quiz Master")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_langgraph_quiz.json")
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
        name="LangGraph Quiz Master Evaluation",
        results=results,
        metrics=["question_count", "question_quality", "topic_relevance", "difficulty_match"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "02_langgraph_quiz_master"}
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
