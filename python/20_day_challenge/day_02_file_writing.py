"""
Day 2: File Writing
===================
Learn to write files, append content, and handle different write modes.

Key concepts:
- Write modes ('w', 'a', 'x')
- Writing strings vs. lines
- Flushing and closing files
- Atomic writes with temp files
"""

import os
import tempfile
import shutil

# =============================================================================
# CONCEPT: Basic File Writing
# =============================================================================

# Write mode - creates new file or overwrites existing
def write_file(filepath, content):
    """Write content to file (overwrites existing)."""
    with open(filepath, 'w') as file:
        file.write(content)


# Append mode - adds to existing file
def append_to_file(filepath, content):
    """Append content to file."""
    with open(filepath, 'a') as file:
        file.write(content)


# Write multiple lines
def write_lines(filepath, lines):
    """Write a list of lines to file."""
    with open(filepath, 'w') as file:
        for line in lines:
            file.write(line + '\n')


# Alternative: writelines (no automatic newlines)
def write_lines_alt(filepath, lines):
    """Write lines using writelines method."""
    with open(filepath, 'w') as file:
        file.writelines(line + '\n' for line in lines)


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_writing():
    """Demonstrate basic file writing."""
    print("=== Basic Write ===")

    # Write a simple file
    write_file('output.txt', 'Hello, World!\nThis is line 2.')

    # Read it back
    with open('output.txt', 'r') as f:
        print(f.read())


def example_append_mode():
    """Demonstrate append mode."""
    print("\n=== Append Mode ===")

    # Create initial file
    write_file('log.txt', 'Log started\n')

    # Append entries
    append_to_file('log.txt', 'Entry 1: User logged in\n')
    append_to_file('log.txt', 'Entry 2: File uploaded\n')
    append_to_file('log.txt', 'Entry 3: User logged out\n')

    # Read it back
    with open('log.txt', 'r') as f:
        print(f.read())


def example_write_lines():
    """Demonstrate writing multiple lines."""
    print("\n=== Write Lines ===")

    todos = [
        "Learn Python file I/O",
        "Practice exercises",
        "Complete challenge",
        "Review concepts"
    ]

    write_lines('todos.txt', todos)

    # Read it back
    with open('todos.txt', 'r') as f:
        print(f.read())


def example_atomic_write():
    """Demonstrate atomic write pattern for safety."""
    print("\n=== Atomic Write (Safe Pattern) ===")

    filepath = 'important_data.txt'
    new_content = "Critical data that must not be corrupted"

    # Write to temp file first, then rename
    # This ensures file is either old or new, never partial
    temp_fd, temp_path = tempfile.mkstemp()
    try:
        with os.fdopen(temp_fd, 'w') as temp_file:
            temp_file.write(new_content)
        # Atomic rename
        shutil.move(temp_path, filepath)
        print(f"Safely wrote to {filepath}")
    except Exception as e:
        os.unlink(temp_path)  # Clean up temp file on error
        raise e

    with open(filepath, 'r') as f:
        print(f"Content: {f.read()}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Config File Writer

    Write a function that creates a config file from a dictionary.
    Format: KEY=VALUE (one per line)

    Example input:
    {'database': 'postgres', 'port': '5432', 'host': 'localhost'}

    Expected output file:
    database=postgres
    port=5432
    host=localhost
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Log Rotator

    Write a function that:
    1. Reads an existing log file
    2. If it has more than 100 lines, move old content to 'log.old.txt'
    3. Keep only the last 50 lines in the original file

    This simulates basic log rotation.
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Numbered Lines

    Write a function that takes an input file and creates an output file
    with each line prefixed by its line number.

    Input:
    Hello
    World

    Output:
    1: Hello
    2: World
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: File Merger

    Write a function that merges multiple text files into one.
    Add a header comment showing the source file for each section.

    Output format:
    # --- From: file1.txt ---
    [content of file1]

    # --- From: file2.txt ---
    [content of file2]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Simple Database File

    Create a simple "database" using a text file with these operations:

    1. create_db(filepath): Create empty database file with header
    2. insert(filepath, record): Add a record (dict) as a new line
    3. read_all(filepath): Read all records as list of dicts
    4. find(filepath, field, value): Find records matching criteria
    5. delete(filepath, field, value): Delete matching records

    File format (CSV-like):
    # name,age,city
    Alice,30,NYC
    Bob,25,LA

    Example usage:
    create_db('people.db')
    insert('people.db', {'name': 'Alice', 'age': '30', 'city': 'NYC'})
    insert('people.db', {'name': 'Bob', 'age': '25', 'city': 'LA'})
    records = read_all('people.db')
    found = find('people.db', 'city', 'NYC')
    delete('people.db', 'name', 'Bob')
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 2: File Writing\n")
    print("=" * 50)

    # Run examples
    example_basic_writing()
    example_append_mode()
    example_write_lines()
    example_atomic_write()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()

    # Cleanup
    for f in ['output.txt', 'log.txt', 'todos.txt', 'important_data.txt']:
        if os.path.exists(f):
            os.remove(f)
