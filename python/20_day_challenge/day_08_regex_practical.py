"""
Day 8: Regex Practical Applications
====================================
Apply regex to real-world text extraction and validation tasks.

Key concepts:
- Extracting structured data from text
- Data cleaning and normalization
- Input validation patterns
- Building robust patterns
"""

import re

# =============================================================================
# CONCEPT: Practical Regex Applications
# =============================================================================

# Email extraction with validation
def extract_emails(text):
    """Extract valid email addresses from text."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


# Phone number extraction (multiple formats)
def extract_phones(text):
    """Extract phone numbers in various formats."""
    pattern = r'''
        (?:
            \+1[-.\s]?)?           # Optional country code
        (?:
            \(?\d{3}\)?           # Area code with optional parens
            [-.\s]?               # Separator
        )?
        \d{3}                     # First 3 digits
        [-.\s]?                   # Separator
        \d{4}                     # Last 4 digits
    '''
    return re.findall(pattern, text, re.VERBOSE)


# URL extraction
def extract_urls(text):
    """Extract URLs from text."""
    pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
    return re.findall(pattern, text)


# =============================================================================
# EXAMPLES
# =============================================================================

def example_email_extraction():
    """Demonstrate email extraction."""
    print("=== Email Extraction ===")

    text = """
    Contact us at:
    - support@example.com
    - sales.team@company.co.uk
    - john.doe+newsletter@subdomain.example.org

    Invalid emails: @invalid.com, missing@, test@.com
    """

    emails = extract_emails(text)
    print(f"Found {len(emails)} emails:")
    for email in emails:
        print(f"  {email}")


def example_phone_extraction():
    """Demonstrate phone number extraction."""
    print("\n=== Phone Extraction ===")

    text = """
    Call us:
    - (555) 123-4567
    - 555.987.6543
    - 555 456 7890
    - +1-555-111-2222
    - 5551234567
    """

    # More precise pattern
    pattern = r'(?:\+1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
    phones = re.findall(pattern, text)

    print(f"Found {len(phones)} phone numbers:")
    for phone in phones:
        print(f"  {phone.strip()}")


def example_url_extraction():
    """Demonstrate URL extraction."""
    print("\n=== URL Extraction ===")

    text = """
    Check out these links:
    - https://www.example.com/page?query=test
    - http://subdomain.example.org/path/to/page
    - https://api.service.com/v1/endpoint#section
    - Visit example.com for more (not a full URL)
    """

    urls = extract_urls(text)
    print(f"Found {len(urls)} URLs:")
    for url in urls:
        print(f"  {url}")


def example_data_cleaning():
    """Demonstrate data cleaning with regex."""
    print("\n=== Data Cleaning ===")

    # Remove extra whitespace
    text = "  Hello    World  \n\t  Example  "
    cleaned = re.sub(r'\s+', ' ', text).strip()
    print(f"Cleaned whitespace: '{cleaned}'")

    # Normalize phone numbers
    phones = ["(555) 123-4567", "555.987.6543", "555 456 7890"]
    for phone in phones:
        normalized = re.sub(r'[^\d]', '', phone)  # Keep only digits
        formatted = f"{normalized[:3]}-{normalized[3:6]}-{normalized[6:]}"
        print(f"  {phone} -> {formatted}")

    # Remove HTML tags
    html = "<p>Hello <b>World</b>!</p>"
    text_only = re.sub(r'<[^>]+>', '', html)
    print(f"HTML stripped: '{text_only}'")


def example_text_parsing():
    """Demonstrate parsing structured text."""
    print("\n=== Text Parsing ===")

    # Parse key-value pairs
    config = """
    host=localhost
    port=8080
    debug=true
    name="My App"
    """

    pattern = r'(\w+)=(?:"([^"]+)"|(\S+))'
    matches = re.findall(pattern, config)
    config_dict = {}
    for key, quoted_val, unquoted_val in matches:
        config_dict[key] = quoted_val or unquoted_val

    print("Parsed config:")
    for k, v in config_dict.items():
        print(f"  {k}: {v}")


def example_log_parsing():
    """Demonstrate log file parsing."""
    print("\n=== Log Parsing ===")

    log_lines = [
        '2026-01-19 10:30:45 INFO [main] Application started',
        '2026-01-19 10:30:46 ERROR [db] Connection failed: timeout',
        '2026-01-19 10:30:47 WARN [api] Rate limit approaching',
    ]

    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) \[(\w+)\] (.+)'

    for line in log_lines:
        match = re.match(pattern, line)
        if match:
            date, time, level, component, message = match.groups()
            print(f"  [{level}] {component}: {message}")


def example_markdown_parsing():
    """Demonstrate parsing Markdown elements."""
    print("\n=== Markdown Parsing ===")

    markdown = """
    # Heading 1
    ## Heading 2

    This is a [link](https://example.com) and **bold text**.

    - Item 1
    - Item 2

    ```python
    print("Hello")
    ```
    """

    # Extract headings
    headings = re.findall(r'^(#+)\s+(.+)$', markdown, re.MULTILINE)
    print("Headings:")
    for hashes, text in headings:
        level = len(hashes)
        print(f"  H{level}: {text}")

    # Extract links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', markdown)
    print("Links:")
    for text, url in links:
        print(f"  {text} -> {url}")

    # Extract bold text
    bold = re.findall(r'\*\*([^*]+)\*\*', markdown)
    print(f"Bold: {bold}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Credit Card Validator

    Write a function that:
    1. Extracts credit card numbers from text
    2. Validates the format (16 digits, possibly with spaces/dashes)
    3. Masks all but the last 4 digits

    text = "Card: 4111-1111-1111-1111 or 5500 0000 0000 0004"
    extract_and_mask(text) -> ["****-****-****-1111", "**** **** **** 0004"]
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Address Parser

    Write a function that parses US addresses into components.

    address = "123 Main St, Apt 4B, New York, NY 10001"
    parse_address(address) -> {
        'street': '123 Main St',
        'unit': 'Apt 4B',
        'city': 'New York',
        'state': 'NY',
        'zip': '10001'
    }
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Citation Extractor

    Extract academic citations from text.

    text = "As shown by Smith (2020) and Johnson et al. (2019)..."
    extract_citations(text) -> [
        {'authors': 'Smith', 'year': '2020'},
        {'authors': 'Johnson et al.', 'year': '2019'}
    ]

    Handle various formats:
    - Smith (2020)
    - Smith & Jones (2020)
    - Smith et al. (2020)
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: SQL Query Parser

    Parse simple SQL SELECT queries.

    query = "SELECT name, age FROM users WHERE age > 18 ORDER BY name"
    parse_sql(query) -> {
        'columns': ['name', 'age'],
        'table': 'users',
        'where': 'age > 18',
        'order_by': 'name'
    }
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Document Analyzer

    Create a document analyzer that uses regex to extract and analyze
    various types of information from unstructured text.

    Functions to implement:

    1. extract_entities(text) -> dict
       Extract:
       - emails
       - phone numbers
       - urls
       - dates (various formats)
       - monetary amounts ($XX.XX, USD XX, etc.)
       - percentages
       - IP addresses
       - social media handles (@username, #hashtag)

    2. extract_people(text) -> list
       Use patterns to identify likely person names:
       - Capitalized words patterns (John Smith)
       - Title patterns (Mr. Smith, Dr. Jones)
       - Full name patterns (John D. Smith Jr.)

    3. extract_organizations(text) -> list
       Identify organization names:
       - Patterns ending in Inc., LLC, Corp., etc.
       - University of X, X University patterns
       - Department of X patterns

    4. generate_summary(text) -> dict
       Return:
       - word count
       - sentence count
       - paragraph count
       - reading time estimate
       - entity summary (counts by type)
       - most common words (excluding stop words)

    5. anonymize(text, config) -> str
       Replace sensitive information based on config:
       - emails -> [EMAIL]
       - phones -> [PHONE]
       - names -> [PERSON]
       - etc.

    Example usage:

    text = '''
    Contact John Smith at john@example.com or (555) 123-4567.
    Visit https://example.com for more info.
    Meeting scheduled for 01/15/2026 at Acme Corp.
    Budget: $50,000 (a 15% increase from last year).
    '''

    entities = extract_entities(text)
    # {'emails': ['john@example.com'], 'phones': ['(555) 123-4567'], ...}

    anonymized = anonymize(text, {'emails': True, 'phones': True})
    # 'Contact John Smith at [EMAIL] or [PHONE]...'
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 8: Regex Practical Applications\n")
    print("=" * 50)

    # Run examples
    example_email_extraction()
    example_phone_extraction()
    example_url_extraction()
    example_data_cleaning()
    example_text_parsing()
    example_log_parsing()
    example_markdown_parsing()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
