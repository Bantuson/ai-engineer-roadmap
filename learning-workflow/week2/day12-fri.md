# Day 12 - Friday, January 30, 2026

## Day Theme
**Type-Safe Agents** - Master Pydantic AI's tool decorator pattern.

## Schedule (Weekday: 13 Hours)

```
08:00 - 08:30  | PROMPT DRILL #1 - Agent Design
08:30 - 09:00  | PROMPT DRILL #2 - Prompt Techniques
09:00 - 09:30  | BREAKFAST BREAK
09:30 - 10:30  | READING (1h) - vulnerabilities/04-data-model-security
10:30 - 12:30  | PYTHON CHALLENGE (2h) - Days 19-20
12:30 - 13:30  | MINI-PROJECT WORK (1h) - Pydantic AI Setup
13:30 - 14:00  | LUNCH BREAK
14:00 - 14:30  | PROMPT DRILL #3 - Security/Evaluation
14:30 - 16:30  | PM COURSE (2h) - Agile Methodologies
16:30 - 19:00  | DSA/LEETCODE (2.5h) - Graphs Introduction
19:00 - 19:30  | DINNER BREAK
19:30 - 20:30  | MINI-PROJECT WORK (1h) - Pydantic AI testing
20:30 - 21:00  | DAILY REFLECTION + NOTES (30min)
```

## Learning Objectives

### Reading: Data & Model Security (1h)
- [ ] Read `vulnerabilities/04-data-model-security/README.md`
- [ ] Data poisoning attacks
- [ ] Model extraction risks
- [ ] Adversarial inputs

**Key Questions to Answer:**
- How can training data be poisoned?
- What is model extraction?
- How do adversarial inputs work?

### Python Challenge (Days 19-20)
- [ ] Build CLI tool combining concepts
- [ ] Capstone mini-project
- [ ] Code organization
- [ ] End-to-end application

**Exercises:**
1. Build a CLI file organizer tool
2. Implement using argparse, pathlib, json
3. Add error handling and logging
4. Create a complete working tool

### Mini-Project: Pydantic AI Calculator (2h total)
- [ ] Navigate to `09_pydantic_ai_calculator/`
- [ ] Understand @agent.tool decorator
- [ ] See type validation in action
- [ ] Test various calculations

**Key Concepts:**
- Tool definitions with decorators
- Pydantic type validation
- Automatic schema generation
- Error handling with types

### PM: Agile Methodologies (2h)
- [ ] Read `02-technical-pm/04-agile.md`
- [ ] Scrum basics
- [ ] Sprint planning
- [ ] Backlog management

### DSA: Graphs Introduction (2.5h)
**Problems:**
1. Number of Islands (LeetCode #200)
2. Clone Graph (LeetCode #133)
3. Course Schedule (LeetCode #207)

**Patterns:**
- Graph BFS/DFS
- Adjacency list representation
- Cycle detection

## Prompt Drills

### Drill #1: Agent Design (08:00-08:30)
**Topic:** Tool Design

1. **Prompt 1:** Design calculator tool with clear inputs/outputs
2. **Prompt 2:** Define validation rules for tool parameters
3. **Prompt 3:** Create error handling for tool failures

### Drill #2: Prompt Techniques (08:30-09:00)
**Topic:** Type-Guided Prompts

4. **Prompt 4:** Design prompt expecting specific JSON structure
5. **Prompt 5:** Create validation prompt for numeric input
6. **Prompt 6:** Handle type conversion in prompts

### Drill #3: Security/Evaluation (14:00-14:30)
**Topic:** Tool Security

7. **Prompt 7:** Prevent arbitrary code execution through tools
8. **Prompt 8:** Design safe math evaluation
9. **Prompt 9:** Create sandboxed tool execution

## Pydantic AI Pattern

```python
from pydantic_ai import Agent

agent = Agent('deepseek:deepseek-chat')

@agent.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@agent.tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## Week 2 Progress Check

**Mini-Projects Status:**
- [ ] LangGraph Quiz Master: Complete
- [ ] LangChain Translator: Complete
- [ ] OpenAI SDK Helpdesk: Complete
- [ ] Pydantic AI Calculator: Complete

## End of Day Checklist

- [ ] Data/model security reading complete
- [ ] Python Days 19-20 completed
- [ ] Pydantic AI project runs
- [ ] Tool decorator pattern understood
- [ ] PM Agile lesson complete
- [ ] 3 DSA graph problems solved
- [ ] 9 prompts written
- [ ] Daily log completed

## Tomorrow Preview (Day 13 - Saturday)
- Weekend schedule: Quiz + Interview Prep
- Weekly assessment
- DSA timed practice
- Week review
