# Technical Trade-offs

## Learning Objectives

- [ ] Understand technical debt and when to pay it down
- [ ] Make informed decisions about scalability investments
- [ ] Apply the build vs. buy framework
- [ ] Navigate security vs. speed trade-offs
- [ ] Facilitate technical trade-off discussions with engineering

## Prerequisites

- Completed: [01 - Tech Foundations](./01-tech-foundations.md)
- Completed: [02 - Working with Engineers](./02-working-with-engineers.md)

---

## Core Content

### The Nature of Technical Trade-offs

Every technical decision involves trade-offs. There's rarely a "right answer"—only answers that are better or worse for your specific context.

**Common trade-off axes:**
- Speed vs. Quality
- Flexibility vs. Simplicity
- Cost vs. Capability
- Now vs. Later
- Buy vs. Build

Your job as PM isn't to make these decisions alone—it's to ensure they're made deliberately with full context.

### Technical Debt

Technical debt is **the implied cost of additional rework caused by choosing an easy solution now instead of a better approach that would take longer.**

#### The Debt Metaphor

Like financial debt:
- **Principal:** The shortcut taken
- **Interest:** Ongoing cost (slower development, more bugs)
- **Paydown:** Refactoring to fix it

Unlike financial debt:
- Interest compounds unpredictably
- You can't always quantify the cost
- Some debt you never pay off (it just slows everything)

#### Types of Technical Debt

**Deliberate, Prudent:** "We know this isn't ideal, but we need to ship. We'll fix it next quarter."
- Conscious decision with a plan
- Often acceptable for market timing

**Deliberate, Reckless:** "We don't have time for design. Just make it work."
- Conscious decision without a plan
- Usually regretted

**Inadvertent, Prudent:** "Now we know how it should have been built."
- Learning revealed better approach
- Normal part of development

**Inadvertent, Reckless:** "What's layered architecture?"
- Lack of skill or knowledge
- Training/hiring issue

```
                  RECKLESS                    PRUDENT
           ┌────────────────────┬────────────────────┐
           │ "We don't have     │ "We must ship now  │
DELIBERATE │  time for design"  │  and deal with     │
           │                    │  consequences"     │
           ├────────────────────┼────────────────────┤
           │ "What's layered    │ "Now we know how   │
INADVERTENT│  architecture?"    │  it should have    │
           │                    │  been built"       │
           └────────────────────┴────────────────────┘
```

#### When to Take On Debt

Taking on technical debt can be the right choice when:

1. **Time-to-market matters more**
   - Competitive window closing
   - Customer commitment at stake
   - Revenue impact of delay exceeds refactor cost

2. **You're learning**
   - MVP validating assumptions
   - Better to build wrong thing quickly than right thing slowly
   - Plan to throw away if successful

3. **The debt is isolated**
   - Won't spread to other systems
   - Can be contained and addressed later

#### When to Pay Down Debt

Prioritize debt reduction when:

1. **Velocity is suffering**
   - "Simple" changes take forever
   - Engineers dread touching certain code
   - Bug rate is increasing

2. **It's blocking features**
   - New work requires the refactor anyway
   - Better to do it now than work around it

3. **Risk is increasing**
   - Security vulnerabilities
   - Scaling limits approaching
   - Key person dependency

#### PM's Role in Technical Debt

**Advocate for visibility:**
Engineering should surface debt; it shouldn't be hidden.

**Include in planning:**
Reserve capacity (10-20%) for debt reduction.

**Make trade-offs explicit:**
"If we take this shortcut, we're agreeing to pay it back in Q2."

**Don't micromanage:**
Trust engineering to identify what debt matters most.

### Scalability Decisions

Scalability is the system's ability to handle growth in users, data, or load.

#### Scaling Approaches

**Vertical scaling (scale up):**
Bigger server, more resources

```
Before:        After:
┌───────┐      ┌─────────────┐
│ Small │  →   │    Large    │
│ Server│      │   Server    │
└───────┘      └─────────────┘
```

- Simpler
- Has limits
- Can be expensive

**Horizontal scaling (scale out):**
More servers, distribute load

```
Before:         After:
┌───────┐       ┌───────┐
│Server │   →   │Server │ ┌───────┐ ┌───────┐
└───────┘       └───────┘ │Server │ │Server │
                          └───────┘ └───────┘
```

- More complex
- Near-unlimited scale
- Requires architectural support

#### When to Invest in Scale

**Too early:**
- Premature optimization
- Building for 1M users when you have 100
- Wasted effort if product fails

**Too late:**
- Site going down
- Customer complaints
- Scrambling during crisis

**Right time signals:**
- 50-70% of current capacity
- Known growth trajectory
- Competitive pressure

#### PM's Role in Scaling

**Provide growth projections:**
What usage do we expect in 6/12/24 months?

**Define acceptable trade-offs:**
Is 2-second load time okay? What about 5 seconds during peak?

**Prioritize scaling work:**
Is it more important than new features right now?

**Communicate constraints:**
"We can handle 10K concurrent users. Marketing needs to throttle launch."

### Build vs. Buy

Every capability can potentially be built in-house, bought from a vendor, or assembled from open source.

#### The Framework

| Factor | Build | Buy |
|--------|-------|-----|
| **Customization** | Exactly what you need | Compromises likely |
| **Time to value** | Longer | Faster |
| **Ongoing cost** | Maintenance burden | Subscription fees |
| **Core competency** | You own the expertise | Vendor dependency |
| **Competitive advantage** | Can differentiate | Competitors can buy same |

#### Decision Criteria

**Build when:**
- It's core to your differentiation
- Existing solutions don't fit
- You need deep customization
- Long-term cost of buying exceeds building
- You have the expertise

**Buy when:**
- It's commoditized (payments, email, auth)
- Speed to market matters
- You lack expertise
- It's not your differentiation
- Total cost of ownership favors it

**Examples:**

| Capability | Most Companies Should... | Exception |
|------------|-------------------------|-----------|
| Payment processing | Buy (Stripe, etc.) | PayPal, Square |
| Authentication | Buy or use framework | Auth company |
| Email sending | Buy (SendGrid, etc.) | Email company |
| Custom UI | Build | Commodity admin tools |
| Core algorithms | Build | If commodity |

#### Total Cost of Ownership

Don't just compare sticker prices:

**Build costs:**
- Development time
- Maintenance and bugs
- Infrastructure
- On-call burden
- Documentation
- Opportunity cost

**Buy costs:**
- License/subscription
- Integration development
- Training
- Vendor management
- Migration risk
- Customization limits

### Security vs. Speed Trade-offs

Security features often add friction or slow development.

#### Common Security Trade-offs

**Authentication requirements:**
- More secure: MFA required, session timeouts
- Faster UX: Remember me, long sessions

**Data validation:**
- More secure: Validate everything, sanitize inputs
- Faster development: Trust inputs, fix later

**Access controls:**
- More secure: Fine-grained permissions, audit logs
- Faster development: Simple roles, add complexity later

**Encryption:**
- More secure: Encrypt at rest and in transit
- Better performance: Less encryption overhead

#### PM's Role in Security

**Understand the threat model:**
What are we protecting? From whom? What's the impact of breach?

**Make risk-based decisions:**
Not all data is equal. Credit cards need more protection than marketing preferences.

**Advocate for users:**
Security shouldn't be so burdensome that users work around it.

**Include security in requirements:**
PRDs should address authentication, authorization, data protection.

### Facilitating Trade-off Discussions

As PM, you facilitate decisions—not dictate them.

#### The RAPID Framework

| Role | Who | Example |
|------|-----|---------|
| **R**ecommend | Engineering lead | "I recommend we use Postgres" |
| **A**gree | Security, Ops | Must sign off (can block) |
| **P**erform | Engineering team | Will implement |
| **I**nput | PM, Design, others | Provide context |
| **D**ecide | PM or Eng lead | Makes final call |

#### Effective Trade-off Conversations

1. **Frame the decision clearly**
   "We need to decide between approaches A and B for [problem]"

2. **Surface options with trade-offs**
   "Option A: [pros, cons]. Option B: [pros, cons]"

3. **Provide business context**
   "From product perspective, [X matters more than Y because...]"

4. **Listen to technical concerns**
   "Help me understand why you're concerned about..."

5. **Drive to decision**
   "Given what we've discussed, I'm recommending [X]. Any objections?"

6. **Document the decision**
   Record what was decided and why for future reference.

#### Example Trade-off Discussion

**Situation:** Building notification feature. Option A: Build custom. Option B: Use third-party service (OneSignal, Pusher).

**PM framing:**
"We need push notifications for iOS and Android. Engineering, can you walk us through the options?"

**Engineering input:**
"Option A (build): 3 weeks, full control, ~$500/month infrastructure, ongoing maintenance. Option B (buy): 1 week integration, $300/month at our scale, some limitations on customization."

**PM context:**
"We're under time pressure for the launch. Notifications aren't differentiating—users won't know or care how we implement them. The cost difference is minimal."

**Discussion:**
"What customization would we lose with Option B?"
"Mainly around delivery scheduling and complex user targeting. We can add that later if needed."

**Decision:**
"Let's go with Option B. We can revisit if we hit limitations. I'll document this decision so we remember the trade-offs we accepted."

---

## Key Takeaways

1. **Technical debt is unavoidable but should be deliberate—know what you're trading off**
2. **Scale too early = wasted effort; scale too late = crisis. Use growth projections to time investments**
3. **Build vs. buy depends on differentiation, speed needs, expertise, and total cost of ownership**
4. **Security trade-offs should be risk-based—not all data deserves the same protection level**
5. **PMs facilitate trade-off decisions by providing business context, not by dictating technical choices**
6. **Document decisions and their rationale—you'll thank yourself later**

---

## Practice

### Reflection Questions
1. Think of a product that clearly took on too much technical debt. What were the signs?
2. When have you seen a build vs. buy decision go wrong? What was missed?
3. How would you convince a CEO to invest in scaling infrastructure before it becomes critical?

### Exercise
**Trade-off Analysis:**

Your team needs to add search functionality to your app. You're deciding between:

**Option A: Build with Elasticsearch**
- 4-6 weeks development
- Full customization (fuzzy search, filters, ranking)
- $800/month infrastructure
- Ongoing maintenance needed
- Team has some Elasticsearch experience

**Option B: Use Algolia (SaaS)**
- 1-2 weeks integration
- Good customization, some limits
- $500/month at current scale, grows with usage
- No maintenance, vendor dependency
- Team has no Algolia experience

**Context:**
- Search is important but not core differentiator
- Launch in 2 months preferred
- Expected to grow 3x users next year
- Budget is available but not unlimited

**Your task:**
1. List pros/cons for each option
2. What questions would you ask engineering?
3. What additional context do you need?
4. What's your recommendation and why?
5. What would change your recommendation?

---

## Further Reading

- **"A Philosophy of Software Design" by John Ousterhout** - Complexity and trade-offs
- **"Designing Data-Intensive Applications" by Martin Kleppmann** - Scalability and system design
- **"The Art of Capacity Planning" by John Allspaw** - When to scale
- **"Staff Engineer" by Will Larson** - Technical leadership and decision-making
- **Martin Fowler's blog on Technical Debt** - Original articulation of the concept
