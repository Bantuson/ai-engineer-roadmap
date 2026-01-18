# Prioritization Frameworks

## Learning Objectives

- [ ] Apply RICE scoring for quantitative prioritization
- [ ] Use MoSCoW for scope negotiation
- [ ] Apply ICE for quick prioritization
- [ ] Understand Kano model for feature categorization
- [ ] Apply Jobs-to-be-Done thinking for opportunity identification

## Prerequisites

- Completed: [01-Foundations module](../01-foundations/)

---

## Core Content

### Why Prioritization Matters

Every product team has more ideas than capacity. Prioritization is how you:
- Focus limited resources on highest impact work
- Make trade-offs explicit and defensible
- Align stakeholders on what matters
- Say no with rationale

**The best PMs are distinguished by their prioritization decisions, not their idea generation.**

### Framework Selection Guide

Different situations call for different frameworks:

| Framework | Best For | Strengths | Weaknesses |
|-----------|----------|-----------|------------|
| **RICE** | Roadmap planning, data-driven teams | Quantitative, comparable | Needs data, can be gamed |
| **MoSCoW** | Scope negotiation, releases | Clear categories, intuitive | Subjective, tendency to over-Must |
| **ICE** | Quick scoring, early-stage | Fast, simple | Less rigorous, inconsistent |
| **Kano** | Feature strategy, delight | Customer-focused, strategic | Requires research, complex |
| **JTBD** | Opportunity identification | Deep insight, durable | Time-intensive, requires skill |

### RICE Framework

RICE provides quantitative scoring for prioritization:

**R** - Reach: How many users affected
**I** - Impact: How much will it improve their experience
**C** - Confidence: How sure are we
**E** - Effort: How much work is required

#### RICE Formula

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

#### Defining Each Component

**Reach (per quarter):**
- How many users or customers will this impact?
- Measure: Number of users, transactions, etc.
- Example: "This will affect 10,000 users per quarter"

**Impact (scale):**
| Score | Meaning |
|-------|---------|
| 3 | Massive impact |
| 2 | High impact |
| 1 | Medium impact |
| 0.5 | Low impact |
| 0.25 | Minimal impact |

**Confidence (percentage):**
| Score | Meaning |
|-------|---------|
| 100% | High confidence (strong data) |
| 80% | Medium confidence (some data) |
| 50% | Low confidence (gut feel) |

**Effort (person-months):**
- Engineering, design, PM time combined
- Use consistent estimates across items

#### RICE Example

| Item | Reach | Impact | Confidence | Effort | Score |
|------|-------|--------|------------|--------|-------|
| Onboarding redesign | 5000 | 2 | 80% | 3 | 2,667 |
| Mobile app | 2000 | 3 | 50% | 6 | 500 |
| API improvements | 500 | 1 | 100% | 1 | 500 |
| Dark mode | 1000 | 0.5 | 80% | 2 | 200 |

**Result:** Onboarding redesign has highest RICE score and should be prioritized.

#### RICE Limitations

- **Gaming:** Teams can inflate numbers to get their pet projects through
- **Data requirements:** Hard when you don't have user data
- **Apples and oranges:** Comparing infrastructure work to features is difficult
- **False precision:** Numbers imply accuracy that doesn't exist

**Mitigation:** Use RICE as input to discussion, not as final arbiter.

### MoSCoW Method

MoSCoW categorizes items by necessity:

**M**ust Have — Non-negotiable for this release
**S**hould Have — Important but not critical
**C**ould Have — Nice to have, lower impact
**W**on't Have — Explicitly out of scope (for now)

#### Using MoSCoW

**Step 1:** List all items under consideration

**Step 2:** Force categorization
- Must: If we don't have this, we shouldn't release
- Should: Significantly diminished value without it
- Could: Adds value but can live without
- Won't: Not this time (may be future)

**Step 3:** Check distribution
- Healthy: ~60% Must, ~20% Should, ~20% Could
- Unhealthy: 90% Must (everything is "critical")

**Step 4:** Negotiate
- If capacity is insufficient for all Musts, re-evaluate
- If time is tight, cut Could first, then Should

#### MoSCoW Example

For MVP launch of a task management app:

| Feature | Category | Rationale |
|---------|----------|-----------|
| Create tasks | Must | Core functionality |
| Mark complete | Must | Core functionality |
| Due dates | Must | Key value prop |
| User accounts | Must | Multi-session requirement |
| Recurring tasks | Should | Significant value, not MVP |
| Tags/labels | Should | Organization, not critical |
| Dark mode | Could | User preference |
| Calendar integration | Could | Enhancement |
| Team sharing | Won't (v2) | Future release |
| Mobile app | Won't (v2) | Future release |

#### MoSCoW Limitations

- **Creeping Musts:** Everything becomes a Must over time
- **Subjectivity:** Different stakeholders disagree on categories
- **Binary thinking:** Doesn't capture degrees of importance within categories

**Mitigation:** Be strict about Must definition; use time-boxing.

### ICE Framework

ICE is a simplified scoring for quick prioritization:

**I** - Impact: Effect on goals (1-10)
**C** - Confidence: How sure we are (1-10)
**E** - Ease: How easy to implement (1-10)

#### ICE Formula

```
ICE Score = Impact × Confidence × Ease
```

#### ICE Example

| Item | Impact | Confidence | Ease | Score |
|------|--------|------------|------|-------|
| Checkout optimization | 9 | 8 | 6 | 432 |
| New payment method | 6 | 9 | 5 | 270 |
| Header redesign | 4 | 5 | 8 | 160 |
| Help center | 3 | 7 | 7 | 147 |

#### When to Use ICE

- Early-stage when you don't have data for RICE
- Quick prioritization in brainstorming
- When you need a starting point for discussion

**Warning:** ICE is subjective. Use it to start conversations, not end them.

### Kano Model

Kano categorizes features by how they affect customer satisfaction:

```
Satisfaction
     │
  High│         ╱ Delighters
     │        ╱
     │       ╱
     │      ╱ Performance
     │     ╱
     │────╱────────────────── Functionality
     │   ╱
  Low│  ╱ Must-Haves
     │ ╱
     └────────────────────────────────────
       Not Implemented    Fully Implemented
```

#### Kano Categories

**Must-Haves (Basic expectations):**
- Absence causes dissatisfaction
- Presence doesn't increase satisfaction (just baseline)
- Example: A car has brakes

**Performance (More is better):**
- Linear relationship with satisfaction
- More implementation = more satisfaction
- Example: A car has better fuel efficiency

**Delighters (Unexpected pleasures):**
- Absence doesn't cause dissatisfaction
- Presence significantly increases satisfaction
- Example: A car has heated steering wheel

**Indifferent (Users don't care):**
- Neither presence nor absence affects satisfaction
- Waste of resources to build

**Reverse (Users actively dislike):**
- Presence decreases satisfaction
- Remove or make optional

#### Kano Research Method

To categorize features, ask users two questions:

1. "How would you feel if this feature was present?"
2. "How would you feel if this feature was absent?"

Answer options: Like it, Expect it, Neutral, Live with it, Dislike it

The combination determines category:

| If Present → | Like | Expect | Neutral | Live with | Dislike |
|-------------|------|--------|---------|-----------|---------|
| **If Absent ↓** | | | | | |
| Like | ? | ? | ? | ? | Reverse |
| Expect | Delighter | Indifferent | Indifferent | Indifferent | Reverse |
| Neutral | Delighter | Indifferent | Indifferent | Indifferent | Reverse |
| Live with | Delighter | Indifferent | Indifferent | Indifferent | Reverse |
| Dislike | Performance | Must-Have | Must-Have | Must-Have | ? |

#### Kano Strategic Implications

| Category | Strategy |
|----------|----------|
| Must-Have | Must build; baseline quality only |
| Performance | Invest proportionally to importance |
| Delighter | Strategic investment for differentiation |
| Indifferent | Don't build |
| Reverse | Definitely don't build (or make optional) |

**Over time:** Delighters become Performance, Performance becomes Must-Have (expectation inflation).

### Jobs-to-be-Done (JTBD)

JTBD focuses on what users are trying to accomplish, not features they want.

**Core principle:** People don't want a quarter-inch drill. They want a quarter-inch hole.

#### The Job Statement

Format:
```
When [situation], I want to [motivation], so I can [expected outcome].
```

Examples:
- "When I have 5 minutes between meetings, I want to check urgent messages, so I can stay responsive without full context switch."
- "When I'm onboarding a new team member, I want to share our project history, so they can get up to speed quickly."

#### JTBD for Prioritization

**Step 1:** Identify key jobs your product addresses

**Step 2:** Understand job importance and current satisfaction
- Important but unsatisfied = opportunity
- Important and satisfied = defend
- Unimportant = deprioritize

**Step 3:** Evaluate features against jobs
- Does this feature help users complete an important job better?
- Or does it address a job they don't actually have?

#### JTBD Opportunity Score

```
Opportunity = Importance + (Importance - Satisfaction)
```

Maximum opportunity exists when importance is high and satisfaction is low.

| Job | Importance (1-10) | Satisfaction (1-10) | Opportunity |
|-----|-------------------|---------------------|-------------|
| Find relevant info quickly | 9 | 4 | 14 |
| Track project progress | 7 | 7 | 7 |
| Share updates with team | 8 | 6 | 10 |
| Export for reporting | 5 | 5 | 5 |

**Result:** "Find relevant info quickly" is biggest opportunity.

### Framework Comparison Table

| Aspect | RICE | MoSCoW | ICE | Kano | JTBD |
|--------|------|--------|-----|------|------|
| Quantitative | ✅ | ❌ | ✅ | ❌ | ✅ |
| Speed | Medium | Fast | Fast | Slow | Slow |
| Data needed | Yes | No | No | Yes (research) | Yes (research) |
| Team alignment | Good | Good | Fair | Good | Excellent |
| Strategic insight | Low | Low | Low | High | High |

### Combining Frameworks

Use multiple frameworks together:

1. **JTBD** to identify which jobs matter (quarterly/annual)
2. **Kano** to categorize features strategically (quarterly)
3. **RICE/MoSCoW** to prioritize what to build (sprint/release)
4. **ICE** for quick daily decisions

---

## Key Takeaways

1. **RICE provides quantitative scoring but requires data and can be gamed**
2. **MoSCoW is intuitive for scope negotiation but watch for "creeping Musts"**
3. **ICE is fast but subjective—use for starting discussions, not ending them**
4. **Kano reveals strategic positioning—Must-Have vs. Delighter changes strategy**
5. **JTBD provides durable insight into what users actually need**
6. **Combine frameworks: JTBD for strategy, RICE/MoSCoW for execution**

---

## Practice

### Exercise 1: RICE Scoring

You have these items to prioritize for next quarter:
1. Improve page load speed by 50%
2. Add social login (Google, Apple)
3. Launch mobile app
4. Implement usage analytics dashboard

Estimate RICE components for each and calculate scores. Document your assumptions.

### Exercise 2: MoSCoW Negotiation

Your sprint has room for 20 story points, but your backlog has:
- Must (25 points): User auth, core feature, bug fix
- Should (15 points): UI polish, minor features
- Could (10 points): Nice-to-haves

How do you resolve this? What conversations need to happen?

### Exercise 3: JTBD Analysis

Pick a product you use daily. Identify 3 "jobs" you hire it for using the job statement format. Rate importance and satisfaction. What opportunities exist?

---

## Further Reading

- **"Inspired" by Marty Cagan** - Product prioritization in context
- **"Competing Against Luck" by Clayton Christensen** - Jobs-to-be-Done deep dive
- **"The Kano Model" by Noriaki Kano** - Original research
- **Intercom on RICE** - Practical RICE guidance
