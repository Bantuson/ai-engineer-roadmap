"""
Day 4: CSV Processing
=====================
Learn to read, write, and manipulate CSV files.

Key concepts:
- csv.reader and csv.writer
- csv.DictReader and csv.DictWriter
- Handling headers
- Different delimiters
- Quoting options
"""

import csv
import os

# =============================================================================
# CONCEPT: CSV Basics
# =============================================================================

# Read CSV as lists
def read_csv_basic(filepath):
    """Read CSV file, return list of rows."""
    rows = []
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


# Read CSV as dictionaries
def read_csv_dict(filepath):
    """Read CSV file, return list of dicts with headers as keys."""
    rows = []
    with open(filepath, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(dict(row))
    return rows


# Write CSV from lists
def write_csv_basic(filepath, rows, headers=None):
    """Write rows to CSV file."""
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(rows)


# Write CSV from dictionaries
def write_csv_dict(filepath, rows, fieldnames):
    """Write list of dicts to CSV file."""
    with open(filepath, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_csv():
    """Demonstrate basic CSV operations."""
    print("=== Basic CSV Operations ===")

    # Create sample data
    headers = ['Name', 'Age', 'City']
    data = [
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Carol', '35', 'Chicago']
    ]

    # Write CSV
    write_csv_basic('people.csv', data, headers)
    print("Created people.csv")

    # Read CSV
    rows = read_csv_basic('people.csv')
    print("\nRead back:")
    for row in rows:
        print(row)


def example_dict_csv():
    """Demonstrate DictReader and DictWriter."""
    print("\n=== Dictionary-Based CSV ===")

    # Data as list of dicts
    employees = [
        {'id': '1', 'name': 'Alice', 'department': 'Engineering', 'salary': '75000'},
        {'id': '2', 'name': 'Bob', 'department': 'Sales', 'salary': '65000'},
        {'id': '3', 'name': 'Carol', 'department': 'Engineering', 'salary': '80000'}
    ]

    # Write using DictWriter
    fieldnames = ['id', 'name', 'department', 'salary']
    write_csv_dict('employees.csv', employees, fieldnames)
    print("Created employees.csv")

    # Read using DictReader
    loaded = read_csv_dict('employees.csv')
    print("\nRead back:")
    for emp in loaded:
        print(f"  {emp['name']}: ${emp['salary']} ({emp['department']})")


def example_filtering():
    """Demonstrate filtering CSV data."""
    print("\n=== Filtering CSV Data ===")

    employees = read_csv_dict('employees.csv')

    # Filter by department
    engineers = [e for e in employees if e['department'] == 'Engineering']
    print(f"Engineers: {[e['name'] for e in engineers]}")

    # Filter by salary
    high_earners = [e for e in employees if int(e['salary']) > 70000]
    print(f"Earning > $70k: {[e['name'] for e in high_earners]}")


def example_aggregation():
    """Demonstrate aggregating CSV data."""
    print("\n=== Aggregating CSV Data ===")

    employees = read_csv_dict('employees.csv')

    # Calculate statistics
    salaries = [int(e['salary']) for e in employees]
    total = sum(salaries)
    average = total / len(salaries)

    print(f"Total salaries: ${total:,}")
    print(f"Average salary: ${average:,.2f}")

    # Group by department
    dept_counts = {}
    for emp in employees:
        dept = emp['department']
        dept_counts[dept] = dept_counts.get(dept, 0) + 1

    print("Employees by department:")
    for dept, count in dept_counts.items():
        print(f"  {dept}: {count}")


def example_custom_delimiter():
    """Demonstrate CSV with custom delimiter."""
    print("\n=== Custom Delimiter (TSV) ===")

    # Write tab-separated values
    with open('data.tsv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Score'])
        writer.writerow(['Alice', '95'])
        writer.writerow(['Bob', '87'])

    # Read tab-separated values
    with open('data.tsv', 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            print(row)


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: CSV Merger

    Write a function that merges multiple CSV files with the same structure.
    Handle the case where files might have headers.

    Example:
    file1.csv: name,age
               Alice,30
    file2.csv: name,age
               Bob,25

    merged.csv: name,age
                Alice,30
                Bob,25
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Column Selector

    Write a function that creates a new CSV with only selected columns.

    Input: employees.csv with columns [id, name, department, salary]
    select_columns('employees.csv', 'selected.csv', ['name', 'salary'])

    Output: selected.csv with columns [name, salary]
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: CSV Sorter

    Write a function that sorts a CSV file by a specified column.
    Handle both string and numeric sorting.

    sort_csv('employees.csv', 'sorted.csv', 'salary', numeric=True, reverse=True)
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: CSV Transformer

    Write a function that applies a transformation to a CSV column.

    Example transformations:
    - uppercase: Convert column to uppercase
    - percentage: Multiply numeric column by 100 and add '%'
    - format_date: Convert date format

    transform_column('data.csv', 'output.csv', 'name', 'uppercase')
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: CSV Data Analyzer

    Create a comprehensive CSV analyzer with these features:

    1. info(filepath): Print basic info (rows, columns, column names, types)
    2. describe(filepath): Print statistics for numeric columns (min, max, mean, median)
    3. value_counts(filepath, column): Count unique values in a column
    4. filter(filepath, output, conditions): Filter rows based on conditions
    5. group_by(filepath, group_col, agg_col, agg_func): Group and aggregate
    6. join(file1, file2, output, on): Join two CSV files on a column

    Example usage:

    info('sales.csv')
    # Output:
    # Rows: 1000
    # Columns: 5 (date, product, quantity, price, region)

    describe('sales.csv')
    # Output:
    # quantity: min=1, max=100, mean=25.5, median=20
    # price: min=9.99, max=999.99, mean=75.50, median=49.99

    value_counts('sales.csv', 'region')
    # Output: {'North': 250, 'South': 300, 'East': 200, 'West': 250}

    filter('sales.csv', 'high_sales.csv', {'quantity': ('>', 50)})

    group_by('sales.csv', 'region', 'quantity', 'sum')
    # Output: {'North': 5000, 'South': 7500, ...}
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 4: CSV Processing\n")
    print("=" * 50)

    # Run examples
    example_basic_csv()
    example_dict_csv()
    example_filtering()
    example_aggregation()
    example_custom_delimiter()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()

    # Cleanup
    for f in ['people.csv', 'employees.csv', 'data.tsv']:
        if os.path.exists(f):
            os.remove(f)
