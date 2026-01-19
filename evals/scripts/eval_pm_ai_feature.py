#!/usr/bin/env python3
"""
AI Feature Planning Evaluation Script

Evaluates AI feature planning artifacts on:
1. AI-Specific Considerations - Are AI challenges addressed?
2. Evaluation Strategy - Is model evaluation planned?
3. Responsible AI - Are ethical concerns considered?
4. Technical Feasibility - Is the approach realistic?

Usage:
    python eval_pm_ai_feature.py
    python eval_pm_ai_feature.py --test-file custom_tests.json
    python eval_pm_ai_feature.py --report --output results.json
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
    output_file: str = "results/eval_pm_ai_feature.json"
    verbose: bool = False
    report: bool = True


AI_CONSIDERATIONS = [
    "data requirements",
    "model evaluation",
    "bias",
    "explainability",
    "fallback",
    "monitoring"
]


DEFAULT_TEST_CASES = [
    {
        "input": {
            "feature": "AI-powered content recommendations",
            "product": "News app",
            "ai_capability": "Personalized article suggestions based on reading history"
        },
        "expected": {
            "ai_keywords": ["recommendation", "personalization", "user behavior", "model"],
            "has_eval_plan": True
        }
    },
    {
        "input": {
            "feature": "Automated customer support chatbot",
            "product": "E-commerce platform",
            "ai_capability": "Natural language understanding for customer queries"
        },
        "expected": {
            "ai_keywords": ["nlp", "intent", "response", "escalation"],
            "has_eval_plan": True
        }
    },
    {
        "input": {
            "feature": "Fraud detection system",
            "product": "Banking app",
            "ai_capability": "Real-time transaction anomaly detection"
        },
        "expected": {
            "ai_keywords": ["fraud", "detection", "anomaly", "false positive"],
            "has_eval_plan": True
        }
    },
    {
        "input": {
            "feature": "Smart image tagging",
            "product": "Photo management app",
            "ai_capability": "Automatic object and face recognition in photos"
        },
        "expected": {
            "ai_keywords": ["image", "recognition", "tagging", "accuracy"],
            "has_eval_plan": True
        }
    },
    # Edge cases
    {
        "input": {
            "feature": "Basic search",
            "product": "Website",
            "ai_capability": ""
        },
        "expected": {"handles_non_ai": True}
    },
]


def load_test_cases(filepath: Optional[str] = None) -> List[Dict]:
    """Load test cases from file or use defaults."""
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return DEFAULT_TEST_CASES


def generate_ai_feature_plan(input_data: Dict) -> Dict[str, Any]:
    """
    Generate AI feature plan based on input.

    Replace with actual generation when available.
    """
    feature = input_data.get("feature", "AI Feature")
    product = input_data.get("product", "Product")
    ai_capability = input_data.get("ai_capability", "")

    if not ai_capability:
        return {
            "plan": "This feature does not appear to require AI capabilities.",
            "is_ai_feature": False,
            "considerations": []
        }

    plan = f"""
# AI Feature Plan: {feature}

## Overview
Implementing {ai_capability} for {product} to enhance user experience.

## Data Requirements
- **Training Data**: Historical user interaction data
- **Volume**: Minimum 100,000 labeled examples
- **Quality**: Human-validated labels with 95%+ accuracy
- **Privacy**: PII anonymization required

## Model Selection
- **Approach**: Start with pre-trained models, fine-tune on domain data
- **Candidates**: Transformer-based models for NLP, CNN for vision tasks
- **Trade-offs**: Accuracy vs. latency vs. cost

## Evaluation Strategy
- **Offline Metrics**:
  - Accuracy/Precision/Recall/F1
  - AUC-ROC for classification
  - NDCG for ranking
- **Online Metrics**:
  - A/B test against baseline
  - User engagement metrics
  - Business impact (conversion, retention)
- **Evaluation Cadence**: Weekly model monitoring

## Responsible AI Considerations
- **Bias Audit**: Test for demographic parity across user segments
- **Explainability**: Provide reasons for AI decisions where possible
- **Transparency**: Clear user communication about AI usage
- **Human Oversight**: Escalation path to human review

## Fallback Strategy
- **Graceful Degradation**: Rule-based fallback when AI unavailable
- **Confidence Threshold**: Route low-confidence predictions to review
- **Error Handling**: Clear user messaging for AI failures

## Monitoring & Operations
- **Model Performance**: Daily accuracy tracking
- **Data Drift Detection**: Weekly input distribution analysis
- **Alert Thresholds**: Page on-call if accuracy drops >5%
- **Retraining Cadence**: Monthly model updates

## Success Criteria
- Model accuracy > 90%
- False positive rate < 5%
- User satisfaction score improvement > 10%
- No significant bias across user segments

## Risks
| Risk | Mitigation |
|------|------------|
| Model degradation | Continuous monitoring + automated alerts |
| Bias in recommendations | Regular fairness audits |
| Privacy concerns | Data anonymization + user consent |
"""

    return {
        "plan": plan,
        "is_ai_feature": True,
        "considerations": [
            "data requirements",
            "model evaluation",
            "bias audit",
            "explainability",
            "fallback strategy",
            "monitoring"
        ],
        "has_eval_plan": True,
        "has_responsible_ai": True
    }


def metric_ai_considerations(considerations: List[str], required: List[str]) -> float:
    """Check if AI-specific considerations are addressed."""
    if not required:
        return 1.0

    addressed = sum(
        1 for r in required
        if any(r.lower() in c.lower() for c in considerations)
    )
    return addressed / len(required)


def metric_eval_strategy(plan: str) -> float:
    """Check if evaluation strategy is comprehensive."""
    eval_keywords = [
        "accuracy", "precision", "recall", "f1",
        "a/b test", "baseline", "metrics",
        "monitoring", "threshold"
    ]

    plan_lower = plan.lower()
    found = sum(1 for k in eval_keywords if k in plan_lower)
    return min(found / 5, 1.0)


def metric_responsible_ai(plan: str) -> float:
    """Check for responsible AI considerations."""
    responsible_keywords = [
        "bias", "fairness", "explainability", "transparency",
        "privacy", "consent", "ethics", "human oversight"
    ]

    plan_lower = plan.lower()
    found = sum(1 for k in responsible_keywords if k in plan_lower)
    return min(found / 4, 1.0)


def metric_technical_feasibility(plan: str) -> float:
    """Evaluate technical feasibility."""
    feasibility_indicators = [
        "data requirements", "model selection",
        "latency", "cost", "scalability",
        "fallback", "monitoring"
    ]

    plan_lower = plan.lower()
    found = sum(1 for k in feasibility_indicators if k in plan_lower)
    return min(found / 4, 1.0)


def evaluate_single(test_case: Dict, config: EvalConfig) -> TestResult:
    """Evaluate a single test case."""
    input_data = test_case["input"]
    expected = test_case.get("expected", {})

    output = generate_ai_feature_plan(input_data)
    plan = output.get("plan", "")

    # Handle non-AI features
    if not output.get("is_ai_feature"):
        if expected.get("handles_non_ai"):
            scores = {
                "ai_considerations": 1.0,
                "eval_strategy": 1.0,
                "responsible_ai": 1.0,
                "technical_feasibility": 1.0
            }
        else:
            scores = {
                "ai_considerations": 0.0,
                "eval_strategy": 0.0,
                "responsible_ai": 0.0,
                "technical_feasibility": 0.0
            }
    else:
        scores = {
            "ai_considerations": metric_ai_considerations(
                output.get("considerations", []), AI_CONSIDERATIONS
            ),
            "eval_strategy": metric_eval_strategy(plan),
            "responsible_ai": metric_responsible_ai(plan),
            "technical_feasibility": metric_technical_feasibility(plan),
        }

    # Pass if most metrics are good
    passed = sum(s >= 0.7 for s in scores.values()) >= 3

    return TestResult(
        test_id=f"ai_feature_{hash(str(input_data)) % 10000:04d}",
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
            print(f"  {status} - responsible_ai: {result.scores['responsible_ai']:.2f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate AI Feature Planning")
    parser.add_argument("--test-file", help="Custom test cases JSON file")
    parser.add_argument("--output", default="results/eval_pm_ai_feature.json")
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
        name="AI Feature Planning Evaluation",
        results=results,
        metrics=["ai_considerations", "eval_strategy", "responsible_ai", "technical_feasibility"],
        config={"test_file": config.test_file},
        metadata={"course": "product-management/ai-pm"}
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
