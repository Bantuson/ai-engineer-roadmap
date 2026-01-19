# Context Setting

## Overview

Context transforms generic AI responses into tailored, relevant outputs. This module covers techniques for providing effective background information, personas, and framing.

## The Context Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                     CONTEXT LAYERS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   SYSTEM CONTEXT (Persistent)                                   │
│   └── Role, capabilities, general guidelines                    │
│                                                                  │
│   SESSION CONTEXT (Conversation-level)                          │
│   └── User preferences, ongoing task, accumulated knowledge     │
│                                                                  │
│   TASK CONTEXT (Request-specific)                               │
│   └── Immediate background, input data, specific requirements   │
│                                                                  │
│   EXAMPLE CONTEXT (Demonstrative)                               │
│   └── Sample inputs/outputs, formatting examples                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Persona Definition

### The RICE Framework for Personas

```
R - Role: Job title or function
I - Identity: Background and expertise
C - Characteristics: Communication style and traits
E - Experience: Knowledge level and history
```

**Example:**

```
ROLE: You are a Senior DevOps Engineer

IDENTITY:
- 10+ years experience in cloud infrastructure
- Specialization in AWS and Kubernetes
- Background in site reliability engineering

CHARACTERISTICS:
- Direct and practical communication style
- Focuses on production-ready solutions
- Considers security and scalability by default
- Explains trade-offs clearly

EXPERIENCE:
- Has managed systems serving millions of users
- Experienced with incident response
- Deep knowledge of monitoring and observability
```

### Persona Templates

**Technical Expert:**
```
You are a [specialty] expert with [years] years of experience.
Your expertise includes [specific skills/technologies].
You communicate in a [style] manner, always [key behavior].
When explaining concepts, you [explanation approach].
```

**Business Professional:**
```
You are a [role] at a [company type].
Your background includes [relevant experience].
You prioritize [key priorities] in your recommendations.
You communicate with [audience type] regularly.
```

**Creative Professional:**
```
You are a [creative role] known for [distinctive style].
Your influences include [relevant influences].
You approach problems by [creative method].
Your work is characterized by [key characteristics].
```

## Background Information

### Structured Background

```
CONTEXT FOR THIS TASK:

## Situation
[Current state, what's happening]

## Background
[History, how we got here]

## Objective
[What we're trying to achieve]

## Constraints
[Limitations, requirements, boundaries]

## Available Resources
[Tools, data, permissions available]
```

**Example:**

```
CONTEXT FOR THIS CODE REVIEW:

## Situation
We're preparing to launch a new payment feature next week.
This PR contains the core payment processing logic.

## Background
- We use Stripe for payment processing
- Current system handles $2M monthly transactions
- Last payment bug caused $50K in refunds

## Objective
Ensure code is secure, reliable, and handles edge cases.

## Constraints
- Must be backwards compatible with v1 API
- Cannot increase latency beyond 200ms
- Must maintain PCI compliance

## Available Resources
- Stripe sandbox for testing
- Load testing environment available
- Security team on standby for questions
```

### Dynamic Context Injection

```python
def build_context(user, task, environment):
    """Build dynamic context for prompts."""

    context = f"""
CURRENT CONTEXT:

User Profile:
- Role: {user.role}
- Expertise: {user.expertise_level}
- Preferences: {user.communication_preferences}

Task Details:
- Type: {task.type}
- Priority: {task.priority}
- Dependencies: {task.dependencies}

Environment:
- Platform: {environment.platform}
- Constraints: {environment.constraints}
- Available Tools: {environment.tools}
"""
    return context
```

## Framing Techniques

### Problem Framing

```
FRAME AS PROBLEM:
"We have a challenge: [problem statement]
Current impact: [consequences]
Desired outcome: [goal]
Help us solve this by [specific request]"

EXAMPLE:
"We have a challenge: Our API response times have increased
from 100ms to 500ms over the past month.

Current impact: User complaints up 40%, conversion down 15%

Desired outcome: Return to sub-200ms response times while
maintaining feature functionality

Help us solve this by analyzing potential causes and
recommending a prioritized optimization strategy."
```

### Audience Framing

```
"Explain [topic] for [audience type]:

AUDIENCE PROFILES:

Technical audience:
- Assume familiarity with jargon
- Include implementation details
- Focus on accuracy over simplicity

Business audience:
- Minimize technical jargon
- Emphasize impact and ROI
- Use analogies and examples

Beginner audience:
- Define all terms
- Build up from fundamentals
- Use step-by-step explanations"
```

### Perspective Framing

```
"Analyze this decision from multiple perspectives:

1. ENGINEERING PERSPECTIVE
   - Technical feasibility
   - Maintenance burden
   - Integration complexity

2. BUSINESS PERSPECTIVE
   - Cost implications
   - Revenue impact
   - Market positioning

3. USER PERSPECTIVE
   - Experience impact
   - Learning curve
   - Value delivered

4. SECURITY PERSPECTIVE
   - Risk profile
   - Compliance implications
   - Attack surface"
```

## Context Windows and Management

### Prioritizing Context

When context exceeds limits, prioritize:

```
PRIORITY 1 (Essential):
- Current task definition
- Critical constraints
- Immediate input data

PRIORITY 2 (Important):
- Relevant background
- User preferences
- Recent conversation

PRIORITY 3 (Supplementary):
- Historical context
- Related examples
- Extended documentation
```

### Context Compression

```
ORIGINAL (verbose):
"The user has been working on this project for several months
and has encountered numerous issues along the way. They started
with a basic implementation but have since expanded it to include
many new features. The codebase has grown significantly and now
includes authentication, authorization, API endpoints, database
models, and a frontend application..."

COMPRESSED:
"Project context: Multi-month development, full-stack app
(auth, API, DB, frontend). User facing scaling challenges."
```

## Conversation Context

### Maintaining State

```
"CONVERSATION STATE:

Previous topics discussed:
1. Database schema design (concluded)
2. API endpoint structure (in progress)
3. Authentication flow (pending)

Current focus: API endpoint structure
User's preferred approach: RESTful over GraphQL
Open questions: Rate limiting strategy

Continue from where we left off on API endpoints."
```

### Referring to Previous Context

```
"Building on our earlier discussion about [topic]:

You previously suggested [summary of suggestion].
The user tried this and found [result].

Given this new information, [new request]."
```

## Context Anti-Patterns

### 1. Information Overload

```
❌ Including every possible detail
✓ Including only relevant, actionable context
```

### 2. Stale Context

```
❌ "As we discussed last week..." (may be forgotten)
✓ "Context: User previously decided to use PostgreSQL. Now asking about..."
```

### 3. Contradictory Context

```
❌ "Be brief and thorough"
✓ "Be concise but complete - prioritize key points"
```

### 4. Missing Audience

```
❌ "Explain machine learning"
✓ "Explain machine learning to a marketing manager who
   needs to understand it for product positioning"
```

## Practical Exercise

Create context for this scenario:

**Scenario:** A startup CTO needs help architecting a new microservices system.

**Well-Crafted Context:**

```
PERSONA:
You are a solutions architect with expertise in microservices,
having designed systems for startups scaling from 1K to 1M users.

SITUATION:
A fintech startup (Series A, 15 engineers) is transitioning
from a monolith to microservices.

BACKGROUND:
- Current stack: Python/Django monolith on AWS
- Pain points: Deployment bottlenecks, scaling issues
- Timeline: 6 months for initial migration
- Budget: Moderate (can afford managed services)

CONSTRAINTS:
- Must maintain 99.9% uptime during migration
- Team has limited Kubernetes experience
- Must remain PCI compliant
- Cannot hire additional engineers immediately

TASK:
Design a migration strategy that:
1. Identifies which services to extract first
2. Recommends infrastructure choices
3. Defines communication patterns
4. Includes a phased rollout plan

OUTPUT:
Provide recommendations as an architecture document with
diagrams (described in text) and prioritized action items.
```

## Next Steps

- [../02-core-techniques/01-zero-shot-prompting.md](../02-core-techniques/01-zero-shot-prompting.md) - Zero-shot prompting
- [../02-core-techniques/02-few-shot-prompting.md](../02-core-techniques/02-few-shot-prompting.md) - Few-shot prompting
