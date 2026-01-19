"""
Day 16: Debugging
=================
Learn debugging techniques and tools.

Key concepts:
- Print debugging
- Python debugger (pdb)
- Debugging strategies
- Common bug patterns
- Logging for debugging
"""

import sys
import traceback

# =============================================================================
# CONCEPT: Debugging Strategies
# =============================================================================

def debugging_strategies():
    """Overview of debugging strategies."""
    strategies = {
        '1. Understand the bug': [
            'Read error messages carefully',
            'Reproduce the bug consistently',
            'Identify when it started happening'
        ],
        '2. Isolate the problem': [
            'Narrow down the failing code',
            'Create minimal reproduction',
            'Check inputs and outputs'
        ],
        '3. Form hypotheses': [
            'What do you think is wrong?',
            'What assumptions are being made?',
            'What changed recently?'
        ],
        '4. Test hypotheses': [
            'Add print statements',
            'Use debugger',
            'Write tests'
        ],
        '5. Fix and verify': [
            'Make one change at a time',
            'Verify the fix works',
            'Check for regressions'
        ]
    }
    return strategies


# =============================================================================
# BUGGY CODE (for debugging exercises)
# =============================================================================

def buggy_sum_evens(numbers):
    """Sum even numbers (has a bug!)."""
    total = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total  # Works, but inefficient


def buggy_find_max(numbers):
    """Find maximum value (has a bug!)."""
    if not numbers:
        return None
    max_val = 0  # Bug: should be numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def buggy_reverse_words(sentence):
    """Reverse words in sentence (has a bug!)."""
    words = sentence.split(' ')
    reversed_words = []
    for i in range(len(words) - 1, 0, -1):  # Bug: should be range(len(words) - 1, -1, -1)
        reversed_words.append(words[i])
    return ' '.join(reversed_words)


def buggy_fibonacci(n):
    """Return nth Fibonacci number (has a bug!)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return buggy_fibonacci(n - 1) + buggy_fibonacci(n - 2)  # Works but very slow


def buggy_merge_dicts(dict1, dict2):
    """Merge two dicts (has a bug!)."""
    result = dict1  # Bug: should be dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    return result


# =============================================================================
# EXAMPLES
# =============================================================================

def example_print_debugging():
    """Demonstrate print debugging."""
    print("=== Print Debugging ===")

    def calculate_average(numbers):
        print(f"DEBUG: Input numbers = {numbers}")  # Debug input

        if not numbers:
            print("DEBUG: Empty list, returning 0")
            return 0

        total = sum(numbers)
        print(f"DEBUG: Total = {total}")  # Debug intermediate

        count = len(numbers)
        print(f"DEBUG: Count = {count}")

        average = total / count
        print(f"DEBUG: Average = {average}")  # Debug output

        return average

    result = calculate_average([10, 20, 30])
    print(f"Result: {result}\n")


def example_strategic_prints():
    """Demonstrate strategic print placement."""
    print("=== Strategic Print Debugging ===")

    def process_data(data):
        print(f">>> ENTRY: process_data(data={data})")  # Entry point

        try:
            results = []
            for i, item in enumerate(data):
                print(f"  Processing item {i}: {item}")  # Loop iteration

                processed = item * 2
                results.append(processed)

            print(f"<<< EXIT: process_data returning {results}")  # Exit point
            return results

        except Exception as e:
            print(f"!!! ERROR in process_data: {e}")  # Error case
            raise

    process_data([1, 2, 3])
    print()


def example_pdb_commands():
    """Show pdb commands (documentation)."""
    print("=== PDB Commands ===")

    commands = """
    Starting pdb:
      import pdb; pdb.set_trace()  # Add breakpoint
      python -m pdb script.py      # Run with pdb

    Navigation:
      n (next)     - Execute next line
      s (step)     - Step into function
      c (continue) - Continue until next breakpoint
      r (return)   - Continue until current function returns
      q (quit)     - Quit debugger

    Inspection:
      p expr       - Print expression
      pp expr      - Pretty print expression
      l (list)     - Show current code
      ll           - Show entire function
      w (where)    - Show stack trace
      u (up)       - Move up in stack
      d (down)     - Move down in stack

    Breakpoints:
      b line_num   - Set breakpoint at line
      b func_name  - Set breakpoint at function
      cl           - Clear breakpoints
      disable num  - Disable breakpoint
      enable num   - Enable breakpoint

    Variables:
      a (args)     - Print function arguments
      locals()     - Print local variables
      dir(obj)     - List object attributes
    """
    print(commands)


def example_pdb_usage():
    """Demonstrate pdb usage (in comments to avoid interactive mode)."""
    print("\n=== PDB Usage Example ===")

    def debug_example(x, y):
        """Example function with pdb breakpoint."""
        # To debug, uncomment the next line:
        # import pdb; pdb.set_trace()

        result = x + y
        result = result * 2
        return result

    # In actual debugging session:
    # >>> p x       # Print x
    # >>> p y       # Print y
    # >>> n         # Execute next line
    # >>> p result  # Print result after assignment

    result = debug_example(5, 3)
    print(f"Result: {result}")


def example_traceback_analysis():
    """Demonstrate traceback analysis."""
    print("\n=== Traceback Analysis ===")

    def level_3():
        return 1 / 0  # This will raise ZeroDivisionError

    def level_2():
        return level_3()

    def level_1():
        return level_2()

    try:
        level_1()
    except ZeroDivisionError:
        print("Caught exception. Traceback:")
        traceback.print_exc()
        print("\nAnalysis:")
        print("  - Error type: ZeroDivisionError")
        print("  - Location: level_3()")
        print("  - Call chain: level_1 -> level_2 -> level_3")


def example_debug_logging():
    """Demonstrate debug logging."""
    print("\n=== Debug Logging ===")

    import logging

    # Setup debug logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s:%(funcName)s:%(lineno)d - %(message)s')
    logger = logging.getLogger(__name__)

    def calculate(x, y, operation):
        logger.debug(f"Input: x={x}, y={y}, op={operation}")

        if operation == 'add':
            result = x + y
        elif operation == 'multiply':
            result = x * y
        else:
            logger.warning(f"Unknown operation: {operation}")
            result = None

        logger.debug(f"Result: {result}")
        return result

    calculate(5, 3, 'add')
    calculate(5, 3, 'unknown')


def example_common_bugs():
    """Demonstrate common bug patterns."""
    print("\n=== Common Bug Patterns ===")

    print("1. Off-by-one errors:")
    # Wrong: for i in range(1, len(arr))  # Misses first element
    # Right: for i in range(len(arr))

    print("2. Mutable default arguments:")
    def bad_append(item, lst=[]):  # Bug: shared list!
        lst.append(item)
        return lst
    print(f"   bad_append(1): {bad_append(1)}")
    print(f"   bad_append(2): {bad_append(2)}")  # Shows [1, 2]!

    print("\n3. Modifying while iterating:")
    # Wrong:
    # for item in items:
    #     if condition:
    #         items.remove(item)  # Bug!
    # Right: items = [item for item in items if not condition]

    print("4. Shallow vs deep copy:")
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    shallow[0][0] = 999
    print(f"   Original after shallow copy modify: {original}")  # Also modified!

    print("\n5. None comparisons:")
    value = None
    # Wrong: if value == None
    # Right: if value is None


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Debug the Bugs

    Fix the buggy functions defined above:
    - buggy_find_max: Fails for negative numbers
    - buggy_reverse_words: Misses first word
    - buggy_merge_dicts: Modifies original dict

    For each:
    1. Write a test that fails
    2. Use print debugging to find the bug
    3. Fix the bug
    4. Verify the fix
    """
    # YOUR CODE HERE

    # Test buggy_find_max
    print("Testing find_max with [-5, -2, -8]:")
    print(f"Result: {buggy_find_max([-5, -2, -8])}")  # Should be -2
    print()

    # Test buggy_reverse_words
    print("Testing reverse_words with 'hello world python':")
    print(f"Result: '{buggy_reverse_words('hello world python')}'")  # Should be 'python world hello'
    print()

    # Test buggy_merge_dicts
    d1 = {'a': 1}
    d2 = {'b': 2}
    result = buggy_merge_dicts(d1, d2)
    print(f"Merged: {result}")
    print(f"Original d1: {d1}")  # Should still be {'a': 1}


def exercise_2():
    """
    Exercise 2: Add Debug Logging

    Add comprehensive debug logging to this function:

    def process_orders(orders):
        total_revenue = 0
        processed = []

        for order in orders:
            if order['status'] == 'completed':
                subtotal = order['quantity'] * order['price']
                if order.get('discount'):
                    subtotal *= (1 - order['discount'])
                total_revenue += subtotal
                processed.append(order['id'])

        return {
            'total_revenue': total_revenue,
            'processed_count': len(processed),
            'processed_ids': processed
        }

    Add logging for:
    - Function entry/exit
    - Each order processing
    - Calculations
    - Skipped orders and why
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Create Debug Helper

    Create a debug helper class:

    class DebugHelper:
        def __init__(self, enabled=True):
            pass

        def log(self, message, level='info'):
            '''Log a debug message'''
            pass

        def watch(self, name, value):
            '''Watch a variable value'''
            pass

        def trace_call(self, func):
            '''Decorator to trace function calls'''
            pass

        def time_it(self, func):
            '''Decorator to time function execution'''
            pass

        def dump_locals(self):
            '''Dump all local variables from caller'''
            pass

    Usage:
    debug = DebugHelper(enabled=True)

    @debug.trace_call
    @debug.time_it
    def my_function(x, y):
        debug.watch('x', x)
        result = x + y
        return result
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Memory Debugging

    Create tools for debugging memory issues:

    class MemoryDebugger:
        def track_object(self, obj, name):
            '''Track an object for memory debugging'''
            pass

        def get_object_size(self, obj, deep=False):
            '''Get size of object in bytes'''
            pass

        def find_references(self, obj):
            '''Find all references to an object'''
            pass

        def get_stats(self):
            '''Get memory statistics'''
            pass

        def check_for_leaks(self):
            '''Check for potential memory leaks'''
            pass

    Hints:
    - Use sys.getsizeof() for object sizes
    - Use gc module for garbage collection info
    - Use weakref for tracking without preventing GC
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Build a Debug Toolkit

    Create a comprehensive debugging toolkit:

    1. Smart Logger:
       - Automatic function tracing
       - Variable watching
       - Conditional logging
       - Log file rotation

    2. Profiler:
       - Function timing
       - Call counting
       - Memory usage
       - Hotspot identification

    3. State Inspector:
       - Inspect object state at any point
       - Compare state between calls
       - Detect state changes

    4. Exception Analyzer:
       - Enhanced tracebacks
       - Local variables at error
       - Suggested fixes for common errors

    5. Interactive Debugger Helper:
       - Commands for common debug tasks
       - Breakpoint management
       - Watch expressions

    Example usage:

    toolkit = DebugToolkit()

    @toolkit.profile
    @toolkit.trace
    def complex_function(data):
        with toolkit.state_snapshot('initial'):
            # Process data
            pass

        toolkit.checkpoint('after_processing')

        return result

    # Get insights
    print(toolkit.get_profile_report())
    print(toolkit.get_trace_log())
    print(toolkit.compare_states('initial', 'after_processing'))

    # When exception occurs
    try:
        complex_function(bad_data)
    except Exception:
        toolkit.analyze_exception()
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 16: Debugging\n")
    print("=" * 50)

    # Run examples
    example_print_debugging()
    example_strategic_prints()
    example_pdb_commands()
    example_pdb_usage()
    example_traceback_analysis()
    example_debug_logging()
    example_common_bugs()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
