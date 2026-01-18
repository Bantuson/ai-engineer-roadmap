# Capstone Project 02: AI Feature Design

Design an AI feature that demonstrates deep understanding of AI product challenges.

## Project Overview

**Scenario:**
You're a PM at "DocuTeam," a document collaboration platform (think Google Docs meets Notion). Leadership wants to add AI capabilities to stay competitive. You're tasked with designing the first major AI feature.

**Your mission:**
Design an AI feature that adds genuine value while addressing AI's unique challenges: non-determinism, evaluation, safety, and user trust.

## Time Estimate

10-15 hours total

## Background

### The Product

**DocuTeam** is a document collaboration platform:
- Real-time collaborative editing
- Templates and structured documents
- Comments and suggestions
- Version history
- Team workspaces
- 500K monthly active users
- B2B SaaS model (teams of 5-500)

### Current Capabilities

**Document features:**
- Rich text editing
- Tables, images, embeds
- Templates library
- Export to PDF, Word

**Collaboration features:**
- Real-time cursors
- Comments and threads
- Suggestion mode
- @mentions

**Organization features:**
- Folders and workspaces
- Search (basic keyword)
- Permissions
- Integrations (Slack, Jira)

### Market Pressure

Competitors are adding AI:
- Notion AI (writing, summarization)
- Google Docs AI (Smart Compose, summarization)
- Coda AI (generation, Q&A)

Leadership message: "We need AI, but we need to do it right. No rushing to ship something half-baked that damages trust."

### User Research (AI-related)

From 20 interviews with DocuTeam users:

**Interest areas:**
- "I spend so much time formatting—wish it was automatic"
- "Finding things in old documents is painful"
- "Writing the first draft is the hardest part"
- "I'd love to know what changed without reading everything"

**Concerns:**
- "I don't want AI making my documents worse"
- "Privacy is crucial—our documents are confidential"
- "I need to trust what it produces"
- "What if it gets things wrong?"

**Expectations:**
- Helpful, not intrusive
- Easy to undo/control
- Transparent about limitations
- Respects document confidentiality

### Constraints

**Technical:**
- Can use LLM APIs (not training custom models)
- Must work with existing document format
- Real-time performance requirements
- Data stays within user's region

**Business:**
- $50K/month initial AI API budget
- Must be defensible (not just wrapping ChatGPT)
- Needs to support existing pricing tiers
- Should drive upgrade conversions

**Team:**
- 2 ML engineers available
- 4 backend engineers (2 dedicated)
- 2 frontend engineers
- 3-month timeline to initial launch

## Deliverables

### 1. AI Opportunity Assessment

Evaluate potential AI features and select one to design in detail.

Include:
- 3-5 potential AI features considered
- Evaluation criteria (user value, feasibility, differentiation, risk)
- Selection rationale
- Why AI is the right approach (vs. traditional software)

### 2. Feature Specification

Detailed design of your chosen feature.

Include:
- Feature description
- User stories (5-7)
- User flow/interaction design
- Human-AI interaction pattern (why this pattern?)
- How uncertainty is handled in the UX
- Fallback behaviors

### 3. Data Strategy

How data enables this feature.

Include:
- What data is needed
- Where it comes from
- Privacy and security approach
- How the system improves over time
- Potential biases and mitigations

### 4. Evaluation Plan

How you'll measure quality.

Include:
- Quality dimensions to measure
- Evaluation methods (automated, LLM-as-judge, human)
- Eval dataset approach
- Quality bar for launch
- Ongoing monitoring plan

### 5. Responsible AI Assessment

Ethical and safety considerations.

Include:
- Potential harms
- Fairness considerations
- Transparency requirements
- Safety measures
- Accountability structure

### 6. Launch Plan

How you'll ship this responsibly.

Include:
- Phased rollout plan
- Success criteria per phase
- Key risks and mitigations
- Resource requirements
- Timeline

## Evaluation Rubric

### Opportunity Assessment (15%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Thoughtful evaluation of options, strong rationale for selection |
| ⭐⭐ | Reasonable selection with some justification |
| ⭐ | Arbitrary selection or AI not appropriate for chosen feature |

### Feature Specification (25%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Clear feature with excellent AI UX—handles uncertainty, gives control |
| ⭐⭐ | Feature makes sense, some AI UX gaps |
| ⭐ | Feature treats AI like deterministic software |

### Data Strategy (15%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Thorough data plan with privacy, improvement loop, bias consideration |
| ⭐⭐ | Data strategy exists with some gaps |
| ⭐ | Data strategy missing or naive |

### Evaluation Plan (20%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Comprehensive eval with clear methods, quality bar, monitoring |
| ⭐⭐ | Evaluation plan covers basics |
| ⭐ | Evaluation missing or insufficient |

### Responsible AI (15%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Thoughtful consideration of risks with real mitigations |
| ⭐⭐ | Addresses obvious concerns |
| ⭐ | Responsible AI treated as afterthought |

### Launch Plan (10%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Realistic phased plan with clear criteria |
| ⭐⭐ | Plan exists |
| ⭐ | Plan is unrealistic or missing |

**Target: 80%+ indicates portfolio-ready quality**

## Feature Ideas (Starting Points)

You can choose one of these or propose your own:

1. **Smart Summary** — AI-generated summaries of long documents
2. **Document Q&A** — Ask questions about document content
3. **Writing Assistant** — Help with drafting, editing, tone
4. **Change Explainer** — Summarize what changed between versions
5. **Smart Search** — Semantic search across workspace documents
6. **Auto-formatting** — Intelligent formatting and structure suggestions

## Getting Started

1. Review all background materials
2. Brainstorm and evaluate AI feature options
3. Select one feature to design in depth
4. Work through each deliverable
5. Review against the rubric
6. Iterate until portfolio-ready

## Submission

Create your deliverables in this directory. Suggested structure:

```
02-ai-feature-design/
├── README.md (this file)
├── opportunity-assessment.md
├── feature-specification.md
├── data-strategy.md
├── evaluation-plan.md
├── responsible-ai.md
└── launch-plan.md
```

## Bonus Challenges

1. **Create a prototype prompt** — Write the system prompt for your feature
2. **Design an eval dataset** — Create 20 test cases with expected outputs
3. **Sketch the UI** — Wireframe key interactions
4. **Cost analysis** — Estimate AI costs at different usage levels
