"""
Day 13 — Simulation Thinking

Problems

Countdown timer

Turn-based counter

Step-by-step process

Focus

State changes per iteration
"""

# Countdown timer
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Time's up!")

# Turn-based counter
counter = 0
turn = "Player A"
max_turns = 6
current_turn = 1

while current_turn <= max_turns:
    print(f"{turn}'s turn. Counter = {counter}")

    counter += 1

    if turn == "Player A":
        turn = "Player B"
    else:
        turn = "Player A"

    current_turn += 1

print("Game over. Final counter:", counter)

# Step-by-step process
steps = ["Start engine", "Warm up", "Drive", "Park"]
current_step = 0

while current_step < len(steps):
    print("Current step:", steps[current_step])
    current_step += 1

print("Process complete.")


