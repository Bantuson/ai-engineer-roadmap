"""
Day 10: Command-Line Arguments
==============================
Learn to build command-line tools using argparse.

Key concepts:
- argparse basics
- Positional and optional arguments
- Subcommands
- Argument types and choices
- Help text and documentation
"""

import argparse
import sys

# =============================================================================
# CONCEPT: Basic Argparse
# =============================================================================

def create_basic_parser():
    """Create a basic argument parser."""
    parser = argparse.ArgumentParser(
        description='A simple example program',
        epilog='Example: python script.py input.txt -o output.txt'
    )

    # Positional argument (required)
    parser.add_argument('input', help='Input file path')

    # Optional argument with short and long form
    parser.add_argument('-o', '--output', help='Output file path')

    # Flag (boolean)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')

    # Optional with default
    parser.add_argument('-n', '--count', type=int, default=10,
                        help='Number of items (default: 10)')

    return parser


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_parsing():
    """Demonstrate basic argument parsing."""
    print("=== Basic Argument Parsing ===")

    parser = create_basic_parser()

    # Simulate command line: script.py input.txt -o output.txt -v -n 5
    args = parser.parse_args(['input.txt', '-o', 'output.txt', '-v', '-n', '5'])

    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Verbose: {args.verbose}")
    print(f"Count: {args.count}")


def example_argument_types():
    """Demonstrate different argument types."""
    print("\n=== Argument Types ===")

    parser = argparse.ArgumentParser()

    # Integer
    parser.add_argument('--count', type=int, help='An integer')

    # Float
    parser.add_argument('--rate', type=float, help='A float')

    # Choice from list
    parser.add_argument('--format', choices=['json', 'csv', 'xml'],
                        help='Output format')

    # Multiple values (nargs)
    parser.add_argument('--files', nargs='+', help='One or more files')

    # Optional multiple values
    parser.add_argument('--tags', nargs='*', help='Zero or more tags')

    args = parser.parse_args([
        '--count', '5',
        '--rate', '0.5',
        '--format', 'json',
        '--files', 'a.txt', 'b.txt',
        '--tags', 'tag1', 'tag2'
    ])

    print(f"Count: {args.count} (type: {type(args.count).__name__})")
    print(f"Rate: {args.rate}")
    print(f"Format: {args.format}")
    print(f"Files: {args.files}")
    print(f"Tags: {args.tags}")


def example_mutually_exclusive():
    """Demonstrate mutually exclusive arguments."""
    print("\n=== Mutually Exclusive Arguments ===")

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    # Only one can be used
    args = parser.parse_args(['-v'])
    print(f"Verbose: {args.verbose}, Quiet: {args.quiet}")

    # This would error: parser.parse_args(['-v', '-q'])


def example_subcommands():
    """Demonstrate subcommands."""
    print("\n=== Subcommands ===")

    parser = argparse.ArgumentParser(description='File management tool')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # 'copy' subcommand
    copy_parser = subparsers.add_parser('copy', help='Copy files')
    copy_parser.add_argument('source', help='Source file')
    copy_parser.add_argument('dest', help='Destination')

    # 'delete' subcommand
    delete_parser = subparsers.add_parser('delete', help='Delete files')
    delete_parser.add_argument('file', help='File to delete')
    delete_parser.add_argument('-f', '--force', action='store_true')

    # 'list' subcommand
    list_parser = subparsers.add_parser('list', help='List files')
    list_parser.add_argument('path', nargs='?', default='.')
    list_parser.add_argument('-l', '--long', action='store_true')

    # Parse different commands
    print("copy file1.txt file2.txt:")
    args = parser.parse_args(['copy', 'file1.txt', 'file2.txt'])
    print(f"  Command: {args.command}, Source: {args.source}, Dest: {args.dest}")

    print("delete -f temp.txt:")
    args = parser.parse_args(['delete', '-f', 'temp.txt'])
    print(f"  Command: {args.command}, File: {args.file}, Force: {args.force}")

    print("list -l /home:")
    args = parser.parse_args(['list', '-l', '/home'])
    print(f"  Command: {args.command}, Path: {args.path}, Long: {args.long}")


def example_custom_validation():
    """Demonstrate custom argument validation."""
    print("\n=== Custom Validation ===")

    def positive_int(value):
        """Custom type that validates positive integers."""
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        return ivalue

    def valid_percentage(value):
        """Custom type for percentages 0-100."""
        fvalue = float(value)
        if not 0 <= fvalue <= 100:
            raise argparse.ArgumentTypeError(f"{value} is not a valid percentage (0-100)")
        return fvalue

    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=positive_int, default=1)
    parser.add_argument('--threshold', type=valid_percentage, default=50.0)

    args = parser.parse_args(['--workers', '4', '--threshold', '75.5'])
    print(f"Workers: {args.workers}")
    print(f"Threshold: {args.threshold}%")


def example_file_arguments():
    """Demonstrate file type arguments."""
    print("\n=== File Arguments ===")

    parser = argparse.ArgumentParser()

    # File for reading
    parser.add_argument('--input', type=argparse.FileType('r'),
                        help='Input file')

    # File for writing
    parser.add_argument('--output', type=argparse.FileType('w'),
                        help='Output file')

    # We'll skip actual file opening in this demo
    print("FileType arguments automatically open files for you")
    print("Example: --input data.txt opens data.txt for reading")


def example_complete_cli():
    """Demonstrate a complete CLI tool structure."""
    print("\n=== Complete CLI Tool ===")

    def main(args=None):
        parser = argparse.ArgumentParser(
            prog='mytool',
            description='A complete example CLI tool',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Examples:
  mytool process data.csv --format json
  mytool analyze --verbose --output report.txt
  mytool config set key value
            '''
        )

        parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
        parser.add_argument('-v', '--verbose', action='count', default=0,
                            help='Increase verbosity (-v, -vv, -vvv)')

        subparsers = parser.add_subparsers(dest='command', required=True)

        # Process command
        process_p = subparsers.add_parser('process', help='Process files')
        process_p.add_argument('file', help='File to process')
        process_p.add_argument('--format', choices=['json', 'csv'], default='json')

        # Analyze command
        analyze_p = subparsers.add_parser('analyze', help='Analyze data')
        analyze_p.add_argument('--output', '-o', help='Output file')

        # Config command with nested subcommands
        config_p = subparsers.add_parser('config', help='Manage configuration')
        config_sub = config_p.add_subparsers(dest='config_action')
        config_set = config_sub.add_parser('set', help='Set a config value')
        config_set.add_argument('key')
        config_set.add_argument('value')
        config_get = config_sub.add_parser('get', help='Get a config value')
        config_get.add_argument('key')

        parsed = parser.parse_args(args)

        # Handle commands
        print(f"Verbosity level: {parsed.verbose}")
        print(f"Command: {parsed.command}")

        if parsed.command == 'process':
            print(f"Processing {parsed.file} as {parsed.format}")
        elif parsed.command == 'analyze':
            print(f"Analyzing, output to: {parsed.output}")
        elif parsed.command == 'config':
            if parsed.config_action == 'set':
                print(f"Setting {parsed.key}={parsed.value}")
            elif parsed.config_action == 'get':
                print(f"Getting {parsed.key}")

    # Demo calls
    print("mytool -vv process data.csv --format csv:")
    main(['-vv', 'process', 'data.csv', '--format', 'csv'])

    print("\nmytool config set theme dark:")
    main(['config', 'set', 'theme', 'dark'])


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: File Converter CLI

    Create a CLI for converting files between formats:

    converter input.csv output.json --format json
    converter input.json output.csv --format csv
    converter input.txt --to-uppercase -o output.txt

    Arguments:
    - input: Input file (required)
    - output: Output file (optional, defaults to stdout)
    - --format: Output format (json, csv, txt)
    - --to-uppercase: Convert text to uppercase
    - --to-lowercase: Convert text to lowercase
    - --pretty: Pretty print output (for JSON)
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Task Manager CLI

    Create a task manager CLI:

    tasks add "Buy groceries" --priority high --due 2026-01-20
    tasks list --status pending --priority high
    tasks complete 1
    tasks delete 1 --force

    Subcommands:
    - add: Add a new task
    - list: List tasks with filters
    - complete: Mark task as complete
    - delete: Delete a task
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: API Client CLI

    Create a CLI for making API requests:

    api get https://api.example.com/users
    api post https://api.example.com/users --data '{"name": "Alice"}'
    api get https://api.example.com/users --header "Authorization: Bearer token"

    Features:
    - Subcommands for HTTP methods (get, post, put, delete)
    - --data/-d for request body
    - --header/-H for headers (can be repeated)
    - --output/-o to save response to file
    - --verbose/-v for detailed output
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Environment Manager CLI

    Create a CLI for managing environment configurations:

    envman create production
    envman switch development
    envman set DATABASE_URL "postgres://..."
    envman get DATABASE_URL
    envman list
    envman export production --format env
    envman import .env --into staging

    Features:
    - Multiple environment support
    - Variable encryption for secrets (--secret flag)
    - Export to different formats (.env, JSON, shell)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Build a Complete CLI Application

    Create a full-featured CLI application for a "Note Taking" system:

    notes new "My First Note" --tags work,important
    notes list --tag work --since 2026-01-01
    notes show 1
    notes edit 1
    notes delete 1 --force
    notes search "keyword" --in title,content
    notes export --format markdown --output notes.md
    notes import notes.json
    notes tags list
    notes tags rename old-tag new-tag
    notes stats

    Features to implement:

    1. Note Management:
       - Create, read, update, delete notes
       - Tags support
       - Search functionality

    2. Data Persistence:
       - Store notes in JSON file
       - Support import/export

    3. Advanced Features:
       - Colored output (use ANSI codes or colorama)
       - Interactive mode for editing
       - Fuzzy search
       - Statistics (notes by tag, by date, etc.)

    4. User Experience:
       - Helpful error messages
       - Confirmation prompts for destructive actions
       - Progress indicators for long operations
       - Tab completion support (bonus)

    5. Configuration:
       - Config file for defaults (~/.notesrc)
       - --config flag to specify config file
       - Environment variable overrides

    The main function should be:

    def main():
        parser = create_parser()
        args = parser.parse_args()
        # Route to appropriate handler
        # Handle errors gracefully
        # Return appropriate exit codes

    if __name__ == '__main__':
        sys.exit(main())
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 10: Command-Line Arguments\n")
    print("=" * 50)

    # Run examples
    example_basic_parsing()
    example_argument_types()
    example_mutually_exclusive()
    example_subcommands()
    example_custom_validation()
    example_file_arguments()
    example_complete_cli()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
