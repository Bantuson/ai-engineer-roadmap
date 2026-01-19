# Week 2: Deep Dive (January 26 - February 1, 2026)

## Week Theme
**Expanding Breadth & Building Depth** - Master 4 new frameworks, write evaluation scripts, dive into Technical and AI PM.

## Schedule Overview

| Day | Date | Type | Python Focus | Project Focus | PM Focus |
|-----|------|------|--------------|---------------|----------|
| 8 | Mon Jan 26 | Weekday | Days 6-7 | LangGraph | Tech PM |
| 9 | Tue Jan 27 | Weekday | Days 8-9 | LangChain | PRD Writing |
| 10 | Wed Jan 28 | Weekday | Days 10-11 | OpenAI SDK | APIs |
| 11 | Thu Jan 29 | Weekday | Day 12 | Pydantic AI | Agile |
| 12 | Fri Jan 30 | Weekday | Eval code | Security Audits | AI PM Start |
| 13 | Sat Jan 31 | Weekend | Quiz | Interview Prep | Quiz |
| 14 | Sun Feb 1 | Weekend | Capstone | Eval System | Review |

## Key Learning Objectives

### Python (20-Day Challenge Days 6-12)
- Logging module
- Regex basics and practical use
- Environment configuration
- CLI arguments (argparse)
- API GET and POST requests

### Mini-Projects (4 frameworks)
1. **LangGraph Quiz Master** - StateGraph with nodes/edges
2. **LangChain Translator** - LCEL pipe operator chains
3. **OpenAI SDK Helpdesk** - Agent handoff/routing
4. **Pydantic AI Calculator** - @agent.tool decorator

### PM Deep Dive
- Technical PM fundamentals
- Working with Engineering
- PRD writing mini-project
- APIs and integration
- Agile methodologies
- AI PM introduction

### DSA Expansion
- Trees and BFS/DFS
- Graphs basics
- Linked lists
- Tree recursion patterns

## Daily Quick Links

- [Day 8 - Monday Jan 26](day08-mon.md)
- [Day 9 - Tuesday Jan 27](day09-tue.md)
- [Day 10 - Wednesday Jan 28](day10-wed.md)
- [Day 11 - Thursday Jan 29](day11-thu.md)
- [Day 12 - Friday Jan 30](day12-fri.md)
- [Day 13 - Saturday Jan 31](day13-sat.md)
- [Day 14 - Sunday Feb 1](day14-sun.md)

## Week 2 Deliverables

### Required
- [ ] 4 new mini-projects understood and running
- [ ] 4 evaluation scripts complete (one per project)
- [ ] Security audit for CrewAI + LlamaIndex
- [ ] PM PRD mini-project complete
- [ ] 20 DSA problems solved
- [ ] 51 prompts documented (weekday drills)

### Stretch Goals
- [ ] Additional eval metrics
- [ ] Security hardening started
- [ ] Extra DSA problems (25+)

## Resources for Week 2

### Python
- `learning-workflow/python/20_day_challenge/` - Days 06-12
- Focus on logging, regex, config, CLI, APIs

### Mini-Projects
- `agent-frameworks/mini-projects/02_langgraph_quiz_master/`
- `agent-frameworks/mini-projects/03_langchain_translator/`
- `agent-frameworks/mini-projects/04_openai_sdk_helpdesk/`
- `agent-frameworks/mini-projects/09_pydantic_ai_calculator/`

### PM Course
- `product-management/02-technical-pm/`
- `product-management/03-ai-product-management/`

### DSA
- `behavioral/02-leetcode-dsa/05-linked-lists/`
- `behavioral/02-leetcode-dsa/06-trees-graphs/`

### Security
- `vulnerabilities/02-prompt-injection/`
- `vulnerabilities/attack-library/`

### Reading Materials
- Monday/Thursday: `evals/` course
- Tuesday/Friday: `vulnerabilities/` course
- Wednesday: `ai-agent-design-patterns/`

## Key Patterns to Master

### LangGraph - StateGraph Pattern
```python
# Nodes define operations
# Edges define flow
# State accumulates through graph
```

### LangChain - LCEL Pattern
```python
# prompt | llm | parser
# Composable chains with pipe operator
```

### OpenAI SDK - Handoff Pattern
```python
# Router agent decides
# Specialist agents execute
# State transfers between agents
```

### Pydantic AI - Tool Pattern
```python
# @agent.tool decorator
# Type-safe tool definitions
# Automatic validation
```

## End of Week Reflection

Assess at week end:
- Framework understanding comparison
- Eval script effectiveness
- Security awareness growth
- Readiness for Week 3 integration
