"""
Day 19 — Command Parsing

Problems

Interpret user commands

Split input into actions

Execute behavior

Focus

Mapping input → behavior
"""

# Interpret user commands
command = "add milk"
parts = command.split()

action = parts[0]
item = parts[1]

print(action)
print(item)


# Split input into actions
command = "remove bread"
parts = command.split()

if parts[0] == "add":
    print("Add item:", parts[1])
elif parts[0] == "remove":
    print("Remove item:", parts[1])
else:
    print("Unknown command")


# Execute behavior
cart = []
command = "add milk"

parts = command.split()
action = parts[0]
item = parts[1]

if action == "add":
    cart.append(item)
elif action == "remove" and item in cart:
    cart.remove(item)

print(cart)


# Interpret user commands as function
def command_interpreter(command):
    parts = command.split()
    action = parts[0]
    item = parts[1]
    return action, item


# Split input into actions as function
def command_actions(command):
    parts = command.split()

    if parts[0] == "add":
        print("Add item:", parts[1])
    elif parts[0] == "remove":
        print("Remove item:", parts[1])
    else:
        print("Unknown command")



# Execute behavior as function
def execute_behavior(cart, action, item):
    if action == "add":
        cart.append(item)
    elif action == "remove" and item in cart:
        cart.remove(item)
    return cart
