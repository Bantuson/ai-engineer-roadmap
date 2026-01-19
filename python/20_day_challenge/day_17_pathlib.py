"""
Day 17: Pathlib
===============
Learn modern path handling with pathlib.

Key concepts:
- Path objects vs strings
- Path operations (join, parent, stem)
- File operations with Path
- Cross-platform paths
- Glob patterns with Path
"""

from pathlib import Path
import os
import tempfile
import shutil

# =============================================================================
# CONCEPT: Path Basics
# =============================================================================

def path_basics():
    """Basic pathlib concepts."""

    # Creating paths
    p1 = Path('/home/user/documents')
    p2 = Path('relative/path')
    p3 = Path.cwd()  # Current working directory
    p4 = Path.home()  # User's home directory

    return p1, p2, p3, p4


# =============================================================================
# EXAMPLES
# =============================================================================

def example_creating_paths():
    """Demonstrate creating and combining paths."""
    print("=== Creating Paths ===")

    # From string
    p1 = Path('/home/user/documents')
    print(f"From string: {p1}")

    # Join paths with /
    p2 = Path('/home') / 'user' / 'documents'
    print(f"Joined with /: {p2}")

    # From current directory
    cwd = Path.cwd()
    print(f"Current directory: {cwd}")

    # Home directory
    home = Path.home()
    print(f"Home directory: {home}")

    # Relative to current
    relative = Path('.')
    absolute = relative.resolve()
    print(f"Resolved: {absolute}")


def example_path_parts():
    """Demonstrate accessing path components."""
    print("\n=== Path Components ===")

    p = Path('/home/user/documents/report.txt')

    print(f"Full path: {p}")
    print(f"Name: {p.name}")           # report.txt
    print(f"Stem: {p.stem}")           # report
    print(f"Suffix: {p.suffix}")       # .txt
    print(f"Parent: {p.parent}")       # /home/user/documents
    print(f"Parents: {list(p.parents)}")
    print(f"Parts: {p.parts}")         # ('/', 'home', 'user', 'documents', 'report.txt')

    # Multiple extensions
    p2 = Path('archive.tar.gz')
    print(f"\nMultiple extensions: {p2.suffixes}")  # ['.tar', '.gz']


def example_path_operations():
    """Demonstrate path operations."""
    print("\n=== Path Operations ===")

    # Create temp directory for demos
    temp_dir = Path(tempfile.mkdtemp())
    print(f"Working in: {temp_dir}")

    # Create paths
    file_path = temp_dir / 'test.txt'
    sub_dir = temp_dir / 'subdir'

    # Check existence
    print(f"\nFile exists: {file_path.exists()}")

    # Create file
    file_path.write_text("Hello, World!")
    print(f"File exists after write: {file_path.exists()}")

    # Create directory
    sub_dir.mkdir()
    print(f"Directory exists: {sub_dir.exists()}")
    print(f"Is directory: {sub_dir.is_dir()}")
    print(f"Is file: {file_path.is_file()}")

    # Change extension
    json_path = file_path.with_suffix('.json')
    print(f"Changed extension: {json_path}")

    # Change name
    new_name = file_path.with_name('renamed.txt')
    print(f"Changed name: {new_name}")

    # Cleanup
    shutil.rmtree(temp_dir)


def example_reading_writing():
    """Demonstrate reading and writing with Path."""
    print("\n=== Reading and Writing ===")

    # Create temp directory
    temp_dir = Path(tempfile.mkdtemp())
    file_path = temp_dir / 'data.txt'

    # Write text
    file_path.write_text("Line 1\nLine 2\nLine 3")
    print(f"Wrote to: {file_path}")

    # Read text
    content = file_path.read_text()
    print(f"Content:\n{content}")

    # Write bytes
    binary_path = temp_dir / 'data.bin'
    binary_path.write_bytes(b'\x00\x01\x02\x03')
    print(f"\nWrote bytes to: {binary_path}")

    # Read bytes
    data = binary_path.read_bytes()
    print(f"Bytes: {data}")

    # Cleanup
    shutil.rmtree(temp_dir)


def example_directory_iteration():
    """Demonstrate iterating over directories."""
    print("\n=== Directory Iteration ===")

    # Create temp structure
    temp_dir = Path(tempfile.mkdtemp())
    (temp_dir / 'file1.txt').touch()
    (temp_dir / 'file2.py').touch()
    (temp_dir / 'file3.txt').touch()
    (temp_dir / 'subdir').mkdir()
    (temp_dir / 'subdir' / 'file4.txt').touch()

    print(f"Contents of {temp_dir.name}/:")

    # iterdir - immediate children only
    print("\nUsing iterdir():")
    for item in temp_dir.iterdir():
        item_type = "DIR" if item.is_dir() else "FILE"
        print(f"  [{item_type}] {item.name}")

    # glob - pattern matching
    print("\nUsing glob('*.txt'):")
    for item in temp_dir.glob('*.txt'):
        print(f"  {item.name}")

    # rglob - recursive glob
    print("\nUsing rglob('*.txt') (recursive):")
    for item in temp_dir.rglob('*.txt'):
        print(f"  {item.relative_to(temp_dir)}")

    # Cleanup
    shutil.rmtree(temp_dir)


def example_file_info():
    """Demonstrate getting file information."""
    print("\n=== File Information ===")

    # Create temp file
    temp_dir = Path(tempfile.mkdtemp())
    file_path = temp_dir / 'info.txt'
    file_path.write_text("Some content here")

    # Get stats
    stats = file_path.stat()
    print(f"File: {file_path.name}")
    print(f"Size: {stats.st_size} bytes")
    print(f"Modified: {stats.st_mtime}")
    print(f"Created: {stats.st_ctime}")

    # Check permissions
    print(f"\nReadable: {os.access(file_path, os.R_OK)}")
    print(f"Writable: {os.access(file_path, os.W_OK)}")
    print(f"Executable: {os.access(file_path, os.X_OK)}")

    # Cleanup
    shutil.rmtree(temp_dir)


def example_practical_patterns():
    """Demonstrate practical patterns with pathlib."""
    print("\n=== Practical Patterns ===")

    # Create project structure
    project = Path(tempfile.mkdtemp()) / 'my_project'
    project.mkdir()

    (project / 'src').mkdir()
    (project / 'tests').mkdir()
    (project / 'src' / '__init__.py').touch()
    (project / 'src' / 'main.py').write_text('def main(): pass')
    (project / 'tests' / 'test_main.py').write_text('def test_main(): pass')
    (project / 'README.md').write_text('# Project')
    (project / 'config.json').write_text('{}')

    # Pattern 1: Find all Python files
    print("Python files:")
    for py_file in project.rglob('*.py'):
        print(f"  {py_file.relative_to(project)}")

    # Pattern 2: Get project root from any file
    def find_project_root(path, marker='README.md'):
        for parent in [path] + list(path.parents):
            if (parent / marker).exists():
                return parent
        return None

    some_file = project / 'src' / 'main.py'
    root = find_project_root(some_file)
    print(f"\nProject root: {root.name}")

    # Pattern 3: Ensure directory exists
    def ensure_dir(path):
        Path(path).mkdir(parents=True, exist_ok=True)
        return Path(path)

    output_dir = ensure_dir(project / 'output' / 'reports')
    print(f"Created: {output_dir.relative_to(project)}")

    # Pattern 4: Unique filename
    def unique_path(path):
        """Get unique path by adding number suffix."""
        original = Path(path)
        if not original.exists():
            return original

        counter = 1
        while True:
            new_path = original.with_stem(f"{original.stem}_{counter}")
            if not new_path.exists():
                return new_path
            counter += 1

    # Cleanup
    shutil.rmtree(project.parent)


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Path Utilities

    Create a PathUtils class with these methods:

    class PathUtils:
        @staticmethod
        def normalize(path):
            '''Normalize path (resolve .., remove trailing slash, etc.)'''
            pass

        @staticmethod
        def common_parent(*paths):
            '''Find common parent of multiple paths'''
            pass

        @staticmethod
        def relative_to_if_possible(path, base):
            '''Return relative path if possible, else absolute'''
            pass

        @staticmethod
        def split_extension(path):
            '''Split path into (base, all_extensions)
            split_extension('file.tar.gz') -> ('file', ['.tar', '.gz'])
            '''
            pass
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: File Finder

    Create a FileFinder class for advanced file searching:

    finder = FileFinder('/path/to/search')

    # Find by patterns
    finder.find('*.py')
    finder.find('*.py', recursive=True)
    finder.find(['*.py', '*.js'])

    # Find with filters
    finder.find('*', min_size=1024, max_size=1024*1024)
    finder.find('*', modified_after=datetime(2026, 1, 1))
    finder.find('*', contains='import')

    # Combined
    finder.find(
        '*.log',
        recursive=True,
        modified_after=datetime(2026, 1, 1),
        max_size=10*1024*1024
    )
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Directory Diff

    Create a function that compares two directories:

    def diff_directories(dir1, dir2):
        '''Compare two directories.

        Returns:
        {
            'only_in_first': [paths only in dir1],
            'only_in_second': [paths only in dir2],
            'different': [paths that exist in both but differ],
            'same': [paths that are identical]
        }
        '''
        pass

    Use:
    - File existence
    - File size
    - File content hash (for 'different' vs 'same')
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Path Template

    Create a path template system for organizing files:

    template = PathTemplate('{year}/{month:02d}/{category}/{name}.{ext}')

    # Generate paths
    path = template.format(
        year=2026,
        month=1,
        category='reports',
        name='sales',
        ext='pdf'
    )
    # Result: '2026/01/reports/sales.pdf'

    # Parse paths
    data = template.parse('2026/01/reports/sales.pdf')
    # Result: {'year': '2026', 'month': '01', 'category': 'reports', 'name': 'sales', 'ext': 'pdf'}

    # Organize files
    template.organize_file('my_file.txt', year=2026, month=1, category='docs')
    # Moves file to 2026/01/docs/my_file.txt
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: File Management System

    Create a comprehensive file management system:

    1. FileManager class:
       - Copy, move, delete files with safety checks
       - Backup before destructive operations
       - Atomic operations (temp file + rename)
       - Progress callbacks for large operations

    2. DirectoryWatcher:
       - Monitor directory for changes
       - Callbacks for create, modify, delete events
       - Filter by patterns
       - Debounce rapid changes

    3. FileOrganizer:
       - Organize files by rules (date, type, name pattern)
       - Undo capability
       - Dry run mode
       - Handle duplicates

    4. DiskUsageAnalyzer:
       - Calculate directory sizes
       - Find largest files
       - Find duplicate files
       - Age analysis (old files)

    Example usage:

    # File operations
    fm = FileManager()
    fm.copy('file.txt', 'backup/', with_backup=True)
    fm.move_batch(['a.txt', 'b.txt'], 'archive/', on_progress=callback)

    # Watch for changes
    watcher = DirectoryWatcher('./src')
    watcher.on('*.py', 'modified', lambda p: print(f'Changed: {p}'))
    watcher.start()

    # Organize files
    organizer = FileOrganizer('./downloads')
    organizer.add_rule('*.pdf', '{year}/{month}/documents/')
    organizer.add_rule('*.jpg', 'photos/{year}/')
    organizer.organize(dry_run=True)

    # Analyze disk usage
    analyzer = DiskUsageAnalyzer('./home')
    print(analyzer.get_size())
    print(analyzer.largest_files(10))
    print(analyzer.find_duplicates())
    print(analyzer.files_older_than(days=365))
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 17: Pathlib\n")
    print("=" * 50)

    # Run examples
    example_creating_paths()
    example_path_parts()
    example_path_operations()
    example_reading_writing()
    example_directory_iteration()
    example_file_info()
    example_practical_patterns()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
