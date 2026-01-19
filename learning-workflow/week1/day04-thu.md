# Day 4 - Thursday, January 22, 2026

## Day Theme
**New Framework Day** - Transition to LlamaIndex, learn about RAG and regex.

## Schedule (Weekday: 13 Hours)

```
08:00 - 08:30  | PROMPT DRILL #1 - Agent Design
08:30 - 09:00  | PROMPT DRILL #2 - Prompt Techniques
09:00 - 09:30  | BREAKFAST BREAK
09:30 - 10:30  | READING (1h) - evals/02-eval-frameworks
10:30 - 12:30  | PYTHON CHALLENGE (2h) - Days 7-8
12:30 - 13:30  | MINI-PROJECT WORK (1h) - LlamaIndex Setup
13:30 - 14:00  | LUNCH BREAK
14:00 - 14:30  | PROMPT DRILL #3 - Security/Evaluation
14:30 - 16:30  | PM COURSE (2h) - Roadmapping
16:30 - 19:00  | DSA/LEETCODE (2.5h) - Two Pointers
19:00 - 19:30  | DINNER BREAK
19:30 - 20:30  | MINI-PROJECT WORK (1h) - LlamaIndex continued
20:30 - 21:00  | DAILY REFLECTION + NOTES (30min)
```

## Learning Objectives

### Reading: Eval Frameworks (1h)
- [ ] Read `evals/02-eval-frameworks/README.md`
- [ ] RAGAS overview
- [ ] DeepEval basics
- [ ] LLM-as-judge patterns

**Key Questions to Answer:**
- What evaluation frameworks exist for RAG?
- How does LLM-as-judge work?
- What metrics matter for RAG evaluation?

### Python Challenge (Days 7-8)
- [ ] Regex match, search, findall
- [ ] Common regex patterns
- [ ] Extracting data with regex
- [ ] Practical regex applications

**Exercises:**
1. Extract all email addresses from text
2. Find all phone numbers in various formats
3. Extract URLs from HTML content
4. Validate input formats (email, phone)

### Mini-Project: LlamaIndex Setup (2h total)
- [ ] Navigate to `06_llamaindex_study_buddy/`
- [ ] Read main.py and understand RAG flow
- [ ] Set up dependencies
- [ ] Run first query

**RAG Concepts to Understand:**
- What is Retrieval-Augmented Generation?
- How does document indexing work?
- What is vector similarity search?
- How does retrieved context improve responses?

### PM: Roadmapping (2h)
- [ ] Read `03-roadmapping.md`
- [ ] Roadmap types and uses
- [ ] Prioritization basics
- [ ] Timeline estimation

### DSA: Two Pointers (2.5h)
**Problems:**
1. Valid Palindrome (LeetCode #125)
2. Two Sum II - Sorted Array (LeetCode #167)
3. Container With Most Water (LeetCode #11)

**Patterns:**
- Left/right pointer convergence
- Start/end pointer technique

## Prompt Drills

### Drill #1: Agent Design (08:00-08:30)
**Topic:** RAG Agent Design

1. **Prompt 1:** Design a retrieval agent role
2. **Prompt 2:** Design an answer synthesis agent role
3. **Prompt 3:** Define context window management rules

### Drill #2: Prompt Techniques (08:30-09:00)
**Topic:** Context Injection

4. **Prompt 4:** How to format retrieved documents for LLM?
5. **Prompt 5:** Create a "answer from context only" prompt
6. **Prompt 6:** Design a "cite your sources" instruction

### Drill #3: Security/Evaluation (14:00-14:30)
**Topic:** RAG-Specific Security

7. **Prompt 7:** What if malicious content is in documents?
8. **Prompt 8:** How to prevent context poisoning?
9. **Prompt 9:** Design document sanitization rules

## LlamaIndex Study Notes

### RAG Architecture
```
User Query → Document Index → Similarity Search → Retrieved Context → LLM → Answer
```

### Key Components in LlamaIndex
```
1. Documents: Raw text input
2. Nodes: Chunked document pieces
3. Index: Vector representations
4. Query Engine: Search + synthesis
5. Response: Final answer
```

## End of Day Checklist

- [ ] Eval frameworks reading complete
- [ ] Python Days 7-8 completed
- [ ] LlamaIndex project runs
- [ ] RAG concepts understood
- [ ] PM Roadmapping complete
- [ ] 3 DSA problems solved
- [ ] 9 prompts written
- [ ] Daily log completed

## Tomorrow Preview (Day 5)
- Reading: vulnerabilities/02-prompt-injection
- Python Days 9-10 (env config, CLI args)
- LlamaIndex RAG deep dive
- PM: Metrics
- DSA: Sliding window technique
