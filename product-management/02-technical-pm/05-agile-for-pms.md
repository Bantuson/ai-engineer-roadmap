# Agile for PMs

## Learning Objectives

- [ ] Understand agile principles and why they matter
- [ ] Compare Scrum and Kanban approaches
- [ ] Function effectively as Product Owner in Scrum
- [ ] Manage product backlogs for maximum team effectiveness
- [ ] Participate in agile ceremonies productively

## Prerequisites

- Completed: [04 - Writing PRDs](./04-writing-prds.md)

---

## Core Content

### What is Agile?

Agile is **a set of principles for software development that emphasizes iterative delivery, collaboration, and responding to change.**

**The Agile Manifesto (2001) values:**

```
Individuals and interactions    over   Processes and tools
Working software                over   Comprehensive documentation
Customer collaboration          over   Contract negotiation
Responding to change            over   Following a plan
```

The items on the right have value, but the items on the left have MORE value.

### Agile vs. Waterfall

**Waterfall:** Sequential phases (requirements → design → build → test → deploy)

```
Waterfall:
────────────────────────────────────────────────────▶
[Requirements] → [Design] → [Build] → [Test] → [Ship]
                                                  │
                                            (6-12 months)
```

**Agile:** Iterative cycles delivering working software frequently

```
Agile:
────────────────────────────────────────────────────▶
[Sprint 1] → [Sprint 2] → [Sprint 3] → [Sprint 4] →
  │ Ship      │ Ship       │ Ship       │ Ship
  ▼           ▼            ▼            ▼
(2 weeks)  (2 weeks)   (2 weeks)   (2 weeks)
```

**Why agile wins for most software:**
- Requirements change (market, users, learning)
- Early feedback is valuable
- Smaller batches reduce risk
- Teams stay engaged with visible progress

**When waterfall might still make sense:**
- Fixed scope with well-understood requirements
- Regulatory requirements for upfront documentation
- Hardware or physical product dependencies

### Scrum: The Most Popular Framework

Scrum is a specific agile framework with defined roles, events, and artifacts.

#### Scrum Roles

| Role | Responsibility | Usually Is |
|------|----------------|------------|
| **Product Owner** | What to build, priority | PM or dedicated PO |
| **Scrum Master** | Process facilitation, blocker removal | Dedicated or rotating |
| **Development Team** | How to build, delivery | Engineers, designers |

**Product Owner is often the PM role in Scrum.** Some organizations separate them:
- PO: Tactical backlog management, sprint-level
- PM: Strategic, roadmap-level, multiple teams

#### Scrum Events (Ceremonies)

**Sprint Planning** (Beginning of sprint)
- Duration: 2-4 hours for 2-week sprint
- Purpose: Decide what to commit to this sprint
- Participants: PO, team, SM
- Output: Sprint backlog

**Daily Standup/Daily Scrum** (Every day)
- Duration: 15 minutes max
- Purpose: Synchronize, identify blockers
- Format: What did I do? What will I do? Any blockers?
- Anti-pattern: Status reports to manager

**Sprint Review** (End of sprint)
- Duration: 1-2 hours
- Purpose: Demo completed work, get feedback
- Participants: Team + stakeholders
- Output: Feedback incorporated into backlog

**Sprint Retrospective** (End of sprint)
- Duration: 1-1.5 hours
- Purpose: Process improvement
- Format: What went well? What could improve? Actions?
- Output: Process improvements to try

```
┌─────────────────────────────────────────────────────────────────┐
│                         SPRINT (2 weeks)                        │
├─────────────────────────────────────────────────────────────────┤
│  DAY 1        │  DAY 2-9              │  DAY 10                 │
│  ──────────── │  ──────────────────── │  ─────────────────────  │
│  Planning     │  Daily work           │  Review                 │
│  (2-4 hrs)    │  + Daily standups     │  (1-2 hrs)              │
│               │  (15 min each)        │  Retrospective          │
│               │                       │  (1-1.5 hrs)            │
└─────────────────────────────────────────────────────────────────┘
```

#### Scrum Artifacts

**Product Backlog:** Prioritized list of all desired work
- Owned by Product Owner
- Single source of truth for "what to build"
- Continuously refined

**Sprint Backlog:** Subset committed to for current sprint
- Owned by team
- Should be achievable within sprint
- Team decides how much to commit

**Increment:** Working software at end of sprint
- Must be "done" (meets Definition of Done)
- Potentially shippable

### The Product Owner Role

If you're a PM working in Scrum, Product Owner responsibilities are critical.

#### PO Responsibilities

1. **Define and communicate product vision**
   - Team understands why they're building what they're building

2. **Own and prioritize the backlog**
   - Items are ordered by value
   - Top items are refined and ready

3. **Make scope decisions**
   - Authority to say yes/no to requests
   - Trade-off decisions when needed

4. **Accept work as done**
   - Review completed items against criteria
   - Provide feedback for improvement

5. **Represent stakeholders**
   - Bring user and business perspective
   - Balance competing interests

#### PO Anti-Patterns

**The Absent PO:**
Not available for questions, delays team

**The Committee:**
Can't make decisions, needs approval for everything

**The Backlog Dumper:**
Adds items without prioritization or refinement

**The Micro-Manager:**
Tells team HOW to build, not WHAT

**The Yes-Person:**
Accepts every request, backlog grows infinitely

### Backlog Management

A well-managed backlog enables team velocity.

#### Backlog Item Types

| Type | Description | Example |
|------|-------------|---------|
| **User Story** | User-facing functionality | "As a user, I can reset password" |
| **Technical Task** | Non-user-facing work | "Upgrade database version" |
| **Bug** | Defect in existing functionality | "Login fails on Safari" |
| **Spike** | Time-boxed research | "Investigate payment providers" |

#### Writing Good Backlog Items

**User Story Format:**
```
As a [user type]
I want to [action]
So that [benefit]

Acceptance Criteria:
□ Criterion 1
□ Criterion 2
□ Criterion 3
```

**Sizing (Story Points or T-Shirt):**

Story points measure relative complexity, not time:
- 1 point: Trivial change
- 2 points: Simple, well-understood
- 3 points: Medium complexity
- 5 points: Significant work
- 8 points: Large, consider breaking down
- 13+: Too big, must break down

T-shirt sizes (S/M/L/XL) work similarly for rougher estimation.

#### Backlog Refinement

Regular sessions (1-2 hours/week) to prepare items for future sprints:

**Activities:**
- Add acceptance criteria
- Break large items into smaller ones
- Estimate complexity
- Identify dependencies
- Clarify questions

**"Ready" items have:**
- Clear description
- Acceptance criteria
- Estimates
- No blocking questions
- Dependencies identified

### Sprint Planning Deep Dive

Sprint planning sets up the sprint for success.

#### Before Sprint Planning (PO Prep)

- Top items are refined and ready
- Priorities are clear
- Questions are answered
- Designs are available (if needed)

#### During Sprint Planning

**Part 1: What can we deliver?** (PO leads)
- PO presents prioritized items
- Team asks clarifying questions
- Team selects items they can commit to
- Sprint goal is defined

**Part 2: How will we deliver?** (Team leads)
- Team breaks stories into tasks
- Identifies technical approach
- Raises concerns or blockers

#### Sprint Goal

A single sentence capturing the sprint's purpose:

```
Sprint Goal: "Enable org admins to view and export usage data"
```

Sprint goals help with:
- Focus: What matters most this sprint
- Flexibility: Individual items can change if goal is met
- Communication: Stakeholders understand the sprint's purpose

### Kanban: The Alternative

Kanban is a continuous flow approach without fixed sprints.

#### Kanban vs. Scrum

| Aspect | Scrum | Kanban |
|--------|-------|--------|
| Cadence | Fixed sprints (2 weeks) | Continuous |
| Roles | PO, SM, Team | Flexible |
| Commitment | Sprint backlog | Work-in-progress limits |
| Planning | Sprint planning | On-demand |
| Changes | Wait for next sprint | Add anytime if capacity |

#### Kanban Board

```
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ BACKLOG  │ READY    │ IN PROG  │ REVIEW   │ DONE     │
│          │ (max 5)  │ (max 3)  │ (max 2)  │          │
├──────────┼──────────┼──────────┼──────────┼──────────┤
│ [Item A] │ [Item D] │ [Item G] │ [Item I] │ [Item J] │
│ [Item B] │ [Item E] │ [Item H] │          │ [Item K] │
│ [Item C] │ [Item F] │          │          │ [Item L] │
│          │          │          │          │          │
└──────────┴──────────┴──────────┴──────────┴──────────┘
```

#### WIP (Work-in-Progress) Limits

The key Kanban principle: **Limit work in progress.**

Why?
- Reduces context switching
- Surfaces bottlenecks
- Improves flow and throughput
- Forces finishing before starting

**When column is at limit:** Help finish existing work before pulling new work.

#### When to Use Kanban

**Kanban works well for:**
- Support/maintenance teams
- Unpredictable work (many interrupts)
- Continuous deployment environments
- Teams uncomfortable with sprint commitment

**Scrum works well for:**
- Feature development teams
- Teams needing structure
- Stakeholders wanting predictable delivery
- New teams learning agile

### PM's Role in Agile Ceremonies

How to participate effectively in each ceremony:

#### Sprint Planning

**Your job:**
- Present prioritized, refined items
- Explain the "why" behind each
- Answer questions immediately
- Negotiate scope based on capacity

**Not your job:**
- Dictate how much team should commit
- Tell team how to implement
- Fill awkward silence—let team discuss

#### Daily Standup

**Your job:**
- Listen for blockers you can remove
- Note items that need clarification
- Be available for follow-up questions

**Not your job:**
- Run the meeting (SM or team self-runs)
- Ask for status reports
- Bring up new requirements

#### Sprint Review

**Your job:**
- Invite relevant stakeholders
- Facilitate feedback collection
- Celebrate team accomplishments
- Connect work to product goals

**Not your job:**
- Criticize incomplete work
- Add new requirements during demo
- Let stakeholders derail with tangents

#### Retrospective

**Your job:**
- Participate as team member
- Share observations about process
- Commit to improvement actions that involve you

**Not your job:**
- Defend yourself against feedback
- Dominate the conversation
- Skip it (your presence matters)

---

## Key Takeaways

1. **Agile values iterative delivery and responding to change over rigid planning**
2. **Scrum has defined roles (PO, SM, Team), events (planning, standup, review, retro), and artifacts (backlogs, increment)**
3. **Product Owner owns the "what" and prioritization; team owns the "how" and commitment**
4. **Well-refined backlogs enable team velocity—invest in preparation**
5. **Kanban provides continuous flow alternative to sprint-based Scrum**
6. **Your role in ceremonies is enabling, not directing—facilitate, don't dictate**

---

## Practice

### Reflection Questions
1. Have you experienced agile done well vs. agile done poorly? What was the difference?
2. What PO anti-patterns have you observed? How did they affect the team?
3. When might Kanban be a better fit than Scrum for a team?

### Exercise
**Sprint Planning Simulation:**

Given this scenario:
- 2-week sprint
- Team velocity: ~30 story points
- 3 engineers available

Backlog (prioritized):
```
1. User login (8 points) - P0
2. Password reset (5 points) - P0
3. User profile page (8 points) - P1
4. Email notifications (13 points) - P1
5. Dark mode (3 points) - P2
6. Performance optimization (8 points) - Tech debt
```

Questions:
1. Which items would you recommend for this sprint? Why?
2. What sprint goal would you propose?
3. What questions would you expect from the team?
4. If velocity turns out to be 20 points, what would you cut?

---

## Further Reading

- **"Scrum Guide" by Schwaber & Sutherland** - Official Scrum definition (free)
- **"User Story Mapping" by Jeff Patton** - Organizing backlogs visually
- **"Kanban" by David Anderson** - Kanban method in depth
- **"The Art of Agile Development" by James Shore** - Practical agile practices
- **Mountain Goat Software blog** - Ongoing agile advice
