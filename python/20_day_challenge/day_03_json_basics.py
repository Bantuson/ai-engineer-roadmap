"""
Day 3: JSON Basics
==================
Learn to work with JSON data - loading, dumping, and handling nested structures.

Key concepts:
- json.load() vs json.loads()
- json.dump() vs json.dumps()
- Handling nested data
- Pretty printing
- Custom encoders
"""

import json
import os

# =============================================================================
# CONCEPT: JSON Basics
# =============================================================================

# Load JSON from file
def load_json_file(filepath):
    """Load JSON from a file."""
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


# Load JSON from string
def load_json_string(json_string):
    """Parse JSON from a string."""
    data = json.loads(json_string)
    return data


# Save JSON to file
def save_json_file(filepath, data, pretty=True):
    """Save data as JSON file."""
    with open(filepath, 'w') as file:
        if pretty:
            json.dump(data, file, indent=2)
        else:
            json.dump(data, file)


# Convert to JSON string
def to_json_string(data, pretty=True):
    """Convert data to JSON string."""
    if pretty:
        return json.dumps(data, indent=2)
    return json.dumps(data)


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_json():
    """Demonstrate basic JSON operations."""
    print("=== Basic JSON Operations ===")

    # Python dict to JSON
    user = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "active": True,
        "roles": ["admin", "user"]
    }

    # Convert to JSON string
    json_str = json.dumps(user)
    print(f"JSON string: {json_str}")

    # Pretty print
    print("\nPretty JSON:")
    print(json.dumps(user, indent=2))

    # Parse back to dict
    parsed = json.loads(json_str)
    print(f"\nParsed back: {parsed['name']}, age {parsed['age']}")


def example_nested_json():
    """Demonstrate working with nested JSON."""
    print("\n=== Nested JSON ===")

    # Nested structure
    company = {
        "name": "TechCorp",
        "founded": 2020,
        "departments": {
            "engineering": {
                "head": "Bob",
                "employees": 50,
                "projects": ["ProjectA", "ProjectB"]
            },
            "sales": {
                "head": "Carol",
                "employees": 20,
                "regions": ["NA", "EU", "APAC"]
            }
        },
        "locations": [
            {"city": "NYC", "country": "USA"},
            {"city": "London", "country": "UK"}
        ]
    }

    # Access nested data
    print(f"Company: {company['name']}")
    print(f"Engineering head: {company['departments']['engineering']['head']}")
    print(f"First location: {company['locations'][0]['city']}")

    # Save to file
    save_json_file('company.json', company)
    print("\nSaved to company.json")

    # Load from file
    loaded = load_json_file('company.json')
    print(f"Loaded back: {loaded['name']}")


def example_json_with_defaults():
    """Handle missing keys safely."""
    print("\n=== Safe Access with Defaults ===")

    json_str = '{"name": "Test", "count": 5}'
    data = json.loads(json_str)

    # Using .get() for safe access
    name = data.get('name', 'Unknown')
    missing = data.get('missing_key', 'default_value')

    print(f"Name: {name}")
    print(f"Missing key: {missing}")


def example_api_response():
    """Simulate handling API response JSON."""
    print("\n=== API Response Handling ===")

    # Simulated API response
    api_response = '''
    {
        "status": "success",
        "data": {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ],
            "total": 2,
            "page": 1
        },
        "meta": {
            "request_id": "abc123",
            "timestamp": "2026-01-19T10:00:00Z"
        }
    }
    '''

    response = json.loads(api_response)

    if response['status'] == 'success':
        users = response['data']['users']
        for user in users:
            print(f"User {user['id']}: {user['name']}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Config Loader

    Write a function that loads a JSON config file and merges it with defaults.

    Default config:
    {"debug": False, "port": 8080, "host": "localhost", "timeout": 30}

    If config file has: {"port": 3000, "debug": True}
    Result should be: {"debug": True, "port": 3000, "host": "localhost", "timeout": 30}
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Nested Value Extractor

    Write a function that extracts a value from nested JSON using a dot-notation path.

    Example:
    data = {"user": {"profile": {"name": "Alice"}}}
    get_nested(data, "user.profile.name") -> "Alice"
    get_nested(data, "user.missing.key") -> None
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: JSON Flattener

    Write a function that flattens nested JSON into a single-level dict with dot-notation keys.

    Input:
    {"user": {"name": "Alice", "address": {"city": "NYC"}}}

    Output:
    {"user.name": "Alice", "user.address.city": "NYC"}
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: JSON Differ

    Write a function that compares two JSON objects and returns the differences.

    Example:
    old = {"name": "Alice", "age": 30, "city": "NYC"}
    new = {"name": "Alice", "age": 31, "country": "USA"}

    Result:
    {
        "added": {"country": "USA"},
        "removed": {"city": "NYC"},
        "changed": {"age": {"old": 30, "new": 31}}
    }
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: JSON-Based Task Manager

    Create a task manager that stores tasks in a JSON file with these operations:

    1. add_task(title, priority, due_date): Add a new task
    2. list_tasks(filter_by=None): List all tasks or filter by status/priority
    3. complete_task(task_id): Mark a task as complete
    4. delete_task(task_id): Remove a task
    5. update_task(task_id, **updates): Update task fields
    6. get_stats(): Return statistics (total, completed, by priority)

    JSON structure:
    {
        "next_id": 1,
        "tasks": [
            {
                "id": 1,
                "title": "Learn JSON",
                "priority": "high",
                "due_date": "2026-01-20",
                "status": "pending",
                "created_at": "2026-01-19T10:00:00"
            }
        ]
    }

    Include proper error handling for missing files, invalid IDs, etc.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 3: JSON Basics\n")
    print("=" * 50)

    # Run examples
    example_basic_json()
    example_nested_json()
    example_json_with_defaults()
    example_api_response()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()

    # Cleanup
    if os.path.exists('company.json'):
        os.remove('company.json')
