# User Research & Discovery

## Learning Objectives

- [ ] Distinguish between generative and evaluative research
- [ ] Conduct effective user interviews
- [ ] Design surveys that yield actionable insights
- [ ] Implement continuous discovery practices
- [ ] Synthesize research into actionable findings

## Prerequisites

- Completed: [01 - What is Product Management?](./01-what-is-pm.md)
- Completed: [02 - Product Lifecycle](./02-product-lifecycle.md)

---

## Core Content

### Why User Research Matters

**The biggest risk in product development is building something nobody wants.**

User research reduces this risk by:
- Validating that problems exist before solving them
- Understanding user context, not just stated preferences
- Identifying opportunities invisible from inside the building
- Informing decisions with evidence rather than opinions

**The uncomfortable truth:** Your intuition about users is probably wrong. Even experienced PMs who are users themselves miss crucial context.

### Generative vs. Evaluative Research

These two categories serve fundamentally different purposes:

| Aspect | Generative Research | Evaluative Research |
|--------|--------------------|--------------------|
| **Purpose** | Discover problems and opportunities | Validate solutions and designs |
| **Question** | "What should we build?" | "Did we build it right?" |
| **Timing** | Early in process | Later in process |
| **Methods** | Interviews, observation, diary studies | Usability tests, A/B tests, surveys |
| **Outcome** | Problem statements, opportunities | Design decisions, go/no-go |

**Common mistake:** Jumping to evaluative research without generative research. You can perfectly validate a solution to the wrong problem.

### User Interviews: The Foundation

Interviews are the PM's most powerful research tool. Done well, they reveal insights no other method can.

#### Preparing for Interviews

**Define your learning goals:**
- What decisions will this research inform?
- What do you need to learn to make those decisions?
- What assumptions are you testing?

**Bad learning goal:** "Understand what users think about our product"
**Good learning goal:** "Understand how users currently solve [specific problem] and what pain points they experience"

**Recruit the right participants:**
- People who actually have the problem you're exploring
- Mix of segments if you're comparing
- 5-8 participants typically reveal major patterns
- Avoid friends, family, and internal employees (bias)

**Create an interview guide:**
Not a rigid script—a flexible framework covering:
1. Warm-up and context
2. Core exploration questions
3. Follow-up prompts
4. Closing and next steps

#### The Interview Itself

**Start with context and behavior:**
- "Tell me about the last time you [relevant activity]"
- "Walk me through how you typically handle [situation]"
- "What does a typical day/week look like for you?"

**The "mom test" principle:**
People will lie to you to be nice. Ask about past behavior, not future intentions.

| Bad Question | Why It's Bad | Better Question |
|--------------|--------------|-----------------|
| "Would you use this feature?" | Future intention = unreliable | "How do you handle this today?" |
| "Is price important to you?" | Everyone says yes | "Tell me about your last purchase decision" |
| "Do you like the design?" | Social pressure for positivity | "What did you try to do? What happened?" |

**Listen more than you talk:**
- Aim for 80% participant, 20% interviewer
- Silence is powerful—let them fill it
- Resist the urge to explain or defend

**Follow the thread:**
When something interesting emerges:
- "Tell me more about that"
- "Why was that?"
- "What happened next?"
- "How did that make you feel?"

**Avoid leading questions:**
- Bad: "Don't you find it frustrating when..."
- Good: "How do you feel when..."

#### Synthesizing Interview Findings

**During/immediately after each interview:**
- Write key quotes verbatim
- Note emotional moments
- Capture surprising insights
- Flag areas for follow-up

**After all interviews:**
1. Review all notes looking for patterns
2. Group similar insights together (affinity mapping)
3. Identify frequency of themes
4. Distinguish strong signals from outliers
5. Document findings with supporting evidence

**Output format:**
```
Finding: [Clear statement of insight]
Evidence: [Number of participants, specific quotes]
Implication: [What this means for the product]
```

### Surveys: Quantitative Insight

Surveys complement interviews by providing scale—answering "how many" after interviews tell you "what" and "why."

#### When to Use Surveys

**Good for:**
- Measuring frequency of problems identified in interviews
- Prioritizing between known options
- Tracking satisfaction over time
- Reaching users you can't interview

**Bad for:**
- Discovering new problems (use interviews)
- Understanding complex behavior (too shallow)
- Anything requiring nuance (forced choices)

#### Survey Design Principles

**Keep it short:**
- Every question must earn its place
- Under 5 minutes completion time
- State estimated time upfront

**Question types:**

| Type | Good For | Watch Out For |
|------|----------|---------------|
| Multiple choice | Clear categories, easy analysis | Forcing false choices |
| Rating scale (1-5) | Comparison, tracking | Meaningless midpoints |
| Open text | Depth, discovering new themes | Analysis is hard to scale |
| Ranking | Prioritization | Cognitive load |

**Avoid common mistakes:**
- Double-barreled questions ("How satisfied are you with speed and reliability?")
- Leading questions ("How much do you love our new feature?")
- Jargon users don't understand
- Required questions they can't answer

**Include an "Other" option** for categories—you might be missing something.

### Continuous Discovery

Rather than big research projects, continuous discovery integrates learning into weekly product work.

#### The Weekly Touch Point

**Goal:** Talk to users every single week. Yes, every week.

**How it works:**
- Schedule regular slots (e.g., two 30-minute calls per week)
- Recruit from existing users, support tickets, signup flow
- Have an evolving set of questions based on current priorities
- Share learnings with the team immediately

**Even 30 minutes per week** compounds into deep user understanding over months.

#### Opportunity Solution Trees

A framework for connecting research to product decisions:

```
                    [Desired Outcome]
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
     [Opportunity]   [Opportunity]   [Opportunity]
           │               │               │
      ┌────┼────┐     ┌────┼────┐     ┌────┼────┐
      ▼    ▼    ▼     ▼    ▼    ▼     ▼    ▼    ▼
    [S1] [S2] [S3]  [S1] [S2] [S3]  [S1] [S2] [S3]
```

- **Outcome:** Business or product goal you're driving toward
- **Opportunities:** User problems, needs, or desires discovered through research
- **Solutions:** Potential ways to address each opportunity

**This structure ensures:**
- Research connects to business goals
- Multiple solutions are considered for each opportunity
- You're solving real problems, not shipping pet features

#### Assumption Mapping

Before building, map your assumptions:

| Assumption | Risk Level | How to Test |
|------------|------------|-------------|
| Users have this problem | High | Interview 5 users |
| Users would pay for solution | High | Pricing test, competitive analysis |
| Users can find this feature | Medium | Usability test prototype |
| Technical approach is feasible | Medium | Engineering spike |

Test the highest-risk assumptions first with the smallest possible investment.

### Research Operations at Scale

As teams grow, research needs structure:

**Research repository:**
- Centralized place for all findings
- Searchable by topic, user segment, date
- Prevents repeating research others already did
- Tools: Dovetail, Notion, Confluence

**Participant panels:**
- Pre-recruited users willing to participate
- Segmented by characteristics
- Incentive tracking
- Consent management

**Research templates:**
- Standard interview guides by type
- Survey templates
- Synthesis frameworks
- Prevents reinventing the wheel

### Common Research Mistakes

**Confirmation bias:**
Seeking evidence that supports what you already believe. Counter this by actively seeking disconfirming evidence.

**Sampling bias:**
Only talking to your most vocal or happiest users. Deliberately include different segments, including churned users.

**The curse of knowledge:**
Forgetting how confusing your product is to new users. Watch true beginners, not power users.

**Feature fixation:**
Asking "what features do you want?" instead of understanding problems. Users describe solutions in terms of what they know.

**Analysis paralysis:**
Researching forever without acting. Set decision deadlines and research scope upfront.

---

## Key Takeaways

1. **Generative research discovers problems; evaluative research validates solutions—do both, in that order**
2. **User interviews reveal the "why" behind behavior—ask about past behavior, not future intentions**
3. **Surveys provide scale but require prior qualitative understanding of what to ask**
4. **Continuous discovery (weekly user contact) beats periodic big research projects**
5. **Test your riskiest assumptions first with the smallest possible investment**
6. **Document and share findings—research that isn't acted on is worthless**

---

## Practice

### Reflection Questions
1. Think of a recent product decision made without user research. What assumptions were being made?
2. Have you ever been surprised by how users actually use a product? What was unexpected?
3. What would weekly user conversations look like in your context?

### Exercise
**Interview Practice:**

1. Identify a product problem you're curious about
2. Write 5 open-ended questions following the principles above
3. Interview one person (friend or colleague as a proxy)
4. Practice:
   - Listening more than talking
   - Following up on interesting threads
   - Avoiding leading questions
5. Write a one-paragraph synthesis of what you learned

**Self-critique:** After the interview, reflect:
- Did I talk too much?
- Did I ask about past behavior or future intention?
- What question generated the most insight?
- What would I do differently next time?

---

## Further Reading

- **"The Mom Test" by Rob Fitzpatrick** - Essential reading on customer interviews
- **"Continuous Discovery Habits" by Teresa Torres** - The continuous discovery framework
- **"Just Enough Research" by Erika Hall** - Practical research for product teams
- **"Interviewing Users" by Steve Portigal** - Comprehensive interview techniques
- **User Interviews blog** - Ongoing tactical research advice
