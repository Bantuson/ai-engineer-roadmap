# Agent Evaluation Course

A comprehensive course on evaluating AI agents and LLM-based systems for production deployment.

## Course Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 15-20 hours |
| **Prerequisites** | Basic Python, familiarity with LLMs |
| **Outcomes** | Build production-grade evaluation systems |

## Why Evaluations Matter

In production AI systems:
- **Quality assurance** - Ensure outputs meet standards
- **Regression detection** - Catch degradation early
- **Continuous improvement** - Data-driven optimization
- **Trust building** - Demonstrate reliability to stakeholders

## Course Structure

```
evals/
├── 01-evaluation-fundamentals/
│   ├── 01-why-evals-matter.md
│   ├── 02-evaluation-metrics.md
│   └── 03-eval-types-comparison.md
├── 02-eval-frameworks/
│   ├── 01-ragas-deepeval.md
│   ├── 02-custom-eval-scripts.md
│   ├── 03-llm-as-judge.md
│   └── mini-project-eval-suite/
├── 03-testing-ai-features/
│   ├── 01-unit-integration-tests.md
│   ├── 02-regression-testing.md
│   └── 03-golden-datasets.md
├── 04-ab-testing-monitoring/
│   ├── 01-ab-testing.md
│   ├── 02-production-monitoring.md
│   └── 03-drift-detection.md
├── 05-capstone-eval-system/
│   └── README.md
└── scripts/
    ├── eval_crewai_story.py
    ├── eval_langgraph_quiz.py
    ├── eval_langchain_translator.py
    ├── eval_openai_helpdesk.py
    ├── eval_llamaindex_study.py
    ├── eval_autogen_debate.py
    ├── eval_semantic_planner.py
    ├── eval_pydantic_calculator.py
    ├── eval_claude_code.py
    ├── eval_google_adk.py
    ├── eval_pm_prd.py
    ├── eval_pm_ai_feature.py
    └── shared/
        ├── metrics.py
        ├── reporters.py
        └── llm_judge.py
```

## Module Overview

### Module 1: Evaluation Fundamentals
- Why evaluations matter in production
- Types of metrics (accuracy, quality, safety)
- Comparison of evaluation approaches

### Module 2: Eval Frameworks
- RAGAS and DeepEval for RAG systems
- Building custom evaluation scripts
- LLM-as-judge techniques

### Module 3: Testing AI Features
- Unit and integration testing for AI
- Regression testing strategies
- Creating golden datasets

### Module 4: A/B Testing & Monitoring
- Setting up A/B tests for AI features
- Production monitoring approaches
- Detecting model drift

### Module 5: Capstone
- Build a complete evaluation system
- Integrate with mini-projects
- Generate reports

## Evaluation Scripts

The `scripts/` directory contains evaluation scripts for each mini-project:

| Script | Mini-Project | Key Metrics |
|--------|--------------|-------------|
| eval_crewai_story.py | Story Crew | Creativity, Coherence |
| eval_llamaindex_study.py | Study Buddy | Retrieval, Accuracy |
| eval_langgraph_quiz.py | Quiz Master | Question Quality |
| eval_langchain_translator.py | Translator | Translation Quality |
| eval_openai_helpdesk.py | Helpdesk | Routing Accuracy |
| eval_pydantic_calculator.py | Calculator | Calculation Accuracy |
| eval_google_adk.py | Voice Assistant | Recognition, Response |
| eval_autogen_debate.py | Debate Club | Argument Quality |
| eval_semantic_planner.py | Planner | Plan Quality |
| eval_claude_code.py | Code Helper | Code Quality |

## Quick Start

```bash
# Navigate to scripts
cd evals/scripts

# Run a specific eval
python eval_pydantic_calculator.py

# Run with test cases
python eval_llamaindex_study.py --test-file tests.json

# Generate report
python eval_crewai_story.py --report
```

## Key Concepts

### Evaluation Types
1. **Automated metrics** - BLEU, ROUGE, exact match
2. **LLM-as-judge** - Use LLMs to evaluate quality
3. **Human evaluation** - Gold standard for subjective tasks
4. **Behavioral testing** - Test specific capabilities

### Metrics Categories
1. **Accuracy metrics** - How correct are outputs?
2. **Quality metrics** - How good are outputs?
3. **Safety metrics** - Are outputs safe?
4. **Efficiency metrics** - How fast/cheap?

### Best Practices
1. **Define clear criteria** before building
2. **Create golden datasets** for consistency
3. **Combine multiple metrics** for robustness
4. **Monitor continuously** in production
5. **Version your evaluations** like code

## Learning Path

1. Read fundamentals (Module 1)
2. Understand frameworks (Module 2)
3. Practice with scripts
4. Learn testing patterns (Module 3)
5. Study production practices (Module 4)
6. Complete capstone (Module 5)

## Related Resources

- [Mini-Projects](../agent-frameworks/mini-projects/)
- [AI Agent Design Patterns](../ai-agent-design-patterns/)
- [Learning Workflow](../learning-workflow/)
