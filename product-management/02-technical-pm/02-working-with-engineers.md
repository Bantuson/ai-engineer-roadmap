# Working with Engineers

## Learning Objectives

- [ ] Build trust and respect with engineering teams
- [ ] Translate between business needs and technical requirements
- [ ] Participate effectively in technical discussions
- [ ] Handle disagreements constructively
- [ ] Avoid common PM behaviors that frustrate engineers

## Prerequisites

- Completed: [01 - Tech Foundations](./01-tech-foundations.md)

---

## Core Content

### The PM-Engineer Relationship

The relationship between PMs and engineers is the most critical collaboration in product development. Get it right, and you build great products. Get it wrong, and you build resentment.

**The fundamental dynamic:**
- PMs are responsible for **what** to build and **why**
- Engineers are responsible for **how** to build it
- The boundary between these is fuzzy, and that's okay

**What great PM-engineer partnerships look like:**
- Mutual respect for different expertise
- Shared ownership of outcomes
- Healthy debate with resolution
- Trust that each is doing their best

### Building Trust with Engineers

Trust is earned, not demanded. Here's how:

#### 1. Respect Their Expertise

Engineers spent years learning their craft. When they say something is hard, believe them.

**Do:**
- Ask "help me understand why" instead of pushing back
- Acknowledge complexity you don't fully grasp
- Value technical opinions in decisions

**Don't:**
- Say "just make it work"
- Question estimates without understanding
- Treat engineering as order-taking

#### 2. Be Prepared

Nothing frustrates engineers more than poorly thought-through requests.

**Before asking for work:**
- Have clarity on the problem, not just the solution
- Know the user context and why it matters
- Anticipate obvious questions
- Have prioritization reasoning ready

#### 3. Protect Their Time

Engineers do deep work that requires focus. Context switching is expensive.

**Respect practices:**
- Don't interrupt for non-urgent questions
- Batch requests when possible
- Honor meeting-free time
- Write things down instead of drive-by conversations

#### 4. Shield from Politics

Engineering teams shouldn't need to navigate organizational politics.

**Your job:**
- Filter stakeholder requests through prioritization
- Translate executive pressure into clear priorities
- Take the heat for saying no
- Celebrate engineering wins up the chain

#### 5. Follow Through

Do what you say you'll do.

**Build credibility:**
- Get answers when you promise them
- Update priorities promptly when they change
- Close loops on feedback and questions
- Admit when you were wrong

### Translating Business to Technical

One of the PM's core jobs is translation:

```
┌────────────────┐         ┌────────────────┐         ┌────────────────┐
│  STAKEHOLDER   │  ─────▶ │       PM       │  ─────▶ │   ENGINEER     │
│  "Make it      │         │                │         │  "Create API   │
│  faster"       │         │  (Translation) │         │  caching with  │
│                │         │                │         │  60s TTL"      │
└────────────────┘         └────────────────┘         └────────────────┘
```

#### Common Translations

| Business Says | Might Mean | Clarify By Asking |
|---------------|------------|-------------------|
| "Make it faster" | Reduce load time? Fewer clicks? Quicker onboarding? | "Faster in what way? What are users experiencing?" |
| "Make it simpler" | Less features? Cleaner UI? Easier onboarding? | "Simpler for whom? What's complex today?" |
| "Enterprise ready" | SSO? Permissions? Audit logs? SLAs? | "What specific capabilities do enterprise customers require?" |
| "We need analytics" | Dashboards? Events? Reports? | "What decisions will analytics inform?" |

#### The "5 Whys" Technique

When a stakeholder requests a feature, dig for the underlying need:

**Request:** "We need a CSV export feature"

1. Why? "So users can get their data out"
2. Why do they need data out? "For reporting to their leadership"
3. Why can't they use our reporting? "It doesn't have the metrics they need"
4. Why those metrics? "They track X and Y for quarterly reviews"
5. Why not build X and Y into our reporting? "...actually, that might be better"

**Result:** Instead of CSV export, build the actual metrics users need.

### Participating in Technical Discussions

PMs should participate in technical discussions—not to dictate solutions, but to represent user and business context.

#### Your Role in Technical Discussions

**Bring:**
- User context and pain points
- Business constraints and priorities
- Acceptance criteria
- Questions about user impact

**Don't bring:**
- Opinions about implementation approach (unless asked)
- Pressure to choose faster options
- Solutions without understanding trade-offs

#### Useful Questions to Ask

**Clarifying impact:**
- "How would this affect user experience?"
- "What are the risks if we go with option A vs B?"
- "What happens if this fails?"

**Understanding trade-offs:**
- "What are we giving up with this approach?"
- "Is there a simpler version we could start with?"
- "What would we need to revisit later?"

**Checking assumptions:**
- "What do we need to be true for this to work?"
- "What don't we know yet?"
- "How will we know if this is working?"

#### When You Don't Understand

It's okay to not understand everything. What's not okay is pretending you do.

**Helpful phrases:**
- "Can you explain that in terms of user impact?"
- "I'm not following the technical part—can you help me understand?"
- "What's the bottom line for what we can ship and when?"

Engineers generally appreciate when PMs honestly engage rather than nod along.

### Handling Disagreements

Disagreements are healthy. How you handle them matters.

#### PM-Engineer Conflicts

**Common sources:**
- Scope and timeline pressure
- Technical approach preferences
- Quality vs. speed trade-offs
- Priority disagreements

**Resolution framework:**

1. **Assume good intent** — They're trying to build a good product too
2. **Understand their position** — Ask questions before arguing
3. **Share your constraints** — Make business context visible
4. **Find common ground** — What do you agree on?
5. **Escalate appropriately** — If truly stuck, involve leadership

#### When Engineers Push Back on Scope

**Typical scenario:** You've specced a feature, engineers say it's too much.

**Unproductive response:**
"We committed to this. Figure it out."

**Productive response:**
"Help me understand what's driving the complexity. What could we cut that would significantly reduce effort while keeping core value?"

**The goal:** Find the version that maximizes value within constraints, not win an argument.

#### When You Think Something Is Easier Than Quoted

**Before challenging:**
1. Do you actually understand the work?
2. Have you asked what's driving the estimate?
3. Are there factors you're not seeing?

**If still unclear:**
"Help me understand the effort. I want to make sure I'm representing this accurately when I'm prioritizing."

**What NOT to say:**
- "That seems like a lot"
- "Can't we just..."
- "It's only a small change"

### Common PM Behaviors That Frustrate Engineers

Avoid these anti-patterns:

#### 1. Changing Requirements Mid-Sprint
**Impact:** Waste, context switching, trust erosion

**Instead:** Batch changes, wait for sprint boundaries, be explicit about trade-offs

#### 2. "Can We Just..."
**Impact:** Minimizes complexity, shows disrespect

**Instead:** "What would it take to..." or "Help me understand the effort for..."

#### 3. Asking for Estimates Then Treating Them as Commitments
**Impact:** Defensive estimating, padded timelines

**Instead:** Understand estimates are ranges, revisit as you learn more

#### 4. Micromanaging Implementation
**Impact:** Undermines expertise, slows decisions

**Instead:** Define outcomes, let engineers decide approach

#### 5. Not Being Available for Questions
**Impact:** Blocks progress, leads to assumptions

**Instead:** Make yourself accessible, respond promptly, clarify quickly

#### 6. Taking Credit, Assigning Blame
**Impact:** Destroys trust, creates adversarial dynamics

**Instead:** Credit the team publicly, take responsibility for PM decisions

### The PM-Engineer Working Agreement

Consider establishing explicit norms:

**Example working agreement:**

```
How we work together:
- PRDs are reviewed before sprint planning
- Questions answered within 4 hours during work hours
- Scope changes require PM-engineering discussion
- Engineers can push back on technical approach
- PM owns priority, engineering owns estimates
- We demo together, celebrate together
```

### Embedded vs. Partnered Models

Different orgs structure PM-engineering relationships differently:

**Embedded:** PM is part of the engineering team
- Pros: Deep context, strong relationships
- Cons: May lose broader perspective

**Partnered:** PM works across multiple teams
- Pros: Cross-team perspective, efficiency
- Cons: Less depth, context switching

**What matters more than structure:** Mutual respect, clear communication, shared goals.

---

## Key Takeaways

1. **The PM-engineer relationship is built on trust, earned through respect, preparation, and follow-through**
2. **Translate between business needs and technical requirements—dig for underlying problems**
3. **Participate in technical discussions to represent users and business, not to dictate solutions**
4. **Handle disagreements by understanding their position first, then sharing your constraints**
5. **Avoid anti-patterns: scope changes, "just" language, estimate-to-commitment conversion, micromanaging**
6. **Establish working agreements to set clear expectations**

---

## Practice

### Reflection Questions
1. Think of a PM or manager who engineers loved working with. What did they do differently?
2. Recall a PM-engineering conflict you've observed or experienced. How was it handled? How could it have been better?
3. What PM behaviors have you seen that created friction with engineering teams?

### Exercise
**Translation Practice:**

For each business request below, write:
1. Clarifying questions you'd ask
2. What the underlying need might be
3. How you'd frame it for engineers

**Request 1:** "Sales needs a dashboard"

**Request 2:** "Make the product more secure"

**Request 3:** "We need to be faster than competitor X"

**Request 4:** "Users are complaining the app is confusing"

**Example format:**
```
Request: "Sales needs a dashboard"

Clarifying questions:
- What information does sales need that they can't get today?
- What decisions will the dashboard inform?
- How often do they need this data refreshed?

Underlying need:
Sales can't see pipeline health and customer activity without asking multiple people

Engineer framing:
"Sales needs visibility into [specific metrics]. We're exploring whether we can add these to existing reports or need a dedicated view. Key questions: what data sources, what refresh rate, who has access?"
```

---

## Further Reading

- **"Team Topologies" by Matthew Skelton** - How team structures affect collaboration
- **"The Manager's Path" by Camille Fournier** - Engineering leadership perspective
- **"Inspired" by Marty Cagan** - The product team triad model
- **Lenny's Podcast** - Interviews with PMs about engineering collaboration
- **Engineering blogs** (Stripe, Shopify, etc.) - See how engineers think
