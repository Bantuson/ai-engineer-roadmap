# APIs, Platforms & Developer Experience

## Learning Objectives

- [ ] Understand REST and GraphQL APIs and when each is appropriate
- [ ] Apply API design principles that developers love
- [ ] Think about products as platforms with extension points
- [ ] Evaluate developer experience (DX) for technical products
- [ ] Manage API versioning and breaking changes

## Prerequisites

- Completed: [01 - Tech Foundations](./01-tech-foundations.md)
- Completed: [02 - Working with Engineers](./02-working-with-engineers.md)

---

## Core Content

### Why APIs Matter for PMs

Even if you're not building a developer product, APIs matter:

- **Every modern product has APIs** — Mobile apps, integrations, internal services all communicate via APIs
- **API decisions are hard to reverse** — Breaking changes upset users and partners
- **APIs are products** — They have users (developers), experiences, and need design thinking
- **Platform thinking drives growth** — The most valuable products become platforms

### API Fundamentals

An API (Application Programming Interface) is a contract defining how software components communicate.

#### REST APIs

REpresentational State Transfer — the dominant approach for web APIs.

**Core concepts:**

**Resources:** Things you can interact with (users, orders, products)
**Endpoints:** URLs that represent resources
**Methods:** Actions you can take (GET, POST, PUT, DELETE)
**Responses:** Data returned, usually as JSON

**Example REST API:**

```
# Get all users
GET /api/users
→ [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# Get specific user
GET /api/users/1
→ {"id": 1, "name": "Alice", "email": "alice@example.com"}

# Create new user
POST /api/users
Body: {"name": "Carol", "email": "carol@example.com"}
→ {"id": 3, "name": "Carol", "email": "carol@example.com"}

# Update user
PUT /api/users/1
Body: {"name": "Alice Smith"}
→ {"id": 1, "name": "Alice Smith", "email": "alice@example.com"}

# Delete user
DELETE /api/users/1
→ 204 No Content
```

**When REST works well:**
- Standard CRUD operations
- Clear resource hierarchy
- Caching is important
- Simplicity is valued

#### GraphQL

A query language that lets clients specify exactly what data they need.

**Example GraphQL query:**

```graphql
query {
  user(id: 1) {
    name
    email
    orders {
      id
      total
      items {
        productName
        quantity
      }
    }
  }
}
```

**Response:**
```json
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "orders": [
        {
          "id": 101,
          "total": 59.99,
          "items": [
            {"productName": "Widget", "quantity": 2}
          ]
        }
      ]
    }
  }
}
```

**When GraphQL works well:**
- Complex data requirements
- Multiple client types (mobile vs web needing different data)
- Rapid iteration on frontend
- Avoiding over-fetching/under-fetching

**Trade-offs:**

| Aspect | REST | GraphQL |
|--------|------|---------|
| Learning curve | Lower | Higher |
| Caching | Built into HTTP | More complex |
| Flexibility | Less (fixed endpoints) | More (client-specified) |
| Tooling | Mature | Growing |
| Performance | Predictable | Can have issues with complex queries |

### API Design Principles

Good APIs are **intuitive, consistent, and forgiving.**

#### 1. Use Intuitive Naming

```
# Good
GET /users
GET /users/123/orders
POST /orders

# Bad
GET /fetchUserData
GET /getOrdersByUserId
POST /createNewOrder
```

**Principles:**
- Nouns for resources, not verbs
- Plural for collections
- Lowercase with hyphens or underscores
- Consistent patterns throughout

#### 2. Design for the Common Case

Make simple things simple, complex things possible.

```
# Simple: Get my profile
GET /users/me

# Flexible: Get any user with specific fields
GET /users/123?fields=name,email,orders
```

#### 3. Return Useful Errors

```json
// Bad error
{"error": "Something went wrong"}

// Good error
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Email format is invalid",
    "field": "email",
    "details": "Must contain @ and valid domain"
  }
}
```

**Good error responses:**
- Have consistent structure
- Include error codes for programmatic handling
- Provide human-readable messages
- Indicate which field failed (for validation)

#### 4. Pagination for Lists

Never return unbounded lists.

```
GET /users?page=1&per_page=20

Response:
{
  "data": [...],
  "meta": {
    "total": 150,
    "page": 1,
    "per_page": 20,
    "total_pages": 8
  }
}
```

#### 5. Use Standard HTTP Status Codes

| Code | Meaning | Use For |
|------|---------|---------|
| 200 | OK | Successful GET, PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation errors |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limiting |
| 500 | Internal Error | Server problems |

### Platform Thinking

A **platform** is a product that others build on. Platform thinking creates exponential value.

```
Product: Users → Product → Value
Platform: Users → Product → Ecosystem → Exponential Value
                              ↓
                         Partners
                         Developers
                         Integrations
```

#### Product vs Platform

| Aspect | Product | Platform |
|--------|---------|----------|
| Value creation | Company builds features | Ecosystem builds features |
| Growth | Linear | Exponential (network effects) |
| Competition | Direct | Ecosystem competition |
| Example | Photoshop | Salesforce AppExchange |

#### Platform Elements

**APIs:** How external developers integrate
**SDKs:** Libraries that make API usage easier
**Webhooks:** Push notifications when events occur
**Documentation:** How developers learn
**Sandbox:** Safe environment to test
**App marketplace:** Distribution for ecosystem products

#### When to Think Platform

Platform investment makes sense when:
- Users want integrations you can't all build
- Partners can create value you can't
- Network effects are achievable
- You can sustain the ecosystem investment

### Developer Experience (DX)

DX is like UX, but for developers using your APIs/tools.

#### The DX Pyramid

```
                    △
                   ╱ ╲
                  ╱   ╲  DELIGHT
                 ╱     ╲  (great docs, helpful errors)
                ╱───────╲
               ╱         ╲  USABILITY
              ╱           ╲  (intuitive API, good defaults)
             ╱─────────────╲
            ╱               ╲  FUNCTIONALITY
           ╱                 ╲  (does what developers need)
          ╱───────────────────╲
         ╱                     ╲  RELIABILITY
        ╱                       ╲  (works consistently)
       ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
```

Must nail each level before the next matters.

#### DX Components

**Documentation:**
- Getting started guide (< 5 minutes to first success)
- Reference documentation (complete, accurate)
- Tutorials (common use cases)
- Examples (copy-paste code)

**Onboarding:**
- Easy signup and API key creation
- Sandbox environment
- Interactive console to try APIs
- Quick wins in first session

**Tooling:**
- SDKs for popular languages
- CLI tools
- IDE extensions
- Postman collections

**Support:**
- Status page
- Community forums
- Support channels
- Feedback mechanisms

#### Measuring DX

**Time to First Hello World (TTFHW):** How long from signup to first successful API call?
**Goal:** Under 5 minutes

**Developer NPS:** How likely are developers to recommend your API?

**API Error Rate:** What percentage of API calls fail?

**Documentation Coverage:** Are all endpoints documented with examples?

### API Versioning and Breaking Changes

APIs are contracts. Breaking them breaks trust.

#### What's a Breaking Change?

Changes that could break existing integrations:
- Removing an endpoint
- Removing a field from responses
- Changing field types
- Adding required parameters
- Changing authentication

**Non-breaking changes (usually safe):**
- Adding new endpoints
- Adding optional parameters
- Adding fields to responses
- Improving performance

#### Versioning Strategies

**URL versioning:**
```
/api/v1/users
/api/v2/users
```

Pros: Explicit, easy to understand
Cons: URL pollution, hard to sunset

**Header versioning:**
```
GET /api/users
Accept-Version: 2
```

Pros: Clean URLs
Cons: Less discoverable

**Query parameter:**
```
/api/users?version=2
```

Pros: Easy to test
Cons: Optional versions can cause confusion

#### Managing Breaking Changes

1. **Communicate early:** Announce deprecations well in advance (months, not days)
2. **Provide migration guides:** Show developers exactly what to change
3. **Sunset gradually:** Support old versions for a reasonable period
4. **Monitor adoption:** Track version usage to know when safe to remove
5. **Consider impact:** Breaking changes for 1000 developers vs. 10 require different approaches

### API Product Management

If your product includes APIs, they need PM attention.

#### API as Product Questions

- Who are the developer users?
- What are they trying to accomplish?
- How do we measure API success?
- What's the competitive landscape?
- How does API usage drive business value?

#### API Metrics to Track

| Metric | What It Tells You |
|--------|-------------------|
| API calls | Usage volume |
| Unique developers | Adoption breadth |
| Error rates | Quality and reliability |
| Latency | Performance |
| Time to first call | Onboarding effectiveness |
| Retention | Ongoing value |

---

## Key Takeaways

1. **APIs are products with developer users—they need design thinking and PM attention**
2. **REST is simpler and widely used; GraphQL offers flexibility for complex data needs**
3. **Good API design is intuitive, consistent, returns useful errors, and handles pagination**
4. **Platform thinking creates exponential value through ecosystems—consider APIs, SDKs, webhooks**
5. **Developer experience (DX) matters: documentation, onboarding, tooling, support**
6. **API versioning and breaking changes require careful management to maintain trust**

---

## Practice

### Reflection Questions
1. Think of an API you've used (Stripe, Twilio, Google Maps, etc.). What made the developer experience good or bad?
2. For a product you know well, what would it take to become a platform? Would it make sense?
3. How would you handle a situation where engineering wants to make a breaking API change to improve the architecture?

### Exercise
**API Design Review:**

You're asked to review an API design for a task management product. Evaluate this endpoint design:

```
POST /api/createTask
Body: {
  "taskName": "Buy groceries",
  "taskDescription": "Milk, eggs, bread",
  "assignedTo": "user_123",
  "dueDate": "2025-01-15"
}

Response: "Task created successfully"
```

1. Identify 3+ issues with this design
2. Propose improved endpoint design
3. Specify what the response should return
4. What error cases should be handled?

**Bonus:** Design the full CRUD API for tasks following REST conventions.

---

## Further Reading

- **"API Design Patterns" by JJ Geewax** - Comprehensive API design
- **Stripe's API documentation** - Gold standard for developer experience
- **"Platform Revolution" by Parker, Van Alstyne** - Platform business models
- **Twilio's API design guide** - Practical API design principles
- **GitHub's GraphQL API** - Well-designed GraphQL example
- **Postman State of the API Report** - Annual API industry insights
