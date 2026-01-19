# Day 3 - Wednesday, January 21, 2026

## Day Theme
**Testing & Experimentation** - Push CrewAI to its limits, learn about error handling and design patterns.

## Schedule (Weekday: 13 Hours)

```
08:00 - 08:30  | PROMPT DRILL #1 - Agent Design
08:30 - 09:00  | PROMPT DRILL #2 - Prompt Techniques
09:00 - 09:30  | BREAKFAST BREAK
09:30 - 10:30  | READING (1h) - ai-agent-design-patterns/
10:30 - 12:30  | PYTHON CHALLENGE (2h) - Days 5-6
12:30 - 13:30  | MINI-PROJECT WORK (1h) - CrewAI Testing
13:30 - 14:00  | LUNCH BREAK
14:00 - 14:30  | PROMPT DRILL #3 - Security/Evaluation
14:30 - 16:30  | PM COURSE (2h) - Strategy
16:30 - 19:00  | DSA/LEETCODE (2.5h) - Hashmaps
19:00 - 19:30  | DINNER BREAK
19:30 - 20:30  | MINI-PROJECT WORK (1h) - Eval script start
20:30 - 21:00  | DAILY REFLECTION + NOTES (30min)
```

## Learning Objectives

### Reading: AI Agent Design Patterns (1h)
- [ ] Read `ai-agent-design-patterns/README.md`
- [ ] ReAct pattern overview
- [ ] Multi-agent patterns

**Key Questions to Answer:**
- What is the ReAct pattern and when to use it?
- How do multi-agent systems coordinate?
- What patterns does CrewAI implement?

### Python Challenge (Days 5-6)
- [ ] Try/except error handling
- [ ] Custom exceptions
- [ ] Logging module basics
- [ ] Log levels and formatting

**Exercises:**
1. Handle file not found errors gracefully
2. Create custom validation exceptions
3. Set up basic logging to file
4. Log at different levels (INFO, WARNING, ERROR)

### Mini-Project: CrewAI Testing + Eval Start (2h total)
- [ ] Test with 5 different story themes
- [ ] Document output quality for each
- [ ] Identify what makes good vs bad output
- [ ] Define evaluation criteria
- [ ] Start designing eval_crewai_story.py

**Testing Scenarios:**
1. Simple theme: "A cat's adventure"
2. Complex theme: "Time travel paradox"
3. Abstract theme: "The color of loneliness"
4. Edge case: Very short input
5. Edge case: Very long/detailed input

### PM: Product Strategy (2h)
- [ ] Read `02-strategy.md`
- [ ] Vision and mission
- [ ] Market analysis basics
- [ ] Competitive positioning

### DSA: Hashmaps (2.5h)
**Problems:**
1. Valid Anagram (LeetCode #242)
2. Group Anagrams (LeetCode #49)
3. Top K Frequent Elements (LeetCode #347)

**Patterns:**
- Character frequency counting
- Hash as key technique
- Heap with hashmap

## Prompt Drills

### Drill #1: Agent Design (08:00-08:30)
**Topic:** Agent Collaboration

1. **Prompt 1:** Design a handoff protocol between agents
2. **Prompt 2:** Define shared context between agents
3. **Prompt 3:** Create conflict resolution rules for agents

### Drill #2: Prompt Techniques (08:30-09:00)
**Topic:** Structured Output

4. **Prompt 4:** Design a JSON output format for story
5. **Prompt 5:** Create XML structured response
6. **Prompt 6:** Design markdown-formatted output

### Drill #3: Security/Evaluation (14:00-14:30)
**Topic:** Prompt Injection Awareness

7. **Prompt 7:** What is prompt injection?
8. **Prompt 8:** Example of injection in story context
9. **Prompt 9:** Basic defense: instruction anchoring

## Eval Script Design

### eval_crewai_story.py - Design Notes

```python
"""
CrewAI Story Evaluation Script

Metrics to evaluate:
1. Creativity (1-5): Novel elements, unexpected twists
2. Coherence (1-5): Logical flow, no contradictions
3. Theme adherence (1-5): How well it matches input theme
4. Grammar (1-5): Language quality
5. Engagement (1-5): Would reader continue?

Approach:
- Run story generation multiple times
- Use LLM-as-judge for subjective metrics
- Calculate averages and variance
"""
```

## End of Day Checklist

- [ ] Design patterns reading complete
- [ ] Python Days 5-6 completed
- [ ] CrewAI tested with 5 themes
- [ ] Eval criteria documented
- [ ] Eval script structure designed
- [ ] PM Strategy lesson complete
- [ ] 3 DSA problems solved
- [ ] 9 prompts written
- [ ] Daily log completed

## Tomorrow Preview (Day 4)
- Reading: evals/02-eval-frameworks
- Python Days 7-8 (regex basics)
- LlamaIndex setup (new project!)
- PM: Roadmapping
- DSA: Two pointers technique
