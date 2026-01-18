# Mini-Project: PRD Writing

## Project Overview

Apply everything you've learned in the Technical PM module by writing a complete, production-quality PRD for a real feature.

This project will give you a portfolio-ready artifact demonstrating your ability to:
- Define problems clearly
- Write user stories with acceptance criteria
- Prioritize requirements
- Consider technical implications
- Plan for launch

## Time Estimate

3-5 hours total

## The Scenario

You're a PM at a B2B SaaS company that provides project management software. Your tool is used by teams of 5-500 people to manage tasks, projects, and team collaboration.

**Current situation:**
- Users can create tasks and assign them to team members
- Tasks have due dates, descriptions, and statuses (To Do, In Progress, Done)
- There's no way to see tasks across projects in one view

**User feedback (from research):**
- "I manage 3 projects and constantly switch between them to see what's due"
- "My manager asks me for a weekly status and I have to manually compile it"
- "I miss deadlines because tasks are scattered across projects"
- "I want to see everything I need to do this week in one place"

**Business context:**
- Competitor launched a "My Work" dashboard 3 months ago
- Customer support tickets about "cross-project view" increased 40% this quarter
- Enterprise customers (your highest-paying segment) cite this as #1 feature request
- Engineering capacity: 2 engineers for 4-6 weeks

## Your Task

Write a complete PRD for a "My Tasks" dashboard feature that addresses the user feedback above.

## Deliverable

A PRD document (Markdown) that includes:

### Required Sections

1. **Overview** (1 page)
   - Problem statement
   - Proposed solution
   - Success metrics

2. **Background & Context** (0.5-1 page)
   - User research summary
   - Business case
   - Competitive context

3. **Goals & Non-Goals** (0.5 page)
   - What's in scope
   - What's explicitly out of scope

4. **User Stories** (1 page)
   - 4-6 user stories with proper format
   - Cover primary use cases

5. **Requirements** (2-3 pages)
   - 8-12 functional requirements with acceptance criteria
   - P0/P1/P2 prioritization
   - 3-5 non-functional requirements
   - Edge cases covered

6. **Design Considerations** (0.5 page)
   - Key UI elements
   - Interaction notes
   - (No need for actual mockups)

7. **Technical Considerations** (0.5 page)
   - Data requirements
   - Dependencies
   - Questions for engineering

8. **Launch Plan** (0.5 page)
   - Rollout strategy
   - Success criteria
   - Monitoring needs

9. **Open Questions** (0.5 page)
   - Unresolved decisions
   - Items needing input

**Total: 7-10 pages**

## Getting Started

1. Review the PRD template in `templates/prd-template.md`
2. Think through the user needs and possible solutions
3. Draft each section, don't aim for perfection on first pass
4. Review and refine, checking for completeness and clarity
5. Self-evaluate against the rubric below

## Evaluation Rubric

Use this rubric to self-assess your PRD:

### Problem Definition (20%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Problem is specific, user-centered, backed by evidence |
| ⭐⭐ | Problem is clear but could use more specificity |
| ⭐ | Problem is vague or solution-focused |

### User Stories (20%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Stories follow format, are testable, cover key scenarios |
| ⭐⭐ | Most stories are well-formed with minor issues |
| ⭐ | Stories are incomplete or don't follow format |

### Requirements Quality (30%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Requirements have clear acceptance criteria, appropriate prioritization, edge cases covered |
| ⭐⭐ | Most requirements are clear with some gaps |
| ⭐ | Requirements lack acceptance criteria or prioritization |

### Technical Considerations (15%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | Shows understanding of technical implications, asks good questions |
| ⭐⭐ | Some technical awareness but gaps |
| ⭐ | Little technical consideration |

### Completeness & Clarity (15%)
| Score | Criteria |
|-------|----------|
| ⭐⭐⭐ | All sections complete, well-organized, easy to follow |
| ⭐⭐ | Most sections complete, generally clear |
| ⭐ | Missing sections or hard to follow |

**Target: 80%+ to demonstrate PM-ready skills**

## Tips for Success

1. **Start with the problem** — Don't jump to features
2. **Be specific** — "Fast" isn't an acceptance criterion; "< 3 seconds" is
3. **Prioritize ruthlessly** — Not everything is P0
4. **Include non-goals** — Show what you deliberately cut
5. **Ask engineering questions** — Show you've thought about implementation
6. **Think about edge cases** — What happens when things go wrong?

## Example Snippets

### Good Problem Statement
```
Enterprise project managers (managing 3+ projects with 20+ team members)
cannot see their tasks across projects in a single view. This forces them
to check each project individually, taking an average of 15 minutes daily
and causing 23% to report missing deadlines due to scattered tasks.
```

### Good User Story
```
As a project manager
I want to see all my tasks due this week across all projects
So that I can prioritize my work without switching between projects

Acceptance Criteria:
□ Shows tasks from all projects I'm a member of
□ Default filter is "This Week" (Mon-Sun of current week)
□ Tasks are sorted by due date, then priority
□ Each task shows: title, project name, due date, status
□ Clicking a task navigates to task detail in its project
```

### Good Requirement
```
REQ-003: Week View

Description:
Users can view tasks due in the current week by default.

Details:
- Week defined as Monday 00:00 to Sunday 23:59 in user's timezone
- Shows tasks due within this range regardless of status
- No-due-date tasks are excluded from this view

Acceptance Criteria:
□ Default view shows current week's tasks on page load
□ Week boundary correctly handles user's timezone
□ Overdue tasks from previous weeks appear with visual indicator
□ Tasks with no due date are not shown in week view

Priority: P0

Edge Cases:
- Task due date is in different timezone than user: Use user's timezone
- Week view on Sunday shows remaining Sunday tasks
```

## Submission

Save your completed PRD as `project.md` in this directory.

Compare your work against the evaluation rubric and note areas for improvement.

## Bonus Challenges

If you want to go further:

1. **Create wireframes** — Sketch the dashboard layout (tool: Excalidraw, Figma, pen and paper)
2. **Define analytics events** — What events would you track?
3. **Write a launch announcement** — 200-word release notes for users
4. **Conduct a mock review** — Have someone play "engineer" and ask questions

## Next Steps

After completing this mini-project:
- Include this PRD in your portfolio
- Use the template for real PRDs at work
- Practice defending your requirements in mock conversations
- Continue to [03-AI Product Management](../../03-ai-product-management/) module
