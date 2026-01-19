"""
Day 6: Logging
==============
Learn to implement proper logging for debugging and monitoring.

Key concepts:
- logging module basics
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Formatters and handlers
- File and console logging
- Structured logging
"""

import logging
import sys
import os

# =============================================================================
# CONCEPT: Logging Basics
# =============================================================================

# Basic configuration
def setup_basic_logging():
    """Setup basic console logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


# Logging with file output
def setup_file_logging(filepath):
    """Setup logging to both console and file."""
    logger = logging.getLogger('my_app')
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    # File handler
    file_handler = logging.FileHandler(filepath)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# =============================================================================
# EXAMPLES
# =============================================================================

def example_log_levels():
    """Demonstrate different log levels."""
    print("=== Log Levels ===")

    # Create a logger
    logger = logging.getLogger('levels_demo')
    logger.setLevel(logging.DEBUG)

    # Add console handler
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        logger.addHandler(handler)

    # Different levels
    logger.debug("Debug: Detailed information for diagnosing problems")
    logger.info("Info: Confirmation that things are working")
    logger.warning("Warning: Something unexpected happened")
    logger.error("Error: Serious problem, some function failed")
    logger.critical("Critical: Program may not be able to continue")


def example_formatted_logging():
    """Demonstrate formatted log messages."""
    print("\n=== Formatted Logging ===")

    logger = logging.getLogger('format_demo')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(funcName)s:%(lineno)d | %(message)s'
        ))
        logger.addHandler(handler)

    # Formatted messages
    user_id = 123
    action = "login"
    logger.info(f"User {user_id} performed {action}")

    # Using % formatting (traditional style)
    logger.info("Processing %d items in batch %s", 50, "A1")

    # Extra fields
    logger.info("Request processed", extra={'request_id': 'abc123'})


def example_exception_logging():
    """Demonstrate logging exceptions."""
    print("\n=== Exception Logging ===")

    logger = logging.getLogger('exception_demo')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        logger.addHandler(handler)

    try:
        result = 1 / 0
    except ZeroDivisionError:
        # Log with stack trace
        logger.exception("An error occurred during calculation")

    try:
        data = {'key': 'value'}
        value = data['missing']
    except KeyError as e:
        # Log error without stack trace
        logger.error(f"Missing key in data: {e}")


def example_context_logging():
    """Demonstrate logging with context."""
    print("\n=== Context Logging ===")

    # Custom logger with context
    class ContextLogger:
        def __init__(self, name, context=None):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)
            if not self.logger.handlers:
                handler = logging.StreamHandler()
                handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
                self.logger.addHandler(handler)
            self.context = context or {}

        def _format(self, message):
            if self.context:
                context_str = ' | '.join(f'{k}={v}' for k, v in self.context.items())
                return f"[{context_str}] {message}"
            return message

        def info(self, message):
            self.logger.info(self._format(message))

        def error(self, message):
            self.logger.error(self._format(message))

    # Usage
    logger = ContextLogger('context_demo', {'user_id': '123', 'session': 'abc'})
    logger.info("Processing request")
    logger.info("Request completed")


def example_file_logging():
    """Demonstrate file logging."""
    print("\n=== File Logging ===")

    # Setup
    log_file = 'app.log'
    logger = setup_file_logging(log_file)

    # Log messages
    logger.debug("This goes to file only")
    logger.info("This goes to both console and file")
    logger.error("Error message")

    # Show file contents
    print(f"\nContents of {log_file}:")
    with open(log_file, 'r') as f:
        print(f.read())

    # Cleanup
    os.remove(log_file)


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Configurable Logger

    Create a function that returns a configured logger based on settings.

    def create_logger(name, level='INFO', log_file=None, console=True):
        # Return configured logger
        pass

    Usage:
    logger = create_logger('my_app', level='DEBUG', log_file='app.log')
    logger.debug("Debug message")
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Request Logger

    Create a decorator that logs function calls with:
    - Function name
    - Arguments
    - Return value
    - Execution time
    - Any exceptions

    @log_calls(logger)
    def process_data(x, y):
        return x + y
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Rotating File Logger

    Create a logger that:
    - Writes to a file
    - Rotates when file exceeds a size limit
    - Keeps only the last N rotated files

    Hint: Use logging.handlers.RotatingFileHandler
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Structured JSON Logger

    Create a logger that outputs JSON-formatted log entries:

    {"timestamp": "2026-01-19T10:00:00", "level": "INFO",
     "message": "User logged in", "user_id": 123, "ip": "1.2.3.4"}

    Include support for extra fields passed at log time.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Application Logging System

    Create a comprehensive logging system for an application with:

    1. Multiple log levels per component (app, database, api, security)
    2. Different outputs:
       - Console: INFO and above, colored output
       - App file: all logs for the main app
       - Error file: ERROR and above from all components
       - Security file: all security logs
    3. Log rotation for all files
    4. Context managers for adding temporary context:

       with log_context(request_id='abc', user='alice'):
           logger.info("Processing")  # Includes request_id and user

    5. Performance logging:
       - Automatic timing of decorated functions
       - Slow operation warnings (configurable threshold)

    6. Error tracking:
       - Count errors by type
       - Alert when error rate exceeds threshold

    Example usage:

    log_system = AppLogging(config={
        'console_level': 'INFO',
        'file_level': 'DEBUG',
        'log_dir': './logs',
        'rotate_size': '10MB',
        'rotate_count': 5
    })

    app_logger = log_system.get_logger('app')
    db_logger = log_system.get_logger('database')

    app_logger.info("Application started")

    with log_system.context(user='alice'):
        app_logger.info("Processing request")

    @log_system.timed('api')
    def api_call():
        pass

    print(log_system.error_stats())
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 6: Logging\n")
    print("=" * 50)

    # Run examples
    example_log_levels()
    example_formatted_logging()
    example_exception_logging()
    example_context_logging()
    example_file_logging()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
