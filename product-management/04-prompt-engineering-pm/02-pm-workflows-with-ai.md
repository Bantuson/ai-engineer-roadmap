# PM Workflows with AI

## Learning Objectives

- [ ] Apply AI to accelerate user research synthesis
- [ ] Use AI for PRD drafting and refinement
- [ ] Leverage AI for competitive analysis
- [ ] Create personas and user journeys with AI assistance
- [ ] Know when AI helps vs. hinders PM work

## Prerequisites

- Completed: [01 - Prompt Fundamentals](./01-prompt-fundamentals.md)
- Access to an AI assistant

---

## Core Content

### The AI-Augmented PM

AI doesn't replace PM thinking—it accelerates it.

**Before AI:**
```
Research → Synthesize → Draft → Refine → Finalize
   (days)    (hours)    (hours)  (hours)   (hours)
```

**With AI:**
```
Research → AI Synthesize → Review → AI Draft → Refine → Finalize
  (days)    (minutes)     (hour)   (minutes) (hour)   (minutes)
```

The thinking remains yours. The processing gets faster.

### Workflow 1: User Research Synthesis

**The challenge:** You have 20 user interview transcripts and need to synthesize key insights.

**Without AI:** Read each, take notes, find patterns, write up. (4-8 hours)

**With AI:** Use AI to accelerate pattern recognition. (1-2 hours)

#### The Process

**Step 1: Prepare the data**
Clean transcripts, remove PII if needed.

**Step 2: First-pass synthesis**
```
I have 20 user interview transcripts about [topic]. I'll provide them
in batches. For each batch:

1. Extract key quotes that reveal user needs or pain points
2. Tag each quote with a theme
3. Note any surprising or contradictory findings

After all batches, I'll ask you to synthesize across them.

Here's batch 1 of 4:
[Paste 5 transcripts]
```

**Step 3: Cross-batch synthesis**
```
Now synthesize across all batches:

1. What are the top 5 themes by frequency?
2. What themes were most emotionally charged?
3. What contradictions or segments emerged?
4. What surprised you about the findings?

Format as an executive summary followed by detailed findings.
```

**Step 4: Human review**
- Verify the themes match your reading
- Check if important nuances were lost
- Add your interpretation and recommendations

#### When to Use This

**Good fit:**
- High volume of feedback to synthesize
- Looking for patterns across many sources
- Need quick first-pass analysis

**Bad fit:**
- Small number of rich interviews (read them yourself)
- Highly sensitive or confidential content
- When nuance and context are critical

### Workflow 2: PRD Drafting

**The challenge:** You need to write a PRD for a new feature.

**AI role:** Generate structured first draft that you refine.

#### The Process

**Step 1: Provide thorough context**
```
I need to write a PRD for a new feature. Here's the context:

Product: [Your product description]
Feature: [What you're building]
User problem: [The problem this solves]
Target user: [Who will use this]
Business goal: [Why we're building this]
Constraints: [Technical, timeline, resource constraints]

Key things I know:
- [Insight 1]
- [Insight 2]
- [Insight 3]

Key things I'm uncertain about:
- [Question 1]
- [Question 2]
```

**Step 2: Request structured draft**
```
Write a PRD draft including:
1. Problem statement
2. Goals and non-goals
3. User stories (5-7)
4. Key requirements (P0/P1/P2 prioritized)
5. Success metrics
6. Open questions

Use our PRD template structure:
[Paste your template or link to it]
```

**Step 3: Iterate on sections**
```
The user stories are good but too high-level. For user story 3:
- Break it into 3 more specific stories
- Add acceptance criteria with edge cases
- Consider error states
```

**Step 4: Critical review**
```
Now act as a skeptical engineering lead reviewing this PRD:
- What's unclear or ambiguous?
- What edge cases are missing?
- What technical concerns would you raise?
- What questions would block starting work?
```

**Step 5: Human finalization**
- Verify accuracy of all claims
- Add your judgment and prioritization rationale
- Fill in things only you know
- Review with actual stakeholders

#### Cautions

- **Don't skip your thinking** — AI drafts can feel "done" when they're not
- **Verify technical claims** — AI may suggest impossible or impractical things
- **Add your context** — AI doesn't know your organization's politics, history, constraints
- **Own the document** — You're accountable for what ships

### Workflow 3: Competitive Analysis

**The challenge:** Understand competitor landscape for planning.

**AI role:** Structured research and comparison.

#### The Process

**Step 1: Landscape mapping**
```
I'm doing competitive analysis for [your product category].

Our product: [Description]
Target market: [Who you serve]
Key differentiators: [What makes you unique]

Based on this context, identify:
1. Direct competitors (similar products, similar market)
2. Indirect competitors (different products, same problem)
3. Potential future competitors (adjacent players who could enter)

For each, note what they're known for.
```

**Step 2: Deep dive on key competitors**
```
For [Competitor X], analyze:

1. Product capabilities
   - Core features
   - Unique features
   - Notable gaps

2. Positioning
   - Target customer
   - Key messaging
   - Pricing model

3. Recent developments
   - New features (last 6 months)
   - Strategic moves
   - Funding/news

4. Strengths to learn from
5. Weaknesses we can exploit

Use only publicly available information.
```

**Step 3: Synthesis**
```
Create a competitive comparison matrix:

| Capability | Us | Competitor A | Competitor B | Competitor C |
|------------|-----|--------------|--------------|--------------|

Include: [List key capabilities to compare]

Then summarize:
- Where we're ahead
- Where we're behind
- Key battleground areas
- Recommended focus
```

#### Cautions

- **Verify with primary sources** — AI may have outdated or incorrect info
- **Check pricing and features** — These change frequently
- **Supplement with user feedback** — What do customers who evaluated competitors say?
- **Don't over-index on features** — Strategy is about positioning, not checklists

### Workflow 4: Persona Development

**The challenge:** Create user personas to guide product decisions.

**AI role:** Structure and flesh out personas from research data.

#### The Process

**Step 1: Provide research foundation**
```
I'm creating personas for our [product]. Here's what we know:

User research findings:
[Paste synthesized research]

Customer segments from data:
[Any segmentation you have]

Sales feedback on customer types:
[What sales team reports]

Create 3 distinct personas that represent our key user segments.
```

**Step 2: Structure each persona**
```
For each persona, include:

1. Basic info
   - Name and role
   - Company type/size
   - Demographics relevant to product use

2. Context
   - Day in their life
   - Goals and motivations
   - Frustrations and pain points

3. Product relationship
   - How they discover solutions
   - What they value most
   - Buying process involvement

4. Quote that captures their mindset

Format as a persona card I could print and share.
```

**Step 3: Validate and refine**
```
Looking at Persona 1 (Sarah):
- Is this consistent with users you've interviewed?
- What would make this more specific and useful?
- What scenarios would Sarah be involved in?
```

**Step 4: Human validation**
- Compare to real users you've met
- Get feedback from sales/support who interact with users
- Refine based on team input
- Ensure personas drive actual decisions

### Workflow 5: Roadmap Communication

**The challenge:** Communicate roadmap to different audiences.

**AI role:** Adapt messaging for different stakeholders.

#### The Process

```
Here's our Q2 roadmap:
[Paste roadmap details]

Create three versions of a roadmap update:

1. Engineering team (weekly all-hands)
   - Focus: Technical priorities, dependencies, what's changing
   - Tone: Detailed, specific
   - Length: 5-7 minutes of talking points

2. Executive team (monthly review)
   - Focus: Business impact, metrics, strategic alignment
   - Tone: High-level, outcome-focused
   - Length: 2 slides worth

3. Customer newsletter (quarterly update)
   - Focus: What's coming for them, timeline expectations
   - Tone: Excited but not overpromising
   - Length: 200 words
```

### When AI Helps vs. Hinders

#### AI Helps With

| Task | Why AI Helps |
|------|--------------|
| Synthesis | Processing large volumes quickly |
| First drafts | Starting from structure vs. blank page |
| Structure | Organizing thoughts into frameworks |
| Edge cases | Generating scenarios you might miss |
| Translation | Adapting content for different audiences |
| Brainstorming | Generating options to evaluate |

#### AI Hinders When

| Situation | Why AI Hurts |
|-----------|--------------|
| Deep context needed | AI doesn't know your org |
| Relationship nuance | Stakeholder dynamics are human |
| Strategic judgment | Trade-offs require your values |
| Original insight | AI remixes existing ideas |
| Accountability | You own the output |

#### The Right Balance

```
         ┌─────────────────────────────────────────┐
         │                                         │
         │    AI-HEAVY          BALANCED           │
         │    ─────────         ────────           │
         │    Synthesis         PRD drafting       │
         │    Formatting        Competitive intel   │
         │    First drafts      Persona creation   │
         │                                         │
         │                                         │
         │    HUMAN-HEAVY                          │
         │    ───────────                          │
         │    Strategy                             │
         │    Relationships                        │
         │    Final decisions                      │
         │    Accountability                       │
         │                                         │
         └─────────────────────────────────────────┘
```

---

## Key Takeaways

1. **AI accelerates PM workflows but doesn't replace PM thinking**
2. **User research synthesis: AI finds patterns in volume; you add interpretation**
3. **PRD drafting: AI generates structure; you add judgment and accountability**
4. **Competitive analysis: AI structures research; you verify and strategize**
5. **Know when to lean on AI (synthesis, drafting) vs. when to rely on yourself (strategy, relationships)**
6. **Always verify AI outputs—you're accountable for the result**

---

## Practice

### Exercise 1: Research Synthesis

Take a set of product reviews or customer feedback for a product you use (Amazon reviews, App Store reviews, etc.).

Use AI to:
1. Synthesize into top 5 themes
2. Identify most emotional topics
3. Find contradictions

Compare AI synthesis to your own reading. What did AI catch? What did it miss?

### Exercise 2: PRD Drafting

Using the scenario from the Technical PM mini-project (My Tasks dashboard), use AI to:
1. Generate a first draft PRD
2. Have AI critique its own draft
3. Iterate based on the critique

Compare to what you would write yourself. How useful was the AI assist?

### Exercise 3: Audience Adaptation

Take a complex feature you understand well. Use AI to explain it:
1. To an engineer (technical depth)
2. To a sales rep (customer benefit)
3. To a user (plain language)
4. To an executive (business impact)

Evaluate which versions are genuinely useful for each audience.

---

## Further Reading

- **"AI for Product Managers" by various** - Blog posts on PM + AI
- **Product Hunt AI tools** - See what's available for PM workflows
- **Reforge AI content** - Strategic thinking about AI in product
