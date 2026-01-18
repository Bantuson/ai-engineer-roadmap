# Roadmapping

## Learning Objectives

- [ ] Distinguish between roadmap types (feature, timeline, outcome-based, now-next-later)
- [ ] Choose the appropriate roadmap format for your context
- [ ] Create outcome-based roadmaps that enable flexibility
- [ ] Avoid common roadmapping pitfalls
- [ ] Use roadmaps as alignment tools, not contracts

## Prerequisites

- Completed: [01 - What is Product Management?](./01-what-is-pm.md)
- Completed: [04 - Product Strategy](./04-product-strategy.md)

---

## Core Content

### What is a Roadmap?

A product roadmap is **a communication tool that shows how your product will evolve to achieve your strategy.**

Note: Communication tool, not project plan.

**What roadmaps DO:**
- Align stakeholders on direction
- Communicate priorities
- Show strategic intent
- Enable coordination across teams

**What roadmaps DON'T (shouldn't):**
- Guarantee specific delivery dates
- List every task or feature
- Replace backlog management
- Lock teams into commitments they can't keep

### The Roadmap Audience Problem

Different audiences need different things from roadmaps:

| Audience | What They Need | What They'll Misuse |
|----------|---------------|---------------------|
| **Executives** | Strategic alignment, major bets | Will quote dates to customers |
| **Sales** | What's coming for deal discussions | Will promise specific features |
| **Engineering** | Priority clarity, dependencies | May treat as unchangeable |
| **Marketing** | Launch planning windows | Will build campaigns around dates |
| **Customers** | Direction and investment signals | Will make buying decisions on promises |

**This is why roadmap format matters:** The same roadmap doesn't serve all audiences well.

### Roadmap Types

#### 1. Feature Roadmap

Lists specific features with release dates.

```
Q1 2025: Advanced search, User profiles 2.0
Q2 2025: Mobile app, Integrations API
Q3 2025: Enterprise SSO, Audit logs
Q4 2025: Marketplace, Analytics dashboard
```

**Pros:**
- Concrete and specific
- Easy to track progress
- Familiar to stakeholders

**Cons:**
- Implies false certainty about timing
- Features may not solve the underlying problem
- Creates commitment pressure
- Discourages learning and pivoting

**When to use:** Internal planning with engineering, near-term (1-2 sprints), already-committed work.

#### 2. Timeline Roadmap

Shows features on a timeline (often swimlanes by theme).

```
            Q1 2025     Q2 2025     Q3 2025     Q4 2025
┌──────────┬───────────┬───────────┬───────────┬───────────┐
│ Growth   │ Onboarding│ Referral  │ Retention │ Expansion │
│          │ revamp    │ program   │ triggers  │ flows     │
├──────────┼───────────┼───────────┼───────────┼───────────┤
│ Platform │ API v2    │ Webhooks  │ SDK       │ Partner   │
│          │           │           │           │ portal    │
├──────────┼───────────┼───────────┼───────────┼───────────┤
│ Trust    │ SOC2      │ GDPR      │ Audit     │ SSO       │
│          │ audit     │ tools     │ logs      │           │
└──────────┴───────────┴───────────┴───────────┴───────────┘
```

**Pros:**
- Shows cross-team dependencies
- Helps capacity planning
- Visually appealing for presentations

**Cons:**
- Dates become promises
- Pressure to fill quarters
- Hard to update when plans change

**When to use:** Executive communication (with heavy caveats), annual planning, coordinating multiple teams.

#### 3. Now-Next-Later Roadmap

Groups work by time horizon without specific dates.

```
┌─────────────────────────────────────────────────────────────────┐
│ NOW (Current quarter)                                           │
│ High certainty - actively being built                           │
│                                                                 │
│ • Onboarding flow rebuild (70% complete)                        │
│ • Performance improvements (in progress)                        │
│ • Critical bug fixes (ongoing)                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ NEXT (1-2 quarters out)                                         │
│ Medium certainty - designed but not started                     │
│                                                                 │
│ • Team collaboration features                                   │
│ • Advanced reporting                                            │
│ • Mobile app MVP                                                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LATER (3+ quarters out)                                         │
│ Low certainty - exploring and researching                       │
│                                                                 │
│ • Enterprise tier expansion                                     │
│ • International markets                                         │
│ • Platform/API strategy                                         │
└─────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Honest about uncertainty
- Enables flexibility
- Reduces false commitment
- Simple to maintain

**Cons:**
- Less satisfying for stakeholders wanting dates
- "Later" can become a dumping ground
- Doesn't show dependencies well

**When to use:** General stakeholder communication, team alignment, situations requiring flexibility.

#### 4. Outcome-Based Roadmap

Organized around outcomes (goals) rather than features.

```
┌─────────────────────────────────────────────────────────────────┐
│ OUTCOME: Reduce time-to-value for new users                     │
│ Metric: 7-day activation rate from 23% → 40%                    │
│                                                                 │
│ Opportunities being explored:                                   │
│ • Guided onboarding experience                                  │
│ • Template library                                              │
│ • Quick-start wizard                                            │
│ • Sample data population                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ OUTCOME: Enable team collaboration to expand accounts           │
│ Metric: Average seats per account from 2.1 → 4.0                │
│                                                                 │
│ Opportunities being explored:                                   │
│ • Shared workspaces                                             │
│ • Permission system                                             │
│ • Activity feeds                                                │
│ • Comments and mentions                                         │
└─────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Focuses on impact, not output
- Allows solution flexibility
- Connects to strategy clearly
- Enables team autonomy

**Cons:**
- Stakeholders may want more specificity
- Requires metrics discipline
- Team must be comfortable with ambiguity

**When to use:** Empowered product teams, OKR-driven organizations, when flexibility is valued.

### The Best Approach: Outcome + Now-Next-Later

Combining outcome-based thinking with time horizons creates the most useful roadmap:

```
┌─────────────────────────────────────────────────────────────────┐
│ NOW - Reducing Time to Value                                    │
│ Goal: 7-day activation 23% → 40%                                │
│                                                                 │
│ Building: Guided onboarding flow, Template library              │
│ Status: Onboarding 80% complete, Templates in design            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ NEXT - Enabling Team Collaboration                              │
│ Goal: Average seats 2.1 → 4.0                                   │
│                                                                 │
│ Exploring: Shared workspaces, permissions, activity feeds       │
│ Status: Discovery research in progress                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LATER - Enterprise Expansion                                    │
│ Goal: Enterprise revenue $0 → $500k ARR                         │
│                                                                 │
│ Considering: SSO, audit logs, advanced admin, compliance        │
│ Status: Customer interviews scheduled                           │
└─────────────────────────────────────────────────────────────────┘
```

This format:
- Shows what you're trying to achieve (outcomes)
- Indicates timing without false precision (now/next/later)
- Lists current thinking (specific initiatives)
- Communicates confidence level (status)

### Creating a Roadmap

#### Step 1: Start with Strategy

Your roadmap should directly support your strategy. If items don't connect to strategic themes, question whether they belong.

Ask: "How does this initiative support our strategic priorities?"

#### Step 2: Define Outcomes

What business or user outcomes are you targeting? Each major roadmap item should have:
- Clear success metric
- Target improvement
- Rationale for prioritization

#### Step 3: Identify Initiatives

What might move those metrics? At this stage:
- List options, don't commit
- Size roughly (T-shirt sizing)
- Consider dependencies

#### Step 4: Prioritize

Using frameworks like RICE, ICE, or value vs. effort (covered in Frameworks module):
- What has highest impact?
- What has acceptable effort?
- What must come first (dependencies)?

#### Step 5: Assign Confidence Levels

Be honest about what you know:
- **Now:** High confidence—committed, in progress
- **Next:** Medium confidence—designed, not started
- **Later:** Low confidence—exploring

#### Step 6: Communicate Appropriately

Different versions for different audiences:
- Internal team: More detail, more specificity
- Executives: Outcome-focused, strategic alignment
- External/customers: High-level themes, no promises

### Roadmap Maintenance

**Regular reviews:**
- Weekly: Team check-ins on "Now" items
- Monthly: Leadership review of progress
- Quarterly: Full roadmap refresh

**When to update:**
- When priorities shift based on learning
- When estimates prove wrong
- When market conditions change
- When resources change

**Versioning:** Keep historical roadmaps. They're useful for retrospectives and demonstrating responsiveness.

### Common Roadmap Mistakes

#### Mistake 1: Feature Factory

Treating the roadmap as a feature list to ship rather than outcomes to achieve.

**Fix:** Start with outcomes, not features. Measure success by metrics, not shipping.

#### Mistake 2: Date Overconfidence

Putting specific dates on uncertain work, creating commitments you can't keep.

**Fix:** Use time horizons (now/next/later) or ranges ("Q2-Q3") for uncertain work.

#### Mistake 3: Everything is P0

When everything is high priority, nothing is. Roadmaps need clear prioritization.

**Fix:** Force stack ranking. Only 1-3 things can truly be "now."

#### Mistake 4: Set and Forget

Creating a roadmap once and not updating it as you learn.

**Fix:** Regular review cadence. Roadmaps are living documents.

#### Mistake 5: Solving for Stakeholder Requests

Loading the roadmap with features requested by loudest stakeholders rather than most valuable outcomes.

**Fix:** Always connect items to outcomes and strategy. Challenge "pet features."

#### Mistake 6: No Explicit Trade-offs

Not showing what you're NOT doing, creating expectation that everything will get done.

**Fix:** Include a "not doing" or "parking lot" section. Make trade-offs visible.

---

## Key Takeaways

1. **Roadmaps are communication tools, not project plans—they align stakeholders on direction**
2. **Different audiences need different formats—one roadmap doesn't serve all needs**
3. **Outcome-based roadmaps focus on impact and enable solution flexibility**
4. **Now-Next-Later provides honest communication about uncertainty**
5. **Regularly maintain and update roadmaps as you learn**
6. **Avoid the feature factory trap—measure success by outcomes, not shipping**

---

## Practice

### Reflection Questions
1. Think of a roadmap you've seen or used. What format was it? How effective was it?
2. Have you experienced roadmap dates becoming problematic commitments? What happened?
3. How might different stakeholders in your organization react to an outcome-based roadmap?

### Exercise
**Create a Now-Next-Later Roadmap:**

For a product you know well (your company's, a side project, or a product you use):

1. Define 2-3 strategic outcomes with metrics
2. List 3-4 potential initiatives for each outcome
3. Assign to now/next/later based on priority
4. Write a one-paragraph "not doing" section

Format:
```
Product: [Name]

NOW (High confidence)
Outcome: [Metric: X → Y]
• Initiative 1
• Initiative 2

NEXT (Medium confidence)
Outcome: [Metric: X → Y]
• Initiative 1
• Initiative 2

LATER (Low confidence)
Outcome: [Metric: X → Y]
• Initiative 1
• Initiative 2

NOT DOING (explicit trade-offs):
[List items you're deliberately deprioritizing and why]
```

---

## Further Reading

- **"Product Roadmaps Relaunched" by C. Todd Lombardo** - Comprehensive roadmapping guide
- **"Escaping the Build Trap" by Melissa Perri** - Outcome-focused product management
- **"Shape Up" by Basecamp** - Alternative approach to planning and roadmapping
- **Silicon Valley Product Group blog** - Ongoing roadmapping best practices
- **Mind the Product** - Community discussions on roadmapping approaches
