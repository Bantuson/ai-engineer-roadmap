# Metrics & Analytics

## Learning Objectives

- [ ] Distinguish between KPIs and metrics
- [ ] Identify and define a North Star Metric
- [ ] Understand and calculate key product metrics (DAU/MAU, retention, LTV, CAC)
- [ ] Build a metrics framework for product decisions
- [ ] Avoid common metrics pitfalls

## Prerequisites

- Completed: [01 - What is Product Management?](./01-what-is-pm.md)
- Completed: [05 - Roadmapping](./05-roadmapping.md)

---

## Core Content

### Why Metrics Matter

**"What gets measured gets managed."** — Peter Drucker

Metrics serve several critical functions:

1. **Decision making:** Data informs priorities and trade-offs
2. **Alignment:** Shared metrics create shared goals
3. **Accountability:** Progress becomes visible and objective
4. **Learning:** Metrics reveal what's working and what isn't

**But metrics aren't neutral.** What you measure shapes behavior—sometimes in unintended ways.

### Metrics vs. KPIs

These terms are often confused:

**Metrics:** Any quantifiable measure of product or business performance.
- Total users
- Page load time
- Support tickets opened
- Feature adoption rate

**KPIs (Key Performance Indicators):** The vital few metrics that indicate overall health and success.
- They're a subset of metrics
- They're directly tied to business outcomes
- They're what leadership watches

**Relationship:** All KPIs are metrics, but not all metrics are KPIs.

### The North Star Metric

A North Star Metric (NSM) is **the single metric that best captures the core value your product delivers to customers.**

#### Characteristics of a Good NSM

1. **Reflects customer value:** Correlates with customers getting value
2. **Leads to revenue:** Customers who hit this metric eventually pay
3. **Measurable:** Can be tracked accurately
4. **Actionable:** Teams can influence it
5. **Understandable:** Everyone can grasp it

#### North Star Examples

| Company | North Star Metric | Why It Works |
|---------|-------------------|--------------|
| **Airbnb** | Nights booked | Directly captures value exchange |
| **Spotify** | Time spent listening | Indicates engagement with core value |
| **Facebook** | Daily active users | Measures habitual engagement |
| **Slack** | Messages sent in team | Shows collaboration happening |
| **Salesforce** | Records created | Indicates CRM value realization |
| **Amplitude** | Weekly learning users | Users who query data = getting value |

#### Finding Your North Star

Ask these questions:

1. What is the core value users get from our product?
2. What action indicates they received that value?
3. How can we measure that action?
4. Does improving this metric drive business outcomes?

**Common mistake:** Choosing revenue as NSM. Revenue is a lagging indicator—it follows value creation. Your NSM should be closer to the value creation moment.

#### North Star Framework

The NSM typically has supporting input metrics:

```
                    ┌─────────────────┐
                    │   NORTH STAR    │
                    │ Nights Booked   │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ INPUT: Breadth  │ │ INPUT: Depth    │ │ INPUT: Frequency│
│ New users       │ │ Booking value   │ │ Repeat booking  │
│ activated       │ │ per trip        │ │ rate            │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

Teams can focus on different input metrics while all contributing to the NSM.

### Core Product Metrics

#### Acquisition Metrics

How users find and start using your product.

**New Users/Signups:** Raw count of new accounts created
- Simple but doesn't indicate quality
- Track by channel to understand acquisition mix

**Activation Rate:** Percentage of new users who reach a meaningful milestone
- "Meaningful" varies by product (first action, completed setup, etc.)
- More valuable than raw signups

```
Activation Rate = (Users who complete activation) / (Total signups) × 100
```

**Example:** If activation = "sent first message" and 1,000 users signed up but only 400 sent a message: Activation Rate = 40%

#### Engagement Metrics

How users interact with your product over time.

**DAU (Daily Active Users):** Users who engage at least once in a day
- "Active" must be defined (login? any action? specific action?)
- Compare to MAU for engagement depth

**MAU (Monthly Active Users):** Users who engage at least once in a month
- Broader view of user base
- Less sensitive to daily fluctuations

**DAU/MAU Ratio (Stickiness):** How frequently users return
```
Stickiness = DAU / MAU
```

| Ratio | Interpretation | Example Products |
|-------|----------------|------------------|
| 50%+ | Exceptional daily habit | Social media, communication |
| 25-50% | Strong engagement | Productivity tools |
| 10-25% | Good for some products | E-commerce, utilities |
| <10% | Concerning for most | May indicate low value |

**Session Metrics:**
- Session duration: How long users stay
- Sessions per user: How often they return
- Actions per session: How engaged each visit

#### Retention Metrics

Whether users come back after their first experience.

**Cohort Retention:** Track the same group of users over time

```
Week 0: 1000 users signed up
Week 1: 400 returned (40% retention)
Week 2: 300 returned (30% retention)
Week 4: 200 returned (20% retention)
Week 8: 150 returned (15% retention)
```

Visualized as a retention curve:

```
100% │●
     │
 80% │
     │
 60% │
     │
 40% │  ●
     │    ●
 20% │        ●        ●
     │                     ●────────●
  0% └───────────────────────────────────▶
     W0  W1  W2  W4  W8  W12 W16 W20
```

**Healthy retention curves flatten**—if they keep dropping, you have a leaky bucket.

**Churn Rate:** Percentage of customers who stop using the product in a period
```
Churn Rate = (Customers lost in period) / (Customers at start of period) × 100
```

For subscription businesses, track:
- **Logo churn:** Customer accounts lost
- **Revenue churn:** Revenue lost (weighted by customer value)

**Net Revenue Retention (NRR):** For B2B SaaS, includes expansion
```
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100
```

NRR > 100% means existing customers are growing faster than they're churning. This is gold.

#### Revenue Metrics

For products with monetization.

**MRR/ARR (Monthly/Annual Recurring Revenue):** Predictable subscription revenue
```
ARR = MRR × 12
```

**ARPU (Average Revenue Per User):** Revenue efficiency
```
ARPU = Total Revenue / Total Users
```

**LTV (Lifetime Value):** Total revenue expected from a customer
```
LTV = ARPU × Average Customer Lifespan
```

Or more precisely:
```
LTV = ARPU × Gross Margin % / Churn Rate
```

**CAC (Customer Acquisition Cost):** Cost to acquire a customer
```
CAC = Total Acquisition Spend / New Customers Acquired
```

**LTV:CAC Ratio:** Unit economics health indicator
```
LTV:CAC = LTV / CAC
```

| Ratio | Interpretation |
|-------|----------------|
| <1:1 | Losing money on each customer |
| 1:1 - 3:1 | Potentially sustainable, watch closely |
| 3:1 - 5:1 | Healthy range for most businesses |
| >5:1 | Could be underinvesting in growth |

**CAC Payback Period:** Months to recover acquisition cost
```
CAC Payback = CAC / (ARPU × Gross Margin %)
```

Generally: <12 months is good, <6 months is great, >18 months is concerning.

### Building a Metrics Framework

Not all metrics deserve equal attention. Structure your approach:

#### Level 1: Health Metrics (Monitor)
Metrics you check regularly to ensure nothing is broken:
- System uptime
- Error rates
- Basic usage (DAU, sessions)

**Action:** Dashboard that alerts on anomalies

#### Level 2: KPIs (Track)
Key metrics tied to quarterly/annual goals:
- North Star Metric
- Revenue metrics
- Key conversion rates

**Action:** Weekly/monthly review, trend analysis

#### Level 3: Feature Metrics (Investigate)
Metrics for specific features or experiments:
- Feature adoption
- A/B test results
- Funnel conversions

**Action:** Analyze when launching or evaluating features

#### Level 4: Research Metrics (Deep Dive)
Metrics requiring special analysis:
- User segmentation analysis
- Predictive churn indicators
- Complex behavioral patterns

**Action:** Periodic research projects

### Metrics Anti-Patterns

#### Vanity Metrics

Metrics that look good but don't drive decisions:
- Total registered users (vs. active users)
- Page views (vs. engagement)
- Downloads (vs. activation)

**Fix:** Ask "What decision would change based on this metric?"

#### Gaming

When teams optimize the metric, not the outcome:
- Clickbait headlines boost clicks, damage trust
- Aggressive notifications boost opens, annoy users
- Discounts boost signups, hurt retention

**Fix:** Pair metrics with counter-metrics (clicks WITH time-on-page)

#### Averages That Lie

Averages can hide important segments:
- "Average session: 5 minutes" hides bimodal distribution (power users at 20 min, bouncers at 30 sec)
- "Average revenue: $100" hides high-value enterprise vs. low-value SMB

**Fix:** Look at distributions, cohorts, and segments—not just averages

#### Short-Term Focus

Optimizing for immediate metrics at long-term expense:
- Dark patterns boost conversion, damage brand
- Feature bloat boosts engagement, hurts usability

**Fix:** Include leading AND lagging indicators; monitor long-term trends

#### Too Many Metrics

Tracking everything means focusing on nothing:
- Dashboard overwhelm
- Analysis paralysis
- Conflicting priorities

**Fix:** Ruthlessly prioritize. If you have 50 KPIs, you have zero.

### Data-Informed, Not Data-Driven

**Data-driven:** Metrics dictate all decisions
**Data-informed:** Metrics inform decisions alongside judgment

Why the distinction matters:
- Data shows what happened, not always why
- Some important things are hard to measure (brand, trust, long-term relationships)
- Over-relying on data can miss breakthrough opportunities

**The balance:**
- Use data to identify problems and opportunities
- Use judgment to interpret and decide
- Validate judgment with data over time

---

## Key Takeaways

1. **Metrics enable decision-making, alignment, and learning—but what you measure shapes behavior**
2. **North Star Metric captures the core value delivered to customers and leads to business outcomes**
3. **Core metrics include acquisition (activation), engagement (DAU/MAU), retention (cohorts), and revenue (LTV/CAC)**
4. **Structure metrics into levels: health monitoring, KPIs, feature metrics, and research deep-dives**
5. **Watch for vanity metrics, gaming, misleading averages, and metric overload**
6. **Be data-informed, not data-driven—use metrics alongside judgment**

---

## Practice

### Reflection Questions
1. What's the implicit North Star Metric for a product you use daily? What inputs might drive it?
2. Have you seen metrics being "gamed"? What was the unintended consequence?
3. Think of a decision you made based on intuition. What data could have informed it?

### Exercise
**Metrics Framework Design:**

For a product (real or hypothetical):

1. **Define the North Star Metric**
   - What is it?
   - Why does it capture customer value?
   - What are 3 input metrics that drive it?

2. **Core KPIs**
   - One acquisition metric
   - One engagement metric
   - One retention metric
   - One revenue metric (if applicable)

3. **For each metric specify:**
   - How it's calculated
   - Current state (estimate if hypothetical)
   - Target
   - Why this target

4. **Identify one potential anti-pattern** and how you'd guard against it

---

## Further Reading

- **"Lean Analytics" by Alistair Croll** - Comprehensive product metrics guide
- **"Measure What Matters" by John Doerr** - OKRs and metrics alignment
- **"How to Measure Anything" by Douglas Hubbard** - Quantifying the seemingly immeasurable
- **Amplitude blog** - Product analytics best practices
- **Reforge** - Growth metrics deep dives
