# AI Engineer Learning Roadmap

A comprehensive learning repository for AI engineering, agent development, and product management for technical teams.

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

### 3. Agent Roles Library (`agent-roles-library/`)

Library of reusable agent role definitions in XML/Markdown format for use with AI systems.

### 4. AI Agent Design Patterns (`ai-agent-design-patterns/`)

Documentation of common AI agent patterns: ReAct, RAG, multi-agent, tool use, and more.

### 5. Python Foundations (`python/30_day_foundation/`)

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
├── agent-roles-library/         # Reusable agent definitions
├── ai-agent-design-patterns/    # Design pattern documentation
└── python/                      # Python learning exercises
```

## Contributing

Contributions are welcome! Please see individual folder READMEs for specific guidelines.

## License

This educational content is provided for learning purposes.
