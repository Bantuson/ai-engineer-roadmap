# PM Prompt Library

A collection of ready-to-use prompts for common PM tasks. Copy, customize, and use immediately.

## How to Use This Library

1. **Find** the prompt for your task
2. **Copy** the template
3. **Customize** the bracketed sections [like this]
4. **Run** the prompt
5. **Iterate** as needed

**Pro tip:** Save prompts you use frequently to your own library with your customizations.

---

## User Research

### Synthesize Interview Notes

```
I have notes from [NUMBER] user interviews about [TOPIC].

For each batch of notes I provide:
1. Extract verbatim quotes that reveal key insights
2. Tag each quote with a theme
3. Note emotional intensity (high/medium/low)
4. Flag anything surprising or contradictory

After all batches, synthesize:
- Top 5 themes by frequency
- Top 3 themes by emotional intensity
- Key user segments that emerged
- Contradictions or tensions
- Gaps in our understanding

Format the final synthesis as an executive summary (3 paragraphs) followed by detailed findings.

Here are the notes:
[PASTE INTERVIEW NOTES]
```

### Create Interview Questions

```
I'm preparing user interviews for [RESEARCH GOAL].

Context:
- Product: [YOUR PRODUCT]
- Target user: [USER TYPE]
- Current hypothesis: [WHAT YOU THINK IS TRUE]
- What we need to learn: [SPECIFIC QUESTIONS]

Create an interview guide with:
1. Warm-up questions (2-3)
2. Core exploration questions (5-7)
3. Follow-up prompts for each core question
4. Closing questions (2)

Follow the "Mom Test" principles:
- Ask about past behavior, not future intentions
- Don't lead the witness
- Focus on their experience, not your idea

Format as a discussion guide I can use during interviews.
```

### Analyze Survey Responses

```
I have [NUMBER] open-ended survey responses to the question:
"[SURVEY QUESTION]"

Analyze these responses:
1. Categorize into themes
2. Count frequency of each theme
3. Pull 2-3 representative quotes per theme
4. Identify sentiment (positive/negative/neutral) distribution
5. Note any unexpected responses

Format as:
## Summary
[2-3 sentences]

## Theme Analysis
| Theme | Count | % | Sentiment | Representative Quote |
|-------|-------|---|-----------|---------------------|

## Notable Outliers
[Any responses that don't fit patterns]

## Recommendations
[What should we do with this information]

Responses:
[PASTE RESPONSES]
```

---

## PRD & Documentation

### Draft PRD Section

```
I need to write the [SECTION NAME] section of a PRD.

Context:
- Feature: [FEATURE DESCRIPTION]
- Problem: [PROBLEM BEING SOLVED]
- Target user: [WHO WILL USE IT]
- Constraints: [KNOWN CONSTRAINTS]

For this section, include:
[WHAT SHOULD BE IN THIS SECTION]

Use this format:
[PASTE YOUR PRD TEMPLATE FORMAT]

Write a first draft that I can refine.
```

### Write User Stories

```
Write user stories for [FEATURE NAME].

Context:
- Product: [YOUR PRODUCT]
- Feature description: [WHAT IT DOES]
- Target users: [WHO WILL USE IT]
- Key scenarios: [MAIN USE CASES]

For each user story:
1. Follow format: As a [user], I want to [action] so that [benefit]
2. Add 3-5 acceptance criteria
3. Note any edge cases
4. Tag as P0/P1/P2

Generate [NUMBER] user stories covering the main scenarios.

Focus on:
- [PRIORITY 1]
- [PRIORITY 2]
- [PRIORITY 3]
```

### Review PRD for Gaps

```
Review this PRD as a [ROLE: e.g., senior engineer / skeptical PM / QA lead].

Focus on:
1. Ambiguities: What's unclear or could be interpreted multiple ways?
2. Missing requirements: What obvious cases aren't covered?
3. Edge cases: What happens when things go wrong?
4. Technical concerns: What might be harder than it seems?
5. Missing success metrics: How will we know this worked?

For each issue found:
- Quote the problematic section
- Explain the concern
- Suggest a fix or clarifying question

PRD:
[PASTE PRD]
```

### Generate Acceptance Criteria

```
For this requirement, generate comprehensive acceptance criteria:

Requirement: [PASTE REQUIREMENT]

Context:
- Product: [YOUR PRODUCT]
- User: [TARGET USER]
- Technical constraints: [ANY KNOWN CONSTRAINTS]

Include:
1. Happy path criteria (the main scenario works)
2. Edge cases (boundary conditions, empty states, max limits)
3. Error handling (what happens when things fail)
4. Performance requirements (if relevant)
5. Accessibility requirements (if relevant)

Format using Given-When-Then where it helps clarity:
Given [context]
When [action]
Then [expected result]
```

---

## Competitive Analysis

### Competitor Overview

```
Create a competitive analysis overview for [COMPETITOR NAME].

What I know:
[ANY INFORMATION YOU HAVE]

Research and summarize (using only public information):
1. Company overview (size, funding, market position)
2. Product capabilities (core features, differentiators)
3. Target market (who they serve, pricing)
4. Recent developments (last 6-12 months)
5. Strengths (what they do well)
6. Weaknesses (where they fall short)

Then assess:
- Threat level to us (low/medium/high)
- What we can learn from them
- Where we can differentiate

Format as a one-pager I can share with stakeholders.
```

### Feature Comparison Matrix

```
Create a feature comparison matrix.

Our product: [YOUR PRODUCT]
Competitors to compare: [LIST COMPETITORS]

Features to compare:
[LIST KEY FEATURES/CAPABILITIES]

For each intersection:
- ✅ Fully supports
- 🟡 Partially supports
- ❌ Doesn't support
- ❓ Unknown

Create the matrix, then summarize:
- Where we're ahead
- Where we're behind
- Biggest gaps to address
```

---

## Strategy & Planning

### SWOT Analysis

```
Conduct a SWOT analysis for [PRODUCT/COMPANY].

Context:
- Market: [MARKET DESCRIPTION]
- Position: [CURRENT POSITION]
- Key competitors: [COMPETITORS]
- Recent developments: [RELEVANT NEWS/CHANGES]

For each quadrant, provide 4-6 specific items (not generic):

Strengths (internal, positive):
- [Be specific to our situation]

Weaknesses (internal, negative):
- [Be specific to our situation]

Opportunities (external, positive):
- [Market trends, competitor weaknesses, etc.]

Threats (external, negative):
- [Competitive moves, market shifts, etc.]

Then provide:
- Top 3 strategic implications
- Recommended actions for each quadrant
```

### Prioritization Analysis

```
Help me prioritize these items using [FRAMEWORK: RICE/ICE/MoSCoW].

Items to prioritize:
[LIST ITEMS]

For RICE, assess:
- Reach: How many users affected per quarter
- Impact: How much will it improve metrics (0.25x to 3x)
- Confidence: How sure are we (0-100%)
- Effort: Person-weeks to complete

[OR for ICE:]
- Impact: Effect on goals (1-10)
- Confidence: How sure we are (1-10)
- Ease: How easy to implement (1-10)

[OR for MoSCoW:]
- Must have
- Should have
- Could have
- Won't have (this time)

Context that might affect prioritization:
[RELEVANT CONTEXT]

Provide the analysis, then a recommended priority order with rationale.
```

### Roadmap Narrative

```
Write a roadmap narrative for [AUDIENCE: executives/team/customers].

Roadmap items:
[LIST WHAT'S PLANNED]

Timeline: [QUARTERS/MONTHS]

For this audience, they care about:
[WHAT MATTERS TO THEM]

Create a narrative that:
1. Opens with the strategic context (why this roadmap)
2. Groups items by theme or goal
3. Explains the sequencing rationale
4. Addresses likely questions
5. Ends with success criteria

Tone: [FORMAL/CONVERSATIONAL/INSPIRING]
Length: [WORD COUNT/PAGE COUNT]
```

---

## Communication

### Stakeholder Update

```
Write a stakeholder update for [AUDIENCE].

What's happened:
[KEY DEVELOPMENTS]

Metrics:
[RELEVANT DATA]

Challenges:
[ISSUES OR BLOCKERS]

What's next:
[UPCOMING WORK]

Format for:
- [ ] Email (conversational, 2-3 paragraphs)
- [ ] Slide deck (bullet points, 3-5 slides)
- [ ] Slack message (brief, highlights only)

Tone should be: [TONE]
Key message to land: [MAIN TAKEAWAY]
```

### Launch Announcement

```
Write a launch announcement for [FEATURE/PRODUCT].

Details:
- What it does: [DESCRIPTION]
- Key benefits: [BENEFITS]
- Availability: [WHO CAN USE IT, WHEN]
- How to access: [STEPS]

Audience: [WHO WILL READ THIS]
Channel: [EMAIL/BLOG/IN-APP/SOCIAL]
Tone: [EXCITED/PROFESSIONAL/UNDERSTATED]

Constraints:
- Length: [WORD COUNT]
- Must include: [REQUIRED ELEMENTS]
- Must avoid: [WHAT NOT TO SAY]

Include:
- Compelling opening
- Clear explanation of value
- Social proof if available
- Call to action
```

### Feedback Response

```
I need to respond to this user/customer feedback:

"[FEEDBACK TEXT]"

Context:
- This is about: [WHAT THEY'RE REFERENCING]
- Current status: [WHERE WE ARE ON THIS]
- What we can say: [WHAT'S APPROPRIATE TO SHARE]

Write a response that:
1. Acknowledges their feedback
2. Thanks them appropriately
3. Addresses their point honestly
4. Sets appropriate expectations
5. Maintains positive relationship

Tone: [EMPATHETIC/PROFESSIONAL/APOLOGETIC/GRATEFUL]
Length: [SHORT/MEDIUM]
```

---

## Analysis

### Data Interpretation

```
Help me interpret this data:

[PASTE DATA/CHARTS/METRICS]

Context:
- This measures: [WHAT THE DATA REPRESENTS]
- Time period: [WHEN]
- Expected outcome was: [WHAT WE HOPED FOR]

Analyze:
1. What does the data show?
2. Is this good, bad, or neutral?
3. What might be causing this?
4. What questions does this raise?
5. What actions might we consider?

Be careful to:
- Note limitations in the data
- Avoid over-claiming causation
- Consider alternative explanations
```

### Root Cause Analysis

```
Help me analyze this problem:

Problem: [DESCRIBE THE ISSUE]

Symptoms:
[WHAT WE'RE OBSERVING]

Context:
[RELEVANT BACKGROUND]

Use the 5 Whys approach:
1. Why is [problem] happening?
2. Why is [answer 1] true?
3. (Continue until root cause)

Then consider:
- Are there multiple root causes?
- What's within our control?
- What's the simplest intervention?

Finally, recommend:
- Immediate actions
- Longer-term fixes
- How to prevent recurrence
```

---

## Quick Prompts

### Brainstorm Ideas

```
Brainstorm [NUMBER] ideas for [WHAT YOU NEED].

Context: [BRIEF CONTEXT]
Constraints: [ANY LIMITATIONS]

For each idea, provide:
- One-line description
- Why it might work
- Biggest risk

Range from obvious to creative.
```

### Simplify Explanation

```
Simplify this for [AUDIENCE]:

"[COMPLEX TEXT]"

Use:
- No jargon
- Everyday language
- Analogies if helpful
- [WORD COUNT] words max
```

### Create Agenda

```
Create a meeting agenda for: [MEETING PURPOSE]

Attendees: [WHO]
Duration: [TIME]
Goal: [WHAT WE NEED TO ACCOMPLISH]

Include:
- Time allocations
- Discussion topics
- Decision points
- Action item capture
```

### Write Email

```
Write an email to [RECIPIENT/ROLE].

Purpose: [WHAT YOU NEED]
Relationship: [YOUR RELATIONSHIP]
Tone: [FORMAL/CASUAL/URGENT]
Key points:
- [POINT 1]
- [POINT 2]

Keep it [SHORT/MEDIUM] length.
Include clear call to action.
```

---

## Tips for Better Results

1. **Add more context** — The more specific you are, the better the output
2. **Show examples** — If you have examples of good output, include them
3. **Iterate** — First output is a draft; refine through follow-ups
4. **Verify claims** — Especially for competitive intel or data interpretation
5. **Save what works** — Build your personal prompt library

---

## Customize This Library

Adapt these prompts to your context:
- Add your company name and product details
- Include your PRD template
- Reference your tone/style guidelines
- Add domain-specific terminology

Make these prompts yours.
