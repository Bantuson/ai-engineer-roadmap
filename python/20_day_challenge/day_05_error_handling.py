"""
Day 5: Error Handling
=====================
Learn to handle errors gracefully with try/except and custom exceptions.

Key concepts:
- try/except/else/finally
- Catching specific exceptions
- Raising exceptions
- Custom exception classes
- Context managers for cleanup
"""

import os

# =============================================================================
# CONCEPT: Error Handling Basics
# =============================================================================

# Basic try/except
def divide(a, b):
    """Divide two numbers with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None


# Multiple exception types
def read_json_file(filepath):
    """Read JSON file with multiple error handling."""
    import json
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'")
        return None


# try/except/else/finally
def process_file(filepath):
    """Demonstrate full try/except/else/finally."""
    file = None
    try:
        file = open(filepath, 'r')
        content = file.read()
    except FileNotFoundError:
        print("File not found")
        content = None
    else:
        # Runs only if no exception occurred
        print("File read successfully")
    finally:
        # Always runs
        if file:
            file.close()
            print("File closed")
    return content


# =============================================================================
# CONCEPT: Custom Exceptions
# =============================================================================

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


def validate_user(user_data):
    """Validate user data, raise custom exceptions on failure."""
    if not user_data.get('name'):
        raise ValidationError('name', 'Name is required')

    if len(user_data.get('name', '')) < 2:
        raise ValidationError('name', 'Name must be at least 2 characters')

    age = user_data.get('age')
    if age is not None:
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValidationError('age', 'Age must be between 0 and 150')

    return True


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_handling():
    """Demonstrate basic error handling."""
    print("=== Basic Error Handling ===")

    # Successful division
    result = divide(10, 2)
    print(f"10 / 2 = {result}")

    # Division by zero
    result = divide(10, 0)
    print(f"10 / 0 = {result}")


def example_multiple_exceptions():
    """Demonstrate catching multiple exception types."""
    print("\n=== Multiple Exceptions ===")

    def parse_int(value):
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            print(f"Cannot convert '{value}': {type(e).__name__}")
            return None

    print(f"Parse '42': {parse_int('42')}")
    print(f"Parse 'abc': {parse_int('abc')}")
    print(f"Parse None: {parse_int(None)}")


def example_exception_info():
    """Demonstrate getting exception details."""
    print("\n=== Exception Information ===")

    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Exception args: {e.args}")


def example_custom_exceptions():
    """Demonstrate custom exceptions."""
    print("\n=== Custom Exceptions ===")

    # Valid user
    try:
        validate_user({'name': 'Alice', 'age': 30})
        print("User is valid")
    except ValidationError as e:
        print(f"Validation failed: {e}")

    # Invalid user - missing name
    try:
        validate_user({'age': 30})
    except ValidationError as e:
        print(f"Validation failed - Field: {e.field}, Message: {e.message}")

    # Invalid user - bad age
    try:
        validate_user({'name': 'Bob', 'age': -5})
    except ValidationError as e:
        print(f"Validation failed: {e}")


def example_reraise():
    """Demonstrate re-raising exceptions."""
    print("\n=== Re-raising Exceptions ===")

    def process_data(data):
        try:
            # Some processing that might fail
            result = int(data)
            return result * 2
        except ValueError:
            print("Logging error for debugging...")
            raise  # Re-raise the same exception

    try:
        process_data("not a number")
    except ValueError as e:
        print(f"Caught re-raised exception: {e}")


def example_exception_chaining():
    """Demonstrate exception chaining."""
    print("\n=== Exception Chaining ===")

    def load_config(filepath):
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except FileNotFoundError as e:
            raise ConfigError(f"Config file missing: {filepath}") from e

    try:
        load_config('nonexistent.conf')
    except ConfigError as e:
        print(f"Config Error: {e}")
        if e.__cause__:
            print(f"Caused by: {e.__cause__}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Safe Dictionary Access

    Write a function safe_get(d, keys, default=None) that safely accesses
    nested dictionary keys without raising KeyError.

    Example:
    data = {'user': {'profile': {'name': 'Alice'}}}
    safe_get(data, ['user', 'profile', 'name']) -> 'Alice'
    safe_get(data, ['user', 'missing'], 'default') -> 'default'
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Retry Decorator

    Write a decorator that retries a function up to N times on exception.

    @retry(max_attempts=3, exceptions=(ConnectionError,))
    def fetch_data():
        # might raise ConnectionError
        pass
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Error Collector

    Write a function that processes a list of items and collects all errors
    instead of stopping at the first one.

    def process_all(items, processor):
        # Process each item, collect errors
        # Return (successful_results, errors)
        pass

    Example:
    results, errors = process_all([1, 'a', 2, 'b'], int)
    # results = [1, 2]
    # errors = [('a', ValueError), ('b', ValueError)]
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Input Validator

    Create a comprehensive input validator that:
    - Validates required fields
    - Validates field types
    - Validates field constraints (min, max, pattern)
    - Collects all validation errors

    schema = {
        'name': {'type': str, 'required': True, 'min_length': 2},
        'age': {'type': int, 'required': True, 'min': 0, 'max': 150},
        'email': {'type': str, 'required': True, 'pattern': r'.*@.*\..*'}
    }

    errors = validate(data, schema)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Robust File Processor

    Create a robust file processor that:

    1. Processes multiple files in a directory
    2. Handles various error conditions:
       - File not found
       - Permission denied
       - Invalid file format
       - Processing errors
    3. Continues processing other files even if one fails
    4. Logs all operations and errors
    5. Provides a summary at the end

    Features:
    - process_directory(path, processor_func, on_error='skip')
      - on_error options: 'skip', 'raise', 'collect'
    - Returns detailed results:
      {
          'processed': [list of successful files],
          'failed': [list of (file, error) tuples],
          'skipped': [list of skipped files],
          'total_time': seconds
      }
    - Custom exception types for different error categories
    - Automatic cleanup on partial failures

    Example usage:

    def parse_json_file(filepath):
        # Your processing logic
        pass

    results = process_directory('./data', parse_json_file, on_error='collect')
    print(f"Processed: {len(results['processed'])} files")
    print(f"Failed: {len(results['failed'])} files")
    for file, error in results['failed']:
        print(f"  {file}: {error}")
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 5: Error Handling\n")
    print("=" * 50)

    # Run examples
    example_basic_handling()
    example_multiple_exceptions()
    example_exception_info()
    example_custom_exceptions()
    example_reraise()
    example_exception_chaining()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
