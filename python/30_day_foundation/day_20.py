"""
Day 20 — Mini System

Build

Small CLI tool of your choice

Rules

At least 3 functions

Persistent state (in memory)
"""

# Small CLI tool of your choice
todos = []

commands = [
    "add study",
    "add exercise",
    "remove study",
    "add sleep"
]

for command in commands:
    parts = command.split()
    action = parts[0]
    item = parts[1]

    if action == "add":
        todos.append(item)
    elif action == "remove" and item in todos:
        todos.remove(item)

print(todos)


# CLI tool as function
def parse_command(command):
    parts = command.split()
    action = parts[0]
    item = parts[1]
    return action, item

def apply_command(todos, action, item):
    if action == "add":
        todos.append(item)
    elif action == "remove" and item in todos:
        todos.remove(item)
    return todos

def run_cli_step(todos, command):
    action, item = parse_command(command)
    return apply_command(todos, action, item)


todos = [] #Example usagw

todos = run_cli_step(todos, "add study")
todos = run_cli_step(todos, "add exercise")
todos = run_cli_step(todos, "remove study")

print(todos)

