# Capstone: Build a Complete Evaluation System

## Overview

Build an end-to-end evaluation system for the mini-projects that includes testing, monitoring, and reporting.

## Project Goals

By the end of this capstone, you will have:

1. **Evaluation Framework** - Reusable eval infrastructure
2. **Test Suite** - Comprehensive tests for all mini-projects
3. **Monitoring Dashboard** - Real-time quality tracking
4. **CI/CD Integration** - Automated evaluation on changes

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Evaluation System Architecture                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Eval Framework                        │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │   │
│  │  │ Metrics │  │  Judge  │  │ Report  │  │ Compare │   │   │
│  │  │ Library │  │  Models │  │  Gen    │  │  Tools  │   │   │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Test Runners                          │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │   │
│  │  │ CrewAI  │  │LangGraph│  │LangChain│  │   ...   │   │   │
│  │  │  Eval   │  │  Eval   │  │  Eval   │  │         │   │   │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                   │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                Results & Monitoring                      │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │   │
│  │  │  JSON   │  │  HTML   │  │ Alerts  │  │ Trends  │   │   │
│  │  │ Reports │  │Dashboard│  │         │  │         │   │   │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Evaluation Framework

### Directory Structure

```
evals/
├── scripts/
│   ├── shared/
│   │   ├── metrics.py       # ✓ Complete
│   │   ├── reporters.py     # ✓ Complete
│   │   ├── llm_judge.py     # ✓ Complete
│   │   └── test_runner.py   # TODO: Create
│   │
│   ├── eval_crewai_story.py
│   ├── eval_langgraph_quiz.py
│   ├── eval_langchain_translator.py
│   ├── eval_openai_helpdesk.py
│   ├── eval_llamaindex_study.py
│   ├── eval_autogen_debate.py
│   ├── eval_semantic_planner.py
│   ├── eval_claude_code.py
│   ├── eval_google_adk.py
│   ├── eval_pydantic_calculator.py  # ✓ Complete
│   ├── eval_pm_prd.py
│   └── eval_pm_ai_feature.py
│
├── golden_datasets/
│   ├── calculator_tests.json
│   ├── translator_tests.json
│   └── ...
│
└── baselines/
    └── v1.0.0/
        └── baseline.json
```

### Step 1.1: Test Runner Framework

Create `scripts/shared/test_runner.py`:

```python
"""
Universal test runner for mini-project evaluations.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import json
import argparse

from metrics import f1_score_text, keyword_coverage, bleu_score
from reporters import TestResult, generate_report, format_text_report, save_report


@dataclass
class EvalConfig:
    """Base evaluation configuration."""
    test_file: Optional[str] = None
    output_file: str = "results.json"
    verbose: bool = False
    report: bool = True
    metrics: List[str] = None


class BaseEvaluator(ABC):
    """Base class for mini-project evaluators."""

    def __init__(self, config: EvalConfig):
        self.config = config
        self.metrics_registry = {
            "f1": f1_score_text,
            "keyword_coverage": keyword_coverage,
            "bleu": bleu_score,
        }

    @abstractmethod
    def get_default_test_cases(self) -> List[Dict]:
        """Return default test cases."""
        pass

    @abstractmethod
    def run_system(self, test_input: Dict) -> Dict:
        """Run the system under test."""
        pass

    @abstractmethod
    def evaluate_output(self, output: Dict, expected: Dict) -> Dict[str, float]:
        """Calculate metrics for a single output."""
        pass

    def load_test_cases(self) -> List[Dict]:
        """Load test cases from file or defaults."""
        if self.config.test_file:
            with open(self.config.test_file) as f:
                return json.load(f)
        return self.get_default_test_cases()

    def run_evaluation(self) -> List[TestResult]:
        """Run complete evaluation."""
        test_cases = self.load_test_cases()
        results = []

        for i, test in enumerate(test_cases):
            if self.config.verbose:
                print(f"Running test {i+1}/{len(test_cases)}...")

            output = self.run_system(test["input"])
            scores = self.evaluate_output(output, test.get("expected", {}))
            passed = self.check_pass(scores)

            results.append(TestResult(
                test_id=test.get("id", f"test_{i:04d}"),
                input_data=test["input"],
                output=output,
                expected=test.get("expected"),
                scores=scores,
                passed=passed,
                metadata=test.get("metadata", {})
            ))

        return results

    def check_pass(self, scores: Dict[str, float]) -> bool:
        """Determine if test passed based on scores."""
        # Default: pass if primary metric >= 0.7
        primary = list(scores.values())[0] if scores else 0
        return primary >= 0.7

    def run(self):
        """Execute evaluation and generate report."""
        results = self.run_evaluation()

        report = generate_report(
            name=self.__class__.__name__,
            results=results,
            metrics=list(self.metrics_registry.keys()),
            config=vars(self.config),
            metadata={"evaluator": self.__class__.__name__}
        )

        if self.config.report:
            print(format_text_report(report))

        save_report(report, self.config.output_file)
        print(f"\nResults saved to: {self.config.output_file}")

        return report
```

### Step 1.2: LLM Judge Enhancement

Enhance `scripts/shared/llm_judge.py` with rubric-based evaluation:

```python
"""
LLM-as-Judge evaluation with rubrics.
"""

RUBRICS = {
    "story_quality": {
        "criteria": [
            {
                "name": "creativity",
                "description": "Originality and imagination",
                "weight": 0.3
            },
            {
                "name": "coherence",
                "description": "Logical flow and consistency",
                "weight": 0.3
            },
            {
                "name": "engagement",
                "description": "Reader interest and enjoyment",
                "weight": 0.2
            },
            {
                "name": "theme_adherence",
                "description": "Follows the given theme",
                "weight": 0.2
            }
        ]
    },
    "translation_quality": {
        "criteria": [
            {
                "name": "accuracy",
                "description": "Correct meaning preservation",
                "weight": 0.4
            },
            {
                "name": "fluency",
                "description": "Natural language in target",
                "weight": 0.3
            },
            {
                "name": "completeness",
                "description": "All content translated",
                "weight": 0.3
            }
        ]
    },
    "helpdesk_quality": {
        "criteria": [
            {
                "name": "relevance",
                "description": "Addresses the user's question",
                "weight": 0.3
            },
            {
                "name": "accuracy",
                "description": "Information is correct",
                "weight": 0.3
            },
            {
                "name": "helpfulness",
                "description": "Provides actionable guidance",
                "weight": 0.2
            },
            {
                "name": "tone",
                "description": "Professional and empathetic",
                "weight": 0.2
            }
        ]
    }
}


def evaluate_with_rubric(
    content: str,
    rubric_name: str,
    context: Dict = None,
    judge_model = None
) -> Dict[str, float]:
    """
    Evaluate content using rubric criteria.

    Args:
        content: Content to evaluate
        rubric_name: Name of rubric to use
        context: Additional context (query, theme, etc.)
        judge_model: LLM judge function

    Returns:
        Scores for each criterion and overall
    """
    rubric = RUBRICS.get(rubric_name)
    if not rubric:
        raise ValueError(f"Unknown rubric: {rubric_name}")

    scores = {}

    for criterion in rubric["criteria"]:
        prompt = f"""
Rate the following content on {criterion['name']} ({criterion['description']}).
Score from 1-5 where:
1 = Poor
2 = Below average
3 = Average
4 = Good
5 = Excellent

Content:
{content}

{f"Context: {context}" if context else ""}

Provide only the numeric score (1-5):
"""
        if judge_model:
            response = judge_model(prompt)
            try:
                score = int(response.strip()[0]) / 5.0
            except:
                score = 0.5
        else:
            score = 0.5  # Default if no judge

        scores[criterion["name"]] = score

    # Calculate weighted overall
    overall = sum(
        scores[c["name"]] * c["weight"]
        for c in rubric["criteria"]
    )
    scores["overall"] = overall

    return scores
```

## Phase 2: Mini-Project Evaluators

### Evaluation Matrix

| Mini-Project | Metrics | Rubric |
|-------------|---------|--------|
| CrewAI Story | creativity, coherence, theme | story_quality |
| LangGraph Quiz | accuracy, explanation | quiz_quality |
| LangChain Translator | BLEU, fluency | translation_quality |
| OpenAI Helpdesk | relevance, tone | helpdesk_quality |
| LlamaIndex Study | retrieval, answer | rag_quality |
| AutoGen Debate | argument, counter | debate_quality |
| Semantic Planner | completeness, feasibility | plan_quality |
| Claude Code | correctness, safety | code_quality |
| Google ADK | intent, action | voice_quality |
| Pydantic Calculator | accuracy, tool_use | calculation_quality |

### Step 2.1: Create Evaluators

Each evaluator follows this pattern:

```python
#!/usr/bin/env python3
"""
Example evaluator structure.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shared'))

from test_runner import BaseEvaluator, EvalConfig
from typing import Dict, List

class MyProjectEvaluator(BaseEvaluator):
    """Evaluator for my mini-project."""

    def get_default_test_cases(self) -> List[Dict]:
        return [
            {
                "id": "test_001",
                "input": {"query": "..."},
                "expected": {"answer": "..."}
            },
            # More test cases...
        ]

    def run_system(self, test_input: Dict) -> Dict:
        # Import and run the mini-project
        # from mini_project import main
        # return main.process(test_input)
        pass

    def evaluate_output(self, output: Dict, expected: Dict) -> Dict[str, float]:
        # Calculate relevant metrics
        return {
            "metric1": 0.9,
            "metric2": 0.85,
        }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-file", help="Test cases file")
    parser.add_argument("--output", default="results.json")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    config = EvalConfig(
        test_file=args.test_file,
        output_file=args.output,
        verbose=args.verbose,
        report=args.report
    )

    evaluator = MyProjectEvaluator(config)
    evaluator.run()
```

## Phase 3: Golden Datasets

### Step 3.1: Create Dataset for Each Project

Create `golden_datasets/calculator_tests.json`:

```json
{
  "name": "Calculator Golden Dataset",
  "version": "1.0.0",
  "test_cases": [
    {
      "id": "calc_001",
      "category": "basic",
      "input": {"query": "What is 5 + 3?"},
      "expected": {"result": 8, "operation": "addition"}
    }
  ]
}
```

### Step 3.2: Dataset Validation

```python
def validate_golden_dataset(filepath: str) -> bool:
    """Validate golden dataset format."""
    with open(filepath) as f:
        data = json.load(f)

    required = ["name", "version", "test_cases"]
    for field in required:
        if field not in data:
            print(f"Missing: {field}")
            return False

    for i, tc in enumerate(data["test_cases"]):
        if "id" not in tc or "input" not in tc:
            print(f"Invalid test case {i}")
            return False

    print(f"Valid: {len(data['test_cases'])} test cases")
    return True
```

## Phase 4: CI/CD Integration

### GitHub Actions Workflow

Create `.github/workflows/eval.yml`:

```yaml
name: Evaluation Pipeline

on:
  push:
    paths:
      - 'agent-frameworks/mini-projects/**'
      - 'evals/**'
  pull_request:

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r evals/requirements.txt

      - name: Run evaluations
        env:
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
        run: |
          cd evals/scripts
          python run_all_evals.py --output results/

      - name: Check thresholds
        run: python evals/scripts/check_thresholds.py results/

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: eval-results
          path: evals/results/
```

## Phase 5: Monitoring Dashboard

### Simple HTML Dashboard

Create `evals/dashboard/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Evaluation Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Mini-Project Evaluation Dashboard</h1>

    <div id="summary">
        <h2>Summary</h2>
        <table id="summary-table"></table>
    </div>

    <div id="charts">
        <canvas id="pass-rate-chart"></canvas>
        <canvas id="metrics-chart"></canvas>
    </div>

    <script>
        // Load and display results
        fetch('results/summary.json')
            .then(r => r.json())
            .then(data => renderDashboard(data));

        function renderDashboard(data) {
            // Render summary table
            // Render charts
        }
    </script>
</body>
</html>
```

## Deliverables Checklist

- [ ] **Framework**
  - [ ] `shared/test_runner.py` - Base evaluator class
  - [ ] Enhanced `shared/llm_judge.py` - Rubric evaluation
  - [ ] `shared/dataset_utils.py` - Dataset utilities

- [ ] **Evaluators** (12 total)
  - [ ] `eval_crewai_story.py`
  - [ ] `eval_langgraph_quiz.py`
  - [ ] `eval_langchain_translator.py`
  - [ ] `eval_openai_helpdesk.py`
  - [ ] `eval_llamaindex_study.py`
  - [ ] `eval_autogen_debate.py`
  - [ ] `eval_semantic_planner.py`
  - [ ] `eval_claude_code.py`
  - [ ] `eval_google_adk.py`
  - [ ] `eval_pydantic_calculator.py` ✓
  - [ ] `eval_pm_prd.py`
  - [ ] `eval_pm_ai_feature.py`

- [ ] **Golden Datasets**
  - [ ] One per mini-project
  - [ ] Minimum 10 test cases each
  - [ ] Include edge cases

- [ ] **Baselines**
  - [ ] Initial baseline for each project
  - [ ] Version v1.0.0

- [ ] **CI/CD**
  - [ ] GitHub Actions workflow
  - [ ] Threshold checks
  - [ ] Artifact storage

- [ ] **Dashboard**
  - [ ] Summary view
  - [ ] Historical trends
  - [ ] Per-project details

## Success Criteria

| Criterion | Threshold |
|-----------|-----------|
| All evaluators run without error | 100% |
| Pass rate per project | ≥ 70% |
| Test coverage per project | ≥ 10 cases |
| CI pipeline success rate | ≥ 95% |

## Time Estimate

| Phase | Duration |
|-------|----------|
| 1. Framework | 2-3 hours |
| 2. Evaluators | 4-6 hours |
| 3. Datasets | 2-3 hours |
| 4. CI/CD | 1-2 hours |
| 5. Dashboard | 2-3 hours |
| **Total** | **11-17 hours** |

## Next Steps

After completing this capstone:
1. Run evaluations on all mini-projects
2. Identify lowest-performing areas
3. Iterate on prompts/systems to improve
4. Set up automated regression detection
