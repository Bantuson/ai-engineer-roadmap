"""
Day 15: Testing Basics
======================
Learn to write tests for your Python code.

Key concepts:
- unittest module
- Test organization
- Assertions
- Setup and teardown
- Test fixtures
"""

import unittest
import os
import tempfile

# =============================================================================
# CONCEPT: Code to Test
# =============================================================================

class Calculator:
    """Simple calculator for testing demonstrations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def parse_csv_line(line):
    """Parse a CSV line into fields."""
    if not line:
        return []
    return [field.strip() for field in line.split(',')]


def is_valid_email(email):
    """Check if email format is valid."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


# =============================================================================
# CONCEPT: Basic Test Cases
# =============================================================================

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)

    def test_subtract(self):
        """Test subtraction."""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        """Test multiplication."""
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        """Test division."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_assertions():
    """Demonstrate basic assertions."""
    print("=== Basic Assertions ===")

    class TestAssertions(unittest.TestCase):
        def test_equality(self):
            self.assertEqual(1 + 1, 2)
            self.assertNotEqual(1 + 1, 3)

        def test_boolean(self):
            self.assertTrue(1 < 2)
            self.assertFalse(1 > 2)

        def test_none(self):
            self.assertIsNone(None)
            self.assertIsNotNone("value")

        def test_contains(self):
            self.assertIn('a', 'abc')
            self.assertNotIn('d', 'abc')

        def test_types(self):
            self.assertIsInstance([], list)
            self.assertIsInstance("hello", str)

        def test_approximate(self):
            # For floating point comparisons
            self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)

    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssertions)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def example_setup_teardown():
    """Demonstrate setup and teardown methods."""
    print("\n=== Setup and Teardown ===")

    class TestWithSetup(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            """Run once before all tests in this class."""
            print("    setUpClass: Creating shared resources")
            cls.shared_data = {"key": "value"}

        @classmethod
        def tearDownClass(cls):
            """Run once after all tests in this class."""
            print("    tearDownClass: Cleaning up shared resources")

        def setUp(self):
            """Run before each test method."""
            print("    setUp: Preparing for test")
            self.temp_data = []

        def tearDown(self):
            """Run after each test method."""
            print("    tearDown: Cleaning up after test")

        def test_one(self):
            """First test."""
            print("    Running test_one")
            self.temp_data.append(1)
            self.assertEqual(len(self.temp_data), 1)

        def test_two(self):
            """Second test."""
            print("    Running test_two")
            self.assertEqual(len(self.temp_data), 0)  # Fresh setup

    suite = unittest.TestLoader().loadTestsFromTestCase(TestWithSetup)
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)


def example_test_exceptions():
    """Demonstrate testing exceptions."""
    print("\n=== Testing Exceptions ===")

    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    class TestExceptions(unittest.TestCase):

        def test_raises_exception(self):
            """Test that exception is raised."""
            with self.assertRaises(ZeroDivisionError):
                divide(1, 0)

        def test_exception_message(self):
            """Test exception message."""
            with self.assertRaises(ZeroDivisionError) as context:
                divide(1, 0)
            self.assertIn("Cannot divide", str(context.exception))

        def test_no_exception(self):
            """Test that no exception is raised for valid input."""
            try:
                result = divide(10, 2)
                self.assertEqual(result, 5.0)
            except Exception:
                self.fail("divide() raised exception unexpectedly")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestExceptions)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def example_parameterized_tests():
    """Demonstrate parameterized-like testing."""
    print("\n=== Parameterized Tests ===")

    class TestParameterized(unittest.TestCase):

        def test_email_validation(self):
            """Test multiple email formats."""
            test_cases = [
                ('valid@email.com', True),
                ('also.valid@sub.domain.com', True),
                ('invalid', False),
                ('@nodomain.com', False),
                ('no@tld', False),
            ]

            for email, expected in test_cases:
                with self.subTest(email=email):
                    result = is_valid_email(email)
                    self.assertEqual(result, expected,
                                   f"Failed for {email}")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestParameterized)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def example_file_testing():
    """Demonstrate testing file operations."""
    print("\n=== Testing File Operations ===")

    class TestFileOperations(unittest.TestCase):

        def setUp(self):
            """Create temp directory for tests."""
            self.test_dir = tempfile.mkdtemp()
            self.test_file = os.path.join(self.test_dir, 'test.txt')

        def tearDown(self):
            """Clean up temp files."""
            if os.path.exists(self.test_file):
                os.remove(self.test_file)
            os.rmdir(self.test_dir)

        def test_write_and_read(self):
            """Test writing and reading a file."""
            content = "Hello, World!"

            # Write
            with open(self.test_file, 'w') as f:
                f.write(content)

            # Read
            with open(self.test_file, 'r') as f:
                result = f.read()

            self.assertEqual(result, content)

        def test_file_exists(self):
            """Test file creation."""
            self.assertFalse(os.path.exists(self.test_file))

            with open(self.test_file, 'w') as f:
                f.write("test")

            self.assertTrue(os.path.exists(self.test_file))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFileOperations)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def example_mocking():
    """Demonstrate basic mocking (without external libraries)."""
    print("\n=== Basic Mocking ===")

    # Function that depends on external service
    def get_user_greeting(user_id, fetch_user):
        """Get greeting for user."""
        user = fetch_user(user_id)
        if user:
            return f"Hello, {user['name']}!"
        return "Hello, Guest!"

    class TestWithMock(unittest.TestCase):

        def test_greeting_with_user(self):
            """Test greeting when user exists."""
            # Mock function
            def mock_fetch_user(user_id):
                return {'id': user_id, 'name': 'Alice'}

            result = get_user_greeting(1, mock_fetch_user)
            self.assertEqual(result, "Hello, Alice!")

        def test_greeting_without_user(self):
            """Test greeting when user doesn't exist."""
            def mock_fetch_user(user_id):
                return None

            result = get_user_greeting(1, mock_fetch_user)
            self.assertEqual(result, "Hello, Guest!")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestWithMock)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: String Utilities Tests

    Write tests for these string utility functions:

    def reverse_string(s):
        return s[::-1]

    def is_palindrome(s):
        cleaned = s.lower().replace(' ', '')
        return cleaned == cleaned[::-1]

    def word_count(s):
        return len(s.split())

    Write tests covering:
    - Normal cases
    - Edge cases (empty string, single character)
    - Special cases (spaces, mixed case)
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Shopping Cart Tests

    Write tests for this shopping cart:

    class ShoppingCart:
        def __init__(self):
            self.items = []

        def add_item(self, name, price, quantity=1):
            self.items.append({'name': name, 'price': price, 'quantity': quantity})

        def remove_item(self, name):
            self.items = [i for i in self.items if i['name'] != name]

        def get_total(self):
            return sum(i['price'] * i['quantity'] for i in self.items)

        def apply_discount(self, percentage):
            for item in self.items:
                item['price'] *= (1 - percentage / 100)

    Test:
    - Adding/removing items
    - Total calculation
    - Discount application
    - Edge cases
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: API Response Handler Tests

    Write tests for this API response handler:

    class APIResponse:
        def __init__(self, status_code, data=None, error=None):
            self.status_code = status_code
            self.data = data
            self.error = error

        def is_success(self):
            return 200 <= self.status_code < 300

        def get_data(self):
            if not self.is_success():
                raise ValueError(f"Request failed: {self.error}")
            return self.data

    Test:
    - Success responses (200, 201, etc.)
    - Error responses (400, 404, 500, etc.)
    - Data extraction
    - Error handling
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Data Processor Tests

    Write tests for this data processor:

    class DataProcessor:
        def __init__(self, filepath):
            self.filepath = filepath

        def read_data(self):
            with open(self.filepath, 'r') as f:
                return [line.strip() for line in f if line.strip()]

        def process(self, transform_func):
            data = self.read_data()
            return [transform_func(item) for item in data]

        def write_results(self, results, output_path):
            with open(output_path, 'w') as f:
                for result in results:
                    f.write(str(result) + '\\n')

    Test:
    - Reading data from file
    - Processing with different transforms
    - Writing results
    - Handle file errors
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Build a Test Suite for a Task Manager

    Create comprehensive tests for a task management system:

    class Task:
        def __init__(self, title, priority='medium', due_date=None):
            self.id = None  # Set when added to manager
            self.title = title
            self.priority = priority
            self.due_date = due_date
            self.completed = False
            self.created_at = datetime.now()

    class TaskManager:
        def __init__(self, storage_path=None):
            self.tasks = []
            self.storage_path = storage_path
            self._next_id = 1

        def add_task(self, task):
            '''Add task and assign ID'''
            pass

        def get_task(self, task_id):
            '''Get task by ID'''
            pass

        def update_task(self, task_id, **updates):
            '''Update task fields'''
            pass

        def delete_task(self, task_id):
            '''Delete task by ID'''
            pass

        def complete_task(self, task_id):
            '''Mark task as completed'''
            pass

        def list_tasks(self, filter_by=None, sort_by=None):
            '''List tasks with optional filtering and sorting'''
            pass

        def get_overdue_tasks(self):
            '''Get tasks past their due date'''
            pass

        def save(self):
            '''Save tasks to storage'''
            pass

        def load(self):
            '''Load tasks from storage'''
            pass

    Write tests covering:

    1. Basic CRUD operations
       - Add, get, update, delete tasks
       - ID assignment
       - Task not found errors

    2. Task completion
       - Mark as complete
       - Prevent duplicate completion
       - Completion timestamp

    3. Filtering and sorting
       - Filter by priority, status, due date
       - Sort by various fields
       - Combined filtering and sorting

    4. Date handling
       - Due dates in past/future
       - Overdue task detection
       - Tasks due today

    5. Persistence
       - Save tasks to file
       - Load tasks from file
       - Handle missing/corrupt file

    6. Edge cases
       - Empty task list
       - Duplicate titles
       - Invalid priorities
       - Invalid dates

    Use unittest features:
    - setUp and tearDown
    - setUpClass and tearDownClass
    - subTest for parameterized tests
    - Mock for date/time testing
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 15: Testing Basics\n")
    print("=" * 50)

    # Run examples
    example_basic_assertions()
    example_setup_teardown()
    example_test_exceptions()
    example_parameterized_tests()
    example_file_testing()
    example_mocking()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
