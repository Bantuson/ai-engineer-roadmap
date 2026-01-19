# AI Engineer Learning Roadmap

A comprehensive learning repository for AI engineering, agent development, product management, and interview preparation for technical teams.

## What's Inside

### 1. Agent Frameworks (`agent-frameworks/`)

Documentation and hands-on mini-projects for 10 AI agent frameworks:
- CrewAI, LangGraph, LangChain, OpenAI SDK, Google ADK
- Claude SDK, LlamaIndex, AutoGen, Semantic Kernel, Pydantic AI

Each mini-project demonstrates a different framework pattern—from multi-agent systems to RAG implementations.

### 2. Product Management (`product-management/`)

A comprehensive, self-study product management course for technical teams:
- **Foundations** — Core PM concepts (user research, strategy, roadmapping, metrics)
- **Technical PM** — Working with engineering teams, writing PRDs, APIs
- **AI Product Management** — Managing AI/ML products, evaluation, responsible AI
- **Prompt Engineering for PMs** — Using AI for productivity, production prompts
- **Frameworks & Tools** — Prioritization, stakeholder management, modern PM toolkit
- **Capstone Projects** — Portfolio-ready projects demonstrating PM skills

Designed for developers transitioning to PM or technical professionals working alongside product teams.

### 3. Agent Evals (`evals/`)

Production-grade LLM evaluation course with practical scripts:
- **Evaluation Fundamentals** — Why evals matter, metrics, eval types
- **Eval Frameworks** — RAGAS, DeepEval, custom scripts, LLM-as-judge
- **Testing AI Features** — Unit tests, integration tests, golden datasets
- **A/B Testing & Monitoring** — Production monitoring, drift detection
- **Eval Scripts** — Ready-to-run evaluation scripts for all mini-projects

Includes shared modules for metrics (BLEU, ROUGE, F1), LLM-as-judge, and reporting.

### 4. AI Security (`vulnerabilities/`)

AI security course covering threats, attacks, and defenses:
- **Threat Landscape** — OWASP Top 10 for LLMs, attack surface mapping
- **Prompt Injection** — Direct/indirect attacks, defense strategies
- **Jailbreaking** — Techniques, guardrail bypasses, defense mechanisms
- **Data & Model Security** — Data poisoning, model extraction, adversarial attacks
- **Defense Strategies** — Input/output validation, rate limiting, monitoring
- **AI Red Teaming** — Methodology, attack playbooks, capstone exercise
- **Attack Library** — Reference patterns for security testing

### 5. Interview Prep (`behavioral/`)

Comprehensive interview preparation for AI Engineer and AI PM roles:
- **Behavioral Interviews** — STAR method, leadership principles, storytelling
- **DSA/LeetCode** — Pattern-based approach (50+ problems across 9 categories)
- **AI Engineer Interviews** — Python proficiency, frameworks, prompt engineering, system design
- **AI PM Interviews** — Product sense, technical depth, AI-specific challenges

Includes question banks, mock interview guides, and mental models.

### 6. Learning Workflow (`learning-workflow/`)

3-week intensive study program (Jan 19 - Feb 7, 2026):
- **Daily Schedule** — 13-hour weekday structure, 6-hour weekend plans
- **Week-by-Week Plans** — Daily objectives, exercises, deliverables
- **Prompt Drills** — 240 prompts across agent design, security, evaluation
- **Trackers** — Progress tracking, skill checklists, deliverables tracker

Structured to build Python, PM, DSA, and AI engineering skills in parallel.

### 7. Agent Roles Library (`agent-roles-library/`)

Library of reusable agent role definitions in XML/Markdown format for use with AI systems.

### 8. AI Agent Design Patterns (`ai-agent-design-patterns/`)

Documentation of common AI agent patterns: ReAct, RAG, multi-agent, tool use, and more.

### 9. Python Foundations (`python/30_day_foundation/`)

Python fundamentals exercises organized as a 30-day learning path.

## Quick Start

### Running AI Agent Mini-Projects

```bash
# Set API key
export DEEPSEEK_API_KEY="your-key"

# Install dependencies
cd agent-frameworks/mini-projects/
pip install -r requirements.txt

# Run a project
cd 09_pydantic_ai_calculator
python main.py
```

### Starting the PM Course

Begin with [`product-management/README.md`](product-management/README.md) for the learning path overview.

## Repository Structure

```
ai-engineer-roadmap/
├── agent-frameworks/
│   ├── documentation/           # Framework documentation
│   └── mini-projects/           # 10 hands-on projects
├── product-management/
│   ├── 01-foundations/          # PM fundamentals
│   ├── 02-technical-pm/         # Working with engineering
│   ├── 03-ai-product-management/# AI/ML product skills
│   ├── 04-prompt-engineering-pm/# AI for PM workflows
│   ├── 05-frameworks-tools/     # PM frameworks and toolkit
│   ├── 06-capstone-projects/    # Portfolio projects
│   └── resources/               # Templates and reading list
├── evals/
│   ├── 01-evaluation-fundamentals/  # Core eval concepts
│   ├── 02-eval-frameworks/          # RAGAS, DeepEval, LLM-as-judge
│   ├── 03-testing-ai-features/      # Unit/integration tests
│   ├── 04-ab-testing-monitoring/    # Production monitoring
│   ├── 05-capstone-eval-system/     # Capstone project
│   └── scripts/                     # Runnable eval scripts
├── vulnerabilities/
│   ├── 01-threat-landscape/         # OWASP Top 10, attack surface
│   ├── 02-prompt-injection/         # Injection attacks & defenses
│   ├── 03-jailbreaking/             # Jailbreak techniques
│   ├── 04-data-model-security/      # Data/model attacks
│   ├── 05-defense-strategies/       # Defense patterns
│   ├── 06-ai-red-teaming/           # Red team methodology
│   └── attack-library/              # Attack reference patterns
├── behavioral/
│   ├── 01-behavioral-interviews/    # STAR method, leadership
│   ├── 02-leetcode-dsa/             # Pattern-based DSA prep
│   ├── 03-ai-engineer-interviews/   # Technical AI interviews
│   └── 04-ai-pm-interviews/         # AI PM interviews
├── learning-workflow/
│   ├── overview/                    # 3-week roadmap, schedules
│   ├── week1/                       # Jan 19-25 daily plans
│   ├── week2/                       # Jan 26-Feb 1 daily plans
│   ├── week3/                       # Feb 2-7 daily plans
│   ├── prompt-drills/               # Daily prompt exercises
│   └── trackers/                    # Progress tracking
├── agent-roles-library/         # Reusable agent definitions
├── ai-agent-design-patterns/    # Design pattern documentation
└── python/                      # Python learning exercises
```

## Contributing

Contributions are welcome! Please see individual folder READMEs for specific guidelines.

## License

This educational content is provided for learning purposes.
