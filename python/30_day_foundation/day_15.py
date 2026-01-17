"""
Day 15 — Validation Functions

Problems

Email validation (basic rules)

Password validation

Focus

One responsibility per function
"""

# Email validation
def validate_email(email):
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if local == "" or domain == "":
        return False

    if "." not in domain:
        return False

    return True

    
# Password validation
def validate_password(password):
    if len(password) < 8:
        return False

    if " " in password:
        return False

    return True


"""

"""
    
