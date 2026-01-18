"""
Claude Agents SDK Code Explainer
=================================
Pattern: ReAct with Tool Use
Framework: Claude Agents SDK with tools

A code helper that:
- Explains code snippets line by line
- Can run simple Python code to demonstrate
- Uses ReAct pattern for step-by-step reasoning
"""

import os
import sys
import io
import asyncio
from anthropic import Anthropic

# Get API key from environment
# This project uses Claude API directly (you can also use DeepSeek via OpenAI compatibility)
api_key = os.getenv("ANTHROPIC_API_KEY")
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key and not deepseek_key:
    print("Error: Please set ANTHROPIC_API_KEY or DEEPSEEK_API_KEY environment variable")
    print("  export ANTHROPIC_API_KEY='your-key-here'")
    print("  OR")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Use Anthropic if available, otherwise use DeepSeek via OpenAI
USE_ANTHROPIC = api_key is not None


# =====================================================
# Tool Definitions
# =====================================================

def run_python_code(code):
    """Execute Python code safely and return the output.

    Args:
        code: Python code to execute

    Returns:
        The output from running the code
    """
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    result = {
        "success": True,
        "output": "",
        "error": None
    }

    try:
        # Create a restricted globals dict
        safe_globals = {
            "__builtins__": {
                "print": print,
                "len": len,
                "range": range,
                "str": str,
                "int": int,
                "float": float,
                "list": list,
                "dict": dict,
                "bool": bool,
                "sum": sum,
                "max": max,
                "min": min,
                "abs": abs,
                "round": round,
                "sorted": sorted,
                "enumerate": enumerate,
                "zip": zip,
                "map": map,
                "filter": filter,
                "True": True,
                "False": False,
                "None": None,
            }
        }

        # Execute the code
        exec(code, safe_globals)

        # Get the output
        result["output"] = sys.stdout.getvalue()

    except Exception as e:
        result["success"] = False
        result["error"] = str(e)

    finally:
        sys.stdout = old_stdout

    return result


def analyze_code_structure(code):
    """Analyze the structure of Python code.

    Args:
        code: Python code to analyze

    Returns:
        Analysis of the code structure
    """
    lines = code.strip().split("\n")

    analysis = {
        "line_count": len(lines),
        "has_functions": False,
        "has_loops": False,
        "has_conditionals": False,
        "has_imports": False,
        "function_names": [],
        "variable_assignments": []
    }

    for line in lines:
        stripped = line.strip()

        # Check for functions
        if stripped.startswith("def "):
            analysis["has_functions"] = True
            # Extract function name
            parts = stripped.split("(")
            if len(parts) > 1:
                name = parts[0].replace("def ", "").strip()
                analysis["function_names"].append(name)

        # Check for loops
        if stripped.startswith("for ") or stripped.startswith("while "):
            analysis["has_loops"] = True

        # Check for conditionals
        if stripped.startswith("if ") or stripped.startswith("elif ") or stripped.startswith("else:"):
            analysis["has_conditionals"] = True

        # Check for imports
        if stripped.startswith("import ") or stripped.startswith("from "):
            analysis["has_imports"] = True

        # Check for variable assignments (simple detection)
        if "=" in stripped and not stripped.startswith("#"):
            if "==" not in stripped and "!=" not in stripped:
                if not stripped.startswith("if ") and not stripped.startswith("elif "):
                    parts = stripped.split("=")
                    if len(parts) >= 2:
                        var_name = parts[0].strip()
                        if var_name.isidentifier():
                            analysis["variable_assignments"].append(var_name)

    return analysis


# =====================================================
# Anthropic Claude Agent
# =====================================================

# Tool schemas for Claude
tools = [
    {
        "name": "run_python",
        "description": "Execute Python code and return the output. Use this to demonstrate code behavior.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute"
                }
            },
            "required": ["code"]
        }
    },
    {
        "name": "analyze_structure",
        "description": "Analyze the structure of Python code to understand its components.",
        "input_schema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to analyze"
                }
            },
            "required": ["code"]
        }
    }
]

SYSTEM_PROMPT = """You are a code explanation assistant. Your job is to help beginners understand Python code.

When explaining code:
1. First analyze the code structure using the analyze_structure tool
2. Explain what the code does step by step
3. Use the run_python tool to demonstrate the code in action
4. Keep explanations simple - assume the user is a beginner

Your explanation style:
- Start with a high-level summary (1-2 sentences)
- Then go line by line for important parts
- Use analogies when helpful
- Highlight common patterns and best practices
- Point out potential issues or improvements

Use the ReAct pattern:
- Thought: What do I need to understand about this code?
- Action: Use a tool to analyze or run the code
- Observation: What did I learn?
- Response: Explain to the user

Always be encouraging and supportive!"""


def handle_tool_call(tool_name, tool_input):
    """Handle a tool call from the assistant."""
    if tool_name == "run_python":
        result = run_python_code(tool_input["code"])
        if result["success"]:
            output = result["output"] if result["output"] else "(No output)"
            return f"Code executed successfully.\nOutput:\n{output}"
        else:
            return f"Error running code: {result['error']}"

    elif tool_name == "analyze_structure":
        analysis = analyze_code_structure(tool_input["code"])
        lines = []
        lines.append(f"Lines of code: {analysis['line_count']}")
        lines.append(f"Has functions: {analysis['has_functions']}")
        if analysis["function_names"]:
            lines.append(f"  Function names: {', '.join(analysis['function_names'])}")
        lines.append(f"Has loops: {analysis['has_loops']}")
        lines.append(f"Has conditionals: {analysis['has_conditionals']}")
        lines.append(f"Has imports: {analysis['has_imports']}")
        if analysis["variable_assignments"]:
            lines.append(f"Variables: {', '.join(analysis['variable_assignments'][:5])}")
        return "\n".join(lines)

    return "Unknown tool"


async def run_claude_agent(client, user_code):
    """Run the Claude agent to explain code."""
    messages = [
        {
            "role": "user",
            "content": f"Please explain this Python code:\n\n```python\n{user_code}\n```"
        }
    ]

    # ReAct loop
    max_iterations = 5
    iteration = 0

    while iteration < max_iterations:
        iteration = iteration + 1

        # Call Claude
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        # Process response
        assistant_message = {"role": "assistant", "content": response.content}
        messages.append(assistant_message)

        # Check if we need to handle tool calls
        if response.stop_reason == "tool_use":
            # Find tool use blocks
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n🔧 Using tool: {block.name}")

                    # Execute the tool
                    result = handle_tool_call(block.name, block.input)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            # Add tool results to messages
            messages.append({"role": "user", "content": tool_results})

        else:
            # No more tool calls, we have the final response
            break

    # Extract final text response
    final_text = ""
    for block in response.content:
        if hasattr(block, "text"):
            final_text = final_text + block.text

    return final_text


# =====================================================
# DeepSeek Alternative (simpler, no tool use)
# =====================================================

async def run_deepseek_agent(user_code):
    """Run a simpler explanation using DeepSeek."""
    from openai import AsyncOpenAI

    client = AsyncOpenAI(
        base_url="https://api.deepseek.com",
        api_key=deepseek_key
    )

    # First, analyze the code locally
    analysis = analyze_code_structure(user_code)

    # Run the code to get output
    run_result = run_python_code(user_code)
    code_output = ""
    if run_result["success"]:
        code_output = run_result["output"] if run_result["output"] else "(No output)"
    else:
        code_output = f"Error: {run_result['error']}"

    # Create prompt with analysis
    prompt = f"""Please explain this Python code to a beginner:

```python
{user_code}
```

Code analysis:
- Lines: {analysis['line_count']}
- Has functions: {analysis['has_functions']} {analysis['function_names'] if analysis['function_names'] else ''}
- Has loops: {analysis['has_loops']}
- Has conditionals: {analysis['has_conditionals']}

When I run this code, the output is:
{code_output}

Please:
1. Give a brief summary of what this code does
2. Explain the important parts line by line
3. Mention any beginner tips or common patterns"""

    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# =====================================================
# Main Functions
# =====================================================

async def explain_code(code):
    """Explain the given code using the appropriate agent."""
    if USE_ANTHROPIC:
        client = Anthropic(api_key=api_key)
        return await run_claude_agent(client, code)
    else:
        return await run_deepseek_agent(code)


def get_code_input():
    """Get code input from the user."""
    print("\nPaste your Python code (type 'END' on a new line when done):")
    print("-" * 40)

    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        except EOFError:
            break

    return "\n".join(lines)


async def main_async():
    """Async main function."""
    print("=" * 60)
    print("  Code Explainer (Claude Agents SDK)")
    print("=" * 60)
    print()

    if USE_ANTHROPIC:
        print("Using: Claude (Anthropic API)")
    else:
        print("Using: DeepSeek (OpenAI-compatible)")

    print()
    print("I'll help you understand Python code!")
    print("Paste any Python snippet and I'll explain it.")
    print()
    print("Commands:")
    print("  'example' - See an example explanation")
    print("  'quit' - Exit the program")
    print("-" * 60)

    # Example code
    example_code = '''def greet(name):
    message = "Hello, " + name + "!"
    return message

names = ["Alice", "Bob", "Charlie"]
for name in names:
    greeting = greet(name)
    print(greeting)'''

    while True:
        print()
        choice = input("Enter 'paste' to input code, 'example', or 'quit': ").strip().lower()

        if choice in ["quit", "exit", "q"]:
            print("\nHappy coding! Goodbye!")
            break

        if choice == "example":
            code = example_code
            print("\nExample code:")
            print("-" * 40)
            print(code)
            print("-" * 40)
        elif choice in ["paste", "p", ""]:
            code = get_code_input()
            if not code.strip():
                print("No code entered. Try again.")
                continue
        else:
            print("Unknown command. Try 'paste', 'example', or 'quit'.")
            continue

        print("\n🔍 Analyzing and explaining code...")
        print("=" * 60)

        try:
            explanation = await explain_code(code)
            print("\n" + explanation)
            print("\n" + "=" * 60)
        except Exception as error:
            print(f"\nError: {error}")
            print("\nTroubleshooting:")
            print("1. Check your API key")
            print("2. Make sure you have anthropic package installed:")
            print("   pip install anthropic")


def main():
    """Main entry point."""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\nSession ended.")


if __name__ == "__main__":
    main()
