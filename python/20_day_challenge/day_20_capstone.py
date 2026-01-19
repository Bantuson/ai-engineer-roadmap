"""
Day 20: Capstone Project - Build Your Own Tool
==============================================
Final day challenge: Build a complete Python tool from scratch.

Choose one of the projects below (or create your own!) and implement
it using all the skills you've learned in the past 19 days.
"""

# =============================================================================
# CAPSTONE OPTIONS
# =============================================================================

"""
OPTION 1: Log Analyzer
======================

Build a comprehensive log file analyzer that:

1. Reads and parses various log formats:
   - Apache/Nginx access logs
   - Application logs (with timestamps and levels)
   - JSON-formatted logs
   - Custom formats (configurable)

2. Analyzes and reports:
   - Error rate over time
   - Most common errors
   - Slowest requests
   - Traffic patterns
   - Anomaly detection (unusual patterns)

3. Features:
   - Real-time tail mode
   - Multiple file support
   - Filtering by date range, level, pattern
   - Export to CSV/JSON
   - Generate HTML reports with charts

4. CLI Interface:
   loganalyzer parse access.log --format nginx
   loganalyzer stats access.log --top-errors 10
   loganalyzer tail -f /var/log/app.log --filter ERROR
   loganalyzer report access.log --output report.html

Skills used:
- File reading (Day 1)
- JSON/CSV (Day 3-4)
- Regex (Day 7-8)
- CLI args (Day 10)
- Datetime (Day 18)
"""

def log_analyzer_starter():
    """Starter code for Log Analyzer."""

    class LogEntry:
        """Represents a parsed log entry."""
        def __init__(self, timestamp, level, message, metadata=None):
            self.timestamp = timestamp
            self.level = level
            self.message = message
            self.metadata = metadata or {}

    class LogParser:
        """Parse various log formats."""

        def parse_line(self, line, format_type):
            """Parse a single log line."""
            # Implement parsing logic
            pass

    class LogAnalyzer:
        """Analyze parsed logs."""

        def __init__(self):
            self.entries = []

        def load(self, filepath, format_type='auto'):
            """Load and parse a log file."""
            pass

        def filter(self, level=None, start_time=None, end_time=None, pattern=None):
            """Filter log entries."""
            pass

        def error_rate(self, interval='hour'):
            """Calculate error rate over time."""
            pass

        def top_errors(self, n=10):
            """Get most common errors."""
            pass

        def generate_report(self, output_path):
            """Generate analysis report."""
            pass

    # YOUR IMPLEMENTATION HERE
    pass


"""
OPTION 2: Task Automation Framework
===================================

Build a task automation framework that:

1. Defines tasks with dependencies:
   - Task definition (function + metadata)
   - Dependency resolution
   - Parallel execution where possible
   - Retry on failure

2. Features:
   - YAML/JSON task definitions
   - Variables and templating
   - Conditional execution
   - Scheduled runs
   - Email notifications on failure

3. Built-in tasks:
   - File operations (copy, move, delete)
   - HTTP requests
   - Shell commands
   - Database queries

4. CLI Interface:
   taskrunner run build
   taskrunner run deploy --env production
   taskrunner list
   taskrunner show build --deps
   taskrunner schedule "0 9 * * *" backup

Skills used:
- JSON/YAML config (Day 3)
- Error handling (Day 5)
- Logging (Day 6)
- CLI args (Day 10)
- API requests (Day 11-12)
"""

def task_framework_starter():
    """Starter code for Task Automation Framework."""

    class Task:
        """Represents an automation task."""

        def __init__(self, name, action, depends_on=None, retries=0):
            self.name = name
            self.action = action
            self.depends_on = depends_on or []
            self.retries = retries
            self.status = 'pending'

        def run(self, context):
            """Execute the task."""
            pass

    class TaskRunner:
        """Execute tasks with dependency resolution."""

        def __init__(self):
            self.tasks = {}
            self.context = {}

        def register(self, task):
            """Register a task."""
            self.tasks[task.name] = task

        def load_from_file(self, filepath):
            """Load task definitions from file."""
            pass

        def resolve_dependencies(self, task_name):
            """Get tasks in execution order."""
            pass

        def run(self, task_name):
            """Run a task and its dependencies."""
            pass

    # YOUR IMPLEMENTATION HERE
    pass


"""
OPTION 3: Personal API Client Generator
=======================================

Build a tool that generates Python API clients from specifications:

1. Input formats:
   - OpenAPI/Swagger spec
   - Simple YAML definition
   - Auto-discover from base URL

2. Generated client features:
   - Type hints
   - Authentication handling
   - Retry logic
   - Caching
   - Response parsing

3. CLI Interface:
   apigen create --spec api.yaml --output my_client.py
   apigen discover https://api.example.com --output client/
   apigen test my_client.py

4. Generated code example:
   ```python
   client = GeneratedAPI(base_url="...", api_key="...")
   users = client.get_users(page=1)
   user = client.create_user(name="Alice", email="...")
   ```

Skills used:
- JSON/YAML parsing (Day 3)
- File writing (Day 2)
- HTTP requests (Day 11-12)
- Regex for parsing (Day 7-8)
- Data validation (Day 14)
"""

def api_generator_starter():
    """Starter code for API Client Generator."""

    class APISpec:
        """Represents an API specification."""

        def __init__(self):
            self.base_url = ""
            self.endpoints = []
            self.auth_type = None
            self.models = {}

        @classmethod
        def from_openapi(cls, spec_path):
            """Load from OpenAPI spec."""
            pass

        @classmethod
        def from_yaml(cls, yaml_path):
            """Load from simple YAML definition."""
            pass

    class ClientGenerator:
        """Generate Python client code from spec."""

        def __init__(self, spec):
            self.spec = spec

        def generate(self, output_path):
            """Generate client code."""
            pass

        def _generate_method(self, endpoint):
            """Generate code for a single endpoint."""
            pass

        def _generate_model(self, model):
            """Generate code for a data model."""
            pass

    # YOUR IMPLEMENTATION HERE
    pass


"""
OPTION 4: Data Pipeline Tool
============================

Build a data processing pipeline tool:

1. Pipeline definition:
   - Source (file, API, database)
   - Transformations (filter, map, aggregate)
   - Destination (file, API, database)

2. Transformations:
   - Filter rows by condition
   - Map/transform fields
   - Aggregate (group by, sum, count)
   - Join multiple sources
   - Deduplicate

3. Features:
   - Streaming for large files
   - Progress reporting
   - Checkpoint/resume
   - Validation at each step
   - Error handling with dead letter queue

4. CLI Interface:
   datapipe run pipeline.yaml
   datapipe validate pipeline.yaml
   datapipe preview pipeline.yaml --limit 10

Skills used:
- File I/O (Day 1-2)
- JSON/CSV (Day 3-4)
- Error handling (Day 5)
- Data validation (Day 14)
- CLI args (Day 10)
"""

def data_pipeline_starter():
    """Starter code for Data Pipeline Tool."""

    class DataSource:
        """Base class for data sources."""

        def read(self):
            """Yield data records."""
            raise NotImplementedError

    class CSVSource(DataSource):
        """Read from CSV file."""

        def __init__(self, filepath, **options):
            self.filepath = filepath
            self.options = options

        def read(self):
            pass

    class Transform:
        """Base class for transformations."""

        def apply(self, record):
            """Transform a single record."""
            raise NotImplementedError

    class FilterTransform(Transform):
        """Filter records by condition."""

        def __init__(self, condition):
            self.condition = condition

        def apply(self, record):
            pass

    class Pipeline:
        """Data processing pipeline."""

        def __init__(self):
            self.source = None
            self.transforms = []
            self.destination = None

        def add_transform(self, transform):
            self.transforms.append(transform)

        def run(self):
            """Execute the pipeline."""
            pass

    # YOUR IMPLEMENTATION HERE
    pass


# =============================================================================
# CAPSTONE TEMPLATE
# =============================================================================

"""
YOUR CUSTOM PROJECT
===================

If you have your own idea, use this template to structure it:

1. Problem statement: What does your tool solve?
2. Features: What can it do?
3. Interface: How do users interact with it?
4. Skills used: Which days' learnings does it incorporate?

Requirements:
- Use at least 10 concepts from the 19 days
- Include proper error handling
- Include logging
- Include CLI interface
- Include configuration file support
- Include tests (at least basic)
- Include documentation (docstrings, --help)
"""

def custom_project_template():
    """Template for custom capstone project."""

    # Configuration
    class Config:
        """Application configuration."""
        pass

    # Core logic
    class MainClass:
        """Main functionality."""

        def __init__(self, config):
            self.config = config

        def main_method(self):
            """Primary operation."""
            pass

    # CLI interface
    def create_parser():
        """Create argument parser."""
        pass

    def main():
        """Entry point."""
        pass

    # YOUR IMPLEMENTATION HERE
    pass


# =============================================================================
# EVALUATION CRITERIA
# =============================================================================

"""
Your capstone will be evaluated on:

1. Functionality (40%)
   - Does it work correctly?
   - Does it handle edge cases?
   - Are errors handled gracefully?

2. Code Quality (30%)
   - Is the code clean and readable?
   - Is it well-organized?
   - Are functions/classes appropriately sized?
   - Is there code duplication?

3. Skills Integration (20%)
   - How many course concepts are used?
   - Are they used appropriately?
   - Is the solution elegant?

4. Documentation (10%)
   - Clear docstrings?
   - Helpful --help output?
   - Usage examples?

Bonus points:
- Tests included
- Goes beyond requirements
- Particularly creative solution
"""

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Day 20: Capstone Project")
    print("=" * 60)

    print("""
CONGRATULATIONS on reaching Day 20!

For your capstone, choose one of these projects:

1. Log Analyzer
   - Parse and analyze log files
   - Generate reports and statistics

2. Task Automation Framework
   - Define and run automated tasks
   - Handle dependencies and retries

3. API Client Generator
   - Generate Python clients from API specs
   - Include auth, caching, retries

4. Data Pipeline Tool
   - Build data processing pipelines
   - Transform and validate data

5. Your Own Project
   - Create something that interests you!
   - Use skills from at least 10 days

Requirements:
- Error handling
- Logging
- CLI interface
- Configuration file support
- Documentation

Take your time to build something you're proud of!

Start by:
1. Choosing your project
2. Sketching out the design
3. Implementing core functionality
4. Adding CLI and config
5. Testing thoroughly
6. Documenting

Good luck!
    """)

    # If you want to test your implementation, add code here
    # Example:
    # analyzer = LogAnalyzer()
    # analyzer.load('sample.log')
    # print(analyzer.top_errors(5))
