# Capstone Project 03: Technical PRD Portfolio

Create three PRDs of varying complexity to demonstrate your technical documentation skills.

## Project Overview

**Goal:**
Build a portfolio of PRDs that showcases your ability to write clear, complete, technical specifications that engineers love to work from.

**Why three PRDs?**
Different features require different levels of detail and technical consideration. This portfolio demonstrates range.

## Time Estimate

8-12 hours total (3-4 hours per PRD)

## The Three PRDs

### PRD 1: Simple Feature

**Feature:** Dark Mode

**Product context:** You're a PM for a web-based project management tool. Users have been requesting dark mode for accessibility and preference reasons.

**Scope:**
- Toggle between light and dark themes
- Persist preference
- System preference detection

**Why this feature:**
- Relatively straightforward
- Demonstrates clean requirements writing
- Shows attention to edge cases and accessibility

### PRD 2: Complex Feature

**Feature:** Real-Time Collaboration

**Product context:** Same project management tool. You're adding real-time collaboration so multiple users can edit the same project simultaneously.

**Scope:**
- Multiple users editing same project
- Real-time cursor visibility
- Conflict resolution
- Presence indicators (who's online)

**Why this feature:**
- Multiple technical considerations
- Requires thinking about failure modes
- Involves UX complexity
- Shows ability to handle ambiguity

### PRD 3: Technical/Infrastructure

**Feature:** API Rate Limiting

**Product context:** Your tool has a public API. You need to implement rate limiting to prevent abuse and ensure fair usage.

**Scope:**
- Rate limit enforcement
- Limit tiers by plan type
- Developer communication (headers, errors)
- Monitoring and alerting

**Why this feature:**
- No direct UI (technical infrastructure)
- Shows ability to communicate technical concepts
- Demonstrates understanding of developer experience
- Requires thinking about system behavior

## Deliverable Requirements

For each PRD, include:

### Required Sections

1. **Overview**
   - Problem statement
   - Proposed solution
   - Success metrics

2. **Goals & Non-Goals**
   - Explicit scope
   - What's not included

3. **User Stories** (or API contracts for PRD 3)
   - Who does what, why
   - Acceptance criteria

4. **Detailed Requirements**
   - Functional requirements with acceptance criteria
   - Non-functional requirements (performance, security, etc.)
   - Edge cases
   - P0/P1/P2 prioritization

5. **Technical Considerations**
   - Dependencies
   - Known constraints
   - Questions for engineering

6. **Open Questions**
   - What's still uncertain
   - Who needs to answer

### Tailored Elements

**PRD 1 (Dark Mode):**
- Accessibility requirements (WCAG)
- Color system specifications
- Migration for existing users

**PRD 2 (Real-Time Collaboration):**
- Conflict resolution strategy
- Latency requirements
- Offline behavior
- Security/permissions considerations

**PRD 3 (API Rate Limiting):**
- Rate limit specifications by tier
- API response format (headers, error bodies)
- Developer documentation requirements
- Monitoring specifications

## Evaluation Rubric

Each PRD is evaluated on the same criteria:

### Clarity (25%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Requirements are unambiguous; engineers could start building |
| ⭐⭐ | Generally clear with some ambiguous areas |
| ⭐ | Significant ambiguity or confusion |

### Completeness (25%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | All necessary sections; edge cases covered; nothing obvious missing |
| ⭐⭐ | Core requirements present, some gaps |
| ⭐ | Missing important sections or requirements |

### Technical Appropriateness (25%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Technical considerations are thoughtful and realistic |
| ⭐⭐ | Some technical awareness |
| ⭐ | Ignores technical realities or makes unrealistic assumptions |

### Testability (25%)

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | All requirements have clear acceptance criteria; QA could write tests |
| ⭐⭐ | Most requirements are testable |
| ⭐ | Vague requirements without clear pass/fail criteria |

### Overall Portfolio

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | All three PRDs are high quality with demonstrated range |
| ⭐⭐ | Two strong PRDs, one weaker |
| ⭐ | Inconsistent quality or missing understanding |

**Target: 80%+ on each PRD indicates portfolio-ready quality**

## PRD-Specific Guidance

### PRD 1: Dark Mode

**Things to consider:**
- How does the toggle work?
- What about images and user-generated content?
- How does it work with system preference?
- What about email notifications (if applicable)?
- Accessibility contrast requirements
- Transition animation?

### PRD 2: Real-Time Collaboration

**Things to consider:**
- What happens with conflicting edits?
- How do you handle latency and delays?
- What shows when someone is editing?
- What if connection drops?
- Permissions—who can edit?
- Performance with many collaborators
- Undo behavior with multiple editors

### PRD 3: API Rate Limiting

**Things to consider:**
- What are the limits (requests per minute/hour/day)?
- How do limits differ by plan?
- What response do developers get when limited?
- What headers communicate remaining quota?
- How are bursts handled?
- How is this monitored internally?
- How do you handle edge cases (API keys shared across apps)?

## Getting Started

1. **Start with PRD 1** (simplest) to establish your style
2. **Use the PRD template** or develop consistent structure
3. **Write as if engineering will actually build from this**
4. **Review against rubric** before moving to next PRD
5. **Iterate** — first draft is never final

## Submission

Create your deliverables in this directory:

```
03-technical-prd-portfolio/
├── README.md (this file)
├── prd-01-dark-mode.md
├── prd-02-real-time-collaboration.md
└── prd-03-api-rate-limiting.md
```

## Using These PRDs

### In Interviews

- Walk through one PRD explaining your thinking
- Be ready to discuss trade-offs you made
- Explain how you'd handle engineering pushback
- Discuss what you'd do differently with more time

### In Your Job

- Use these as templates for real PRDs
- Adapt the structure to your organization
- Reference when training others

## Bonus Challenges

1. **Get engineer feedback** — Have an engineer review one PRD and incorporate feedback
2. **Add wireframes** — Sketch the UI for PRD 1 or 2
3. **Write API docs** — Document the rate limit API as developers would see it
4. **Create test cases** — Write 10 test cases for one PRD
