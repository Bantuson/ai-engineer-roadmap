"""
Day 11: API GET Requests
========================
Learn to make HTTP GET requests and handle API responses.

Key concepts:
- requests library basics
- HTTP status codes
- Query parameters
- Response handling (JSON, text)
- Error handling for network requests
"""

import json
import time

# Note: Run `pip install requests` if not installed

# =============================================================================
# CONCEPT: HTTP GET Basics
# =============================================================================

def make_get_request(url, params=None, headers=None, timeout=10):
    """Make a GET request with error handling."""
    try:
        import requests
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise exception for 4xx/5xx
        return response
    except ImportError:
        print("Please install requests: pip install requests")
        return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None


def parse_json_response(response):
    """Parse JSON from response."""
    if response is None:
        return None
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        return None


# =============================================================================
# SIMULATED API (for examples without external dependencies)
# =============================================================================

class MockAPI:
    """Simulated API for demonstration."""

    USERS = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Carol', 'email': 'carol@example.com'},
    ]

    POSTS = [
        {'id': 1, 'userId': 1, 'title': 'First Post', 'body': 'Hello World'},
        {'id': 2, 'userId': 1, 'title': 'Second Post', 'body': 'More content'},
        {'id': 3, 'userId': 2, 'title': 'Bob Post', 'body': 'Bob content'},
    ]

    @classmethod
    def get(cls, endpoint, params=None):
        """Simulate GET request."""
        time.sleep(0.1)  # Simulate network delay

        if endpoint == '/users':
            return {'status': 200, 'data': cls.USERS}
        elif endpoint.startswith('/users/'):
            user_id = int(endpoint.split('/')[-1])
            user = next((u for u in cls.USERS if u['id'] == user_id), None)
            if user:
                return {'status': 200, 'data': user}
            return {'status': 404, 'error': 'User not found'}
        elif endpoint == '/posts':
            data = cls.POSTS
            if params and 'userId' in params:
                data = [p for p in data if p['userId'] == int(params['userId'])]
            return {'status': 200, 'data': data}
        else:
            return {'status': 404, 'error': 'Not found'}


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_get():
    """Demonstrate basic GET request."""
    print("=== Basic GET Request ===")

    # Using simulated API
    response = MockAPI.get('/users')

    if response['status'] == 200:
        users = response['data']
        print(f"Got {len(users)} users:")
        for user in users:
            print(f"  - {user['name']} ({user['email']})")
    else:
        print(f"Error: {response.get('error')}")


def example_get_with_params():
    """Demonstrate GET request with query parameters."""
    print("\n=== GET with Query Parameters ===")

    # Get posts for specific user
    response = MockAPI.get('/posts', params={'userId': 1})

    if response['status'] == 200:
        posts = response['data']
        print(f"Posts for user 1:")
        for post in posts:
            print(f"  - {post['title']}")


def example_get_single_resource():
    """Demonstrate getting a single resource."""
    print("\n=== GET Single Resource ===")

    # Get specific user
    response = MockAPI.get('/users/2')

    if response['status'] == 200:
        user = response['data']
        print(f"User: {user['name']}")
        print(f"Email: {user['email']}")
    elif response['status'] == 404:
        print("User not found")


def example_error_handling():
    """Demonstrate error handling for API requests."""
    print("\n=== Error Handling ===")

    # Try to get non-existent user
    response = MockAPI.get('/users/999')

    if response['status'] == 200:
        print(f"Found: {response['data']}")
    elif response['status'] == 404:
        print(f"Not found: {response.get('error')}")
    elif response['status'] == 401:
        print("Unauthorized - check your API key")
    elif response['status'] == 429:
        print("Rate limited - slow down requests")
    elif response['status'] >= 500:
        print("Server error - try again later")


def example_real_api():
    """Example with real API (commented out to avoid dependencies)."""
    print("\n=== Real API Example (demonstration) ===")

    # This would work with actual requests library:
    """
    import requests

    # JSONPlaceholder - free fake API for testing
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url, params={'userId': 1})

    if response.status_code == 200:
        posts = response.json()
        print(f"Got {len(posts)} posts")
        for post in posts[:3]:
            print(f"  - {post['title'][:50]}...")
    """

    print("To test with real API:")
    print("  1. pip install requests")
    print("  2. Use JSONPlaceholder: https://jsonplaceholder.typicode.com")


def example_pagination():
    """Demonstrate handling paginated API responses."""
    print("\n=== Pagination Handling ===")

    def get_all_pages(base_url, per_page=10, max_pages=None):
        """Fetch all pages of a paginated API."""
        all_items = []
        page = 1

        while True:
            # Simulated response
            if page <= 3:
                items = [f"Item {(page-1)*per_page + i}" for i in range(1, per_page+1)]
                has_more = page < 3
            else:
                items = []
                has_more = False

            all_items.extend(items)
            print(f"  Fetched page {page}: {len(items)} items")

            if not has_more or (max_pages and page >= max_pages):
                break
            page += 1

        return all_items

    items = get_all_pages('/items', per_page=5, max_pages=3)
    print(f"Total items: {len(items)}")


def example_retry_logic():
    """Demonstrate retry logic for failed requests."""
    print("\n=== Retry Logic ===")

    def request_with_retry(url, max_retries=3, backoff=1):
        """Make request with retry logic."""
        for attempt in range(max_retries):
            try:
                # Simulated request
                if attempt < 2:  # Fail first 2 attempts
                    raise ConnectionError("Connection failed")

                print(f"Attempt {attempt + 1}: Success!")
                return {'status': 200, 'data': 'OK'}

            except ConnectionError as e:
                print(f"Attempt {attempt + 1}: {e}")
                if attempt < max_retries - 1:
                    wait_time = backoff * (2 ** attempt)
                    print(f"  Retrying in {wait_time}s...")
                    time.sleep(0.1)  # Shortened for demo

        return {'status': 503, 'error': 'Max retries exceeded'}

    result = request_with_retry('/api/data')
    print(f"Final result: {result}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: API Client Class

    Create an APIClient class that:
    - Stores base URL and optional auth headers
    - Has methods for common endpoints
    - Handles errors consistently
    - Returns parsed JSON or raises exceptions

    client = APIClient('https://api.example.com', api_key='xxx')
    users = client.get_users()
    user = client.get_user(1)
    posts = client.get_posts(user_id=1)
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Rate Limiter

    Create a rate limiter for API requests:
    - Limit to N requests per second
    - Queue requests if limit exceeded
    - Track request counts

    limiter = RateLimiter(requests_per_second=10)

    @limiter.limit
    def fetch_data(url):
        return make_request(url)

    # This should automatically respect rate limits
    for url in urls:
        fetch_data(url)
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Response Cache

    Create a cache for API responses:
    - Cache successful responses
    - Configurable TTL (time-to-live)
    - Cache invalidation
    - Memory limit

    cache = ResponseCache(ttl=300, max_size=100)

    @cache.cached
    def fetch_user(user_id):
        return api.get(f'/users/{user_id}')

    user = fetch_user(1)  # Fetches from API
    user = fetch_user(1)  # Returns cached
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Parallel Fetcher

    Create a function that fetches multiple URLs in parallel:
    - Limit concurrent requests
    - Handle individual failures
    - Return results in order
    - Progress reporting

    urls = ['url1', 'url2', 'url3', ...]
    results = parallel_fetch(urls, max_concurrent=5, on_progress=callback)
    # results = [response1, response2, ...]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: GitHub API Client

    Build a GitHub API client that can:

    1. Authentication:
       - Support personal access token
       - Handle rate limiting (check X-RateLimit headers)

    2. User operations:
       - get_user(username) - Get user profile
       - get_user_repos(username) - Get user's repos
       - get_user_activity(username) - Get recent activity

    3. Repository operations:
       - get_repo(owner, repo) - Get repo details
       - get_repo_issues(owner, repo) - Get issues with pagination
       - get_repo_commits(owner, repo, since=None) - Get commits
       - search_repos(query, sort='stars') - Search repositories

    4. Advanced features:
       - Automatic pagination
       - Response caching
       - Rate limit awareness (wait when near limit)
       - Retry on transient failures

    Example usage:

    github = GitHubClient(token='your-token')

    # Get user info
    user = github.get_user('octocat')
    print(f"{user['name']} has {user['public_repos']} repos")

    # Search repos
    repos = github.search_repos('python machine learning', sort='stars')
    for repo in repos[:5]:
        print(f"{repo['full_name']}: {repo['stargazers_count']} stars")

    # Get all issues (handles pagination)
    issues = github.get_repo_issues('python', 'cpython', state='open')
    print(f"Total open issues: {len(issues)}")

    # Check rate limit
    print(f"Remaining requests: {github.rate_limit_remaining}")
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 11: API GET Requests\n")
    print("=" * 50)

    # Run examples
    example_basic_get()
    example_get_with_params()
    example_get_single_resource()
    example_error_handling()
    example_real_api()
    example_pagination()
    example_retry_logic()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
