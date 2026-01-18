"""
Pydantic AI Smart Calculator
============================
Pattern: Tool Use with Validation
Framework: Pydantic AI with @agent.tool decorator

A calculator agent that can:
- Perform basic math operations
- Convert between units
- Explain formulas step by step
"""

import os
import math
from pydantic_ai import Agent, RunContext

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Create agent with DeepSeek model
agent = Agent(
    "deepseek:deepseek-chat",
    system_prompt="""You are a helpful calculator assistant. You can:
1. Calculate math expressions using the calculate tool
2. Convert between units using the convert_units tool
3. Explain formulas step by step using the explain_formula tool

Always use the appropriate tool for the user's request.
Show your work and explain results clearly."""
)


# Tool: Basic calculator
@agent.tool_plain
def calculate(expression: str):
    """
    Calculate a math expression.

    Args:
        expression: A math expression like "2 + 2" or "sqrt(16)"

    Returns:
        The calculated result
    """
    # Safe math functions we allow
    safe_functions = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "log10": math.log10,
        "exp": math.exp,
        "pow": pow,
        "abs": abs,
        "round": round,
        "pi": math.pi,
        "e": math.e,
    }

    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": {}}, safe_functions)
        return f"Result: {expression} = {result}"
    except Exception as error:
        return f"Error calculating '{expression}': {error}"


# Tool: Unit converter
@agent.tool_plain
def convert_units(value: float, from_unit: str, to_unit: str):
    """
    Convert between common units.

    Args:
        value: The numeric value to convert
        from_unit: The source unit (e.g., "km", "miles", "celsius")
        to_unit: The target unit (e.g., "miles", "km", "fahrenheit")

    Returns:
        The converted value with explanation
    """
    # Conversion factors (to base units)
    length_to_meters = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254,
        "yards": 0.9144,
    }

    weight_to_grams = {
        "g": 1,
        "kg": 1000,
        "mg": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495,
        "lbs": 453.592,
        "oz": 28.3495,
    }

    # Temperature conversions
    if from_unit.lower() in ["celsius", "c"] and to_unit.lower() in ["fahrenheit", "f"]:
        result = (value * 9/5) + 32
        return f"{value}°C = {result:.2f}°F"

    if from_unit.lower() in ["fahrenheit", "f"] and to_unit.lower() in ["celsius", "c"]:
        result = (value - 32) * 5/9
        return f"{value}°F = {result:.2f}°C"

    if from_unit.lower() in ["celsius", "c"] and to_unit.lower() in ["kelvin", "k"]:
        result = value + 273.15
        return f"{value}°C = {result:.2f}K"

    if from_unit.lower() in ["kelvin", "k"] and to_unit.lower() in ["celsius", "c"]:
        result = value - 273.15
        return f"{value}K = {result:.2f}°C"

    # Length conversions
    from_lower = from_unit.lower()
    to_lower = to_unit.lower()

    if from_lower in length_to_meters and to_lower in length_to_meters:
        meters = value * length_to_meters[from_lower]
        result = meters / length_to_meters[to_lower]
        return f"{value} {from_unit} = {result:.4f} {to_unit}"

    # Weight conversions
    if from_lower in weight_to_grams and to_lower in weight_to_grams:
        grams = value * weight_to_grams[from_lower]
        result = grams / weight_to_grams[to_lower]
        return f"{value} {from_unit} = {result:.4f} {to_unit}"

    return f"Sorry, I don't know how to convert from {from_unit} to {to_unit}"


# Tool: Formula explainer
@agent.tool_plain
def explain_formula(formula_name: str):
    """
    Explain a common math formula step by step.

    Args:
        formula_name: Name of the formula (e.g., "pythagorean", "quadratic", "area_circle")

    Returns:
        Step-by-step explanation of the formula
    """
    formulas = {
        "pythagorean": """
Pythagorean Theorem: a² + b² = c²

Used to find the length of a side in a right triangle.

Steps:
1. Identify the two shorter sides (a and b)
2. Square each side: a² and b²
3. Add them together: a² + b²
4. Take the square root to find c: c = √(a² + b²)

Example: If a=3 and b=4
- 3² = 9
- 4² = 16
- 9 + 16 = 25
- √25 = 5
So c = 5
""",
        "quadratic": """
Quadratic Formula: x = (-b ± √(b²-4ac)) / 2a

Used to solve equations in the form ax² + bx + c = 0

Steps:
1. Identify a, b, and c from your equation
2. Calculate the discriminant: b² - 4ac
3. Take the square root of the discriminant
4. Calculate x = (-b + √discriminant) / 2a for one solution
5. Calculate x = (-b - √discriminant) / 2a for the other solution

Example: x² + 5x + 6 = 0 (a=1, b=5, c=6)
- Discriminant = 25 - 24 = 1
- √1 = 1
- x = (-5 + 1) / 2 = -2
- x = (-5 - 1) / 2 = -3
Solutions: x = -2 or x = -3
""",
        "area_circle": """
Area of a Circle: A = πr²

Steps:
1. Measure the radius (r) of the circle
2. Square the radius: r²
3. Multiply by π (approximately 3.14159)

Example: Circle with radius 5
- r² = 25
- A = π × 25 ≈ 78.54

The area is approximately 78.54 square units.
""",
        "slope": """
Slope Formula: m = (y₂ - y₁) / (x₂ - x₁)

Used to find the steepness of a line between two points.

Steps:
1. Identify your two points: (x₁, y₁) and (x₂, y₂)
2. Subtract the y-coordinates: y₂ - y₁ (rise)
3. Subtract the x-coordinates: x₂ - x₁ (run)
4. Divide rise by run

Example: Points (2, 3) and (6, 11)
- Rise = 11 - 3 = 8
- Run = 6 - 2 = 4
- Slope = 8 / 4 = 2

The slope is 2 (rises 2 units for every 1 unit right).
""",
        "compound_interest": """
Compound Interest: A = P(1 + r/n)^(nt)

Where:
- A = Final amount
- P = Principal (starting amount)
- r = Annual interest rate (as decimal)
- n = Times interest compounds per year
- t = Number of years

Steps:
1. Convert interest rate to decimal (5% = 0.05)
2. Divide rate by compounding frequency: r/n
3. Add 1: (1 + r/n)
4. Raise to power of total periods: (1 + r/n)^(nt)
5. Multiply by principal: P × result

Example: $1000 at 5% annual, compounded monthly, for 2 years
- r/n = 0.05/12 = 0.00417
- 1 + 0.00417 = 1.00417
- nt = 12 × 2 = 24
- 1.00417^24 = 1.1049
- A = 1000 × 1.1049 = $1104.94
""",
    }

    name_lower = formula_name.lower().replace(" ", "_")

    if name_lower in formulas:
        return formulas[name_lower]

    available = ", ".join(formulas.keys())
    return f"Formula '{formula_name}' not found. Available formulas: {available}"


def main():
    """Main function to run the calculator."""
    print("=" * 50)
    print("  Smart Calculator (Pydantic AI + DeepSeek)")
    print("=" * 50)
    print()
    print("I can help you with:")
    print("  - Math calculations (e.g., 'what is 15 * 7 + 3?')")
    print("  - Unit conversions (e.g., 'convert 100 km to miles')")
    print("  - Formula explanations (e.g., 'explain the pythagorean theorem')")
    print()
    print("Type 'quit' to exit.")
    print("-" * 50)

    while True:
        print()
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        # Run the agent synchronously
        try:
            result = agent.run_sync(user_input)
            print()
            print(f"Calculator: {result.data}")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
