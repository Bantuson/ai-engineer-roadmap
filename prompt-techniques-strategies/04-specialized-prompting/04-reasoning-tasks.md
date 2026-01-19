# Reasoning Task Prompting

## Overview

Reasoning prompts tackle logical, mathematical, and analytical problems. This module covers techniques for guiding models through complex reasoning while maintaining accuracy.

## Reasoning Task Types

```
┌─────────────────────────────────────────────────────────────────┐
│                    REASONING CATEGORIES                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LOGICAL REASONING          MATHEMATICAL REASONING             │
│   ├── Deduction              ├── Arithmetic                    │
│   ├── Induction              ├── Algebra                       │
│   ├── Abduction              ├── Geometry                      │
│   └── Syllogisms             └── Statistics                    │
│                                                                  │
│   ANALYTICAL REASONING       CAUSAL REASONING                  │
│   ├── Comparison             ├── Cause and effect              │
│   ├── Classification         ├── Counterfactuals               │
│   ├── Pattern recognition    ├── Prediction                    │
│   └── Evaluation             └── Root cause analysis           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Logical Reasoning Prompts

### Deductive Reasoning

```
Solve this deductive reasoning problem:

PREMISES:
1. All mammals are warm-blooded.
2. All whales are mammals.
3. Warm-blooded animals need to regulate body temperature.

QUESTION: What can we conclude about whales?

APPROACH:
1. List all premises clearly
2. Identify the logical chain
3. Apply deductive rules step by step
4. State the conclusion
5. Verify the logic

SOLVE:
[Work through the deduction]

CONCLUSION:
[State what can be definitively concluded]

CONFIDENCE:
[High/Medium/Low - are there any logical gaps?]
```

### Syllogistic Reasoning

```
Analyze this syllogism:

ARGUMENT:
Premise 1: All successful companies have good leadership.
Premise 2: TechCorp has good leadership.
Conclusion: Therefore, TechCorp is a successful company.

ANALYSIS FRAMEWORK:
1. Identify the structure (major premise, minor premise, conclusion)
2. Check for valid syllogistic form
3. Test for fallacies
4. Determine if conclusion follows necessarily

EVALUATION:
- Valid form? [Yes/No + explanation]
- Sound argument? [Yes/No + explanation]
- Fallacy present? [Name and explain if yes]
- Correct conclusion? [What should it be, if different]
```

### Conditional Logic

```
Evaluate these conditional statements:

GIVEN:
- If it rains (R), the ground gets wet (W)
- If the ground is wet (W), it's slippery (S)
- It rained this morning

QUESTIONS:
1. Is the ground wet?
2. Is it slippery?
3. If the ground is dry, did it rain?
4. If it didn't rain, is the ground necessarily dry?

For each question:
- Identify the logical operation (modus ponens, modus tollens, etc.)
- Show the reasoning
- State the answer with certainty level

Format:
Q1: [Answer]
Logic: R → W, R is true, therefore W is true (modus ponens)
Certainty: Definite
```

## Mathematical Reasoning

### Word Problem Solving

```
Solve this word problem systematically:

PROBLEM:
{word_problem}

STRUCTURED APPROACH:

1. UNDERSTAND
   - What is being asked?
   - What information is given?
   - What are the unknowns?

2. PLAN
   - What mathematical concepts apply?
   - What equations or formulas are needed?
   - What's the solution strategy?

3. EXECUTE
   - Set up equations
   - Show all calculation steps
   - Track units throughout

4. VERIFY
   - Does the answer make sense?
   - Check by substitution
   - Verify units are correct

5. ANSWER
   - State final answer with units
   - Round appropriately if needed
```

### Statistical Reasoning

```
Analyze this statistical scenario:

DATA:
{statistical_data}

QUESTIONS:
1. What is the appropriate statistical test?
2. What are the null and alternative hypotheses?
3. Calculate the test statistic
4. Interpret the results

ANALYSIS:
1. Data characteristics:
   - Sample size
   - Distribution type
   - Independence assumptions

2. Test selection:
   - Why this test is appropriate
   - Assumptions being made

3. Calculation:
   - Step-by-step computation
   - Show all work

4. Interpretation:
   - Statistical significance
   - Practical significance
   - Limitations and caveats
```

### Optimization Problems

```
Solve this optimization problem:

PROBLEM:
{optimization_scenario}

APPROACH:

1. IDENTIFY
   - Objective function (what to maximize/minimize)
   - Decision variables
   - Constraints

2. FORMULATE
   - Mathematical expression of objective
   - Mathematical expression of constraints
   - Domain restrictions

3. SOLVE
   - Method selection (calculus, linear programming, etc.)
   - Step-by-step solution
   - Check boundary conditions

4. VERIFY
   - Is solution feasible?
   - Is it indeed optimal?
   - Sensitivity analysis

SOLUTION:
[Complete solution with all steps]
```

## Analytical Reasoning

### Comparison Analysis

```
Compare these options systematically:

OPTIONS:
A: {option_a}
B: {option_b}
C: {option_c}

COMPARISON FRAMEWORK:

1. CRITERIA IDENTIFICATION
   - What factors matter?
   - Weight each factor (1-5)

2. EVALUATION MATRIX
   | Criteria | Weight | A | B | C |
   |----------|--------|---|---|---|
   | [factor] | [1-5]  |   |   |   |

3. SCORING
   - Rate each option on each criterion (1-10)
   - Calculate weighted scores

4. ANALYSIS
   - Clear winner?
   - Trade-offs to consider
   - Sensitivity to weights

5. RECOMMENDATION
   - Best choice and why
   - When alternatives might be better
```

### Root Cause Analysis

```
Perform root cause analysis:

PROBLEM:
{observed_problem}

5 WHYS ANALYSIS:
Why 1: Why did [problem] occur?
→ [immediate cause]

Why 2: Why did [immediate cause] occur?
→ [deeper cause]

Why 3: Why did [deeper cause] occur?
→ [underlying cause]

Why 4: Why did [underlying cause] occur?
→ [systemic cause]

Why 5: Why did [systemic cause] occur?
→ [root cause]

FISHBONE DIAGRAM (Categories):
- People: [factors]
- Process: [factors]
- Equipment: [factors]
- Materials: [factors]
- Environment: [factors]
- Management: [factors]

ROOT CAUSES IDENTIFIED:
1. [Primary root cause]
2. [Secondary root cause]

RECOMMENDATIONS:
- Short-term fix: [action]
- Long-term solution: [action]
- Prevention: [action]
```

### Decision Analysis

```
Analyze this decision:

DECISION:
{decision_to_make}

FRAMEWORK:

1. STAKEHOLDER ANALYSIS
   - Who is affected?
   - What are their interests?
   - Who decides?

2. OPTION GENERATION
   - Option 1: [description]
   - Option 2: [description]
   - Option 3: [description]
   - Status quo: [description]

3. IMPACT ANALYSIS
   For each option:
   - Pros
   - Cons
   - Risks
   - Costs
   - Timeline

4. DECISION MATRIX
   | Factor | Weight | Opt 1 | Opt 2 | Opt 3 |
   |--------|--------|-------|-------|-------|

5. RECOMMENDATION
   - Recommended option
   - Key reasons
   - Implementation considerations
   - Contingency plan
```

## Causal Reasoning

### Cause-Effect Analysis

```
Analyze the causal relationships:

SCENARIO:
{scenario_description}

ANALYSIS:

1. IDENTIFY VARIABLES
   - Potential causes: [list]
   - Observed effects: [list]
   - Confounding factors: [list]

2. CAUSAL CHAINS
   [Cause A] → [Intermediate] → [Effect X]
   [Cause B] → [Effect Y]

3. EVIDENCE ASSESSMENT
   For each proposed cause:
   - Correlation present? [Yes/No]
   - Temporal precedence? [Yes/No]
   - Alternative explanations ruled out? [Yes/No]
   - Mechanism plausible? [Yes/No]

4. CONCLUSIONS
   - Strong causal claims: [list]
   - Probable causes: [list]
   - Needs more evidence: [list]
```

### Counterfactual Reasoning

```
Analyze this counterfactual:

ACTUAL OUTCOME:
{what_happened}

COUNTERFACTUAL QUESTION:
"What if {alternative_action} had happened instead?"

ANALYSIS:

1. IDENTIFY KEY DECISION POINT
   - When/where was the fork?
   - What were the alternatives?

2. TRACE CONSEQUENCES
   - Immediate effects of change
   - Second-order effects
   - Long-term trajectory

3. ASSESS LIKELIHOOD
   - How certain is the alternative outcome?
   - What assumptions are required?
   - What could still vary?

4. CONCLUSION
   - Most likely counterfactual outcome
   - Confidence level
   - Key uncertainties
```

## Best Practices

1. **Show all work** - Explicit reasoning improves accuracy
2. **Check logic** - Verify each step follows from previous
3. **Consider alternatives** - Don't anchor on first approach
4. **Quantify uncertainty** - Not all conclusions are equally certain
5. **Verify answers** - Always check results make sense

## Next Steps

- [../05-optimization/01-prompt-debugging.md](../05-optimization/01-prompt-debugging.md) - Debugging prompts
- [../05-optimization/02-iterative-refinement.md](../05-optimization/02-iterative-refinement.md) - Improving prompts
