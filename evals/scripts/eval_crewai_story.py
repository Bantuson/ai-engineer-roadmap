#!/usr/bin/env python3
"""
CrewAI Story Crew Evaluation Script

Evaluates the multi-agent story generation mini-project on:
1. Story Coherence - Does the story flow logically?
2. Character Development - Are characters well-defined?
3. Theme Adherence - Does it follow the given theme?
4. Creativity - Is the story original and engaging?

Usage:
    python eval_crewai_story.py
    python eval_crewai_story.py --test-file custom_tests.json
    python eval_crewai_story.py --report --output results.json
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
    output_file: str = "results/eval_crewai_story.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"theme": "adventure", "setting": "forest", "characters": ["brave knight", "wise owl"]},
        "expected": {"keywords": ["forest", "knight", "owl", "adventure"], "min_length": 200}
    },
    {
        "input": {"theme": "mystery", "setting": "old mansion", "characters": ["detective", "butler"]},
        "expected": {"keywords": ["mansion", "detective", "mystery", "clue"], "min_length": 200}
    },
    {
        "input": {"theme": "friendship", "setting": "school", "characters": ["shy student", "popular kid"]},
        "expected": {"keywords": ["school", "friend", "student"], "min_length": 200}
    },
    {
        "input": {"theme": "courage", "setting": "mountain", "characters": ["young climber"]},
        "expected": {"keywords": ["mountain", "climb", "courage", "brave"], "min_length": 150}
    },
    {
        "input": {"theme": "discovery", "setting": "underwater city", "characters": ["marine biologist", "mermaid"]},
        "expected": {"keywords": ["underwater", "city", "discover"], "min_length": 200}
    },
    # Edge cases
    {
        "input": {"theme": "love", "setting": "", "characters": []},
        "expected": {"keywords": ["love"], "min_length": 100, "handles_empty": True}
    },
    {
        "input": {"theme": "hope", "setting": "post-apocalyptic world", "characters": ["survivor", "child", "robot"]},
        "expected": {"keywords": ["hope", "survivor"], "min_length": 250}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_story_crew(input_data: Dict) -> Dict[str, Any]:
    """
    Run the CrewAI story crew mini-project.

    Replace with actual import when mini-project is available.
    """
    # Mock implementation
    theme = input_data.get("theme", "adventure")
    setting = input_data.get("setting", "unknown place")
    characters = input_data.get("characters", ["protagonist"])

    # Simulated story generation
    char_str = " and ".join(characters) if characters else "a mysterious figure"
    story = f"""
    In {setting if setting else 'a distant land'}, a tale of {theme} unfolds.
    {char_str} embarked on a journey that would change everything.
    The {theme} they sought was not easily found, but through perseverance,
    they discovered what truly mattered.

    As they ventured deeper into {setting if setting else 'the unknown'},
    challenges arose that tested their resolve. But the spirit of {theme}
    guided them forward.

    In the end, {char_str} learned that the greatest treasures
    are not material, but the bonds formed and lessons learned along the way.
    """

    return {
        "story": story.strip(),
        "theme": theme,
        "word_count": len(story.split()),
        "agents_used": ["researcher", "writer", "editor"]
    }


def metric_theme_adherence(story: str, theme: str) -> float:
    """Check if story adheres to theme."""
    theme_keywords = {
        "adventure": ["journey", "quest", "discover", "adventure", "explore"],
        "mystery": ["mystery", "clue", "secret", "hidden", "investigate"],
        "friendship": ["friend", "together", "bond", "trust", "companion"],
        "courage": ["brave", "courage", "fear", "overcome", "strength"],
        "discovery": ["discover", "find", "reveal", "uncover", "learn"],
        "love": ["love", "heart", "care", "affection", "devotion"],
        "hope": ["hope", "future", "believe", "possible", "light"],
    }

    keywords = theme_keywords.get(theme.lower(), [theme.lower()])
    return keyword_coverage(story, keywords)


def metric_coherence(story: str) -> float:
    """Evaluate story coherence."""
    if not story.strip():
        return 0.0

    sentences = story.split('.')
    if len(sentences) < 3:
        return 0.5

    # Check for basic structure
    has_beginning = any(w in story.lower()[:200] for w in ["once", "in", "the", "a"])
    has_ending = any(w in story.lower()[-200:] for w in ["end", "finally", "last", "learned"])

    score = 0.5
    if has_beginning:
        score += 0.25
    if has_ending:
        score += 0.25

    return score


def metric_character_presence(story: str, characters: List[str]) -> float:
    """Check if characters appear in story."""
    if not characters:
        return 1.0

    story_lower = story.lower()
    present = 0

    for char in characters:
        char_words = char.lower().split()
        if any(w in story_lower for w in char_words):
            present += 1

    return present / len(characters)


def metric_length_adequacy(story: str, min_length: int) -> float:
    """Check if story meets minimum length."""
    word_count = len(story.split())
    if word_count >= min_length:
        return 1.0
    return word_count / min_length


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_story_crew(input_data)
    story = output.get("story", "")

    scores = {
        "theme_adherence": metric_theme_adherence(story, input_data.get("theme", "")),
        "coherence": metric_coherence(story),
        "character_presence": metric_character_presence(story, input_data.get("characters", [])),
        "length_adequacy": metric_length_adequacy(story, expected.get("min_length", 100)),
        "keyword_coverage": keyword_coverage(story, expected.get("keywords", [])),
    }

    # Overall pass: all metrics >= 0.6
    passed = all(s >= 0.6 for s in scores.values())

    return TestResult(
        test_id=f"story_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"theme": input_data.get("theme")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            print(f"Evaluating {i+1}/{len(test_cases)}: theme={test_case['input'].get('theme')}...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - coherence: {result.scores['coherence']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate CrewAI Story Crew")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_crewai_story.json")
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
        name="CrewAI Story Crew Evaluation",
        results=results,
        metrics=["theme_adherence", "coherence", "character_presence", "length_adequacy", "keyword_coverage"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "01_crewai_story_crew"}
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
