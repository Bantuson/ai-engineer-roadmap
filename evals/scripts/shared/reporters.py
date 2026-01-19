"""
Evaluation Report Generation Module

This module provides functions for generating evaluation reports.
"""

import json
import statistics
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict


# ============= Data Classes =============

@dataclass
class TestResult:
    """Single test case result."""
    test_id: str
    input_data: Dict[str, Any]
    output: Any
    expected: Any
    scores: Dict[str, float]
    passed: bool
    metadata: Dict[str, Any] = None


@dataclass
class EvalReport:
    """Complete evaluation report."""
    name: str
    timestamp: str
    config: Dict[str, Any]
    summary: Dict[str, Any]
    results: List[Dict]
    metadata: Dict[str, Any] = None


# ============= Report Generation =============

def generate_summary(results: List[TestResult], metrics: List[str]) -> Dict[str, Any]:
    """
    Generate summary statistics from results.

    Args:
        results: List of TestResult objects
        metrics: List of metric names

    Returns:
        Summary dictionary
    """
    summary = {
        "total_tests": len(results),
        "passed": sum(1 for r in results if r.passed),
        "failed": sum(1 for r in results if not r.passed),
        "pass_rate": 0.0,
        "metrics": {}
    }

    if len(results) > 0:
        summary["pass_rate"] = summary["passed"] / len(results)

    for metric in metrics:
        scores = [r.scores.get(metric, 0) for r in results if metric in r.scores]
        if scores:
            summary["metrics"][metric] = {
                "mean": statistics.mean(scores),
                "std": statistics.stdev(scores) if len(scores) > 1 else 0,
                "min": min(scores),
                "max": max(scores),
                "median": statistics.median(scores)
            }

    return summary


def generate_report(
    name: str,
    results: List[TestResult],
    metrics: List[str],
    config: Dict[str, Any] = None,
    metadata: Dict[str, Any] = None
) -> EvalReport:
    """
    Generate complete evaluation report.

    Args:
        name: Evaluation name
        results: List of TestResult objects
        metrics: List of metric names
        config: Evaluation configuration
        metadata: Additional metadata

    Returns:
        EvalReport object
    """
    summary = generate_summary(results, metrics)

    return EvalReport(
        name=name,
        timestamp=datetime.now().isoformat(),
        config=config or {},
        summary=summary,
        results=[asdict(r) for r in results],
        metadata=metadata
    )


# ============= Output Formatters =============

def format_text_report(report: EvalReport) -> str:
    """
    Format report as human-readable text.

    Args:
        report: EvalReport object

    Returns:
        Formatted text string
    """
    lines = [
        "=" * 60,
        f"EVALUATION REPORT: {report.name}",
        "=" * 60,
        f"Timestamp: {report.timestamp}",
        "",
        "SUMMARY",
        "-" * 40,
        f"Total Tests: {report.summary['total_tests']}",
        f"Passed: {report.summary['passed']}",
        f"Failed: {report.summary['failed']}",
        f"Pass Rate: {report.summary['pass_rate']:.1%}",
        "",
        "METRICS",
        "-" * 40,
    ]

    for metric, stats in report.summary.get("metrics", {}).items():
        lines.append(f"{metric}:")
        lines.append(f"  Mean:   {stats['mean']:.3f}")
        lines.append(f"  Std:    {stats['std']:.3f}")
        lines.append(f"  Median: {stats['median']:.3f}")
        lines.append(f"  Range:  [{stats['min']:.3f}, {stats['max']:.3f}]")

    # Sample results (first 5 failed, then first 5 passed)
    lines.extend(["", "SAMPLE RESULTS", "-" * 40])

    failed = [r for r in report.results if not r.get("passed", True)]
    passed = [r for r in report.results if r.get("passed", True)]

    if failed:
        lines.append("\nFailed Tests:")
        for r in failed[:5]:
            lines.append(f"  [{r.get('test_id', 'N/A')}]")
            inp = str(r.get('input_data', {}))[:50]
            lines.append(f"    Input: {inp}...")
            lines.append(f"    Scores: {r.get('scores', {})}")

    if passed:
        lines.append("\nPassed Tests (sample):")
        for r in passed[:3]:
            lines.append(f"  [{r.get('test_id', 'N/A')}]")
            lines.append(f"    Scores: {r.get('scores', {})}")

    if len(report.results) > 8:
        lines.append(f"\n... and {len(report.results) - 8} more results")

    lines.extend(["", "=" * 60])

    return "\n".join(lines)


def format_json_report(report: EvalReport) -> str:
    """
    Format report as JSON.

    Args:
        report: EvalReport object

    Returns:
        JSON string
    """
    return json.dumps(asdict(report), indent=2)


def format_markdown_report(report: EvalReport) -> str:
    """
    Format report as Markdown.

    Args:
        report: EvalReport object

    Returns:
        Markdown string
    """
    lines = [
        f"# Evaluation Report: {report.name}",
        "",
        f"**Timestamp:** {report.timestamp}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total Tests | {report.summary['total_tests']} |",
        f"| Passed | {report.summary['passed']} |",
        f"| Failed | {report.summary['failed']} |",
        f"| Pass Rate | {report.summary['pass_rate']:.1%} |",
        "",
        "## Metrics",
        "",
    ]

    for metric, stats in report.summary.get("metrics", {}).items():
        lines.extend([
            f"### {metric}",
            "",
            f"- **Mean:** {stats['mean']:.3f}",
            f"- **Std Dev:** {stats['std']:.3f}",
            f"- **Median:** {stats['median']:.3f}",
            f"- **Range:** [{stats['min']:.3f}, {stats['max']:.3f}]",
            "",
        ])

    # Results table
    if report.results:
        lines.extend([
            "## Detailed Results",
            "",
            "| Test ID | Passed | Key Scores |",
            "|---------|--------|------------|",
        ])

        for r in report.results[:20]:
            test_id = r.get('test_id', 'N/A')
            passed = "✓" if r.get('passed') else "✗"
            scores = r.get('scores', {})
            score_str = ", ".join([f"{k}:{v:.2f}" for k, v in list(scores.items())[:3]])
            lines.append(f"| {test_id} | {passed} | {score_str} |")

        if len(report.results) > 20:
            lines.append(f"\n*... and {len(report.results) - 20} more results*")

    return "\n".join(lines)


def format_csv_results(results: List[TestResult]) -> str:
    """
    Format results as CSV.

    Args:
        results: List of TestResult objects

    Returns:
        CSV string
    """
    if not results:
        return ""

    # Get all metric names
    all_metrics = set()
    for r in results:
        all_metrics.update(r.scores.keys())

    # Header
    lines = ["test_id,passed," + ",".join(sorted(all_metrics))]

    # Rows
    for r in results:
        row = [r.test_id, str(r.passed)]
        for metric in sorted(all_metrics):
            row.append(f"{r.scores.get(metric, 0):.4f}")
        lines.append(",".join(row))

    return "\n".join(lines)


# ============= File Output =============

def save_report(report: EvalReport, filepath: str, format: str = "json"):
    """
    Save report to file.

    Args:
        report: EvalReport object
        filepath: Output file path
        format: 'json', 'text', 'markdown', or 'csv'
    """
    formatters = {
        "json": format_json_report,
        "text": format_text_report,
        "markdown": format_markdown_report,
    }

    formatter = formatters.get(format, format_json_report)
    content = formatter(report)

    with open(filepath, 'w') as f:
        f.write(content)


def save_results_csv(results: List[TestResult], filepath: str):
    """Save results as CSV file."""
    content = format_csv_results(results)
    with open(filepath, 'w') as f:
        f.write(content)


# ============= Comparison Reports =============

def compare_reports(report_a: EvalReport, report_b: EvalReport) -> Dict[str, Any]:
    """
    Compare two evaluation reports.

    Args:
        report_a: First report
        report_b: Second report

    Returns:
        Comparison summary
    """
    comparison = {
        "report_a": report_a.name,
        "report_b": report_b.name,
        "pass_rate_diff": (
            report_b.summary["pass_rate"] - report_a.summary["pass_rate"]
        ),
        "metrics_diff": {}
    }

    # Compare metrics
    metrics_a = report_a.summary.get("metrics", {})
    metrics_b = report_b.summary.get("metrics", {})

    all_metrics = set(metrics_a.keys()) | set(metrics_b.keys())

    for metric in all_metrics:
        mean_a = metrics_a.get(metric, {}).get("mean", 0)
        mean_b = metrics_b.get(metric, {}).get("mean", 0)
        comparison["metrics_diff"][metric] = {
            "a_mean": mean_a,
            "b_mean": mean_b,
            "diff": mean_b - mean_a,
            "pct_change": ((mean_b - mean_a) / mean_a * 100) if mean_a != 0 else 0
        }

    # Determine winner
    improvements = sum(1 for m in comparison["metrics_diff"].values() if m["diff"] > 0)
    regressions = sum(1 for m in comparison["metrics_diff"].values() if m["diff"] < 0)

    comparison["summary"] = {
        "improvements": improvements,
        "regressions": regressions,
        "winner": "B" if improvements > regressions else ("A" if regressions > improvements else "Tie")
    }

    return comparison


# ============= Console Output =============

def print_summary(report: EvalReport):
    """Print quick summary to console."""
    print(f"\n{'='*50}")
    print(f"Evaluation: {report.name}")
    print(f"Pass Rate: {report.summary['pass_rate']:.1%}")
    print(f"{'='*50}")

    for metric, stats in report.summary.get("metrics", {}).items():
        print(f"{metric}: {stats['mean']:.3f} (±{stats['std']:.3f})")


# ============= For Testing =============

if __name__ == "__main__":
    print("Testing reporters module...")

    # Create test results
    results = [
        TestResult(
            test_id="test_001",
            input_data={"query": "What is 2+2?"},
            output="4",
            expected="4",
            scores={"accuracy": 1.0, "clarity": 0.9},
            passed=True
        ),
        TestResult(
            test_id="test_002",
            input_data={"query": "What is the capital of France?"},
            output="London",
            expected="Paris",
            scores={"accuracy": 0.0, "clarity": 0.8},
            passed=False
        ),
    ]

    # Generate report
    report = generate_report(
        name="Test Evaluation",
        results=results,
        metrics=["accuracy", "clarity"],
        config={"model": "test"}
    )

    print("\n--- Text Report ---")
    print(format_text_report(report))

    print("\n--- Markdown Report ---")
    print(format_markdown_report(report)[:500] + "...")

    print("\n--- CSV Results ---")
    print(format_csv_results(results))

    print("\nAll tests passed!")
