"""
Day 9 — Rule Systems

Problems

Shipping cost calculator

Discount eligibility

Login validation (mock rules)

Focus

Multiple conditions

Logical grouping
"""

# Shipping cost calculator
"""
facts: price, distance, weight affect total cost
types: prices, distance and weight are floats/integers
decisions: total cost aggragates price, distance and weight
"""
item_price = 2999
weight = 23
distance = 1.6
base_shipping_cost = 50
total_cost = item_price + base_shipping_cost

if distance > 1.5 and weight > 20:
    total_cost += 20  # surcharge applied

print(total_cost)


# Discount eligibility
"""
facts: eligibilty requires satisfying minimum spend, or using coupon, membership card.
types: boolean for coupon or membership, integer for spend 
decisions: if any one of the conditions is met, apply discount
"""
has_coupon = True
spend = 200
apply_discount = False

if has_coupon or spend > 100:
    apply_discount = True

print(apply_discount)


# Login validation (mock rules)
"""
facts: requires both email and password credentials
types: email is string, password can be int/string
decisions: password must belong to email for validation to pass
"""
stored_email = "user@example.com"
stored_password = "secure123"

input_email = "user@example.com"
input_password = "secure123"

login_success = False

if input_email == stored_email and input_password == stored_password:
    login_success = True

print(login_success)


