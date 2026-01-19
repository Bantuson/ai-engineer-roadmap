# Day 10 - Wednesday, January 28, 2026

## Day Theme
**Chain Composition** - Master LangChain's LCEL pattern.

## Schedule (Weekday: 13 Hours)

```
08:00 - 08:30  | PROMPT DRILL #1 - Agent Design
08:30 - 09:00  | PROMPT DRILL #2 - Prompt Techniques
09:00 - 09:30  | BREAKFAST BREAK
09:30 - 10:30  | READING (1h) - ai-agent-design-patterns/ (RAG patterns)
10:30 - 12:30  | PYTHON CHALLENGE (2h) - Days 15-16
12:30 - 13:30  | MINI-PROJECT WORK (1h) - LangChain Setup
13:30 - 14:00  | LUNCH BREAK
14:00 - 14:30  | PROMPT DRILL #3 - Security/Evaluation
14:30 - 16:30  | PM COURSE (2h) - PRD Writing Continued
16:30 - 19:00  | DSA/LEETCODE (2.5h) - Trees Introduction
19:00 - 19:30  | DINNER BREAK
19:30 - 20:30  | MINI-PROJECT WORK (1h) - LangChain testing
20:30 - 21:00  | DAILY REFLECTION + NOTES (30min)
```

## Learning Objectives

### Reading: RAG Design Patterns (1h)
- [ ] Read `ai-agent-design-patterns/rag.md` (or similar)
- [ ] RAG architecture patterns
- [ ] Chunking strategies
- [ ] Query optimization

**Key Questions to Answer:**
- What are the key RAG design patterns?
- How does chunking affect retrieval quality?
- What query optimization techniques exist?

### Python Challenge (Days 15-16)
- [ ] Basic unit testing concepts
- [ ] pytest basics
- [ ] Debugging with pdb
- [ ] Print debugging and logging

**Exercises:**
1. Write tests for a calculator function
2. Test edge cases (division by zero)
3. Use pdb to debug a broken function
4. Add logging to track execution flow

### Mini-Project: LangChain Translator (2h total)
- [ ] Navigate to `03_langchain_translator/`
- [ ] Understand LCEL pipe syntax
- [ ] Trace chain composition
- [ ] Test with multiple language pairs

**Key Concepts:**
- Prompt templates
- Pipe operator (|)
- Chain composition
- Output parsers

### PM: PRD Writing Continued (2h)
- [ ] Continue PRD mini-project
- [ ] User stories section
- [ ] Requirements (functional/non-functional)
- [ ] Design section

### DSA: Trees Introduction (2.5h)
**Problems:**
1. Maximum Depth of Binary Tree (LeetCode #104)
2. Invert Binary Tree (LeetCode #226)
3. Same Tree (LeetCode #100)

**Patterns:**
- Recursive tree traversal
- DFS basics
- Tree comparison

## Prompt Drills

### Drill #1: Agent Design (08:00-08:30)
**Topic:** Chain Design

1. **Prompt 1:** Design a multi-step translation chain
2. **Prompt 2:** Define intermediate processing steps
3. **Prompt 3:** Create chain with fallback behavior

### Drill #2: Prompt Techniques (08:30-09:00)
**Topic:** Template Design

4. **Prompt 4:** Design parameterized prompt template
5. **Prompt 5:** Create template with examples placeholder
6. **Prompt 6:** Design template for structured output

### Drill #3: Security/Evaluation (14:00-14:30)
**Topic:** Chain Security

7. **Prompt 7:** How to prevent injection in templates?
8. **Prompt 8:** Design input validation for translation
9. **Prompt 9:** Create safe variable interpolation

## LangChain Key Pattern

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator from {source} to {target}."),
    ("user", "Translate: {text}")
])

# Create chain with pipe operator
chain = prompt | llm | StrOutputParser()

# Run chain
result = chain.invoke({
    "source": "English",
    "target": "Spanish",
    "text": "Hello, world!"
})
```

## End of Day Checklist

- [ ] RAG patterns reading complete
- [ ] Python Days 15-16 completed
- [ ] LangChain project runs
- [ ] LCEL pattern understood
- [ ] PRD mini-project progressing
- [ ] 3 DSA tree problems solved
- [ ] 9 prompts written
- [ ] Daily log completed

## Tomorrow Preview (Day 11)
- Reading: evals/04-ab-testing-monitoring
- Python Days 17-18 (pathlib, datetime)
- OpenAI SDK Helpdesk (new project!)
- PM: APIs and Integration
- DSA: Tree traversal (BFS/DFS)
