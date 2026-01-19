#!/usr/bin/env python3
"""
Semantic Kernel Planner Evaluation Script

Evaluates the daily planner mini-project on:
1. Plan Completeness - Does plan cover all required tasks?
2. Time Feasibility - Are time allocations realistic?
3. Task Organization - Are tasks logically ordered?
4. Plugin Usage - Are appropriate plugins invoked?

Usage:
    python eval_semantic_planner.py
    python eval_semantic_planner.py --test-file custom_tests.json
    python eval_semantic_planner.py --report --output results.json
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
    output_file: str = "results/eval_semantic_planner.json"
    verbose: bool = False
    report: bool = True


DEFAULT_TEST_CASES = [
    {
        "input": {"tasks": ["meeting at 10am", "lunch with client", "finish report"], "date": "2025-01-20"},
        "expected": {"task_count": 3, "has_times": True}
    },
    {
        "input": {"tasks": ["gym", "grocery shopping", "cook dinner", "watch movie"], "date": "2025-01-21"},
        "expected": {"task_count": 4, "has_times": True}
    },
    {
        "input": {"tasks": ["doctor appointment 9am", "pick up prescription"], "date": "2025-01-22"},
        "expected": {"task_count": 2, "has_times": True, "ordered": True}
    },
    {
        "input": {"tasks": ["project deadline", "team standup", "code review", "deploy to staging"], "date": "2025-01-23"},
        "expected": {"task_count": 4, "has_times": True}
    },
    {
        "input": {"tasks": ["flight at 2pm", "pack luggage", "airport shuttle"], "date": "2025-01-24"},
        "expected": {"task_count": 3, "has_times": True, "ordered": True}
    },
    # Edge cases
    {
        "input": {"tasks": [], "date": "2025-01-25"},
        "expected": {"handles_empty": True}
    },
    {
        "input": {"tasks": ["task1", "task2", "task3", "task4", "task5", "task6", "task7", "task8", "task9", "task10"], "date": "2025-01-26"},
        "expected": {"handles_many": True, "task_count": 10}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def run_planner(input_data: Dict) -> Dict[str, Any]:
    """
    Run the Semantic Kernel Planner mini-project.

    Replace with actual import when mini-project is available.
    """
    tasks = input_data.get("tasks", [])
    date = input_data.get("date", "today")

    if not tasks:
        return {
            "plan": [],
            "summary": "No tasks to plan for today.",
            "total_hours": 0,
            "plugins_used": []
        }

    # Mock plan generation
    plan = []
    current_hour = 8  # Start at 8am

    for task in tasks:
        # Extract time if mentioned
        import re
        time_match = re.search(r'(\d{1,2})(am|pm)', task.lower())

        if time_match:
            hour = int(time_match.group(1))
            if time_match.group(2) == 'pm' and hour != 12:
                hour += 12
            start_time = f"{hour:02d}:00"
        else:
            start_time = f"{current_hour:02d}:00"
            current_hour += 1

        plan.append({
            "task": task,
            "start_time": start_time,
            "duration_minutes": 60,
            "priority": "medium"
        })

    return {
        "plan": plan,
        "date": date,
        "summary": f"Planned {len(plan)} tasks for {date}",
        "total_hours": len(plan),
        "plugins_used": ["TimePlugin", "CalendarPlugin", "PriorityPlugin"]
    }


def metric_plan_completeness(plan: List[Dict], expected_count: int) -> float:
    """Check if plan covers all tasks."""
    if expected_count == 0:
        return 1.0 if len(plan) == 0 else 0.5

    return min(len(plan) / expected_count, 1.0)


def metric_time_feasibility(plan: List[Dict]) -> float:
    """Check if time allocations are realistic."""
    if not plan:
        return 1.0

    score = 0
    for task in plan:
        duration = task.get("duration_minutes", 0)
        has_time = bool(task.get("start_time"))

        # Duration should be reasonable (15-240 minutes)
        if 15 <= duration <= 240:
            score += 0.5

        # Should have start time
        if has_time:
            score += 0.5

    return score / len(plan)


def metric_task_organization(plan: List[Dict]) -> float:
    """Check if tasks are logically ordered."""
    if len(plan) < 2:
        return 1.0

    # Check if times are in order
    times = []
    for task in plan:
        time_str = task.get("start_time", "")
        if time_str:
            try:
                hour = int(time_str.split(":")[0])
                times.append(hour)
            except:
                pass

    if not times:
        return 0.5

    # Check if mostly ascending
    ascending = sum(1 for i in range(1, len(times)) if times[i] >= times[i-1])
    return ascending / (len(times) - 1)


def metric_plugin_usage(output: Dict) -> float:
    """Check if appropriate plugins were used."""
    plugins = output.get("plugins_used", [])

    expected_plugins = ["TimePlugin", "CalendarPlugin"]
    found = sum(1 for p in expected_plugins if any(p.lower() in plugin.lower() for plugin in plugins))

    return found / len(expected_plugins) if expected_plugins else 1.0


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = run_planner(input_data)
    plan = output.get("plan", [])

    scores = {
        "plan_completeness": metric_plan_completeness(plan, expected.get("task_count", len(input_data.get("tasks", [])))),
        "time_feasibility": metric_time_feasibility(plan),
        "task_organization": metric_task_organization(plan),
        "plugin_usage": metric_plugin_usage(output),
    }

    # Pass if most metrics are good
    passed = sum(s >= 0.7 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"plan_{hash(str(input_data)) % 10000:04d}",
        input_data=input_data,
        output=output,
        expected=expected,
        scores=scores,
        passed=passed,
        metadata={"task_count": len(input_data.get("tasks", []))}
    )


def evaluate_all(test_cases: List[Dict], config: EvalConfig) -> List[TestResult]:
    """Evaluate all test cases."""
    results = []

    for i, test_case in enumerate(test_cases):
        if config.verbose:
            task_count = len(test_case['input'].get('tasks', []))
            print(f"Evaluating {i+1}/{len(test_cases)}: {task_count} tasks...")

        result = evaluate_single(test_case, config)
        results.append(result)

        if config.verbose:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status} - completeness: {result.scores['plan_completeness']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate Semantic Kernel Planner")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_semantic_planner.json")
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
        name="Semantic Kernel Planner Evaluation",
        results=results,
        metrics=["plan_completeness", "time_feasibility", "task_organization", "plugin_usage"],
        config={"test_file": config.test_file},
        metadata={"mini_project": "08_semantic_kernel_planner"}
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
