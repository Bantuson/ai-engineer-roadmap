# Day 11 - Thursday, January 29, 2026

## Day Theme
**Agent Handoff** - Master the OpenAI SDK's multi-agent routing pattern.

## Schedule (Weekday: 13 Hours)

```
08:00 - 08:30  | PROMPT DRILL #1 - Agent Design
08:30 - 09:00  | PROMPT DRILL #2 - Prompt Techniques
09:00 - 09:30  | BREAKFAST BREAK
09:30 - 10:30  | READING (1h) - evals/04-ab-testing-monitoring
10:30 - 12:30  | PYTHON CHALLENGE (2h) - Days 17-18
12:30 - 13:30  | MINI-PROJECT WORK (1h) - OpenAI SDK Setup
13:30 - 14:00  | LUNCH BREAK
14:00 - 14:30  | PROMPT DRILL #3 - Security/Evaluation
14:30 - 16:30  | PM COURSE (2h) - APIs & Integration
16:30 - 19:00  | DSA/LEETCODE (2.5h) - Tree Traversal
19:00 - 19:30  | DINNER BREAK
19:30 - 20:30  | MINI-PROJECT WORK (1h) - OpenAI SDK testing
20:30 - 21:00  | DAILY REFLECTION + NOTES (30min)
```

## Learning Objectives

### Reading: A/B Testing & Monitoring (1h)
- [ ] Read `evals/04-ab-testing-monitoring/README.md`
- [ ] A/B testing for AI features
- [ ] Production monitoring patterns
- [ ] Drift detection

**Key Questions to Answer:**
- How do you A/B test AI features?
- What metrics to monitor in production?
- What is drift and how do you detect it?

### Python Challenge (Days 17-18)
- [ ] Modern path handling with pathlib
- [ ] Path operations and manipulation
- [ ] Dates and times with datetime
- [ ] Date formatting and parsing

**Exercises:**
1. Use pathlib to list files in a directory
2. Create paths and check if they exist
3. Parse dates from strings
4. Calculate date differences

### Mini-Project: OpenAI SDK Helpdesk (2h total)
- [ ] Navigate to `04_openai_sdk_helpdesk/`
- [ ] Understand triage/routing pattern
- [ ] See how agents hand off to each other
- [ ] Test with different support scenarios

**Key Concepts:**
- Router agent pattern
- Specialist agents
- Context handoff
- State management across agents

### PM: APIs and Integration (2h)
- [ ] Read `02-technical-pm/03-apis-integration.md`
- [ ] API design basics
- [ ] Integration patterns
- [ ] Technical debt considerations

### DSA: Tree Traversal (2.5h)
**Problems:**
1. Binary Tree Level Order Traversal (LeetCode #102)
2. Validate Binary Search Tree (LeetCode #98)
3. Symmetric Tree (LeetCode #101)

**Patterns:**
- BFS with queue
- DFS (inorder, preorder, postorder)
- Level-order traversal

## Prompt Drills

### Drill #1: Agent Design (08:00-08:30)
**Topic:** Router Agent Design

1. **Prompt 1:** Design a triage agent for customer support
2. **Prompt 2:** Define specialist agent roles (billing, tech, sales)
3. **Prompt 3:** Create handoff protocol between agents

### Drill #2: Prompt Techniques (08:30-09:00)
**Topic:** Classification Prompts

4. **Prompt 4:** Design intent classification prompt
5. **Prompt 5:** Create confidence scoring for routing
6. **Prompt 6:** Handle ambiguous requests

### Drill #3: Security/Evaluation (14:00-14:30)
**Topic:** Multi-Agent Security

7. **Prompt 7:** Prevent unauthorized agent access
8. **Prompt 8:** Design agent authentication
9. **Prompt 9:** Create audit trail for agent actions

## Agent Handoff Pattern

```
Customer Query → Triage Agent → Route to Specialist → Response

Specialists:
- Billing Agent: Refunds, payments, subscriptions
- Technical Agent: Bugs, features, how-to
- Sales Agent: Pricing, upgrades, enterprise
```

## End of Day Checklist

- [ ] A/B testing reading complete
- [ ] Python Days 17-18 completed
- [ ] OpenAI SDK project runs
- [ ] Handoff pattern understood
- [ ] PM APIs lesson complete
- [ ] 3 DSA tree problems solved
- [ ] 9 prompts written
- [ ] Daily log completed

## Tomorrow Preview (Day 12)
- Reading: vulnerabilities/04-data-model-security
- Python Days 19-20 (mini-project, capstone)
- Pydantic AI Calculator (new project!)
- PM: Agile methodologies
- DSA: Graph basics
