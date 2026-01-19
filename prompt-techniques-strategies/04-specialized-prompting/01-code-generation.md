# Code Generation Prompting

## Overview

Code generation requires precise prompts that specify language, functionality, constraints, and quality requirements. This module covers techniques for generating reliable, maintainable code.

## Code Generation Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                  CODE GENERATION PROMPT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LANGUAGE & ENVIRONMENT                                         │
│   └── Language, version, frameworks, dependencies               │
│                                                                  │
│   FUNCTIONALITY                                                  │
│   └── What the code should do (input → output)                  │
│                                                                  │
│   CONSTRAINTS                                                    │
│   └── Performance, security, compatibility                      │
│                                                                  │
│   QUALITY REQUIREMENTS                                          │
│   └── Style, documentation, testing                             │
│                                                                  │
│   EXAMPLES                                                       │
│   └── Sample inputs/outputs, usage patterns                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Prompt Patterns for Code

### Pattern 1: Function Generation

```
Write a Python function with the following specifications:

FUNCTION NAME: validate_email

DESCRIPTION:
Validate an email address according to RFC 5322 standards.

PARAMETERS:
- email (str): The email address to validate

RETURNS:
- bool: True if valid, False otherwise

REQUIREMENTS:
- Use regex for validation
- Handle common edge cases
- No external dependencies
- Include type hints
- Include docstring with examples

EDGE CASES TO HANDLE:
- Empty string
- Missing @ symbol
- Multiple @ symbols
- Invalid domain format
- Unicode characters

Example usage:
>>> validate_email("user@example.com")
True
>>> validate_email("invalid-email")
False
```

### Pattern 2: Class Generation

```
Create a Python class with the following specification:

CLASS NAME: RateLimiter

PURPOSE:
Implement a token bucket rate limiter for API calls.

ATTRIBUTES:
- rate: float - tokens added per second
- capacity: int - maximum tokens
- tokens: float - current token count
- last_update: float - timestamp of last update

METHODS:
- __init__(rate: float, capacity: int)
- allow() -> bool: Check if request is allowed, consume token
- wait_time() -> float: Time until next token available
- reset(): Reset to full capacity

THREAD SAFETY:
- Must be thread-safe using threading.Lock

INCLUDE:
- Type hints for all methods
- Docstrings with usage examples
- Unit tests in a separate code block
```

### Pattern 3: Algorithm Implementation

```
Implement the following algorithm in Python:

ALGORITHM: Dijkstra's Shortest Path

INPUT:
- graph: Dict[str, Dict[str, int]] - Adjacency list with weights
- start: str - Starting node

OUTPUT:
- distances: Dict[str, int] - Shortest distance to each node
- paths: Dict[str, List[str]] - Shortest path to each node

REQUIREMENTS:
- Time complexity: O((V + E) log V) using heap
- Handle disconnected graphs (infinity for unreachable)
- Validate input graph format
- Include step-by-step comments

TEST CASES:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start = 'A'
Expected: distances = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### Pattern 4: API Endpoint

```
Create a FastAPI endpoint with these specifications:

ENDPOINT: POST /api/users

PURPOSE: Create a new user account

REQUEST BODY:
{
  "email": string (required, valid email),
  "password": string (required, min 8 chars),
  "name": string (required, 1-100 chars)
}

RESPONSE:
Success (201):
{
  "id": string (UUID),
  "email": string,
  "name": string,
  "created_at": string (ISO datetime)
}

Error (400):
{
  "error": string,
  "details": [{"field": string, "message": string}]
}

REQUIREMENTS:
- Use Pydantic for validation
- Hash password with bcrypt
- Generate UUID for user ID
- Include proper error handling
- Add OpenAPI documentation
```

## Code Quality Specifications

### Style and Documentation

```
CODING STANDARDS:

Style:
- Follow PEP 8 guidelines
- Maximum line length: 88 (Black formatter)
- Use snake_case for functions and variables
- Use PascalCase for classes

Documentation:
- Google-style docstrings
- Include parameter types and descriptions
- Include return type and description
- Include at least one usage example
- Note any exceptions raised

Type Hints:
- All function parameters
- All return types
- Use typing module for complex types

Comments:
- Explain non-obvious logic
- No redundant comments
- Keep comments up-to-date with code
```

### Security Requirements

```
SECURITY CHECKLIST for generated code:

[ ] Input validation on all user inputs
[ ] Parameterized queries (no SQL injection)
[ ] Output encoding (no XSS)
[ ] Secure password handling (hash, never store plain)
[ ] No hardcoded secrets
[ ] Proper authentication checks
[ ] Authorization for sensitive operations
[ ] Rate limiting where appropriate
[ ] Logging without sensitive data
[ ] Error messages without internal details
```

### Performance Specifications

```
PERFORMANCE REQUIREMENTS:

Time Complexity:
- State expected Big O
- Justify algorithm choice

Space Complexity:
- State memory requirements
- Consider streaming for large data

Optimization:
- Use appropriate data structures
- Consider caching where helpful
- Avoid premature optimization
- Profile before optimizing
```

## Few-Shot Code Examples

### Few-Shot for Style Consistency

```
Generate code following this style:

EXAMPLE 1:
def calculate_discount(price: float, percentage: float) -> float:
    """
    Calculate discounted price.

    Args:
        price: Original price in dollars.
        percentage: Discount percentage (0-100).

    Returns:
        Discounted price rounded to 2 decimal places.

    Raises:
        ValueError: If percentage not in valid range.
    """
    if not 0 <= percentage <= 100:
        raise ValueError(f"Percentage must be 0-100, got {percentage}")

    discount = price * (percentage / 100)
    return round(price - discount, 2)

EXAMPLE 2:
def validate_age(age: int) -> bool:
    """
    Check if age is valid for registration.

    Args:
        age: User's age in years.

    Returns:
        True if age is valid (18-120), False otherwise.
    """
    return 18 <= age <= 120

NOW GENERATE:
A function to calculate compound interest given principal,
rate, and years. Follow the exact same style.
```

### Few-Shot for Patterns

```
Generate a repository pattern implementation following these examples:

EXAMPLE - UserRepository:
class UserRepository:
    def __init__(self, db: Database):
        self.db = db
        self.table = "users"

    def get_by_id(self, user_id: str) -> Optional[User]:
        row = self.db.query_one(
            f"SELECT * FROM {self.table} WHERE id = ?",
            [user_id]
        )
        return User.from_row(row) if row else None

    def save(self, user: User) -> User:
        self.db.execute(
            f"INSERT INTO {self.table} (id, email, name) VALUES (?, ?, ?)",
            [user.id, user.email, user.name]
        )
        return user

NOW GENERATE:
ProductRepository with the same pattern, for products
with fields: id, name, price, category
```

## Debugging and Fixing Code

### Bug Fix Prompt

```
Fix the bug in this code:

CODE:
{buggy_code}

OBSERVED BEHAVIOR:
{what_happens}

EXPECTED BEHAVIOR:
{what_should_happen}

ERROR MESSAGE (if any):
{error}

Instructions:
1. Identify the root cause
2. Explain the bug
3. Provide the fixed code
4. Add a test case that would catch this bug
```

### Code Review Prompt

```
Review this code for issues:

CODE:
{code}

Review for:
1. Bugs and logical errors
2. Security vulnerabilities
3. Performance issues
4. Code style and readability
5. Missing error handling
6. Test coverage gaps

For each issue:
- Location (line number or function)
- Severity (Critical/High/Medium/Low)
- Description
- Suggested fix
```

## Refactoring Prompts

```
Refactor this code to improve quality:

CURRENT CODE:
{messy_code}

REFACTORING GOALS:
- [ ] Extract repeated code into functions
- [ ] Improve naming clarity
- [ ] Add proper error handling
- [ ] Follow single responsibility principle
- [ ] Add type hints and documentation

CONSTRAINTS:
- Maintain existing functionality
- Keep public interface unchanged
- No new dependencies

Output:
1. List of changes made
2. Refactored code
3. Before/after comparison for key improvements
```

## Best Practices

1. **Be specific about language/version** - Python 3.10+ differs from 3.7
2. **Include test cases** - Verify generated code works
3. **Specify error handling** - Don't leave to chance
4. **Request documentation** - Comments and docstrings
5. **Iterate and refine** - First generation rarely perfect

## Next Steps

- [02-creative-writing.md](02-creative-writing.md) - Creative content prompts
- [03-data-extraction.md](03-data-extraction.md) - Structured data extraction
