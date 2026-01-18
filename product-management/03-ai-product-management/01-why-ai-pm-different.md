# Why AI PM is Different

## Learning Objectives

- [ ] Understand the shift from deterministic to probabilistic systems
- [ ] Identify the unique challenges of AI product management
- [ ] Recognize the dual metrics problem (model metrics vs. product metrics)
- [ ] Apply the "AI as colleague" mental model
- [ ] Know when AI is (and isn't) the right solution

## Prerequisites

- Completed: [01-Foundations](../01-foundations/) module
- Completed: [02-Technical PM](../02-technical-pm/) module (recommended)

---

## Core Content

### The Fundamental Shift

Traditional software is **deterministic**: given the same inputs, you get the same outputs. Always.

```
Traditional Software:
add(2, 3) → 5  (Every time, forever)
```

AI systems are **probabilistic**: given the same inputs, you might get different outputs. And even the same output might be wrong.

```
AI System:
classify("Is this email spam?") → "Yes" (97% confidence)
                                → Maybe wrong 3% of the time
                                → Different models = different answers
```

**This changes everything about how you build, test, and manage products.**

### Deterministic vs. Probabilistic

| Aspect | Deterministic Software | AI/ML Systems |
|--------|----------------------|---------------|
| **Behavior** | Predictable | Probabilistic |
| **Testing** | Pass/fail | Accuracy/quality ranges |
| **Bugs** | Code is wrong | Model is "wrong" sometimes by design |
| **Improvement** | Fix the code | Retrain, tune, more data |
| **Explanation** | Can trace exactly why | Often opaque |
| **Failure mode** | Crash or wrong output | Confidently wrong |

### The AI PM's New Challenges

#### Challenge 1: Defining "Correct"

Traditional software: `calculateTax(income, state)` has one correct answer.

AI systems: "Write a professional email" has infinite correct answers, and correctness is subjective.

**PM implication:** You can't just say "it should work." You need to define what "good enough" looks like across dimensions:
- Accuracy/correctness
- Relevance
- Tone/style
- Safety
- Speed
- Cost

#### Challenge 2: Managing Expectations

Users expect software to work 100% of the time. AI won't.

**PM implication:** Design for graceful failure:
- Set appropriate expectations in UX
- Provide fallbacks when AI fails
- Make confidence visible when appropriate
- Give users control and override options

**Example:** Auto-suggest reply feature
- Good: "Here are some suggested replies. Edit as needed."
- Bad: "Sending your reply now..." (with AI-generated content user didn't review)

#### Challenge 3: The Black Box Problem

Traditional code: You can trace exactly why output X came from input Y.

AI models: You often can't explain why the model made a specific decision.

**PM implication:**
- Consider explainability requirements (especially for sensitive domains)
- Plan for "why did it do that?" questions
- Decide when users need explanations vs. just results

#### Challenge 4: Continuous Change

Traditional software: Behavior changes only when you deploy new code.

AI systems: Behavior can change through:
- Model updates
- Data drift (world changes)
- Distribution shifts (users change)
- Retraining cycles

**PM implication:** Your product is always changing, even without code deploys. You need:
- Continuous monitoring
- Evaluation pipelines
- Regression detection
- Change communication strategy

#### Challenge 5: The Data Dependency

Traditional software: Works regardless of data quality.

AI systems: Quality is bounded by data quality. "Garbage in, garbage out."

**PM implication:** Data strategy is product strategy:
- Where does training data come from?
- How do we get labeled data?
- What biases exist in our data?
- How do we improve data over time?

### The Dual Metrics Problem

AI products require two kinds of metrics:

#### Model Metrics (Technical)
How well does the model perform on technical measures?

| Metric | What It Measures |
|--------|------------------|
| Accuracy | % of predictions correct |
| Precision | Of positive predictions, % actually positive |
| Recall | Of actual positives, % correctly predicted |
| F1 Score | Harmonic mean of precision/recall |
| Latency | How fast the model responds |
| Perplexity | How surprised the model is (LLMs) |

#### Product Metrics (Business)
How does the AI feature impact user and business outcomes?

| Metric | What It Measures |
|--------|------------------|
| Task completion rate | Users achieving their goal |
| User satisfaction | NPS, ratings, feedback |
| Engagement | Usage of AI feature |
| Conversion | Business impact |
| Support tickets | Problems caused |

**The trap:** Improving model metrics doesn't always improve product metrics.

**Example:**
- Spam filter improved precision from 95% → 99%
- Model metrics: Better!
- Product metrics: Users complained more
- Why: The 4% reduction in false positives wasn't worth the 1% increase in false negatives (missing important emails)

**PM responsibility:** Keep focus on product metrics. Model improvements are only valuable if they improve user outcomes.

### The "AI as Colleague" Mental Model

A useful mental model: Think of AI features as a capable but imperfect colleague.

**A good colleague:**
- Gets most things right
- Learns from feedback
- Might make mistakes you need to catch
- Handles tasks you delegate to them
- Needs clear instructions
- Works better with context

**Design implications:**

| Colleague Reality | Design Response |
|-------------------|-----------------|
| Might be wrong | Review workflows, easy corrections |
| Needs context | Provide relevant information |
| Varies in confidence | Show confidence, allow override |
| Can improve | Feedback mechanisms |
| Has limitations | Clear scope, graceful handoffs |

### When AI Is (and Isn't) the Right Solution

AI isn't always the answer. Use this framework:

#### AI is a good fit when:

1. **Pattern recognition at scale**
   - Humans can do it, but not fast enough
   - Example: Content moderation for millions of posts

2. **Personalization**
   - Too many combinations for rules
   - Example: Recommendations for unique users

3. **Natural language understanding**
   - Semantic meaning vs. keyword matching
   - Example: Search intent understanding

4. **Generation and creativity assist**
   - Draft generation, suggestions, variations
   - Example: Writing assistance, design suggestions

5. **Prediction from complex data**
   - More variables than rules can handle
   - Example: Fraud detection from behavioral patterns

#### AI is a poor fit when:

1. **Deterministic correctness is required**
   - Calculations, compliance, exact matches
   - Example: Tax calculations, legal document parsing

2. **Perfect accuracy is necessary**
   - Medical diagnosis, autonomous vehicles (without human oversight)
   - Stakes are too high for probabilistic errors

3. **Data doesn't exist or is biased**
   - Can't train without data
   - Biased data = biased outcomes

4. **Simple rules suffice**
   - Don't use ML when if/else works
   - Example: Password validation

5. **Explainability is mandatory**
   - Regulated decisions requiring documentation
   - Example: Credit decisions (in some jurisdictions)

### The AI PM Toolkit Expansion

Traditional PM toolkit still applies, but AI adds new tools:

| New Tool | Purpose |
|----------|---------|
| Evaluation frameworks | Defining and measuring "good" |
| Data quality assessment | Understanding training data |
| Model cards | Documenting model capabilities/limits |
| Fairness audits | Checking for bias |
| A/B testing for AI | Comparing model versions |
| Human-in-the-loop design | Combining AI and human judgment |
| Feedback pipelines | Continuous improvement from users |

### The Stakes Are Higher

AI products carry unique risks:

**Reputation risk:** AI saying something offensive, biased, or wrong is public relations nightmare material.

**Fairness risk:** AI making biased decisions against protected groups has legal and ethical implications.

**Safety risk:** AI in high-stakes domains can cause real harm.

**Trust risk:** One bad experience with AI can permanently destroy user trust.

**PM implication:** Invest more in:
- Testing edge cases and adversarial inputs
- Safety and content guidelines
- Human review for high-stakes decisions
- Clear accountability structures

---

## Key Takeaways

1. **AI systems are probabilistic, not deterministic—this changes everything about testing, expectations, and failure modes**
2. **New challenges include defining "correct," managing user expectations, the black box problem, continuous change, and data dependency**
3. **Track both model metrics AND product metrics—improving the model doesn't always improve the product**
4. **Think of AI as a capable but imperfect colleague—design for review, feedback, and graceful failure**
5. **AI isn't always the right solution—use it for pattern recognition at scale, personalization, NLU, generation, and complex prediction**
6. **Stakes are higher—invest in safety, fairness, and building appropriate user trust**

---

## Practice

### Reflection Questions
1. Think of an AI feature you use daily (recommendations, autocomplete, etc.). What expectations do you have? How does it handle failure?
2. Have you experienced an AI feature being confidently wrong? What was the impact?
3. For a product you know well, where might AI add value? Where would it be a poor fit?

### Exercise
**AI Suitability Assessment:**

For each scenario, determine if AI is a good fit and explain why:

1. **Password strength checker**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

2. **Email subject line suggestions**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

3. **Matching job candidates to openings**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

4. **Calculating invoice totals**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

5. **Detecting fraudulent transactions**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

6. **Generating legal contract terms**
   - AI fit? Yes/No
   - Reasoning: [Your answer]

---

## Further Reading

- **"Prediction Machines" by Ajay Agrawal** - Economic thinking about AI
- **"Human + Machine" by Paul Daugherty** - AI augmentation patterns
- **Anthropic's "Claude's Character"** - How AI companies think about AI behavior
- **Google's PAIR (People + AI Research)** - AI UX design guidelines
- **AI Incident Database** - Real examples of AI failures
