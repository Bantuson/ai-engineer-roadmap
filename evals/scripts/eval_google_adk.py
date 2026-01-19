#!/usr/bin/env python3
"""
Google ADK Voice Assistant Evaluation Script

Evaluates the voice assistant mini-project on:
1. Intent Recognition - Is user intent correctly identified?
2. Action Execution - Are appropriate actions taken?
3. Response Naturalness - Is response conversational?
4. Tool Integration - Are tools used correctly?

Usage:
    python eval_google_adk.py
    python eval_google_adk.py --test-file custom_tests.json
    python eval_google_adk.py --report --output results.json
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
    output_file: str = "results/eval_google_adk.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"utterance": "What's the weather like today?", "context": {}},
        "expected": {"intent": "weather", "has_response": True}
    },
    {
        "input": {"utterance": "Set a timer for 5 minutes", "context": {}},
        "expected": {"intent": "timer", "action": "set_timer", "has_confirmation": True}
    },
    {
        "input": {"utterance": "Play some relaxing music", "context": {}},
        "expected": {"intent": "music", "action": "play_music"}
    },
    {
        "input": {"utterance": "What time is it?", "context": {}},
        "expected": {"intent": "time", "has_response": True}
    },
    {
        "input": {"utterance": "Remind me to call mom at 5pm", "context": {}},
        "expected": {"intent": "reminder", "action": "set_reminder", "has_confirmation": True}
    },
    {
        "input": {"utterance": "Turn off the lights", "context": {"smart_home": True}},
        "expected": {"intent": "smart_home", "action": "control_device"}
    },
    # Edge cases
    {
        "input": {"utterance": "", "context": {}},
        "expected": {"handles_empty": True}
    },
    {
        "input": {"utterance": "blah blah random words", "context": {}},
        "expected": {"handles_unclear": True, "asks_clarification": True}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_voice_assistant(input_data: Dict) -> Dict[str, Any]:
    """
    Run the Google ADK Voice Assistant mini-project.

    Replace with actual import when mini-project is available.
    """
    utterance = input_data.get("utterance", "").lower()
    context = input_data.get("context", {})

    if not utterance:
        return {
            "response": "I'm listening. How can I help you?",
            "intent": "waiting",
            "action": None,
            "tools_used": []
        }

    # Intent classification
    intent_patterns = {
        "weather": ["weather", "temperature", "forecast", "rain", "sunny"],
        "timer": ["timer", "countdown", "alarm"],
        "music": ["play", "music", "song", "playlist"],
        "time": ["time", "clock", "what time"],
        "reminder": ["remind", "reminder", "don't forget"],
        "smart_home": ["light", "turn on", "turn off", "thermostat"],
    }

    detected_intent = "unknown"
    for intent, patterns in intent_patterns.items():
        if any(p in utterance for p in patterns):
            detected_intent = intent
            break

    # Generate response based on intent
    responses = {
        "weather": {
            "response": "It's currently 72°F and sunny. Perfect weather for being outside!",
            "action": "get_weather",
            "data": {"temperature": 72, "condition": "sunny"}
        },
        "timer": {
            "response": "I've set a timer for 5 minutes. I'll let you know when it's done.",
            "action": "set_timer",
            "data": {"duration_minutes": 5}
        },
        "music": {
            "response": "Playing relaxing music for you now.",
            "action": "play_music",
            "data": {"genre": "relaxing"}
        },
        "time": {
            "response": "It's currently 3:30 PM.",
            "action": "get_time",
            "data": {"time": "15:30"}
        },
        "reminder": {
            "response": "I'll remind you to call mom at 5 PM.",
            "action": "set_reminder",
            "data": {"task": "call mom", "time": "17:00"}
        },
        "smart_home": {
            "response": "Turning off the lights.",
            "action": "control_device",
            "data": {"device": "lights", "state": "off"}
        },
        "unknown": {
            "response": "I'm not sure I understand. Could you please rephrase that?",
            "action": None,
            "data": {}
        }
    }

    result = responses.get(detected_intent, responses["unknown"])

    return {
        "response": result["response"],
        "intent": detected_intent,
        "action": result["action"],
        "data": result["data"],
        "tools_used": ["IntentClassifier", "ResponseGenerator", result["action"]] if result["action"] else ["IntentClassifier"]
    }


def metric_intent_recognition(detected: str, expected: str) -> float:
    """Check if intent was correctly recognized."""
    if not expected:
        return 1.0
    return 1.0 if detected.lower() == expected.lower() else 0.0


def metric_action_execution(output: Dict, expected_action: str) -> float:
    """Check if correct action was taken."""
    if not expected_action:
        return 1.0

    action = output.get("action", "")
    return 1.0 if action == expected_action else 0.0


def metric_response_naturalness(response: str) -> float:
    """Evaluate response naturalness."""
    if not response:
        return 0.0

    score = 0.0

    # Reasonable length (not too short or long)
    if 10 < len(response) < 200:
        score += 0.3

    # Conversational indicators
    conversational = ["i've", "i'll", "you", "your", "please", "let me"]
    if any(c in response.lower() for c in conversational):
        score += 0.3

    # Complete sentences
    if response[0].isupper() and response.rstrip().endswith(('.', '!', '?')):
        score += 0.2

    # No technical jargon
    technical = ["error", "exception", "null", "undefined"]
    if not any(t in response.lower() for t in technical):
        score += 0.2

    return score


def metric_tool_usage(output: Dict) -> float:
    """Check if appropriate tools were used."""
    tools = output.get("tools_used", [])
    action = output.get("action")

    # Should have at least intent classifier
    if "IntentClassifier" not in tools:
        return 0.5

    # If action expected, should have action tool
    if action and action not in tools:
        return 0.7

    return 1.0


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_voice_assistant(input_data)

    scores = {
        "intent_recognition": metric_intent_recognition(
            output.get("intent", ""), expected.get("intent", "")
        ),
        "action_execution": metric_action_execution(output, expected.get("action", "")),
        "response_naturalness": metric_response_naturalness(output.get("response", "")),
        "tool_usage": metric_tool_usage(output),
    }

    # Intent recognition is critical
    passed = scores["intent_recognition"] >= 0.5 and sum(s >= 0.6 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"voice_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"intent": output.get("intent")}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            utterance_preview = test_case['input'].get('utterance', '')[:40]
            print(f"Evaluating {i+1}/{len(test_cases)}: '{utterance_preview}'...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            intent = result.output.get("intent", "unknown")
            print(f"  {status} - intent: {intent}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate Google ADK Voice Assistant")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_google_adk.json")
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
        name="Google ADK Voice Assistant Evaluation",
        results=results,
        metrics=["intent_recognition", "action_execution", "response_naturalness", "tool_usage"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "05_google_adk_voice_assistant"}
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
