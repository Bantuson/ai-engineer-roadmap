"""
Day 1: File Reading
===================
Learn to read text files, iterate through lines, and process file content.

Key concepts:
- Opening files with open()
- Reading modes ('r', 'rb')
- Context managers (with statement)
- Iterating through lines
- Reading entire file vs. line by line
"""

# =============================================================================
# CONCEPT: Basic File Reading
# =============================================================================

# Reading entire file at once
def read_entire_file(filepath):
    """Read and return entire file content as a string."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content


# Reading file line by line (memory efficient for large files)
def read_lines(filepath):
    """Read file and return list of lines."""
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines


# Iterating through lines (most memory efficient)
def process_lines(filepath):
    """Process file line by line without loading entire file."""
    with open(filepath, 'r') as file:
        for line in file:
            # Remove trailing newline
            line = line.strip()
            print(f"Processing: {line}")


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_reading():
    """Demonstrate basic file reading."""
    # Create a sample file for demonstration
    sample_content = """Line 1: Hello, World!
Line 2: Python is great.
Line 3: File I/O is essential.
Line 4: Practice makes perfect."""

    # Write sample file
    with open('sample.txt', 'w') as f:
        f.write(sample_content)

    print("=== Reading Entire File ===")
    content = read_entire_file('sample.txt')
    print(content)
    print()

    print("=== Reading as Lines ===")
    lines = read_lines('sample.txt')
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")
    print()

    print("=== Processing Line by Line ===")
    process_lines('sample.txt')


def example_counting_words():
    """Count words in a file."""
    with open('sample.txt', 'r') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += len(words)
    print(f"Total words: {word_count}")


def example_finding_pattern():
    """Find lines containing a specific word."""
    search_word = "Python"
    print(f"\n=== Lines containing '{search_word}' ===")

    with open('sample.txt', 'r') as file:
        for line_num, line in enumerate(file, 1):
            if search_word in line:
                print(f"Line {line_num}: {line.strip()}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Line Counter

    Write a function that counts the number of non-empty lines in a file.

    Expected output for sample.txt: 4
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Character Counter

    Write a function that counts total characters (excluding newlines).

    Hint: Use len() on stripped lines
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Longest Line

    Write a function that finds and returns the longest line in a file.

    Return both the line content and its length.
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Line Filter

    Write a function that reads a file and returns only lines that:
    - Are not empty
    - Don't start with '#' (comments)
    - Have more than 5 characters
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: File Statistics

    Create a function that analyzes a text file and returns a dictionary with:
    - 'total_lines': total number of lines
    - 'empty_lines': number of empty lines
    - 'total_words': total word count
    - 'total_chars': total character count (excluding newlines)
    - 'avg_line_length': average line length
    - 'longest_word': the longest word in the file

    Example return:
    {
        'total_lines': 10,
        'empty_lines': 2,
        'total_words': 50,
        'total_chars': 300,
        'avg_line_length': 30.0,
        'longest_word': 'programming'
    }
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 1: File Reading\n")
    print("=" * 50)

    # Run examples
    example_basic_reading()
    example_counting_words()
    example_finding_pattern()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")
    print("Uncomment and run each exercise function to test.")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()

    # Cleanup
    import os
    if os.path.exists('sample.txt'):
        os.remove('sample.txt')
