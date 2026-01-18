# Production Prompts

## Learning Objectives

- [ ] Understand how production prompts differ from casual prompting
- [ ] Design system prompts for AI features
- [ ] Implement prompt versioning and A/B testing
- [ ] Collaborate with engineering on prompt development
- [ ] Manage prompt maintenance and improvement

## Prerequisites

- Completed: [01 - Prompt Fundamentals](./01-prompt-fundamentals.md)
- Completed: [03-AI Product Management module](../03-ai-product-management/) (recommended)

---

## Core Content

### Production Prompts Are Different

Casual prompting (your daily AI use):
- One-off interactions
- Tolerance for inconsistency
- Easy to iterate in real-time
- Only you see the output

Production prompts (shipping to users):
- Thousands to millions of executions
- Consistency is critical
- Changes affect all users
- Quality at scale matters

**This changes everything about how you develop prompts.**

### The Anthropic PM Role: A Case Study

Anthropic's PM role ($320k-$405k) focuses on production prompts:

> "Writing system prompts for each Claude model release, creating meta-prompts for research pipelines, reviewing prompt changes from product teams, leading response to behavioral issues in production"

This is the bleeding edge of PM work—treating prompts as products.

### Anatomy of a Production Prompt

Production prompts have distinct components:

```
┌─────────────────────────────────────────────────────────────────┐
│                      SYSTEM PROMPT                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ IDENTITY & ROLE                                           │ │
│  │ Who is the AI? What's its purpose?                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ BEHAVIORAL GUIDELINES                                      │ │
│  │ How should it behave? What's the tone?                    │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ CAPABILITIES & LIMITATIONS                                 │ │
│  │ What can/can't it do? When should it decline?             │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ OUTPUT FORMAT                                              │ │
│  │ How should responses be structured?                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ SAFETY RAILS                                               │ │
│  │ What should trigger refusal or escalation?                 │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      USER MESSAGE                               │
│  [Dynamic: user input + context variables]                      │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      MODEL RESPONSE                             │
│  [Output following system prompt guidelines]                    │
└─────────────────────────────────────────────────────────────────┘
```

### Writing System Prompts

#### Section 1: Identity & Role

Define who the AI is in your product:

```
You are a customer support assistant for Acme Corp, a project
management software company.

Your name is "Acme Assistant" and you help users with:
- Understanding product features
- Troubleshooting common issues
- Finding documentation and resources

You are helpful, professional, and knowledgeable about Acme's
products but cannot access user accounts or make changes.
```

**Key decisions:**
- Named persona or generic assistant?
- First person ("I") or third person?
- Expert or helpful guide?

#### Section 2: Behavioral Guidelines

Set the interaction style:

```
Communication style:
- Be concise and direct; users are busy professionals
- Use clear, jargon-free language
- Lead with the answer, then provide details if needed
- Acknowledge user frustration without being defensive

When uncertain:
- Be honest about limitations
- Offer to escalate to human support
- Never make up product features or policies

Avoid:
- Marketing language or upselling
- Excessive enthusiasm or emojis
- Lengthy responses when short ones suffice
```

#### Section 3: Capabilities & Limitations

Be explicit about what the AI can and cannot do:

```
You CAN:
- Answer questions about product features
- Explain how to use the product
- Troubleshoot common issues using the knowledge base
- Provide documentation links
- Escalate to human support

You CANNOT:
- Access or modify user accounts
- Process refunds or billing changes
- Make promises about future features
- Provide legal, financial, or medical advice
- Access information outside your knowledge base

If asked about something outside your capabilities, clearly explain
what you can't do and suggest the appropriate alternative (usually
contacting human support).
```

#### Section 4: Output Format

Specify response structure:

```
Response formatting:
- Keep responses under 200 words unless detail is necessary
- Use bullet points for steps or lists
- Include relevant documentation links when helpful
- End with "Is there anything else I can help with?" only if the
  conversation feels incomplete

For troubleshooting:
1. Acknowledge the issue
2. Provide numbered steps to resolve
3. Offer escalation if steps don't work

Example response format:
"[Brief acknowledgment of issue]

To resolve this:
1. [Step one]
2. [Step two]
3. [Step three]

If this doesn't help, I can connect you with our support team."
```

#### Section 5: Safety Rails

Define boundaries and escalations:

```
Safety and escalation:
- If a user expresses frustration or asks to speak to a human,
  immediately offer to connect them with support
- Never argue with users or tell them they're wrong
- If asked about competitors, remain neutral and factual
- Decline requests that seem malicious or abusive

Immediate escalation triggers:
- User mentions legal action
- User reports data loss or security concerns
- User uses profanity or abusive language
- Request involves account access or billing

Escalation response:
"I understand this is important. Let me connect you with our
support team who can better assist you. [Provide contact info
or transfer mechanism]"
```

### Prompt Variables

Production prompts include dynamic elements:

```
System prompt:
You are a customer support assistant for {{company_name}}.

The user you're helping is:
- Name: {{user_name}}
- Account type: {{account_type}}
- Tenure: {{account_age_months}} months

Context from their account:
{{relevant_account_context}}

Previous messages in this conversation:
{{conversation_history}}
```

**Variable considerations:**
- What context improves responses?
- What's the token cost of added context?
- Privacy: what data should/shouldn't be included?
- Freshness: how current does context need to be?

### Prompt Versioning

Treat prompts like code:

```
prompts/
├── customer_support/
│   ├── v1.0.0_2024-01-15/
│   │   ├── system_prompt.txt
│   │   ├── config.json
│   │   └── eval_results.json
│   │
│   ├── v1.1.0_2024-02-01/
│   │   ├── system_prompt.txt
│   │   ├── config.json
│   │   ├── eval_results.json
│   │   └── changelog.md
│   │
│   └── v1.2.0_2024-03-15/
│       └── ...
```

**Version tracking includes:**
- The prompt itself
- Configuration (model, temperature, etc.)
- Evaluation results
- What changed and why
- Rollback instructions

### A/B Testing Prompts

Test prompt changes before full rollout:

#### What to Test

| Element | Testable Change | Example |
|---------|-----------------|---------|
| Tone | Formal vs. casual | "I'd be happy to help" vs. "Sure!" |
| Length | Verbose vs. concise | Detailed steps vs. brief pointers |
| Structure | Different formats | Bullets vs. paragraphs |
| Instructions | Different emphasis | Safety-first vs. helpful-first |

#### A/B Testing Process

1. **Hypothesis:** "A more concise prompt will improve user satisfaction"

2. **Metrics:**
   - Primary: User satisfaction rating
   - Secondary: Task completion rate
   - Guardrail: Safety incident rate

3. **Test design:**
   - 50/50 split
   - Random assignment by user or session
   - Sufficient sample size (power analysis)

4. **Duration:**
   - Enough time for statistical significance
   - Enough variety of use cases

5. **Analysis:**
   - Statistical significance of primary metric
   - Check guardrails aren't violated
   - Segment analysis (does it help some users but hurt others?)

### PM-Engineering Collaboration

Prompt development involves both PM and engineering:

#### PM Responsibilities

- Define behavior requirements
- Write initial prompt drafts
- Create evaluation criteria
- Review output quality
- Prioritize improvements

#### Engineering Responsibilities

- Implement prompt infrastructure
- Manage context variables
- Handle edge cases and errors
- Build evaluation pipelines
- Deploy and monitor

#### Collaboration Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROMPT DEVELOPMENT CYCLE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PM                              Engineering                    │
│  ──                              ───────────                    │
│                                                                 │
│  Define requirements ──────────────────▶                        │
│                                                                 │
│  Draft prompt ──────────────────────────▶                       │
│                                                                 │
│  ◀────────────────────────── Technical review                   │
│                                                                 │
│  Create eval cases ─────────────────────▶                       │
│                                                                 │
│  ◀────────────────────────── Implement pipeline                 │
│                                                                 │
│  Review results ────────────────────────▶                       │
│                                                                 │
│  Approve for deploy ────────────────────▶                       │
│                                                                 │
│  ◀────────────────────────── Deploy + monitor                   │
│                                                                 │
│  ◀────────────────────────── Report issues                      │
│                                                                 │
│  Prioritize fixes ──────────────────────▶                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Prompt Maintenance

Production prompts require ongoing work:

#### Regular Reviews

- **Weekly:** Check metrics and alerts
- **Monthly:** Review user feedback and edge cases
- **Quarterly:** Comprehensive quality audit

#### Common Maintenance Tasks

| Task | Trigger | Action |
|------|---------|--------|
| Bug fix | User reports bad behavior | Patch prompt, test, deploy |
| Coverage | New use case emerges | Expand prompt, add examples |
| Performance | Latency or cost concerns | Optimize prompt length |
| Model update | New model available | Test, potentially revise |
| Brand update | Tone/voice changes | Update style guidelines |

#### Incident Response

When a prompt produces harmful or incorrect output:

1. **Detect:** Monitoring, user reports, internal discovery
2. **Assess:** Severity, scope, root cause
3. **Mitigate:** Quick fix or rollback
4. **Fix:** Proper solution with testing
5. **Prevent:** Update evals to catch similar issues

---

## Key Takeaways

1. **Production prompts differ from casual prompts—they need consistency, safety, and scalability**
2. **System prompts include: identity, behavioral guidelines, capabilities, format, and safety rails**
3. **Use variables for dynamic context but be mindful of tokens and privacy**
4. **Version prompts like code—track changes, evaluate results, enable rollback**
5. **A/B test prompt changes before full rollout to validate improvements**
6. **Establish clear PM-engineering collaboration on prompt development**
7. **Maintain prompts continuously—they're never "done"**

---

## Practice

### Exercise 1: Write a System Prompt

Create a complete system prompt for this scenario:

**Product:** A recipe suggestion app
**Feature:** AI that suggests recipes based on ingredients the user has
**Constraints:**
- Should not give medical/dietary advice
- Should note common allergens
- Should be friendly and encouraging

Write all five sections:
1. Identity & Role
2. Behavioral Guidelines
3. Capabilities & Limitations
4. Output Format
5. Safety Rails

### Exercise 2: Design an A/B Test

You want to test whether a more conversational tone improves engagement.

Current prompt excerpt:
> "Based on your query, here are the relevant support articles..."

Proposed change:
> "Great question! I found some articles that should help..."

Design the A/B test:
1. Hypothesis
2. Metrics (primary, secondary, guardrail)
3. Test design
4. Duration
5. Success criteria

### Exercise 3: Incident Response

Scenario: Your AI assistant started recommending a competitor's product when asked about pricing.

Walk through:
1. How would you detect this?
2. How would you assess severity?
3. What's your immediate mitigation?
4. How would you fix it properly?
5. How would you prevent recurrence?

---

## Further Reading

- **Anthropic's System Prompt Documentation** - Official guidance
- **OpenAI's Production Best Practices** - Deployment patterns
- **"Building LLM Applications for Production" (Chip Huyen)** - Comprehensive overview
- **LangChain/LangSmith documentation** - Tooling for prompt management
- **PromptLayer** - Prompt versioning and tracking
