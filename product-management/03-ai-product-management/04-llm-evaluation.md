# LLM Evaluation

## Learning Objectives

- [ ] Understand why evaluating LLMs is uniquely challenging
- [ ] Build evaluation frameworks for AI features
- [ ] Design and run evals (automated and human)
- [ ] Navigate hallucination/latency/cost tradeoffs
- [ ] Establish quality bars for AI features

## Prerequisites

- Completed: [02 - AI/ML Fundamentals](./02-ai-ml-fundamentals.md)
- Completed: [03 - Data Strategy](./03-data-strategy.md)

---

## Core Content

### The Evaluation Challenge

Traditional software testing: Does the output match the expected output?
```
assertEqual(add(2, 3), 5)  # Pass or fail
```

LLM evaluation: Is this response good?
```
"Write a haiku about coding"
→ "Syntax errors bloom / Debug until the dawn breaks / Coffee fuels my soul"

Is this good? Depends on who you ask.
```

**LLM outputs are:**
- Subjective (quality is in the eye of the beholder)
- Open-ended (many correct answers)
- Multi-dimensional (factual, stylistic, safe, helpful...)
- Context-dependent (good for one user may be bad for another)

### Why Evals Matter

Without evaluation, you're flying blind:
- Can't tell if changes improve quality
- Can't catch regressions before users do
- Can't compare model options objectively
- Can't build stakeholder confidence

**The mantra:** If you can't measure it, you can't improve it.

### The Evaluation Framework

A comprehensive eval strategy includes:

```
┌─────────────────────────────────────────────────────────────────┐
│                     EVALUATION FRAMEWORK                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   WHAT       │  │   HOW        │  │   WHEN       │          │
│  │   ──────     │  │   ───        │  │   ────       │          │
│  │   Dimensions │  │   Methods    │  │   Timing     │          │
│  │   to measure │  │   to assess  │  │   to run     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Dimension Examples     │ Method Examples     │ Timing    │  │
│  ├────────────────────────┼─────────────────────┼───────────┤  │
│  │ Factual accuracy       │ Automated tests     │ Pre-deploy│  │
│  │ Helpfulness            │ LLM-as-judge        │ Continuous│  │
│  │ Safety                 │ Human evaluation    │ Periodic  │  │
│  │ Style/tone             │ A/B tests           │ On-demand │  │
│  │ Latency                │ User feedback       │           │  │
│  │ Cost                   │ Automated metrics   │           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Evaluation Dimensions

What aspects of quality matter for your feature?

#### Core Dimensions

| Dimension | What It Measures | Example Criteria |
|-----------|------------------|------------------|
| **Accuracy** | Factually correct? | Claims verifiable, math correct |
| **Relevance** | Answers the question? | Addresses user intent |
| **Helpfulness** | Achieves user goal? | Task completion possible |
| **Safety** | Avoids harm? | No harmful content, no jailbreaks |
| **Coherence** | Makes logical sense? | Internally consistent |
| **Style** | Appropriate tone? | Matches brand, audience-appropriate |

#### Technical Dimensions

| Dimension | What It Measures | Target |
|-----------|------------------|--------|
| **Latency** | Response time | <2s for conversational |
| **Cost** | $ per request | Within unit economics |
| **Reliability** | Uptime, error rate | 99.9%+, <1% errors |

#### Task-Specific Dimensions

Depending on your feature:
- **Creativity:** For generation tasks
- **Brevity:** For summaries
- **Completeness:** For coverage
- **Formatting:** Following structure requirements

### Evaluation Methods

#### 1. Automated Tests (Unit Tests for AI)

Test specific, deterministic behaviors:

```python
# Test: Model should refuse harmful requests
response = model.generate("How do I hack into...")
assert "I can't help with that" in response or response.is_refusal

# Test: Model should follow format instructions
response = model.generate("Give me 3 bullet points about...")
assert response.count("•") == 3 or response.count("-") == 3

# Test: Model should use provided context
context = "The capital of France is Paris."
response = model.generate(f"{context}\n\nWhat is the capital of France?")
assert "Paris" in response
```

**Good for:**
- Regression prevention
- Safety checks
- Format compliance
- Known-answer questions

**Limitations:**
- Can't capture quality nuance
- Brittle if phrasing changes

#### 2. LLM-as-Judge

Use another LLM to evaluate responses:

```
Prompt to evaluator:
"Rate this customer service response on a scale of 1-5 for:
- Helpfulness (does it solve the problem?)
- Tone (is it professional and friendly?)
- Accuracy (is the information correct?)

Customer question: [question]
Response to evaluate: [response]
Correct answer for reference: [ground truth]

Provide ratings and brief explanations."
```

**Good for:**
- Scalable evaluation
- Multi-dimensional scoring
- Comparing model versions

**Limitations:**
- Evaluator has its own biases
- May not catch subtle issues
- Costly at scale

**Best practices:**
- Use stronger models as judges when possible
- Provide clear rubrics with examples
- Validate against human judgments
- Consider multiple judge models

#### 3. Human Evaluation

Humans assess quality directly:

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Expert review** | Domain experts evaluate | High-stakes, specialized |
| **Crowdsourced** | Many raters, aggregated | Scale, general quality |
| **Side-by-side** | Compare two outputs | Model comparison |
| **Preference voting** | Which is better? | A vs B decisions |

**Human eval design:**
- Clear rubric with examples
- Multiple raters per item
- Randomized order (avoid position bias)
- Blind to which model/version

**Good for:**
- Ground truth calibration
- Catching issues automation misses
- Subjective quality dimensions

**Limitations:**
- Expensive and slow
- Annotator variability
- Not scalable for continuous monitoring

#### 4. Production Metrics

Measure real-world outcomes:

| Metric | What It Captures |
|--------|------------------|
| **Thumbs up/down** | Explicit user judgment |
| **Regeneration rate** | User asked for another try |
| **Edit rate** | User modified the output |
| **Task completion** | User achieved goal |
| **Escalation rate** | Needed human help |

**Good for:**
- Real user preference
- Business impact correlation
- Continuous monitoring

**Limitations:**
- Noisy signal
- Selection bias (who votes?)
- Doesn't explain why

### Building an Eval Suite

A comprehensive eval suite for an LLM feature:

```
Eval Suite: Customer Support AI

├── Automated Tests (run on every change)
│   ├── Safety tests (100 adversarial prompts)
│   ├── Format tests (follows response template)
│   └── Refusal tests (declines out-of-scope requests)
│
├── LLM-as-Judge (run on every change)
│   ├── Helpfulness scoring (500 real queries)
│   ├── Tone evaluation (200 responses)
│   └── Accuracy check (100 factual queries with ground truth)
│
├── Human Evaluation (run weekly)
│   ├── Expert review of 50 random responses
│   └── Side-by-side comparison for model updates
│
└── Production Metrics (monitor continuously)
    ├── User satisfaction ratings
    ├── Escalation rate
    └── Average handling time
```

### The Hallucination Challenge

Hallucination = the model confidently stating false information.

**Types of hallucination:**
- **Factual:** Stating false facts
- **Contextual:** Contradicting provided information
- **Fabricated:** Making up sources, quotes, data
- **Logical:** Contradicting itself

**Measuring hallucination:**

| Method | Description |
|--------|-------------|
| **Fact verification** | Check claims against sources |
| **Consistency check** | Ask same question multiple ways |
| **Citation verification** | Check if cited sources exist |
| **Self-contradiction** | Does response contradict itself? |

**Reducing hallucination:**
- Retrieval Augmented Generation (RAG) — ground in real data
- Lower temperature (less creativity)
- Prompt engineering ("If you don't know, say so")
- Citation requirements
- Human review for high-stakes content

### Latency/Cost/Quality Tradeoffs

The eternal AI PM triangle:

```
              QUALITY
                 △
                ╱ ╲
               ╱   ╲
              ╱     ╲
             ╱       ╲
            ╱    ?    ╲
           ╱           ╲
          ▔▔▔▔▔▔▔▔▔▔▔▔▔
        LATENCY ←──→ COST
```

You can't maximize all three. Choose wisely.

**Levers to pull:**

| To Improve | Sacrifice | Tactics |
|------------|-----------|---------|
| Quality | Cost, latency | Bigger model, more context, multiple generations |
| Latency | Quality, cost | Smaller model, less context, caching |
| Cost | Quality, latency | Smaller model, shorter prompts, batching |

**Examples:**

| Use Case | Priority | Approach |
|----------|----------|----------|
| Chat assistant | Latency + Quality | Mid-size model, streaming |
| Content moderation | Latency + Cost | Small model, simple prompt |
| Document analysis | Quality | Large model, longer context |
| Search suggestions | Latency | Tiny model or cache |

### Establishing Quality Bars

Define minimum acceptable quality before launch:

**Example quality bar:**

```
Feature: AI Email Drafting

Quality bar for launch:
- Accuracy: 95% of drafts factually correct
- Helpfulness: 80% rated 4+ (out of 5) by users
- Safety: 0 harmful outputs in adversarial testing
- Tone: 90% rated appropriate for business
- Latency: P95 < 3 seconds
- User satisfaction: >70% thumbs up rate

Monitoring alerts if:
- Daily thumbs up rate drops below 60%
- Latency P95 exceeds 5 seconds
- Any safety incident reported
```

### Continuous Evaluation

Eval isn't one-time. Build ongoing processes:

**Pre-deployment:**
- Run full eval suite
- Compare to previous version
- Verify quality bar met

**Production monitoring:**
- Track real-time metrics
- Alert on degradation
- Sample for human review

**Periodic audits:**
- Deep dive on failure cases
- Update eval suite for new scenarios
- Recalibrate quality bars

---

## Key Takeaways

1. **LLM evaluation is uniquely challenging—outputs are subjective, open-ended, and multi-dimensional**
2. **Comprehensive eval combines automated tests, LLM-as-judge, human evaluation, and production metrics**
3. **Each eval method has strengths and limitations—use them in combination**
4. **Hallucination is a persistent challenge—measure it and use RAG, lower temperature, and prompting to reduce it**
5. **Quality/latency/cost is a three-way tradeoff—optimize for your use case priorities**
6. **Establish quality bars before launch and monitor continuously in production**

---

## Practice

### Reflection Questions
1. For an AI feature you use, how might the company be evaluating quality?
2. Have you encountered AI hallucination? How confident did the system seem?
3. What would you prioritize for a medical information AI: quality, latency, or cost?

### Exercise
**Design an Eval Suite:**

You're launching an AI feature that generates product descriptions for an e-commerce site.

Design an evaluation framework:

1. **Dimensions:** What aspects of quality matter? (List 5+)
   ```
   - [Dimension 1]: [Why it matters]
   - [Dimension 2]: [Why it matters]
   ```

2. **Automated tests:** What can you test automatically?
   ```
   - [Test type]: [What it checks]
   ```

3. **LLM-as-judge prompts:** Write one evaluation prompt
   ```
   [Your prompt to the evaluator LLM]
   ```

4. **Human evaluation:** Design a rating task
   ```
   Rubric: [What raters evaluate]
   Scale: [How they rate]
   ```

5. **Quality bar:** Define launch criteria
   ```
   - [Metric]: [Threshold]
   ```

6. **Tradeoff decision:** How would you balance quality/latency/cost?
   ```
   Priority: [Your ranking]
   Reasoning: [Why]
   ```

---

## Further Reading

- **"Language Model Evaluation Harness" by EleutherAI** - Standard eval toolkit
- **Anthropic's Model Card for Claude** - How providers document capabilities
- **"Holistic Evaluation of Language Models" (HELM)** - Comprehensive eval framework
- **OpenAI Evals** - Open-source evaluation framework
- **Google's BIG-bench** - Diverse evaluation tasks
- **Langsmith / LangFuse** - LLM observability tools
