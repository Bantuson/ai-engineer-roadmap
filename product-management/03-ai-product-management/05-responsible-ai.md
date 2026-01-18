# Responsible AI

## Learning Objectives

- [ ] Understand the ethical dimensions of AI products
- [ ] Identify and mitigate bias in AI systems
- [ ] Design for AI safety (content safety, misuse prevention)
- [ ] Navigate explainability requirements
- [ ] Stay informed on AI regulations and compliance

## Prerequisites

- Completed: [01 - Why AI PM is Different](./01-why-ai-pm-different.md)
- Completed: [03 - Data Strategy](./03-data-strategy.md)

---

## Core Content

### Why Responsible AI Matters for PMs

AI products can cause real harm:
- Biased hiring systems rejecting qualified candidates
- Content moderation failing to catch harmful content
- AI assistants providing dangerous medical advice
- Surveillance systems enabling discrimination

**As a PM, you're accountable.** "The algorithm did it" isn't an acceptable answer.

**The business case is also clear:**
- Reputation damage from AI failures is severe and public
- Regulatory scrutiny is increasing globally
- Users are increasingly aware and demanding
- Employees want to work on ethical products

### The Responsible AI Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                     RESPONSIBLE AI                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │  FAIRNESS   │ │   SAFETY    │ │ TRANSPARENCY│ │ PRIVACY   │ │
│  │             │ │             │ │             │ │           │ │
│  │ No bias/    │ │ No harm to  │ │ Explainable │ │ Data      │ │
│  │ discrimination│ users/society│ │ & auditable │ │ protected │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └───────────┘ │
│                                                                 │
│                  ┌─────────────────────────┐                    │
│                  │     ACCOUNTABILITY      │                    │
│                  │                         │                    │
│                  │  Clear ownership and    │                    │
│                  │  mechanisms for redress │                    │
│                  └─────────────────────────┘                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Fairness: Bias Detection and Mitigation

AI bias isn't just a PR problem—it can cause real discrimination.

#### What Bias Looks Like

**Historical bias:**
Resume screening AI learned from past hiring decisions, which reflected human biases. Result: Penalized women candidates.

**Representation bias:**
Facial recognition trained on datasets with limited diversity. Result: Higher error rates for darker-skinned faces.

**Measurement bias:**
Recidivism prediction used arrest data as proxy for criminality. Result: Disproportionately flagged minorities (who are arrested at higher rates for same behaviors).

**Aggregation bias:**
Same model applied to different populations. Result: Medical AI less accurate for underrepresented groups.

#### Fairness Metrics

Different definitions of "fair" can conflict:

| Metric | Definition | Tension |
|--------|------------|---------|
| **Demographic parity** | Same positive rate across groups | May require different thresholds |
| **Equalized odds** | Same true/false positive rates across groups | May conflict with accuracy |
| **Individual fairness** | Similar individuals treated similarly | Defining "similar" is subjective |
| **Counterfactual fairness** | Decision wouldn't change if protected attribute changed | Often impossible to verify |

**The uncomfortable truth:** You can't satisfy all fairness definitions simultaneously. Choose based on context and values.

#### Bias Mitigation Strategies

**In data:**
- Audit training data for representation
- Remove or reduce biased features
- Collect more representative data
- Use fairness-aware sampling

**In modeling:**
- Add fairness constraints to training
- Use bias-aware algorithms
- Ensemble methods to reduce individual model biases

**In deployment:**
- Test across demographic groups before launch
- Monitor for disparate impact in production
- Implement appeals and human review processes
- Regular audits

#### PM Actions on Fairness

1. **Ask questions early:** "What groups could be negatively impacted?"
2. **Require testing:** Evaluate performance across demographics
3. **Document decisions:** Why we chose this fairness definition
4. **Plan for feedback:** How will affected users report issues?
5. **Own accountability:** Don't hide behind "the algorithm"

### Safety: Preventing Harm

AI safety encompasses preventing the system from causing harm.

#### Content Safety

For generative AI, preventing harmful outputs:

| Category | Examples | Mitigation |
|----------|----------|------------|
| **Violence** | Instructions for harm | Content filters, training |
| **Hate speech** | Slurs, discrimination | Safety training, detection |
| **Sexual content** | Explicit material | NSFW classifiers |
| **Misinformation** | False medical/legal advice | Disclaimers, citations |
| **Personal data** | Leaking training data | Output filtering |

**Safety layers:**
```
User Input → Input Filter → Model → Output Filter → User
              (Block bad      (Trained to   (Catch what
               requests)       be safe)      slipped through)
```

#### Misuse Prevention

Designing against intentional bad actors:

**Jailbreaking:** Users trying to bypass safety guidelines
- Red-team testing
- Prompt injection defenses
- Layered safety measures

**Automation of harm:** Using AI at scale for bad purposes
- Rate limiting
- Use case restrictions
- Monitoring for abuse patterns

**Impersonation:** AI pretending to be human
- Disclosure requirements
- Watermarking
- Authentication

#### Safety Testing

Before launch:
- **Red teaming:** Adversarial testing by internal or external teams
- **Automated probes:** Run thousands of known-bad prompts
- **Edge case exploration:** What happens with unusual inputs?

In production:
- **Monitoring:** Alert on safety-flagged outputs
- **User reports:** Clear reporting mechanism
- **Incident response:** Plan for when things go wrong

### Transparency: Explainability and Disclosure

Users and stakeholders deserve to understand AI systems.

#### Levels of Explainability

| Level | Description | Example |
|-------|-------------|---------|
| **No explanation** | Just output | "You were denied" |
| **Factor disclosure** | What inputs were used | "Based on credit score, income, employment" |
| **Feature importance** | Which factors mattered most | "Credit score was the primary factor" |
| **Counterfactual** | What would change the outcome | "With income above $X, you'd qualify" |
| **Full trace** | Complete reasoning chain | (Usually infeasible for complex models) |

**Appropriate level depends on:**
- Regulatory requirements (some decisions require explanation)
- User needs (will explanation help them?)
- Competitive concerns (don't reveal gaming strategies)
- Technical feasibility

#### AI Disclosure

Users should know when they're interacting with AI:

**Good practices:**
- Clear labeling ("AI-generated content")
- Bot identification in conversations
- Watermarking for AI content
- Transparency about limitations

**Bad practices:**
- AI pretending to be human
- Undisclosed AI decision-making
- Hidden automation in human-labeled processes

#### Model Documentation

**Model cards** document:
- What the model does
- Training data description
- Performance characteristics
- Known limitations
- Intended use cases
- Fairness analysis

**PM role:** Ensure documentation exists and is accurate.

### Privacy: Data Protection in AI

AI introduces unique privacy challenges.

#### Training Data Privacy

- Personal data in training sets
- Memorization of specific examples
- Inference of sensitive attributes

**Mitigations:**
- Anonymization and differential privacy
- Data minimization
- Consent for training use
- Right to removal requests

#### Inference Privacy

- What data is collected during use
- How inputs are stored and processed
- Who has access to user interactions

**PM questions:**
- Do we need to store user inputs?
- Are we using inputs for training?
- Have users consented to data use?
- How long do we retain data?

### Regulatory Landscape

AI regulation is evolving rapidly. Key frameworks:

#### EU AI Act (2024+)

- Risk-based regulation (unacceptable, high, limited, minimal risk)
- High-risk AI requires: transparency, human oversight, accuracy, security
- Prohibited: Social scoring, real-time biometric surveillance, manipulation

**PM impact:** Products in EU may need conformity assessments, registration, documentation.

#### US Approach

- Sector-specific regulation (FDA for medical, FTC for consumer protection)
- State laws emerging (CA, CO, IL have AI-related laws)
- Executive orders setting standards for federal AI use

**PM impact:** Monitor sector and state requirements for your specific product.

#### Global Considerations

- **China:** Specific rules for recommendation algorithms, deep synthesis
- **UK:** Pro-innovation approach with sector regulators
- **Canada, Brazil, others:** Various stages of AI legislation

**PM approach:**
- Know regulations for your markets
- Build compliance into product from start
- Document decisions for potential audits
- Engage legal and policy teams early

### Building Responsible AI into Product Development

#### Responsible AI Checklist

Before launch, verify:

**Fairness:**
- [ ] Identified potentially impacted groups
- [ ] Tested performance across demographics
- [ ] Documented fairness approach and trade-offs
- [ ] Established monitoring for disparate impact

**Safety:**
- [ ] Conducted red team testing
- [ ] Implemented content safety filters
- [ ] Created incident response plan
- [ ] Established user reporting mechanism

**Transparency:**
- [ ] Appropriate AI disclosure in UX
- [ ] Explainability meets use case requirements
- [ ] Model documentation completed
- [ ] User-facing limitations documented

**Privacy:**
- [ ] Data collection minimized
- [ ] User consent obtained where required
- [ ] Data retention policy defined
- [ ] Privacy impact assessment completed

**Accountability:**
- [ ] Clear ownership for AI system
- [ ] Appeal/override mechanism for affected users
- [ ] Audit trail for decisions
- [ ] Regular review cadence established

---

## Key Takeaways

1. **Responsible AI isn't optional—it's core to product development and PM accountability**
2. **Fairness requires proactive testing across groups and explicit trade-off decisions**
3. **Safety demands layered defenses: input filters, training, output filters, and monitoring**
4. **Transparency needs appropriate to context: disclosure, explainability, documentation**
5. **Privacy protections must cover training data and inference-time data handling**
6. **Regulations are evolving—stay informed and build compliance in from the start**

---

## Practice

### Reflection Questions
1. Have you experienced AI bias (in a product or reported in news)? What went wrong?
2. When should AI not be used for a decision, even if it's technically possible?
3. How would you handle a situation where improving model accuracy conflicted with fairness?

### Exercise
**Responsible AI Assessment:**

You're launching an AI feature that analyzes resumes and ranks candidates for recruiters.

Complete this responsible AI assessment:

1. **Fairness Analysis:**
   - What groups could be negatively impacted?
   - What fairness metric would you prioritize? Why?
   - What testing would you require before launch?

2. **Safety Considerations:**
   - What could go wrong?
   - What safety measures would you implement?

3. **Transparency Requirements:**
   - What explanation do candidates deserve?
   - What disclosure is needed for recruiters?
   - What documentation is required?

4. **Privacy Assessment:**
   - What data is collected?
   - Who has access?
   - What consent is needed?

5. **Accountability:**
   - Who is responsible if the system makes a biased decision?
   - How can candidates appeal?

---

## Further Reading

- **"Atlas of AI" by Kate Crawford** - Power and politics of AI
- **"Algorithms of Oppression" by Safiya Noble** - Bias in search algorithms
- **Anthropic's "Core Views on AI Safety"** - AI safety principles
- **NIST AI Risk Management Framework** - US government AI guidance
- **AI Now Institute Reports** - Annual analysis of AI's social implications
- **Partnership on AI** - Multi-stakeholder AI ethics
