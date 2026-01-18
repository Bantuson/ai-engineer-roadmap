# AI Product Lifecycle

## Learning Objectives

- [ ] Understand how AI product development differs from traditional software
- [ ] Manage training cycles and model versioning
- [ ] Monitor AI products in production effectively
- [ ] Design continuous improvement pipelines
- [ ] Implement human-in-the-loop patterns

## Prerequisites

- Completed: [02 - AI/ML Fundamentals](./02-ai-ml-fundamentals.md)
- Completed: [04 - LLM Evaluation](./04-llm-evaluation.md)

---

## Core Content

### The AI Product Lifecycle

AI products have a different lifecycle than traditional software:

```
Traditional Software:
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Design  │ → │  Build   │ → │  Test    │ → │  Deploy  │ → Maintain
└──────────┘   └──────────┘   └──────────┘   └──────────┘

AI Products:
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Design  │ → │  Data    │ → │  Train   │ → │  Eval    │
└──────────┘   └──────────┘   └──────────┘   └──────────┘
                                                  │
┌──────────────────────────────────────────────────┘
│
▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│  Deploy  │ → │  Monitor │ → │  Iterate │ → Back to Data/Train
└──────────┘   └──────────┘   └──────────┘
```

Key differences:
- **Data is central** — Not just code
- **Continuous training** — Not one-time development
- **Degradation happens** — Quality decays without intervention
- **Longer iteration cycles** — Training takes time

### Phase 1: Design for AI

AI feature design requires unique considerations:

#### Scoping AI Features

Before committing to AI, validate:

| Question | Why It Matters |
|----------|----------------|
| Is AI the right approach? | Simpler solutions may work |
| What data exists? | No data = no AI |
| What's "good enough"? | 100% accuracy isn't possible |
| What's the fallback? | Plan for AI failure |
| What's the human role? | Hybrid solutions often best |

#### Defining Success Criteria

For AI features, you need:

**Model success:** Technical metrics (accuracy, latency, cost)
**Product success:** User outcome metrics (task completion, satisfaction)
**Business success:** Impact metrics (revenue, retention, efficiency)

**Example:**

```
Feature: AI email drafting for sales team

Model success:
- Drafts pass quality eval 85%+ of time
- Generation latency <3s

Product success:
- 60% of generated drafts used (with edits)
- User satisfaction >4/5
- Time to send email reduced 40%

Business success:
- Sales rep efficiency up 20%
- Response rate to AI-drafted emails maintained
```

### Phase 2: Data Preparation

Before training begins:

#### Data Inventory

Document what exists:
- What data is available?
- What's the quality?
- What labels exist?
- What gaps need filling?

#### Data Preparation Activities

| Activity | Description | Time |
|----------|-------------|------|
| Collection | Gathering raw data | Variable |
| Cleaning | Removing errors, inconsistencies | 20-40% of project |
| Labeling | Creating training labels | Often the bottleneck |
| Splitting | Train/validation/test sets | Technical task |
| Augmentation | Creating variations | If data is limited |

**PM role:** Ensure data work is scoped, resourced, and on the timeline.

### Phase 3: Training

The model development phase.

#### Training Cycles

Training isn't instant:

| Model Type | Training Time | Cost |
|------------|---------------|------|
| Fine-tuning LLM | Hours to days | $100s-$10Ks |
| Training from scratch | Days to weeks | $10Ks-$Ms |
| Prompt optimization | Hours | Minimal |

**PM implications:**
- Plan for iteration time
- Budget for compute costs
- Expect multiple training runs

#### Working with ML Teams

During training, you might:
- Provide domain expertise for features
- Clarify ambiguous labeling cases
- Prioritize which metrics to optimize
- Make trade-off decisions (accuracy vs. latency)

**Don't:**
- Demand arbitrary deadlines
- Expect precise estimates
- Ignore negative results

### Phase 4: Evaluation

Rigorous testing before deployment.

#### Evaluation Gates

```
┌─────────────────────────────────────────────────────────────────┐
│                     EVALUATION GATES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Gate 1: Technical Validation                                   │
│  ├── Model metrics meet thresholds                              │
│  ├── Latency and cost within bounds                             │
│  └── No obvious failures                                        │
│                                                                 │
│  Gate 2: Quality Evaluation                                     │
│  ├── Human evaluation passes quality bar                        │
│  ├── Edge cases handled appropriately                           │
│  └── Comparison to baseline (if exists)                         │
│                                                                 │
│  Gate 3: Safety Review                                          │
│  ├── Red team testing completed                                 │
│  ├── Bias audit passed                                          │
│  └── Safety filters verified                                    │
│                                                                 │
│  Gate 4: Stakeholder Sign-off                                   │
│  ├── Legal/compliance review                                    │
│  ├── Business approval                                          │
│  └── Launch criteria met                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Model Versioning

Track model versions like code versions:

```
Model: email-drafter
├── v1.0 (2024-01-15)
│   ├── Training data: dataset-v1
│   ├── Config: config-v1.yaml
│   ├── Eval results: 78% quality score
│   └── Status: Deprecated
│
├── v1.1 (2024-03-01)
│   ├── Training data: dataset-v2 (added 10k examples)
│   ├── Config: config-v1.yaml
│   ├── Eval results: 83% quality score
│   └── Status: Production
│
└── v1.2 (2024-04-15)
    ├── Training data: dataset-v2
    ├── Config: config-v2.yaml (tuned params)
    ├── Eval results: 86% quality score
    └── Status: Canary (10%)
```

### Phase 5: Deployment

Rolling out AI to production.

#### Deployment Strategies

| Strategy | Description | Risk Level |
|----------|-------------|------------|
| **Shadow mode** | AI runs but outputs not shown | Very low |
| **Canary** | Small % of traffic sees AI | Low |
| **A/B test** | Compare AI to baseline | Low |
| **Gradual rollout** | Increase % over time | Medium |
| **Full launch** | 100% immediately | Higher |

**Best practice:** Start with shadow mode, progress through canary and gradual rollout.

#### Feature Flagging for AI

```python
if feature_flag.is_enabled("ai_email_drafting", user_id):
    if user.segment == "beta_testers":
        return ai_model.generate(context)
    elif rollout_percentage.check(user_id, 25):  # 25% rollout
        return ai_model.generate(context)
    else:
        return legacy_template(context)
else:
    return legacy_template(context)
```

### Phase 6: Production Monitoring

AI requires different monitoring than traditional software.

#### What to Monitor

**Technical health:**
- Latency distribution
- Error rates
- Resource utilization
- Cost per request

**Model quality:**
- Prediction distribution shifts
- Confidence scores over time
- User feedback (thumbs up/down)
- Downstream metrics (click-through, completion)

**Safety:**
- Content safety flags
- User reports
- Anomalous inputs

#### Detecting Degradation

AI quality degrades over time due to:

**Data drift:** The world changes, but the model doesn't.
- User behavior shifts
- New topics emerge
- Seasonal patterns

**Model decay:** Performance erodes.
- Training data becomes stale
- Edge cases accumulate
- Adversarial patterns discovered

**Concept drift:** The definition of "good" changes.
- User expectations evolve
- Business requirements shift

**Monitoring for drift:**

```
┌─────────────────────────────────────────────────────────────────┐
│                     DRIFT MONITORING                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input Monitoring:                                              │
│  ├── Distribution of input features                             │
│  ├── New input patterns (OOD detection)                         │
│  └── Input volume and mix changes                               │
│                                                                 │
│  Output Monitoring:                                             │
│  ├── Prediction distribution                                    │
│  ├── Confidence calibration                                     │
│  └── Output diversity                                           │
│                                                                 │
│  Outcome Monitoring:                                            │
│  ├── User feedback trends                                       │
│  ├── Downstream metric changes                                  │
│  └── Error pattern analysis                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 7: Continuous Improvement

AI products require ongoing investment to maintain quality.

#### Improvement Triggers

| Trigger | Response |
|---------|----------|
| Quality degradation | Investigate, retrain if needed |
| New capability needs | Expand training data, fine-tune |
| Cost optimization | Model compression, prompt optimization |
| Safety issues | Emergency patches, expanded testing |
| User feedback | Targeted improvements |

#### The Improvement Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌──────────────┐        ┌──────────────┐                    │
│    │  Production  │───────▶│   Collect    │                    │
│    │  Monitoring  │        │   Feedback   │                    │
│    └──────────────┘        └──────────────┘                    │
│           ▲                       │                             │
│           │                       │                             │
│           │                       ▼                             │
│    ┌──────────────┐        ┌──────────────┐                    │
│    │   Deploy     │◀───────│   Analyze    │                    │
│    │   Update     │        │   & Improve  │                    │
│    └──────────────┘        └──────────────┘                    │
│           ▲                       │                             │
│           │                       │                             │
│           │                       ▼                             │
│    ┌──────────────┐        ┌──────────────┐                    │
│    │   Evaluate   │◀───────│   Retrain    │                    │
│    │   New Model  │        │   / Update   │                    │
│    └──────────────┘        └──────────────┘                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Feedback Loops

Build mechanisms to capture improvement signals:

**Explicit feedback:**
- Thumbs up/down
- Ratings
- "Was this helpful?"
- Error reports

**Implicit feedback:**
- Did user accept/edit/reject?
- Did user achieve their goal?
- Did user come back?

**Expert feedback:**
- Periodic review by domain experts
- Quality audits
- Escalation analysis

### Human-in-the-Loop Patterns

Many AI products work best with human involvement:

#### Pattern 1: AI Suggests, Human Decides

```
[AI] → Suggestions → [Human] → Decision → [Action]
```

**Example:** AI recommends content, human approves publishing.

**When to use:** High-stakes decisions, quality-critical applications.

#### Pattern 2: AI Drafts, Human Edits

```
[AI] → Draft → [Human] → Edits → [Final Output]
```

**Example:** AI writes email draft, human reviews and sends.

**When to use:** Creative tasks, personalization needed.

#### Pattern 3: AI Acts, Human Reviews

```
[AI] → Action → [Logging] → [Human Review (sampled)]
```

**Example:** AI moderates content, humans audit samples.

**When to use:** High-volume, lower-stakes, with audit needs.

#### Pattern 4: AI Escalates to Human

```
[AI] → Confident? → Yes → Action
              └─── No ──→ [Human]
```

**Example:** AI handles simple support, escalates complex cases.

**When to use:** Variable complexity, need to handle edge cases.

**PM role:** Design the human-AI interface, set escalation thresholds, ensure human workflow is viable.

---

## Key Takeaways

1. **AI products have a unique lifecycle: data → train → evaluate → deploy → monitor → iterate**
2. **Plan for training cycles—they take time and compute, and iteration is expected**
3. **Establish evaluation gates before deployment: technical, quality, safety, stakeholder**
4. **Monitor AI differently than software: track drift, degradation, and outcome metrics**
5. **Build continuous improvement loops: feedback collection, analysis, retraining, deployment**
6. **Human-in-the-loop patterns combine AI capability with human judgment where needed**

---

## Practice

### Reflection Questions
1. For an AI product you use regularly, how do you think they improve it over time?
2. What signals would tell you that an AI feature is degrading?
3. When would you choose "AI suggests, human decides" vs. "AI acts, human reviews"?

### Exercise
**AI Lifecycle Planning:**

You're launching an AI feature that automatically categorizes incoming customer support tickets.

Plan the lifecycle:

1. **Design phase:**
   - What data do you need?
   - What's "good enough" accuracy?
   - What's the fallback?

2. **Training phase:**
   - How will you get labeled data?
   - How long will training take?
   - What trade-offs might you make?

3. **Evaluation phase:**
   - What are your evaluation gates?
   - What quality bar must be met?
   - Who needs to sign off?

4. **Deployment phase:**
   - What rollout strategy would you use?
   - How will you handle the transition?

5. **Monitoring phase:**
   - What metrics will you track?
   - What would indicate drift?
   - How would you detect issues?

6. **Improvement phase:**
   - How will you collect feedback?
   - What triggers retraining?
   - What's the improvement cadence?

7. **Human-in-the-loop:**
   - Which pattern would you use?
   - How do humans fit into the workflow?

---

## Further Reading

- **"Machine Learning Engineering" by Andriy Burkov** - ML lifecycle practices
- **"Building Machine Learning Powered Applications" by Emmanuel Ameisen** - End-to-end ML product development
- **Google's MLOps Maturity Model** - Stages of ML operations
- **Evidently AI** - ML monitoring best practices
- **MLflow documentation** - ML lifecycle management tools
- **Human-in-the-loop Machine Learning** by Robert Munro - Active learning and annotation
