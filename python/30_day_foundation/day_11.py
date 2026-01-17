"""
Day 11 — Menu Systems

Problems

Text menu with options

Repeating until exit

Invalid input handling

Focus

Loop control

Program state
"""

# Text menu with options
menu_options = ["Town", "City", "Province"]

choice = input(f"Choose an address type {menu_options}: ")

if choice in menu_options:
    print(f"Your selection is {choice}")
else:
    print("Invalid selection")


# Repeating until exit
menu_options = ["Town", "City", "Province", "Exit"]
running = True

while running:
    choice = input(f"Choose an option {menu_options}: ")

    if choice == "Exit":
        running = False
        print("Exiting menu")
    elif choice in menu_options:
        print(f"You selected {choice}")
    else:
        print("Invalid option")


# Invalid input handling
user_input = "15-12-2020"
is_valid = True

parts = user_input.split("-")

if len(parts) != 3:
    is_valid = False
else:
    day, month, year = parts

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        is_valid = False
    else:
        day = int(day)
        month = int(month)
        year = int(year)

        if not (1 <= day <= 31):
            is_valid = False
        if not (1 <= month <= 12):
            is_valid = False
        if not (1900 <= year <= 2026):
            is_valid = False

print(is_valid)



"""
Core Concept: Program State
A menu system is a loop-controlled state machine that waits for valid input, responds to it, and only exits on command.

A menu program always has:

State – Is the program still running?

Input – What did the user choose?

Transition – What happens after the choice?

Exit condition – When does it stop?

Ask yourself every time:

What state am I in?

What input changes the state?

When do I exit?
"""


"""
What is the input?

What is the state?

What makes input invalid?

When does the program stop?
"""