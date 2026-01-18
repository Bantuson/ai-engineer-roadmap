# Writing PRDs

## Learning Objectives

- [ ] Understand the purpose and audience of PRDs
- [ ] Structure PRDs with clear sections that engineers need
- [ ] Write effective user stories and acceptance criteria
- [ ] Apply prioritization frameworks (P0/P1/P2) to requirements
- [ ] Create PRDs that engineers love to work from

## Prerequisites

- Completed: [01 - Tech Foundations](./01-tech-foundations.md)
- Completed: [02 - Working with Engineers](./02-working-with-engineers.md)

---

## Core Content

### What is a PRD?

A Product Requirements Document (PRD) is **a written specification of what a product or feature should do and why.**

**What it is:**
- A communication tool between PM, engineering, and design
- A reference document during development
- A record of decisions made
- A basis for testing and QA

**What it is NOT:**
- A legal contract
- An unchangeable decree
- A substitute for conversation
- A complete technical specification

### The PRD Audience

Different readers need different things:

| Audience | What They Need |
|----------|---------------|
| **Engineers** | Clear requirements, acceptance criteria, edge cases |
| **Designers** | User context, goals, constraints |
| **QA** | Testable criteria, expected behaviors |
| **Stakeholders** | Business context, success metrics |
| **Future You** | Why decisions were made |

The best PRDs serve all these audiences.

### PRD Structure

A solid PRD typically includes these sections:

```
1. Overview
   - Problem statement
   - Proposed solution
   - Success metrics

2. Background & Context
   - User research/evidence
   - Business case
   - Competitive context

3. Goals & Non-Goals
   - What we're trying to achieve
   - What's explicitly out of scope

4. User Stories
   - Who is doing what and why

5. Requirements
   - Detailed specifications
   - Acceptance criteria
   - Edge cases

6. Design
   - Mockups/wireframes (or links)
   - Interaction details

7. Technical Considerations
   - Known constraints
   - Dependencies
   - Questions for engineering

8. Launch Plan
   - Rollout strategy
   - Success criteria
   - Monitoring needs

9. Open Questions
   - Unresolved decisions
   - Items needing input
```

Let's dig into each section.

### Section 1: Overview

Start with the essentials. A reader should understand the basic what and why in 30 seconds.

**Problem Statement:**
What problem are we solving? For whom? Why now?

```
Bad: "Users want a dashboard"

Good: "Enterprise customers (50+ seats) cannot see usage
across their organization, leading to 30% of them
requesting manual reports from support monthly."
```

**Proposed Solution:**
One-paragraph summary of what we're building.

**Success Metrics:**
How will we know this worked?
- Primary metric: The main thing that should change
- Secondary metrics: Supporting indicators
- Guardrail metrics: Things that shouldn't get worse

### Section 2: Background & Context

Establish why this matters and what we know.

**User Research:**
- What evidence supports this problem?
- Quotes, data, observations
- Link to research documents

**Business Case:**
- How does this support company goals?
- Revenue impact, retention impact, strategic value

**Competitive Context:**
- How do competitors handle this?
- What can we learn?

### Section 3: Goals & Non-Goals

Explicit scope prevents scope creep.

**Goals:**
```
✓ Allow org admins to view usage metrics for all users
✓ Enable export of usage data for compliance needs
✓ Reduce manual report requests by 80%
```

**Non-Goals (equally important):**
```
✗ Real-time usage tracking (batch daily is acceptable)
✗ Individual user notifications about usage
✗ Integration with external BI tools (future consideration)
```

Being explicit about non-goals prevents "while we're at it" expansion.

### Section 4: User Stories

User stories describe functionality from the user's perspective.

**Format:**
```
As a [type of user]
I want to [action]
So that [benefit/goal]
```

**Examples:**

```
As an org admin
I want to see total active users per week
So that I can report on adoption to leadership

As an org admin
I want to export usage data as CSV
So that I can include it in quarterly compliance reports

As an org admin
I want to identify users who haven't logged in recently
So that I can follow up with them about training
```

**Good user stories:**
- Specify the user type
- Focus on the goal, not the implementation
- Are testable (you can verify if it's met)
- Are independent (can be built separately)

### Section 5: Requirements

This is the meat of the PRD. Engineers will reference this section constantly.

#### Functional Requirements

What the system should DO.

**Structure each requirement:**

```
REQ-001: Dashboard Overview

Description:
The dashboard displays a summary of organizational usage metrics.

Details:
- Shows total active users (logged in within 30 days)
- Shows total actions performed (all action types)
- Shows date range selector (default: last 30 days)
- Data refreshes daily at midnight UTC

Acceptance Criteria:
□ Org admin can view dashboard after clicking "Usage" in nav
□ Dashboard loads in < 3 seconds
□ Numbers match backend calculations within 24 hours
□ Date range selector allows: 7d, 30d, 90d, custom
□ "Active users" tooltip explains the 30-day definition

Edge Cases:
- New org with no usage: Show "No data yet" state
- Single user org: Show singular language ("1 user")
- Data still processing: Show "Updating..." indicator
```

#### Non-Functional Requirements

How the system should PERFORM.

```
NFR-001: Performance
- Dashboard loads in < 3 seconds for 95th percentile
- Export generates in < 30 seconds for orgs up to 1000 users
- No degradation for orgs up to 5000 users

NFR-002: Security
- Dashboard only accessible to org admin role
- Export only includes users in admin's organization
- Activity logged for compliance audit

NFR-003: Accessibility
- WCAG 2.1 AA compliance
- Keyboard navigation support
- Screen reader compatible
```

### Writing Great Acceptance Criteria

Acceptance criteria make requirements testable. Use the "Given-When-Then" format for complex scenarios:

```
Scenario: Admin views dashboard with usage data

Given: The org has 50 active users
When: Admin navigates to Usage Dashboard
Then: Dashboard shows "50 active users"
And: Load time is under 3 seconds
And: User count matches backend data
```

**Characteristics of good acceptance criteria:**
- **Testable:** Can be verified as pass/fail
- **Clear:** No ambiguity about what's expected
- **Complete:** Covers happy path and key edge cases
- **Atomic:** Each criterion tests one thing

**Common acceptance criteria mistakes:**

```
Bad: "Dashboard should be fast"
Good: "Dashboard loads in < 3 seconds for 95th percentile"

Bad: "Handle errors appropriately"
Good: "If data fails to load, show retry button with 'Unable to load data' message"

Bad: "Works on mobile"
Good: "Dashboard is responsive at 375px width, with horizontal scroll for tables"
```

### Prioritization: P0/P1/P2

Not all requirements are equal. Prioritize explicitly:

| Priority | Meaning | Ship Without? |
|----------|---------|---------------|
| **P0** | Must have | Cannot ship |
| **P1** | Should have | Ship with workaround |
| **P2** | Nice to have | Ship without |

**Example prioritized requirements:**

```
P0 (Must Have - Launch Blockers):
- Dashboard displays active user count
- Dashboard displays total actions
- Admin-only access control
- Data accurate within 24 hours

P1 (Should Have - Important but not blocking):
- Date range selector
- CSV export
- User-level breakdown

P2 (Nice to Have - Future iterations):
- Chart visualizations
- Scheduled email reports
- Comparison to previous period
```

**Using priorities in trade-off discussions:**
"We're running behind. If we cut P2 items and half of P1, can we hit the deadline?"

### Section 6: Design

Link to or embed design artifacts:
- Wireframes
- High-fidelity mockups
- Prototype links
- Interaction specifications

**Design callouts in PRD:**
```
Design Note: See Figma link for final designs
- Empty state: Show illustration with "Get started" prompt
- Loading state: Skeleton placeholder for numbers
- Error state: Inline error with retry button
```

### Section 7: Technical Considerations

What engineering needs to think about:

```
Technical Considerations:

Data Source:
- Usage data available in analytics_events table
- Requires aggregation queries (performance concern for large orgs)
- Consider pre-aggregated daily rollup table

Dependencies:
- Requires analytics service API (currently in development)
- Blocked until auth service supports org-level permissions

Known Constraints:
- Historical data only available for last 12 months
- Export limited by API rate limits (100 requests/minute)

Questions for Engineering:
1. Is daily refresh acceptable or do we need more frequent?
2. What's the performance impact of custom date ranges?
3. Should export be synchronous or async (email when ready)?
```

### Section 8: Launch Plan

How this gets to users:

```
Rollout Strategy:
- Week 1: Internal testing (dogfooding)
- Week 2: 5% of enterprise accounts (beta)
- Week 3: 25% of enterprise accounts
- Week 4: 100% of enterprise accounts

Success Criteria (2 weeks post-launch):
- 60% of org admins have viewed dashboard
- Support ticket requests for reports down 50%
- No P0 bugs reported

Monitoring:
- Dashboard load time (alert if > 5s)
- Error rate (alert if > 1%)
- Data freshness (alert if > 48 hours stale)

Rollback Plan:
- Feature flag allows instant disable
- Previous manual report process still available
```

### Section 9: Open Questions

Be honest about what you don't know:

```
Open Questions:

Product:
- Should we send email notification when export is ready?
  - Leaning toward yes for large exports

Design:
- Dashboard as separate page or overlay?
  - Need design input on navigation flow

Technical:
- Can we support real-time updates in future?
  - Need to understand infrastructure implications

Business:
- Any data privacy concerns with org-level visibility?
  - Legal review scheduled for 1/15
```

### PRD Anti-Patterns to Avoid

**The Novel:** 50-page documents nobody reads
- Fix: Write concisely, use headings, highlight key points

**The Vague:** "System should handle errors gracefully"
- Fix: Specify exact behaviors with acceptance criteria

**The Premature:** Fully specced before research
- Fix: Use lightweight specs for discovery, detailed for execution

**The Unchangeable:** Treating PRD as carved in stone
- Fix: Version and update as you learn; note changes made

**The Technical Spec:** Prescribing implementation details
- Fix: Focus on WHAT, let engineers determine HOW

### PRD Templates

A template provides structure while allowing customization:

**Minimal PRD (for smaller features):**
```
# [Feature Name]
One-line summary

## Problem
What problem are we solving and for whom?

## Solution
What are we building?

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Success Metrics
How will we know this worked?

## Open Questions
What do we still need to figure out?
```

**Full PRD:** See the template in [resources/templates/prd-template.md](../resources/templates/prd-template.md)

---

## Key Takeaways

1. **PRDs are communication tools—write for your audience (engineers, designers, stakeholders)**
2. **Structure matters: overview, context, goals/non-goals, user stories, requirements, design, tech considerations, launch plan**
3. **Requirements need acceptance criteria that are testable, clear, and complete**
4. **Prioritize explicitly (P0/P1/P2) to enable trade-off discussions**
5. **Include non-goals to prevent scope creep**
6. **Maintain open questions section—transparency about unknowns builds trust**
7. **Keep PRDs living documents—update as you learn**

---

## Practice

### Reflection Questions
1. Think of a feature you've seen poorly specced. What was missing?
2. What's the minimum PRD you'd write for a one-day project vs. a quarter-long project?
3. How would you adapt PRD format for different audiences (enterprise vs. startup)?

### Exercise
**Write a Mini-PRD:**

Create a PRD for this feature:

**Feature:** Add "Mark as complete" functionality to a task management app

Your PRD should include:
1. Problem statement (2-3 sentences)
2. 2-3 user stories
3. 5+ functional requirements with acceptance criteria
4. P0/P1/P2 prioritization
5. 2+ edge cases
6. 1+ non-functional requirement
7. 2+ open questions

**Time target:** 30-45 minutes

---

## Further Reading

- **"Shape Up" by Basecamp** - Alternative to detailed PRDs (pitches)
- **"Writing Great Specifications" by Kamil Nicieja** - Deep dive on requirements
- **Figma's PRD template** - Real-world example
- **Product Hunt makers** - See how startups describe their products
- **Stripe's API documentation** - Excellent example of clear specification
