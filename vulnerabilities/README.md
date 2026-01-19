# AI Security & Vulnerabilities Course

A comprehensive course on AI security, covering attack vectors, defense strategies, and red teaming for AI systems.

## Course Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 15-20 hours |
| **Prerequisites** | Basic understanding of LLMs and agents |
| **Outcomes** | Identify, test, and defend against AI vulnerabilities |

## Why AI Security Matters

AI systems face unique security challenges:
- **Non-deterministic** - Hard to predict all behaviors
- **Natural language** - Vulnerable to linguistic attacks
- **Context-dependent** - Behavior changes with input
- **Opaque** - Difficult to audit decisions

## Course Structure

```
vulnerabilities/
├── 01-threat-landscape/
│   ├── 01-ai-security-overview.md
│   └── 02-attack-surface-mapping.md
├── 02-prompt-injection/
│   ├── 01-injection-fundamentals.md
│   ├── 02-direct-indirect-attacks.md
│   ├── 03-defense-strategies.md
│   └── mini-project-injection-lab/
├── 03-jailbreaking/
│   ├── 01-jailbreak-techniques.md
│   ├── 02-guardrail-bypasses.md
│   └── 03-defense-mechanisms.md
├── 04-data-model-security/
│   ├── 01-data-poisoning-leakage.md
│   ├── 02-model-extraction.md
│   └── 03-adversarial-attacks.md
├── 05-defense-strategies/
│   ├── 01-input-output-validation.md
│   ├── 02-rate-limiting-monitoring.md
│   └── mini-project-secure-agent/
├── 06-ai-red-teaming/
│   ├── 01-red-team-methodology.md
│   ├── 02-attack-playbooks.md
│   └── capstone-red-team-exercise/
└── attack-library/
    ├── injection-examples.md
    ├── jailbreak-examples.md
    └── defense-patterns.md
```

## Module Overview

### Module 1: Threat Landscape
- Understanding AI-specific threats
- Mapping attack surfaces
- Risk assessment frameworks

### Module 2: Prompt Injection
- Direct and indirect injection attacks
- Real-world examples
- Defense mechanisms

### Module 3: Jailbreaking
- Techniques to bypass safety measures
- Guardrail circumvention
- Building robust defenses

### Module 4: Data & Model Security
- Training data poisoning
- Data leakage prevention
- Model extraction attacks

### Module 5: Defense Strategies
- Input/output validation
- Monitoring and rate limiting
- Building secure agents

### Module 6: AI Red Teaming
- Methodology for testing AI systems
- Attack playbooks
- Capstone exercise

## Key Topics

### Attack Categories

| Category | Description | Severity |
|----------|-------------|----------|
| Prompt Injection | Manipulate LLM via input | High |
| Jailbreaking | Bypass safety guardrails | High |
| Data Poisoning | Corrupt training/retrieval data | Medium |
| Data Leakage | Extract sensitive information | High |
| Model Extraction | Steal model capabilities | Medium |
| DoS | Overwhelm with resource usage | Medium |

### Defense Principles

1. **Defense in Depth** - Multiple layers of protection
2. **Least Privilege** - Minimize agent capabilities
3. **Input Validation** - Sanitize all inputs
4. **Output Filtering** - Check before responding
5. **Monitoring** - Detect anomalies
6. **Rate Limiting** - Prevent abuse

## Quick Start

1. **Understand threats** - Start with Module 1
2. **Learn attacks** - Modules 2-3 cover main vectors
3. **Practice defense** - Module 5 has hands-on exercises
4. **Test systems** - Module 6 for red teaming

## Ethical Guidelines

This course is for **defensive purposes**:
- ✅ Testing your own systems
- ✅ Authorized security assessments
- ✅ Learning to build safer AI
- ❌ Attacking systems without permission
- ❌ Causing harm or damage
- ❌ Distributing malicious tools

## Related Resources

- [Evals Course](../evals/) - Testing AI quality
- [Agent Design Patterns](../ai-agent-design-patterns/)
- [Mini-Projects](../agent-frameworks/mini-projects/)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
