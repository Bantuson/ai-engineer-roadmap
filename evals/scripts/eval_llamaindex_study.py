#!/usr/bin/env python3
"""
LlamaIndex Study Buddy Evaluation Script

Evaluates the RAG-based study assistant on:
1. Retrieval Quality - Are relevant documents retrieved?
2. Answer Accuracy - Is the answer correct based on context?
3. Source Attribution - Are sources properly cited?
4. Explanation Quality - Is the explanation clear and educational?

Usage:
    python eval_llamaindex_study.py
    python eval_llamaindex_study.py --test-file custom_tests.json
    python eval_llamaindex_study.py --report --output results.json
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
    output_file: str = "results/eval_llamaindex_study.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"question": "What is photosynthesis?", "subject": "biology"},
        "expected": {"keywords": ["plant", "sunlight", "oxygen", "carbon dioxide"], "has_sources": True}
    },
    {
        "input": {"question": "Explain the Pythagorean theorem", "subject": "math"},
        "expected": {"keywords": ["triangle", "right", "a2", "b2", "c2", "hypotenuse"], "has_sources": True}
    },
    {
        "input": {"question": "What caused World War I?", "subject": "history"},
        "expected": {"keywords": ["assassination", "alliance", "austria", "serbia"], "has_sources": True}
    },
    {
        "input": {"question": "How does gravity work?", "subject": "physics"},
        "expected": {"keywords": ["force", "mass", "newton", "attract"], "has_sources": True}
    },
    {
        "input": {"question": "What is a variable in programming?", "subject": "computer science"},
        "expected": {"keywords": ["store", "value", "data", "memory"], "has_sources": True}
    },
    # Edge cases
    {
        "input": {"question": "", "subject": "general"},
        "expected": {"handles_empty": True}
    },
    {
        "input": {"question": "Explain quantum entanglement in simple terms", "subject": "physics"},
        "expected": {"keywords": ["particle", "connect", "distance"], "educational": True}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_study_buddy(input_data: Dict) -> Dict[str, Any]:
    """
    Run the LlamaIndex Study Buddy mini-project.

    Replace with actual import when mini-project is available.
    """
    question = input_data.get("question", "")
    subject = input_data.get("subject", "general")

    # Mock RAG responses
    responses = {
        "photosynthesis": {
            "answer": "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into glucose and oxygen. This occurs in the chloroplasts of plant cells.",
            "sources": ["Biology Textbook Ch. 5", "Khan Academy: Photosynthesis"]
        },
        "pythagorean": {
            "answer": "The Pythagorean theorem states that in a right triangle, a² + b² = c², where c is the hypotenuse. This fundamental relationship helps calculate distances and is used extensively in geometry.",
            "sources": ["Mathematics Reference", "Geometry Fundamentals"]
        },
        "world war": {
            "answer": "World War I was caused by a complex web of factors including the assassination of Archduke Franz Ferdinand, alliance systems, militarism, and nationalism. The assassination in Sarajevo triggered a chain reaction of declarations of war.",
            "sources": ["World History Encyclopedia", "WWI Documentary Transcript"]
        },
        "gravity": {
            "answer": "Gravity is a fundamental force of nature that causes objects with mass to attract each other. According to Newton's law of gravitation, the force is proportional to the masses and inversely proportional to the square of the distance.",
            "sources": ["Physics Principles", "Newton's Laws Explained"]
        },
        "variable": {
            "answer": "A variable in programming is a named storage location in memory that holds a value. Variables can store different types of data like numbers, text, or boolean values, and their values can change during program execution.",
            "sources": ["Programming Basics", "Computer Science 101"]
        },
        "quantum": {
            "answer": "Quantum entanglement is a phenomenon where two particles become connected in such a way that measuring one instantly affects the other, regardless of the distance between them. Einstein called it 'spooky action at a distance.'",
            "sources": ["Quantum Physics Simplified", "Physics Today"]
        }
    }

    if not question:
        return {
            "answer": "Please ask a question and I'll help you study!",
            "sources": [],
            "documents_retrieved": 0
        }

    # Find matching response
    question_lower = question.lower()
    for key, response in responses.items():
        if key in question_lower:
            return {
                "answer": response["answer"],
                "sources": response["sources"],
                "documents_retrieved": len(response["sources"]),
                "subject": subject
            }

    # Default response
    return {
        "answer": f"Based on my knowledge of {subject}, I can help explain this concept. Let me provide some context...",
        "sources": ["General Knowledge Base"],
        "documents_retrieved": 1,
        "subject": subject
    }


def metric_answer_relevance(answer: str, keywords: List[str]) -> float:
    """Check if answer contains expected keywords."""
    if not keywords:
        return 1.0
    return keyword_coverage(answer, keywords)


def metric_source_attribution(output: Dict) -> float:
    """Check if sources are properly attributed."""
    sources = output.get("sources", [])
    docs_retrieved = output.get("documents_retrieved", 0)

    if docs_retrieved == 0:
        return 0.5  # May be valid for simple questions

    # Has sources
    if len(sources) > 0:
        return 1.0
    return 0.0


def metric_explanation_quality(answer: str) -> float:
    """Evaluate explanation quality."""
    if not answer:
        return 0.0

    score = 0.0

    # Length check (educational explanations should be substantial)
    if len(answer) > 100:
        score += 0.3
    elif len(answer) > 50:
        score += 0.2

    # Has educational indicators
    educational_words = ["because", "therefore", "this means", "for example", "in other words"]
    if any(w in answer.lower() for w in educational_words):
        score += 0.3

    # Has structure (periods indicate multiple sentences)
    sentences = answer.split('.')
    if len(sentences) >= 2:
        score += 0.2

    # Doesn't have uncertainty markers
    uncertain = ["i don't know", "not sure", "cannot answer"]
    if not any(u in answer.lower() for u in uncertain):
        score += 0.2

    return min(score, 1.0)


def metric_retrieval_quality(output: Dict) -> float:
    """Evaluate retrieval quality."""
    docs_retrieved = output.get("documents_retrieved", 0)

    if docs_retrieved >= 2:
        return 1.0
    elif docs_retrieved == 1:
        return 0.7
    else:
        return 0.3


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_study_buddy(input_data)

    scores = {
        "answer_relevance": metric_answer_relevance(
            output.get("answer", ""), expected.get("keywords", [])
        ),
        "source_attribution": metric_source_attribution(output),
        "explanation_quality": metric_explanation_quality(output.get("answer", "")),
        "retrieval_quality": metric_retrieval_quality(output),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.6 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"study_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"subject": input_data.get("subject")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            question_preview = test_case['input'].get('question', '')[:40]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{question_preview}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - relevance: {result.scores['answer_relevance']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate LlamaIndex Study Buddy")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_llamaindex_study.json")
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
        name="LlamaIndex Study Buddy Evaluation",
        results=results,
        metrics=["answer_relevance", "source_attribution", "explanation_quality", "retrieval_quality"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "06_llamaindex_study_buddy"}
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
