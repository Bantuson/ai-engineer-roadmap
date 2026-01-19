# Tree-of-Thought Prompting

## Overview

Tree-of-Thought (ToT) extends chain-of-thought by exploring multiple reasoning branches simultaneously, enabling the model to evaluate, backtrack, and find optimal solution paths.

## ToT vs Chain-of-Thought

```
┌─────────────────────────────────────────────────────────────────┐
│              CHAIN-OF-THOUGHT vs TREE-OF-THOUGHT                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   CHAIN-OF-THOUGHT (Linear):                                    │
│   Problem → Step 1 → Step 2 → Step 3 → Answer                   │
│                                                                  │
│   TREE-OF-THOUGHT (Branching):                                  │
│                                                                  │
│                        Problem                                   │
│                           │                                      │
│              ┌────────────┼────────────┐                        │
│              ↓            ↓            ↓                        │
│           Branch A    Branch B     Branch C                     │
│              │            │            ✗ (dead end)             │
│         ┌────┴────┐      │                                      │
│         ↓         ↓      ↓                                      │
│       A.1       A.2     B.1                                     │
│         ✗        │       │                                      │
│                  ↓       ↓                                      │
│               A.2.1    B.1.1                                    │
│                  │       ✗                                      │
│                  ↓                                               │
│               Answer                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## When to Use ToT

| Best For | Not Ideal For |
|----------|---------------|
| Creative problem-solving | Simple factual questions |
| Game strategy | Direct computations |
| Planning tasks | Translation tasks |
| Design decisions | Classification |
| Puzzles and riddles | Text summarization |

## ToT Implementation Patterns

### Pattern 1: Explicit Branch Exploration

```
Solve this puzzle by exploring different approaches:

Puzzle: You have a 3-gallon jug and a 5-gallon jug. How do
you measure exactly 4 gallons of water?

BRANCH 1: Start by filling the 5-gallon jug
├── Step 1: Fill 5-gallon (5,0)
├── Step 2: Pour into 3-gallon (2,3)
├── Step 3: Empty 3-gallon (2,0)
├── Step 4: Pour 2 into 3-gallon (0,2)
├── Step 5: Fill 5-gallon (5,2)
├── Step 6: Pour into 3-gallon until full (4,3) ✓
└── SOLUTION FOUND: 4 gallons in 5-gallon jug

BRANCH 2: Start by filling the 3-gallon jug
├── Step 1: Fill 3-gallon (0,3)
├── Step 2: Pour into 5-gallon (3,0)
├── Step 3: Fill 3-gallon (3,3)
├── Step 4: Pour into 5-gallon until full (1,5)
├── Continue exploration...
└── Also reaches solution but more steps

Optimal solution: Branch 1 (6 steps)
```

### Pattern 2: Evaluation-Based Exploration

```
Design a logo for a tech startup. Explore three concepts and evaluate.

CONCEPT 1: Abstract geometric
├── Description: Interlocking hexagons in gradient blue
├── Strengths: Modern, scalable, versatile
├── Weaknesses: Common in tech, less memorable
└── Score: 7/10

CONCEPT 2: Letter-based mark
├── Description: Stylized company initial with circuit pattern
├── Strengths: Brand recognition, unique
├── Weaknesses: May not scale down well
└── Score: 6/10

CONCEPT 3: Symbolic representation
├── Description: Rising arrow formed by connected nodes
├── Strengths: Conveys growth, tech-forward
├── Weaknesses: Arrow motif is overused
└── Score: 7.5/10

Refinement of highest-scoring concept (CONCEPT 3):
├── Variation 3a: Simplify to 3 nodes
├── Variation 3b: Add subtle gradient
├── Variation 3c: Integrate company initial
└── Best variation: 3a (clean, memorable)

Final recommendation: Concept 3a - Simplified node-arrow
```

### Pattern 3: Iterative Deepening

```
Write an opening line for a thriller novel.

LEVEL 1 - Three initial directions:
A) "The phone call came at midnight."
B) "She hadn't expected to see her own face on the news."
C) "The last thing he remembered was the smell of chloroform."

EVALUATION:
A) Clichéd but effective hook - EXPLORE FURTHER
B) Intriguing mystery, unique - EXPLORE FURTHER
C) Too on-the-nose - PRUNE

LEVEL 2 - Expand promising branches:

Branch A refinements:
A1) "The phone call came at midnight, but the voice wasn't human."
A2) "The phone call came at midnight from a number that no longer existed."
A3) "The phone call came at midnight. It was her mother—who had been dead for three years."

Branch B refinements:
B1) "She hadn't expected to see her own face on the news—not until she committed a crime worth reporting."
B2) "She hadn't expected to see her own face on the news, especially not her own funeral."
B3) "She hadn't expected to see her own face on the news, staring back from a mugshot she'd never posed for."

FINAL EVALUATION:
- A3: Strong emotional hook, supernatural element ★★★★
- B2: Extremely intriguing, raises immediate questions ★★★★★
- B3: Mystery with identity thriller potential ★★★★

BEST: B2 - "She hadn't expected to see her own face on the
news, especially not her own funeral."
```

## Structured ToT Framework

### The MCTS-Inspired Pattern

```
Problem: [STATE PROBLEM]

# SELECTION - Choose promising branches to explore
Based on the problem, identify 3 high-potential approaches:
1. [Approach A]
2. [Approach B]
3. [Approach C]

# EXPANSION - Develop each approach
For each approach, generate 2-3 next steps:

Approach A:
├── Step A1: [action]
│   └── Evaluation: [promise/risk]
├── Step A2: [action]
│   └── Evaluation: [promise/risk]

[Repeat for B and C]

# SIMULATION - Project outcomes
For the most promising paths, simulate to completion:
Path [X]: [project final outcome]
Path [Y]: [project final outcome]

# BACKPROPAGATION - Update assessments
Based on simulated outcomes:
- Best path: [selected path]
- Reasoning: [why this is optimal]

# FINAL SOLUTION
[Present solution from best path]
```

### The Debate Pattern

```
Problem: Should our company adopt a 4-day work week?

PROPONENT BRANCH:
├── Argument 1: Increased productivity per hour
│   └── Evidence: Microsoft Japan study showed 40% boost
├── Argument 2: Better talent attraction
│   └── Evidence: 63% of job seekers prioritize flexibility
├── Argument 3: Reduced burnout
│   └── Evidence: 78% of 4-day workers report better work-life balance
└── Conclusion: Strong case for adoption

OPPONENT BRANCH:
├── Argument 1: Customer service coverage gaps
│   └── Evidence: 5 days of coverage still needed
├── Argument 2: Implementation complexity
│   └── Evidence: Requires significant process redesign
├── Argument 3: Not suitable for all roles
│   └── Evidence: Some positions require daily presence
└── Conclusion: Significant challenges exist

SYNTHESIS BRANCH:
├── Reconciliation: Hybrid approach
├── Proposal: 4-day week for suitable roles, flexibility for others
├── Mitigation: Staggered schedules for coverage
└── Recommendation: Pilot program with select teams

FINAL DECISION: Proceed with pilot, expand based on results
```

## ToT for Complex Planning

```
Plan a product launch for a new mobile app.

BRANCH 1: Viral Marketing Focus
├── Phase 1: Influencer partnerships (Week 1-2)
│   ├── Cost: $50K
│   ├── Expected reach: 500K
│   └── Risk: Dependent on influencer engagement
├── Phase 2: Referral program (Week 3-4)
│   ├── Cost: $20K incentives
│   ├── Expected signups: 50K
│   └── Risk: May attract low-quality users
└── Projected outcome: High volume, uncertain quality

BRANCH 2: PR & Media Focus
├── Phase 1: Press outreach (Week 1-2)
│   ├── Cost: $30K PR agency
│   ├── Expected coverage: 10 major outlets
│   └── Risk: No guaranteed coverage
├── Phase 2: Launch event (Week 3)
│   ├── Cost: $40K
│   ├── Expected attendees: 200 key stakeholders
│   └── Risk: High cost, one-time impact
└── Projected outcome: Credibility, targeted reach

BRANCH 3: Community-Building Focus
├── Phase 1: Beta community (Week 1-4)
│   ├── Cost: $10K community management
│   ├── Expected beta users: 1K highly engaged
│   └── Risk: Slow initial growth
├── Phase 2: User-generated content campaign
│   ├── Cost: $15K prizes/incentives
│   ├── Expected UGC: 500 pieces
│   └── Risk: Content quality varies
└── Projected outcome: Strong foundation, organic growth

EVALUATION MATRIX:
| Criteria      | Branch 1 | Branch 2 | Branch 3 |
|---------------|----------|----------|----------|
| Cost          | $70K     | $70K     | $25K     |
| Speed         | Fast     | Medium   | Slow     |
| Quality       | Low      | High     | High     |
| Sustainability| Low      | Medium   | High     |
| Risk          | High     | Medium   | Low      |

OPTIMAL PATH: Hybrid of Branch 2 + Branch 3
- Start with community building (low cost, high quality)
- Add PR push after community validation
- Skip pure viral tactics (low quality risk)
```

## Implementation Code Pattern

```python
def tree_of_thought_solve(problem, max_depth=3, branch_factor=3):
    """
    Solve problem using tree-of-thought exploration.
    """
    prompt = f"""
You are solving a problem using tree-of-thought reasoning.

Problem: {problem}

At each step:
1. Generate {branch_factor} distinct approaches
2. Evaluate each approach (score 1-10)
3. Expand the most promising branch
4. If a branch leads to dead end, backtrack
5. Continue until solution found or max depth reached

Current depth: 0
Max depth: {max_depth}

Begin exploration:
"""
    return call_llm(prompt)


def tot_with_evaluation(problem, evaluator):
    """
    ToT with separate evaluation function.
    """
    # Generate initial branches
    branches_prompt = f"""
Generate 3 different approaches to solve:
{problem}

For each approach, provide:
- Approach name
- Key steps
- Potential risks
- Estimated likelihood of success
"""
    branches = call_llm(branches_prompt)

    # Evaluate each branch
    for branch in parse_branches(branches):
        evaluation = evaluator(branch)
        if evaluation['score'] > 7:
            # Expand this branch
            expanded = expand_branch(branch, problem)
            # Continue recursive exploration...

    return best_solution
```

## Best Practices

1. **Define clear evaluation criteria** - Know how to judge branches
2. **Prune aggressively** - Don't explore obvious dead ends
3. **Limit depth** - Prevent infinite exploration
4. **Document backtracking** - Explain why branches were abandoned
5. **Synthesize at the end** - Combine insights from multiple branches

## Next Steps

- [02-react-prompting.md](02-react-prompting.md) - Reasoning with actions
- [03-prompt-chaining.md](03-prompt-chaining.md) - Multi-step workflows
