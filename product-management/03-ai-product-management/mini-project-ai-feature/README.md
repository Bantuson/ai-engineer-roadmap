# Mini-Project: AI Feature Design

## Project Overview

Apply everything you've learned in the AI Product Management module by designing an AI feature for an existing product—from problem definition through launch planning.

This project demonstrates your ability to:
- Identify appropriate AI applications
- Navigate AI's unique challenges (non-determinism, evaluation, safety)
- Design human-AI interaction patterns
- Plan for the AI product lifecycle

## Time Estimate

4-6 hours total

## The Scenario

You're a PM at a company with an established B2B SaaS product used by professional services firms (consulting, legal, accounting) to manage client projects.

**Current product capabilities:**
- Project creation and tracking
- Task management with assignments
- Time tracking
- Document storage
- Client communication portal
- Basic reporting

**Company context:**
- 5,000 business customers
- $50M ARR, growing 30% YoY
- 40-person engineering team
- No current AI features
- Competitors starting to add AI capabilities

**Executive mandate:**
"We need to add AI to stay competitive. What should our first AI feature be?"

## Your Task

Design a complete AI feature, including:
1. Identifying the right opportunity
2. Addressing AI-specific challenges
3. Planning the full lifecycle

## Deliverable

A comprehensive AI feature design document (Markdown) including all sections below.

### Required Sections

#### Part 1: Opportunity Identification (1-2 pages)

**1.1 Problem Selection**
- What problem will AI solve?
- Who has this problem?
- Why is AI the right approach (vs. traditional software)?

**1.2 Opportunity Assessment**
- User pain point (with evidence or reasoning)
- Business value
- Technical feasibility
- Competitive context

**1.3 AI Fit Analysis**
Using the framework from the course:
- Why AI is appropriate for this problem
- What makes this NOT a rules-based solution

#### Part 2: Feature Design (2-3 pages)

**2.1 Feature Description**
- What does the feature do?
- How does the user interact with it?
- What's the human-AI interaction pattern?

**2.2 User Stories**
- 3-5 user stories with acceptance criteria
- Cover primary use cases and edge cases

**2.3 Success Metrics**
- Model metrics (accuracy, latency, etc.)
- Product metrics (adoption, satisfaction)
- Business metrics (efficiency, revenue impact)

**2.4 UX Considerations**
- How will you handle AI uncertainty?
- What feedback mechanisms exist?
- What's the fallback when AI fails?

#### Part 3: AI-Specific Planning (2-3 pages)

**3.1 Data Strategy**
- What data is needed?
- Where will it come from?
- How will you handle labeling?
- What biases might exist?

**3.2 Evaluation Plan**
- How will you measure quality?
- What's your eval suite structure?
- What's the quality bar for launch?

**3.3 Responsible AI Assessment**
- Fairness considerations
- Safety requirements
- Transparency needs
- Privacy implications

**3.4 Lifecycle Planning**
- Training approach
- Deployment strategy
- Monitoring plan
- Improvement cycle

#### Part 4: Launch Plan (1 page)

**4.1 Rollout Strategy**
- Phased approach
- Success criteria per phase

**4.2 Resource Needs**
- Engineering, data, ML resources
- Timeline estimate (rough)

**4.3 Risks and Mitigations**
- Top 3-5 risks
- Mitigation strategies

**Total: 6-9 pages**

## Getting Started

1. **Brainstorm opportunities** — List 3-5 potential AI features for this product
2. **Select the best one** — Use the AI fit analysis to choose
3. **Design thoroughly** — Work through each section
4. **Review for completeness** — Check against the rubric

## Evaluation Rubric

### Opportunity Identification (25%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Clear problem, strong AI fit justification, good business case |
| ⭐⭐ | Reasonable problem, some AI fit gaps |
| ⭐ | Weak problem definition or AI not appropriate |

### Feature Design (25%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Clear feature, good UX, addresses AI uncertainty |
| ⭐⭐ | Feature makes sense but gaps in AI-specific UX |
| ⭐ | Feature unclear or ignores AI challenges |

### AI-Specific Planning (30%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Thorough data/eval/responsible AI/lifecycle planning |
| ⭐⭐ | Most areas covered with some gaps |
| ⭐ | Missing major AI considerations |

### Launch Plan & Practicality (20%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Realistic plan, clear risks, phased approach |
| ⭐⭐ | Plan exists but some unrealistic elements |
| ⭐ | Plan missing or impractical |

**Target: 80%+ demonstrates AI PM readiness**

## Example Feature Ideas

To spark your thinking (but feel free to choose something else):

1. **Smart time entry suggestions** — AI predicts time entries based on calendar, past patterns
2. **Document intelligence** — Auto-tagging, summarization, key term extraction
3. **Project health prediction** — Risk indicators based on project signals
4. **Meeting notes to tasks** — Convert meeting transcripts into actionable tasks
5. **Client communication drafting** — Draft status updates, proposals

## Tips for Success

1. **Pick a focused problem** — Better to do one thing well than many things poorly
2. **Justify the AI fit** — Be honest about whether AI is needed
3. **Address uncertainty explicitly** — Don't pretend AI will be perfect
4. **Plan for the lifecycle** — AI features need ongoing investment
5. **Consider responsible AI early** — Not as an afterthought
6. **Be realistic about resources** — A 4-person team can't build GPT-5

## Submission

Save your completed design as `project.md` in this directory.

Use the rubric to self-evaluate and identify areas for improvement.

## Bonus Challenges

If you want to go further:

1. **Create a prototype prompt** — If using an LLM, draft the system prompt
2. **Design an eval dataset** — Create 10 example inputs with expected outputs
3. **Sketch the UI** — Wireframe the key interactions
4. **Write a launch announcement** — 300 words for customers

## Next Steps

After completing this mini-project:
- Add to your portfolio as an AI PM case study
- Use the framework for evaluating AI opportunities at work
- Continue to [04-Prompt Engineering for PMs](../../04-prompt-engineering-pm/)
- Complete capstone projects in Module 06
