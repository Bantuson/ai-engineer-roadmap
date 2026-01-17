"""
Day 17 — Data-Driven Programs

Problems

Todo list

Shopping cart

Score tracker

Focus

Lists & dictionaries

CRUD logic
"""

# Todo list
def create_todo(item, time, day):
    return {
        "item": item,
        "time": time,
        "day": day,
        "done": False
    }

def add_todo(todo_list, todo):
    todo_list.append(todo)

def mark_done(todo):
    todo["done"] = True

def show_todos(todo_list):
    for todo in todo_list:
        status = "✓" if todo["done"] else "✗"
        print(f"{status} {todo['item']} @ {todo['time']} ({todo['day']})")

todos = [] # example usage

t1 = create_todo("Study Python", "18:00", "Monday")
t2 = create_todo("Gym", "07:00", "Tuesday")

add_todo(todos, t1)
add_todo(todos, t2)

mark_done(t1)

show_todos(todos)



# Shopping cart
def create_product(name, price, quantity):
    return {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def add_to_cart(cart, product):
    cart.append(product)

def cart_total(cart):
    total = 0
    for product in cart:
        total += product["price"] * product["quantity"]
    return total

cart = [] # example usage

p1 = create_product("Milk", 20, 2)
p2 = create_product("Bread", 15, 1)

add_to_cart(cart, p1)
add_to_cart(cart, p2)

print("Total:", cart_total(cart))


# Score tracker
def create_tracker():
    return {}

def add_score(tracker, player, score):
    if player not in tracker:
        tracker[player] = []
    tracker[player].append(score)

def average_score(tracker, player):
    scores = tracker.get(player, [])
    if not scores:
        return 0
    return sum(scores) / len(scores)

tracker = create_tracker() # example usage

add_score(tracker, "Alice", 80)
add_score(tracker, "Alice", 90)
add_score(tracker, "Bob", 70)

print("Alice avg:", average_score(tracker, "Alice"))
print("Bob avg:", average_score(tracker, "Bob"))

"""
When you see a problem now, ask:

What is one item? → dictionary

What is many items? → list

What changes over time? → list/dict mutation

What stays derived? → calculated when needed
"""