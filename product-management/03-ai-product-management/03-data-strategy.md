# Data Strategy

## Learning Objectives

- [ ] Understand why data quality determines AI quality
- [ ] Design data collection strategies for AI features
- [ ] Know the data annotation landscape (methods, costs, challenges)
- [ ] Build and manage data pipelines
- [ ] Detect and mitigate bias in training data

## Prerequisites

- Completed: [02 - AI/ML Fundamentals](./02-ai-ml-fundamentals.md)

---

## Core Content

### Data is the New Code

In traditional software, code determines behavior. In AI products, **data determines behavior.**

```
Traditional: Better code → Better product
AI:          Better data → Better model → Better product
```

**This is why data strategy is product strategy for AI PMs.**

### The Data Hierarchy of Needs

Before fancy models matter, you need data fundamentals:

```
                    △
                   ╱ ╲ Model Quality
                  ╱───╲
                 ╱     ╲ Data Volume
                ╱───────╲
               ╱         ╲ Data Quality
              ╱───────────╲
             ╱             ╲ Data Access
            ╱───────────────╲
           ╱                 ╲ Data Existence
          ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
```

Each level depends on the one below. No amount of model sophistication fixes bad data.

### Data Quality Dimensions

Quality isn't a single measure. Evaluate across multiple dimensions:

| Dimension | What It Means | Example Problem |
|-----------|---------------|-----------------|
| **Accuracy** | Data reflects reality | Customer ages are wrong |
| **Completeness** | No missing values | 30% of records lack emails |
| **Consistency** | Same thing = same representation | "US", "USA", "United States" |
| **Timeliness** | Data is current | Using 2-year-old preferences |
| **Relevance** | Data matters for the task | Training on irrelevant features |
| **Representativeness** | Data reflects real distribution | Only enterprise customers in data |

### Data Collection Strategies

Where does training data come from?

#### 1. Existing Product Data

**What:** Data your product already collects

**Examples:**
- User behavior logs
- Search queries
- Transactions
- Content created

**Pros:** Free, relevant, continuously growing
**Cons:** May have biases, may not be labeled, privacy concerns

#### 2. User-Generated Labels

**What:** Signals from user behavior that indicate quality

**Examples:**
- Clicks, purchases, engagement (implicit)
- Likes, ratings, reports (explicit)
- A/B test winner selection

**Pros:** Scales with usage, reflects real preferences
**Cons:** Noisy, popularity bias, cold start problem

#### 3. Human Annotation

**What:** Humans label data specifically for training

**Examples:**
- Rating content quality
- Labeling images
- Categorizing support tickets
- Evaluating AI outputs

**Pros:** High quality if done well, can label anything
**Cons:** Expensive, slow, introduces annotator bias

#### 4. Synthetic Data

**What:** Artificially generated training data

**Examples:**
- LLM-generated training examples
- Simulated scenarios
- Data augmentation

**Pros:** Unlimited volume, can create rare cases
**Cons:** May not match real distribution, can amplify biases

#### 5. Public Datasets

**What:** Existing datasets available for training

**Examples:**
- Academic datasets (ImageNet, Common Crawl)
- Open-source datasets
- Government data

**Pros:** Immediately available, often large
**Cons:** May not fit your domain, potential license issues

### Data Annotation Deep Dive

Annotation is often the bottleneck for AI products.

#### Annotation Methods

| Method | Best For | Cost | Quality |
|--------|----------|------|---------|
| **In-house experts** | Domain-specific, high-stakes | High | Highest |
| **Crowdsourcing** | High volume, clear tasks | Medium | Variable |
| **Active learning** | Efficient labeling | Medium | High |
| **Weak supervision** | Low-cost bootstrapping | Low | Lower |

#### Annotation Quality Control

**Agreement metrics:**
- Inter-annotator agreement: Do multiple annotators agree?
- Cohen's Kappa: Agreement adjusted for chance

**Quality practices:**
- Clear, detailed guidelines with examples
- Training and calibration sessions
- Gold standard sets (known answers)
- Regular audits and feedback
- Multiple annotators per item for disagreement detection

#### Annotation Costs

Rough cost ranges (2025 estimates):

| Task Type | Cost per Item | Example |
|-----------|---------------|---------|
| Simple binary | $0.01-0.05 | Is this spam? |
| Multi-class | $0.05-0.20 | Topic classification |
| Complex labeling | $0.20-2.00 | Entity extraction |
| Expert annotation | $1.00-50.00 | Medical image labeling |
| Conversation evaluation | $0.50-5.00 | LLM response quality |

**PM implication:** Budget for annotation. It's often more expensive than expected.

### Data Pipelines

Data pipelines move data from sources to model training:

```
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌─────────────┐
│  Sources    │───▶│  Ingestion   │───▶│ Processing │───▶│  Training   │
│  ────────   │    │  ──────────  │    │ ─────────  │    │  ─────────  │
│  - Logs     │    │  - Collect   │    │ - Clean    │    │ - Split     │
│  - Events   │    │  - Validate  │    │ - Transform│    │ - Train     │
│  - Labels   │    │  - Store     │    │ - Feature  │    │ - Validate  │
└─────────────┘    └──────────────┘    └────────────┘    └─────────────┘
```

#### Pipeline Considerations

**Freshness:** How current does data need to be?
- Real-time: Streaming pipelines
- Daily: Batch pipelines
- Ad-hoc: Manual processes

**Reliability:** What happens when things fail?
- Monitoring and alerting
- Replay capabilities
- Data validation checks

**Scalability:** Can it handle growth?
- Volume increases
- New data sources
- New features

### Bias Detection and Mitigation

Bias in data leads to bias in models—with real-world consequences.

#### Types of Data Bias

| Bias Type | Description | Example |
|-----------|-------------|---------|
| **Selection bias** | Non-representative sampling | Only surveying active users |
| **Historical bias** | Past reflects problematic patterns | Historical hiring data |
| **Measurement bias** | Proxy measures don't capture truth | Using arrest data for criminality |
| **Labeling bias** | Annotator perspective skews labels | Cultural differences in "appropriate" |
| **Representation bias** | Some groups underrepresented | Faces in training data predominantly light-skinned |

#### Detecting Bias

**Exploratory analysis:**
- Break down data by demographic groups
- Look for imbalances in representation
- Check label distributions across groups

**Model analysis:**
- Compare performance across groups
- Check for disparate error rates
- Test with adversarial examples

**Questions to ask:**
- Who is in our training data? Who is missing?
- How were labels assigned? By whom?
- What historical patterns might be embedded?
- What proxies might encode protected attributes?

#### Mitigating Bias

**Pre-processing (data level):**
- Oversample underrepresented groups
- Undersample overrepresented groups
- Remove or modify biased features

**In-processing (training level):**
- Add fairness constraints to training
- Use adversarial debiasing
- Adjust objective functions

**Post-processing (prediction level):**
- Calibrate outputs across groups
- Apply different thresholds by group
- Add human review for sensitive decisions

**The hard truth:** You can't eliminate bias entirely. The goal is to understand it, mitigate it where possible, and be transparent about limitations.

### The Data Flywheel

The most powerful AI products create virtuous cycles:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌──────────────┐                    ┌──────────────┐        │
│    │  Better      │───────────────────▶│  More Users  │        │
│    │  Model       │                    │              │        │
│    └──────────────┘                    └──────────────┘        │
│           ▲                                   │                 │
│           │                                   │                 │
│           │                                   ▼                 │
│    ┌──────────────┐                    ┌──────────────┐        │
│    │  Better      │◀───────────────────│  More Data   │        │
│    │  Training    │                    │              │        │
│    └──────────────┘                    └──────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Designing for the flywheel:**
- Use implicit signals from product usage
- Make feedback easy and natural
- Store data that enables future improvements
- Build pipelines that can process growing volume

### Data Governance

As data becomes valuable, governance becomes critical:

**Privacy:**
- What data can you collect and use?
- GDPR, CCPA, and other regulations
- User consent requirements

**Security:**
- Who can access training data?
- How is it protected?
- Audit trails

**Retention:**
- How long do you keep data?
- When must it be deleted?
- Training data vs. production data

**Lineage:**
- Where did this data come from?
- How was it transformed?
- Which models were trained on it?

---

## Key Takeaways

1. **Data quality determines AI quality—no model sophistication can overcome bad data**
2. **Data collection sources: existing product data, user signals, human annotation, synthetic data, public datasets**
3. **Annotation is often the bottleneck—budget time and money appropriately**
4. **Bias in data leads to bias in models—detect across multiple dimensions and mitigate at data, training, or inference levels**
5. **Build for the data flywheel—more users → more data → better models → more users**
6. **Data governance (privacy, security, retention, lineage) becomes critical at scale**

---

## Practice

### Reflection Questions
1. For a product you use, where do you think they get training data? What biases might exist?
2. Have you seen an AI product that seems to get better the more you use it? How might they be using your data?
3. What are the privacy implications of collecting training data from user behavior?

### Exercise
**Data Strategy Design:**

You're building an AI-powered customer support tool that suggests responses to agents.

Design a data strategy covering:

1. **Data sources:** Where will training data come from?
   - [List at least 3 sources with pros/cons]

2. **Labeling approach:** How will you label "good" responses?
   - [Describe method, quality control, estimated cost]

3. **Bias concerns:** What biases might exist?
   - [List at least 3 potential biases and how you'd detect/mitigate]

4. **Data flywheel:** How will the product improve over time?
   - [Describe the feedback loop]

5. **Governance:** What privacy/security considerations apply?
   - [List key concerns and how you'd address them]

---

## Further Reading

- **"Data and Goliath" by Bruce Schneier** - Data privacy implications
- **"Weapons of Math Destruction" by Cathy O'Neil** - Bias in AI systems
- **Google's Data Cascades Paper** - Real-world data quality challenges
- **Snorkel Documentation** - Weak supervision approaches
- **Model Cards and Datasheets** - Documentation standards for ML
