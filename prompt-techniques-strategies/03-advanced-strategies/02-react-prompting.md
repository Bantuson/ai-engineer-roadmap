# ReAct Prompting

## Overview

ReAct (Reasoning + Acting) combines reasoning traces with action execution, enabling models to interleave thinking with tool use, searches, or other external actions.

## The ReAct Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                       REACT LOOP                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐               │
│   │  THOUGHT │ ──→ │  ACTION  │ ──→ │OBSERVATION│              │
│   │ (Reason) │     │ (Execute)│     │ (Result)  │              │
│   └──────────┘     └──────────┘     └──────────┘               │
│        ↑                                   │                    │
│        └───────────────────────────────────┘                    │
│                    (Repeat until done)                          │
│                                                                  │
│   THOUGHT: What do I need to do next?                           │
│   ACTION: [tool_name](parameters)                               │
│   OBSERVATION: [result of action]                               │
│   THOUGHT: Based on observation, next I should...               │
│   ...                                                           │
│   FINAL ANSWER: [conclusion]                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## ReAct Format

### Basic ReAct Structure

```
Question: What is the population of the capital of France?

Thought 1: I need to find the capital of France first.
Action 1: Search[capital of France]
Observation 1: The capital of France is Paris.

Thought 2: Now I need to find the population of Paris.
Action 2: Search[population of Paris]
Observation 2: The population of Paris is approximately 2.1 million
in the city proper, or 12 million in the metropolitan area.

Thought 3: I have the answer. The question asks about the capital's
population, so I'll provide both figures for completeness.
Final Answer: The population of Paris, the capital of France, is
approximately 2.1 million (city proper) or 12 million (metro area).
```

### ReAct with Multiple Tools

```
Available Tools:
- Search[query]: Search the web for information
- Calculate[expression]: Perform mathematical calculation
- Lookup[term]: Look up a specific term in knowledge base

Question: How much would it cost to buy 15 copies of the
best-selling book of 2024 at full retail price?

Thought 1: I need to find what the best-selling book of 2024 is.
Action 1: Search[best-selling book 2024]
Observation 1: "Fourth Wing" by Rebecca Yarros was among the
top sellers in 2024, with a retail price of $29.99.

Thought 2: Now I can calculate the total cost for 15 copies.
Action 2: Calculate[15 * 29.99]
Observation 2: 449.85

Thought 3: I have all the information needed.
Final Answer: Buying 15 copies of "Fourth Wing" at full retail
price ($29.99 each) would cost $449.85.
```

## ReAct Prompt Template

```
You are an assistant that solves problems by reasoning step-by-step
and taking actions when needed.

Available actions:
{list of tools with descriptions}

Format your response as:
Thought: [your reasoning about what to do next]
Action: [tool_name][parameters]
Observation: [you will receive the result here]
... (repeat as needed)
Final Answer: [your final response]

Important rules:
1. Always think before acting
2. Use observations to inform next steps
3. If an action fails, reason about alternatives
4. Provide a clear final answer when done

Question: {user_question}
```

## ReAct for Different Tasks

### Research Task

```
Question: Compare the market caps of Apple and Microsoft as of today.

Thought 1: I need current market cap data for both companies.
Let me start with Apple.
Action 1: Search[Apple market cap 2024]
Observation 1: Apple's market cap is approximately $2.9 trillion.

Thought 2: Now I need Microsoft's current market cap.
Action 2: Search[Microsoft market cap 2024]
Observation 2: Microsoft's market cap is approximately $3.0 trillion.

Thought 3: I have both figures. Let me compare them.
Action 3: Calculate[3.0 - 2.9]
Observation 3: 0.1

Thought 4: Microsoft is ahead by about $100 billion.
Final Answer: As of 2024, Microsoft's market cap (~$3.0T) slightly
exceeds Apple's (~$2.9T) by approximately $100 billion. Microsoft
currently holds the position of most valuable public company.
```

### Code Debugging Task

```
Question: Debug this Python function that should return the
second largest number in a list.

def second_largest(nums):
    nums.sort()
    return nums[-2]

Thought 1: Let me analyze the function and test with edge cases.
Action 1: Execute[second_largest([1, 2, 3, 4, 5])]
Observation 1: Returns 4. Correct for this case.

Thought 2: Let me test with duplicates.
Action 2: Execute[second_largest([5, 5, 5, 5])]
Observation 2: Returns 5. This might not be the intended behavior
if we want the second largest unique value.

Thought 3: Let me test with a small list.
Action 3: Execute[second_largest([1])]
Observation 3: IndexError: list index out of range

Thought 4: I've identified two issues:
1. Doesn't handle lists shorter than 2 elements
2. Doesn't handle duplicate maximum values

Final Answer: The function has two bugs:
1. No check for list length < 2 (causes IndexError)
2. With duplicates, it returns the same value as max

Fixed version:
def second_largest(nums):
    if len(nums) < 2:
        return None
    unique = list(set(nums))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]
```

### Planning Task

```
Question: Plan a 3-day trip to Tokyo for a food enthusiast.

Thought 1: I should gather information about top food
experiences in Tokyo.
Action 1: Search[best food experiences Tokyo]
Observation 1: Top experiences include Tsukiji Outer Market,
ramen shops in various neighborhoods, depachika (department
store basements), izakaya in Yurakucho, and sushi at Ginza.

Thought 2: I should check which areas to focus on for each day.
Action 2: Search[Tokyo food neighborhoods map]
Observation 2: Key areas: Tsukiji/Ginza (seafood), Shinjuku
(ramen, izakaya), Shibuya (trendy), Asakusa (traditional).

Thought 3: Now I can structure a 3-day itinerary.
Action 3: Search[Tokyo restaurant reservations needed]
Observation 3: High-end sushi requires months of advance
booking. Ramen shops are walk-in. Some izakayas take same-day.

Thought 4: I have enough information to create the plan.
Final Answer:

**Day 1: Tsukiji & Ginza (Seafood Focus)**
- Morning: Tsukiji Outer Market for fresh sushi breakfast
- Lunch: Walk through depachika at Ginza Mitsukoshi
- Dinner: Mid-range sushi at a Ginza restaurant (book ahead)

**Day 2: Shinjuku & Shibuya (Modern Scene)**
- Morning: Coffee at a kissaten (traditional coffee house)
- Lunch: Ramen crawl in Shinjuku (Fuunji, Ichiran)
- Dinner: Izakaya hopping under the Yurakucho tracks

**Day 3: Asakusa & Neighborhood Gems**
- Morning: Senso-ji temple area street food
- Lunch: Unagi (eel) at a traditional restaurant
- Afternoon: Depachika sweets tasting
- Dinner: Monjayaki in Asakusa

Tips: Book Ginza sushi 2+ weeks ahead. Arrive at Tsukiji by 7am.
```

## Advanced ReAct Patterns

### ReAct with Self-Correction

```
Question: What percentage of Earth's surface is covered by water?

Thought 1: Let me search for this information.
Action 1: Search[percentage Earth surface water]
Observation 1: About 71% of Earth's surface is covered by water.

Thought 2: I should verify this with another source.
Action 2: Search[Earth ocean coverage percentage NASA]
Observation 2: NASA states oceans cover about 71% of Earth's surface.

Thought 3: Both sources agree. The answer is reliable.
Final Answer: Approximately 71% of Earth's surface is covered
by water (primarily oceans).
```

### ReAct with Error Handling

```
Question: Find the CEO of the company that made GPT-4.

Thought 1: GPT-4 was made by OpenAI. Let me find their CEO.
Action 1: Search[OpenAI CEO]
Observation 1: Sam Altman is the CEO of OpenAI.

Thought 2: I should verify this is current information.
Action 2: Search[Sam Altman OpenAI 2024]
Observation 2: Sam Altman returned as CEO of OpenAI in late 2023
after a brief departure.

Thought 3: The information is current and verified.
Final Answer: Sam Altman is the CEO of OpenAI, the company
that created GPT-4.
```

### Multi-Agent ReAct

```
You are coordinating multiple specialist agents to answer:
"Design a sustainable packaging solution for food delivery."

Thought 1: I need input from multiple domains.

Action 1: Ask[MaterialsExpert, "sustainable packaging materials for food"]
Observation 1: Recommended materials: bamboo fiber, sugarcane
bagasse, PLA (corn-based), recycled cardboard, beeswax coatings.

Action 2: Ask[FoodSafetyExpert, "requirements for food packaging"]
Observation 2: Must be: FDA-approved, grease-resistant, maintain
temperature, prevent contamination, clearly labeled.

Action 3: Ask[CostAnalyst, "cost comparison sustainable vs plastic"]
Observation 3: Sustainable options are 15-30% more expensive but
costs are decreasing. Consumer willingness to pay premium: ~72%.

Action 4: Ask[LogisticsExpert, "stackability storage requirements"]
Observation 4: Must be stackable, lightweight, nest when empty,
survive shipping conditions.

Thought 2: I can now synthesize a recommendation.
Final Answer: [Synthesized recommendation combining all expert input]
```

## Implementation Template

```python
REACT_SYSTEM_PROMPT = """
You solve problems by alternating between reasoning and action.

Available Tools:
{tools_description}

Response Format:
Thought: [reasoning]
Action: [tool_name][args]
Observation: [wait for result]
... repeat ...
Thought: [final reasoning]
Final Answer: [answer]

Rules:
1. Always explain your reasoning in Thought
2. Only one Action per turn
3. Wait for Observation before next Thought
4. End with Final Answer when done
"""


def react_agent(question, tools, max_iterations=10):
    """Run ReAct loop until answer or max iterations."""
    messages = [
        {"role": "system", "content": REACT_SYSTEM_PROMPT.format(
            tools_description=describe_tools(tools)
        )},
        {"role": "user", "content": question}
    ]

    for i in range(max_iterations):
        response = call_llm(messages)

        if "Final Answer:" in response:
            return extract_final_answer(response)

        if "Action:" in response:
            action, args = parse_action(response)
            observation = tools[action](args)
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": f"Observation: {observation}"})

    return "Max iterations reached without answer"
```

## Best Practices

1. **Define tools clearly** - Unambiguous names and parameters
2. **Limit action scope** - Prevent dangerous operations
3. **Handle failures gracefully** - Plan for action errors
4. **Set iteration limits** - Prevent infinite loops
5. **Log all steps** - Enable debugging and auditing

## Next Steps

- [03-prompt-chaining.md](03-prompt-chaining.md) - Multi-step workflows
- [04-meta-prompting.md](04-meta-prompting.md) - Prompts generating prompts
