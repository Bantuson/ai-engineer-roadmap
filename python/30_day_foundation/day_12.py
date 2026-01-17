"""
Day 12 — Game Logic

Problems

Guess the number

Limited attempts

Win / lose state

Focus

State over time

Loop exit conditions
"""

# Guess the number
number = 7
guess = int(input("Guess the number: "))

correct_guess = False

if guess == number:
    correct_guess = True

print(correct_guess)

"""
Game comparisons must be type-safe before logic runs
"""


# Limited attempts
place = "japan"
max_tries = 3
tries = 0
correct_guess = False

while tries < max_tries and not correct_guess:
    attempt = input("Guess the place: ")

    if attempt == place:
        correct_guess = True
        print("Correct!")
    else:
        tries += 1
        print("Incorrect, try again")

if not correct_guess:
    print("No tries left. You lose.")

"""
WHILE game is running:
    get input
    update state
    check win/lose
    exit if terminal state

"""


# Win / lose state
number = 7
max_tries = 3
tries = 0
won = False

while tries < max_tries:
    guess = int(input("Guess the number: "))

    if guess == number:
        won = True
        break
    else:
        tries += 1
        print("Wrong guess")

if won:
    print("You win!")
else:
    print("You lose!")


"""
Game logic is state + time + exit conditions — not if/else alone.

Games are not single decisions
They evolve:

Attempts increase

Flags flip

Conditions eventually terminate the loop

2. Terminal states

Every game must end in exactly one:

Win

Lose

If you cannot point to where that happens, the logic is incomplete.

3. Loop exit conditions

Loops should end because:

A win condition is met (break)

A limit is reached (tries == max_tries)

Never rely on “it feels done”.
"""






