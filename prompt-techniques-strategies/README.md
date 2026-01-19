# Prompt Techniques & Strategies

A comprehensive guide to prompt engineering for AI systems.

## Purpose

This course provides reading material for understanding and mastering prompt engineering techniques. Use these materials alongside hands-on practice in the `learning-workflow/prompt-drills/` exercises.

## Course Structure

```
prompt-techniques-strategies/
├── 01-prompting-fundamentals/     # Core concepts
│   ├── 01-anatomy-of-prompts.md   # Components, structure, formatting
│   ├── 02-instruction-clarity.md  # Clear directions, constraints
│   └── 03-context-setting.md      # Background, personas, framing
│
├── 02-core-techniques/            # Essential methods
│   ├── 01-zero-shot-prompting.md  # Direct instructions
│   ├── 02-few-shot-prompting.md   # Learning from examples
│   ├── 03-chain-of-thought.md     # Step-by-step reasoning
│   └── 04-self-consistency.md     # Multiple reasoning paths
│
├── 03-advanced-strategies/        # Complex patterns
│   ├── 01-tree-of-thought.md      # Branching reasoning
│   ├── 02-react-prompting.md      # Reasoning + Acting
│   ├── 03-prompt-chaining.md      # Multi-step workflows
│   └── 04-meta-prompting.md       # Prompts generating prompts
│
├── 04-specialized-prompting/      # Domain-specific
│   ├── 01-code-generation.md      # Programming prompts
│   ├── 02-creative-writing.md     # Storytelling, content
│   ├── 03-data-extraction.md      # Structured output
│   └── 04-reasoning-tasks.md      # Logic, math, analysis
│
├── 05-optimization/               # Improving prompts
│   ├── 01-prompt-debugging.md     # Finding/fixing issues
│   ├── 02-iterative-refinement.md # Systematic improvement
│   └── 03-evaluation-metrics.md   # Measuring effectiveness
│
└── prompt-library/                # Ready-to-use prompts
    ├── agent-design-prompts.md    # 20+ agent design prompts
    ├── security-prompts.md        # 20+ security prompts
    └── evaluation-prompts.md      # 20+ eval prompts
```

## Learning Path

### Week 1: Foundations
- **Day 1-2**: Module 01 - Prompting Fundamentals
- **Day 3-4**: Module 02 - Core Techniques
- **Day 5**: Practice with prompt-library examples

### Week 2: Advanced
- **Day 1-2**: Module 03 - Advanced Strategies
- **Day 3-4**: Module 04 - Specialized Prompting
- **Day 5**: Apply techniques to real projects

### Week 3: Mastery
- **Day 1-2**: Module 05 - Optimization
- **Day 3-5**: Create your own prompt library

## Key Concepts

### The Prompt Engineering Equation

```
Effective Prompt = Clear Task + Relevant Context + Output Format + Examples
```

### Quality Dimensions

1. **Clarity** - Unambiguous instructions
2. **Specificity** - Precise requirements
3. **Context** - Relevant background
4. **Examples** - Concrete demonstrations
5. **Constraints** - Defined boundaries

## Integration with Other Courses

| Course | Prompt Focus |
|--------|--------------|
| Agent Frameworks | Agent design prompts |
| Vulnerabilities | Security-aware prompting |
| Evals | Evaluation prompts |
| Product Management | PRD and feature prompts |

## Quick Reference

### Prompt Template

```
[ROLE/PERSONA]
You are a [expert type] with expertise in [domain].

[CONTEXT]
Background: [relevant information]
Constraints: [limitations or requirements]

[TASK]
Your task is to [specific action].

[OUTPUT FORMAT]
Provide your response as:
- [format specification]
- [structure requirements]

[EXAMPLES] (optional)
Example input: [sample]
Example output: [sample]
```

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| Zero-shot | Simple, well-defined tasks |
| Few-shot | Tasks needing examples |
| Chain-of-thought | Complex reasoning |
| ReAct | Tool-using agents |
| Tree-of-thought | Exploration problems |

## Resources

- Practice drills: `learning-workflow/prompt-drills/`
- Agent examples: `agent-frameworks/mini-projects/`
- Eval scripts: `evals/scripts/`

## Next Steps

Start with [01-prompting-fundamentals/01-anatomy-of-prompts.md](01-prompting-fundamentals/01-anatomy-of-prompts.md)
