# Tech Foundations for PMs

## Learning Objectives

- [ ] Understand the software development lifecycle and deployment process
- [ ] Grasp basic architectural concepts (frontend/backend, databases, APIs)
- [ ] Know how code moves from a developer's machine to production
- [ ] Recognize different types of technical work (feature, bug fix, infrastructure)
- [ ] Understand enough to ask good questions and spot red flags

## Prerequisites

- Completed: [01-Foundations](../01-foundations/) module
- No coding experience required

---

## Core Content

### Why Technical Foundations Matter

You don't need to code, but you need to understand:
- **How things work** — to have productive conversations
- **What's hard vs. easy** — to prioritize and set expectations
- **Where things break** — to anticipate problems
- **What trade-offs exist** — to make informed decisions

Engineers will respect you more if you understand their world, even at a basic level.

### The Software Stack

Modern applications have layers, each with different concerns:

```
┌─────────────────────────────────────────────────────────────────┐
│                          USERS                                  │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  FRONTEND (Client)                                              │
│  What users see and interact with                               │
│  • Web browsers, mobile apps, desktop apps                      │
│  • HTML, CSS, JavaScript                                        │
│  • React, Vue, Swift, Kotlin                                    │
└─────────────────────────────────────────────────────────────────┘
                               │ API Calls
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  BACKEND (Server)                                               │
│  Business logic and data processing                             │
│  • Receives requests, processes, returns responses              │
│  • Python, Java, Go, Node.js                                    │
│  • Authentication, authorization, validation                    │
└─────────────────────────────────────────────────────────────────┘
                               │ Queries
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  DATABASE                                                       │
│  Persistent data storage                                        │
│  • User data, transactions, content                             │
│  • PostgreSQL, MySQL, MongoDB                                   │
│  • Read/write operations                                        │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  INFRASTRUCTURE                                                 │
│  Everything that keeps it running                               │
│  • Servers (AWS, GCP, Azure)                                    │
│  • Networking, load balancers, CDNs                            │
│  • Monitoring, logging, alerting                                │
└─────────────────────────────────────────────────────────────────┘
```

### Frontend vs. Backend

#### Frontend
The part users directly interact with.

**What it handles:**
- Visual presentation (layouts, colors, typography)
- User interactions (clicks, scrolls, inputs)
- Immediate feedback (animations, loading states)
- Local state (form data before submission)

**Technologies:** HTML, CSS, JavaScript, TypeScript, React, Vue, Angular, Swift, Kotlin

**PM relevance:**
- User experience and design live here
- Performance affects user perception directly
- Changes are often visible and easier to demo
- Mobile vs. web = different frontends, same backend

#### Backend
The logic and data behind the scenes.

**What it handles:**
- Business rules (pricing, eligibility, workflows)
- Data storage and retrieval
- User authentication and permissions
- External integrations (payment processors, email services)

**Technologies:** Python, Java, Go, Node.js, Ruby, C#

**PM relevance:**
- Business logic complexity lives here
- Security and compliance concerns center here
- Changes are invisible to users but critical
- Performance at scale is often a backend problem

### Databases: Where Data Lives

Databases store persistent information—the stuff that survives server restarts.

#### Types of Databases

**Relational Databases (SQL)**
Data in tables with rows and columns, related through keys.

```
┌─────────────────────────────┐      ┌─────────────────────────────┐
│ USERS                       │      │ ORDERS                      │
├─────────────────────────────┤      ├─────────────────────────────┤
│ id │ name    │ email        │      │ id │ user_id │ total │ date │
├────┼─────────┼──────────────┤      ├────┼─────────┼───────┼──────┤
│ 1  │ Alice   │ a@email.com  │◄────►│ 1  │ 1       │ $50   │ 1/15 │
│ 2  │ Bob     │ b@email.com  │      │ 2  │ 1       │ $30   │ 1/20 │
└────┴─────────┴──────────────┘      │ 3  │ 2       │ $75   │ 1/22 │
                                      └────┴─────────┴───────┴──────┘
```

**Examples:** PostgreSQL, MySQL, SQLite

**Good for:** Structured data with relationships, transactions, complex queries

**NoSQL Databases**
More flexible structures—documents, key-value pairs, graphs.

**Examples:** MongoDB (documents), Redis (key-value), Neo4j (graph)

**Good for:** Unstructured data, rapid iteration, specific use cases (caching, relationships)

**PM relevance:**
- Database choice affects what's easy/hard to build
- Schema changes can be significant work
- Queries that are slow at scale cause problems
- Data migration between systems is painful

### APIs: How Systems Talk

APIs (Application Programming Interfaces) are contracts for how software components communicate.

#### REST APIs
The most common approach. Uses HTTP methods:

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve data | Get user profile |
| POST | Create new data | Create new order |
| PUT | Update existing data | Update user settings |
| DELETE | Remove data | Delete a comment |

```
GET /users/123
→ Returns: {"id": 123, "name": "Alice", "email": "alice@email.com"}

POST /orders
Body: {"user_id": 123, "items": [...]}
→ Returns: {"order_id": 456, "status": "created"}
```

#### GraphQL
Newer approach where clients specify exactly what data they want.

```
query {
  user(id: 123) {
    name
    orders {
      total
      date
    }
  }
}
```

**PM relevance:**
- API design affects developer experience
- Public APIs are products unto themselves
- Breaking API changes upset partner integrations
- Understanding API capabilities helps spec features

### How Code Gets to Production

The journey from idea to running software:

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Write   │ → │  Review  │ → │   Test   │ → │  Deploy  │ → │ Monitor  │
│  Code    │   │  Code    │   │          │   │          │   │          │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

#### 1. Write Code
Developer writes code on their local machine, often in a feature "branch" (isolated copy of the codebase).

#### 2. Code Review
Other engineers review the changes:
- Does it work correctly?
- Is it secure?
- Is it maintainable?
- Does it follow standards?

Pull Request (PR) / Merge Request (MR): The formal request to merge changes into the main codebase.

#### 3. Test
**Unit tests:** Test individual functions
**Integration tests:** Test components working together
**End-to-end tests:** Test complete user flows
**Manual QA:** Human verification of functionality

CI (Continuous Integration): Automated testing that runs on every code change.

#### 4. Deploy
Moving code from development to production environments:

| Environment | Purpose |
|-------------|---------|
| Development | Engineers' machines |
| Staging | Pre-production testing |
| Production | Live users |

CD (Continuous Deployment): Automated deployment when tests pass.

#### 5. Monitor
Watching the live system:
- Is it up and responsive?
- Are errors occurring?
- Is performance acceptable?
- Are users doing expected things?

### Types of Engineering Work

Different work types have different characteristics:

#### Feature Work
Building new capabilities.
- Often involves frontend AND backend changes
- Requires PRD and design
- Most visible to stakeholders

#### Bug Fixes
Correcting incorrect behavior.
- May be urgent (severity 1) or not
- Often requires investigation time
- Sometimes reveals deeper issues

#### Technical Debt
Improving code quality without user-visible changes.
- Refactoring messy code
- Updating old libraries
- Improving test coverage

**PM challenge:** Hard to prioritize against features, but ignoring it slows future development.

#### Infrastructure
Work on the systems that support the product.
- Database optimization
- Security improvements
- Scaling preparation

**PM relevance:** Often invisible but critical. Infrastructure problems become product problems.

### Understanding Technical Complexity

Not all features are equal. Complexity drivers:

#### Data Complexity
- New data models required?
- Changes to existing schemas?
- Data migrations needed?

#### Integration Complexity
- External services involved?
- Authentication/authorization changes?
- Timing dependencies?

#### Scale Complexity
- How many users affected?
- How much data processed?
- What's the performance requirement?

#### Unknowns
- New technology for the team?
- Unclear requirements?
- Exploratory work needed?

**Red flags for complexity:**
- "We've never done anything like this"
- "It depends on [external system]"
- "We'd need to change the data model"
- "It might affect performance at scale"

### Questions PMs Should Ask

Instead of accepting estimates blindly, ask questions:

**Scope questions:**
- "What's the smallest version we could build?"
- "What would make this significantly harder?"
- "What are we NOT building in this version?"

**Risk questions:**
- "What could go wrong?"
- "What don't we know yet?"
- "What dependencies do we have?"

**Alternative questions:**
- "Are there other ways to achieve this?"
- "What if we didn't build this?"
- "Can we use an existing tool?"

**Process questions:**
- "What needs to happen before we can start?"
- "Who else needs to be involved?"
- "What's blocking progress?"

---

## Key Takeaways

1. **The stack (frontend → backend → database → infrastructure) each has different concerns and expertise**
2. **APIs are contracts between systems—understanding them helps you spec features**
3. **Code moves through development, review, testing, deployment, and monitoring—each step matters**
4. **Different work types (features, bugs, tech debt, infrastructure) compete for engineering time**
5. **Complexity comes from data, integrations, scale, and unknowns—learn to spot the signs**
6. **Ask good questions instead of accepting technical explanations you don't understand**

---

## Practice

### Reflection Questions
1. Think of a feature in a product you use. What frontend changes does it require? Backend? Database?
2. Have you experienced a bug that was easy to describe but hard to fix? What made it complex?
3. What questions would you ask an engineer about a feature that integrates with an external payment system?

### Exercise
**Feature Decomposition:**

Pick a feature (real or imagined):

1. Describe it in one sentence
2. List what the frontend needs to do
3. List what the backend needs to do
4. What data needs to be stored?
5. What external systems are involved?
6. Identify 2-3 questions you'd ask engineers about complexity

**Example:**
```
Feature: "Allow users to export their data as CSV"

Frontend:
- Export button in settings
- Loading state during export
- Download trigger

Backend:
- Generate CSV from user data
- Handle large datasets (pagination?)
- Secure access (only own data)

Data:
- No new storage needed
- Reading existing user data

External systems:
- None (or cloud storage for large files)

Questions:
- "How large could exports get? Do we need background processing?"
- "What data is included—just their content or also activity history?"
- "Are there any data privacy considerations for the export format?"
```

---

## Further Reading

- **"The Phoenix Project" by Gene Kim** - IT operations and DevOps as a novel
- **"Web Development 101"** - FreeCodeCamp's basics (even for non-coders)
- **High Scalability blog** - How big systems work
- **Martin Fowler's blog** - Software architecture concepts explained
- **ByteByteGo** - System design visualizations
