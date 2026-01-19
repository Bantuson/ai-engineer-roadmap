"""
Day 13: Web Scraping
====================
Learn to extract data from web pages using BeautifulSoup.

Key concepts:
- HTML parsing with BeautifulSoup
- Finding elements (find, find_all, select)
- Extracting text and attributes
- Navigating the DOM
- Handling edge cases
"""

# Note: Run `pip install beautifulsoup4` if not installed

# =============================================================================
# CONCEPT: HTML Parsing Basics
# =============================================================================

# Simulated HTML for examples (no external requests needed)
SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <header>
        <nav>
            <a href="/" class="logo">Home</a>
            <ul class="menu">
                <li><a href="/about">About</a></li>
                <li><a href="/products">Products</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h1>Welcome to Our Store</h1>

        <div class="products">
            <div class="product" data-id="1">
                <h2 class="product-name">Widget Pro</h2>
                <p class="price">$29.99</p>
                <p class="description">The best widget for professionals.</p>
                <span class="stock in-stock">In Stock</span>
            </div>

            <div class="product" data-id="2">
                <h2 class="product-name">Gadget Plus</h2>
                <p class="price">$49.99</p>
                <p class="description">Advanced gadget with extra features.</p>
                <span class="stock out-of-stock">Out of Stock</span>
            </div>

            <div class="product" data-id="3">
                <h2 class="product-name">Tool Master</h2>
                <p class="price">$19.99</p>
                <p class="description">Essential tool for everyone.</p>
                <span class="stock in-stock">In Stock</span>
            </div>
        </div>

        <table class="specs">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Weight</th>
                    <th>Dimensions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Widget Pro</td>
                    <td>0.5 kg</td>
                    <td>10x10x5 cm</td>
                </tr>
                <tr>
                    <td>Gadget Plus</td>
                    <td>1.2 kg</td>
                    <td>20x15x10 cm</td>
                </tr>
            </tbody>
        </table>
    </main>

    <footer>
        <p>&copy; 2026 Sample Store</p>
        <a href="mailto:contact@example.com">Email Us</a>
    </footer>
</body>
</html>
"""


def get_soup(html):
    """Create BeautifulSoup object from HTML string."""
    try:
        from bs4 import BeautifulSoup
        return BeautifulSoup(html, 'html.parser')
    except ImportError:
        print("Please install beautifulsoup4: pip install beautifulsoup4")
        return None


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_parsing():
    """Demonstrate basic HTML parsing."""
    print("=== Basic Parsing ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    # Get title
    title = soup.title.string
    print(f"Page title: {title}")

    # Get first h1
    h1 = soup.find('h1')
    print(f"Main heading: {h1.text}")

    # Get all links
    links = soup.find_all('a')
    print(f"Found {len(links)} links")


def example_finding_elements():
    """Demonstrate different ways to find elements."""
    print("\n=== Finding Elements ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    # By tag name
    print("By tag name (find):")
    first_p = soup.find('p')
    print(f"  First <p>: {first_p.text}")

    # By class name
    print("\nBy class name:")
    products = soup.find_all(class_='product')
    print(f"  Found {len(products)} products")

    # By ID (if there was one)
    # element = soup.find(id='my-id')

    # By attribute
    print("\nBy attribute:")
    product_2 = soup.find(attrs={'data-id': '2'})
    print(f"  Product 2: {product_2.find('h2').text}")

    # Multiple conditions
    print("\nMultiple conditions:")
    in_stock = soup.find_all('span', class_='in-stock')
    print(f"  In-stock items: {len(in_stock)}")


def example_css_selectors():
    """Demonstrate CSS selector syntax."""
    print("\n=== CSS Selectors ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    # Single element
    logo = soup.select_one('a.logo')
    print(f"Logo text: {logo.text}")

    # Multiple elements
    menu_links = soup.select('ul.menu a')
    print(f"Menu links: {[a.text for a in menu_links]}")

    # Nested selectors
    product_names = soup.select('.product .product-name')
    print(f"Products: {[p.text for p in product_names]}")

    # Attribute selectors
    external_links = soup.select('a[href^="mailto:"]')
    print(f"Email links: {[a['href'] for a in external_links]}")


def example_extracting_data():
    """Demonstrate extracting text and attributes."""
    print("\n=== Extracting Data ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    products = soup.find_all(class_='product')

    for product in products:
        # Get data attribute
        product_id = product.get('data-id')

        # Get text content
        name = product.find(class_='product-name').text.strip()
        price = product.find(class_='price').text.strip()
        desc = product.find(class_='description').text.strip()

        # Check class for stock status
        stock_elem = product.find(class_='stock')
        in_stock = 'in-stock' in stock_elem.get('class', [])

        print(f"  ID: {product_id}")
        print(f"  Name: {name}")
        print(f"  Price: {price}")
        print(f"  In Stock: {in_stock}")
        print()


def example_table_parsing():
    """Demonstrate parsing table data."""
    print("=== Table Parsing ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    table = soup.find('table', class_='specs')

    # Get headers
    headers = [th.text for th in table.find_all('th')]
    print(f"Headers: {headers}")

    # Get rows
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        row = [td.text.strip() for td in tr.find_all('td')]
        rows.append(row)

    # Convert to list of dicts
    data = [dict(zip(headers, row)) for row in rows]

    print("Table data:")
    for item in data:
        print(f"  {item}")


def example_navigation():
    """Demonstrate DOM navigation."""
    print("\n=== DOM Navigation ===")

    soup = get_soup(SAMPLE_HTML)
    if not soup:
        return

    product = soup.find(class_='product')

    # Parent
    parent = product.parent
    print(f"Parent class: {parent.get('class')}")

    # Siblings
    next_sibling = product.find_next_sibling(class_='product')
    if next_sibling:
        print(f"Next product: {next_sibling.find('h2').text}")

    # Children
    children = list(product.children)
    # Filter out NavigableString (whitespace)
    elements = [c for c in children if hasattr(c, 'name')]
    print(f"Direct children tags: {[e.name for e in elements]}")


def example_cleaning_text():
    """Demonstrate text cleaning."""
    print("\n=== Cleaning Text ===")

    messy_html = """
    <div>
        <p>
            This is some    text with
            weird   spacing
            and    newlines.
        </p>
    </div>
    """

    soup = get_soup(messy_html)
    if not soup:
        return

    # Raw text
    raw = soup.find('p').text
    print(f"Raw: {repr(raw)}")

    # Cleaned text
    import re
    cleaned = ' '.join(soup.find('p').text.split())
    print(f"Cleaned: {cleaned}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Product Scraper

    Create a function that extracts all product data from the sample HTML:

    def scrape_products(html):
        # Return list of dicts:
        # [
        #   {
        #     'id': '1',
        #     'name': 'Widget Pro',
        #     'price': 29.99,  # as float
        #     'description': '...',
        #     'in_stock': True
        #   },
        #   ...
        # ]
        pass
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Link Extractor

    Create a function that extracts and categorizes links:

    def extract_links(html):
        # Return dict:
        # {
        #   'internal': ['/about', '/products', ...],
        #   'external': ['https://...'],
        #   'email': ['mailto:...'],
        #   'tel': ['tel:...']
        # }
        pass
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Form Parser

    Create a function that extracts form data:

    sample_form_html = '''
    <form action="/submit" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password">
        <select name="country">
            <option value="us">United States</option>
            <option value="uk">United Kingdom</option>
        </select>
        <textarea name="bio"></textarea>
        <input type="submit" value="Submit">
    </form>
    '''

    def parse_form(html):
        # Return:
        # {
        #   'action': '/submit',
        #   'method': 'post',
        #   'fields': [
        #     {'name': 'username', 'type': 'text', 'required': True, ...},
        #     ...
        #   ]
        # }
        pass
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Structured Data Extractor

    Create a function that finds and parses JSON-LD structured data:

    html_with_jsonld = '''
    <html>
    <head>
        <script type="application/ld+json">
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Widget",
            "price": "29.99"
        }
        </script>
    </head>
    <body>...</body>
    </html>
    '''

    def extract_structured_data(html):
        # Return list of parsed JSON-LD objects
        pass
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Web Page Analyzer

    Create a comprehensive web page analyzer that extracts:

    1. Metadata:
       - Title, description, keywords
       - Open Graph tags
       - Twitter Card tags
       - Canonical URL

    2. Content Analysis:
       - All headings (h1-h6) with hierarchy
       - Main text content (paragraphs)
       - Images with alt text
       - Internal/external links

    3. Technical Info:
       - All CSS files
       - All JavaScript files
       - Meta tags
       - Structured data (JSON-LD)

    4. Accessibility Check:
       - Images without alt text
       - Links without text
       - Missing form labels
       - Heading hierarchy issues

    Example output:

    analysis = analyze_page(html)

    print(analysis['metadata'])
    # {'title': '...', 'description': '...', 'og_title': '...', ...}

    print(analysis['content']['headings'])
    # [{'level': 1, 'text': '...'}, {'level': 2, 'text': '...'}, ...]

    print(analysis['accessibility']['issues'])
    # [
    #   {'type': 'missing_alt', 'element': '<img src="...">'},
    #   {'type': 'empty_link', 'element': '<a href="..."></a>'},
    #   ...
    # ]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 13: Web Scraping\n")
    print("=" * 50)

    # Run examples
    example_basic_parsing()
    example_finding_elements()
    example_css_selectors()
    example_extracting_data()
    example_table_parsing()
    example_navigation()
    example_cleaning_text()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
