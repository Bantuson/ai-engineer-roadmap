"""
Day 12: API POST Requests
=========================
Learn to make HTTP POST requests with data, headers, and authentication.

Key concepts:
- POST, PUT, PATCH, DELETE methods
- Request bodies (JSON, form data)
- Headers and authentication
- File uploads
- Handling responses
"""

import json
import base64
import time

# =============================================================================
# CONCEPT: HTTP Methods Beyond GET
# =============================================================================

def explain_http_methods():
    """Explain different HTTP methods."""
    methods = {
        'GET': 'Retrieve data (safe, idempotent)',
        'POST': 'Create new resource',
        'PUT': 'Replace entire resource (idempotent)',
        'PATCH': 'Partial update of resource',
        'DELETE': 'Remove resource (idempotent)',
    }
    return methods


# =============================================================================
# SIMULATED API (for examples)
# =============================================================================

class MockAPIServer:
    """Simulated REST API server."""

    def __init__(self):
        self.users = [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        ]
        self.next_id = 3
        self.auth_tokens = {'valid-token': 'user1'}

    def authenticate(self, headers):
        """Check authentication."""
        auth = headers.get('Authorization', '')
        if auth.startswith('Bearer '):
            token = auth.split(' ')[1]
            return token in self.auth_tokens
        return False

    def post(self, endpoint, data=None, headers=None):
        """Handle POST request."""
        headers = headers or {}

        if endpoint == '/users':
            if not self.authenticate(headers):
                return {'status': 401, 'error': 'Unauthorized'}

            if not data or 'name' not in data:
                return {'status': 400, 'error': 'Name is required'}

            new_user = {
                'id': self.next_id,
                'name': data['name'],
                'email': data.get('email', '')
            }
            self.users.append(new_user)
            self.next_id += 1

            return {'status': 201, 'data': new_user}

        elif endpoint == '/login':
            if data.get('username') == 'admin' and data.get('password') == 'secret':
                return {'status': 200, 'data': {'token': 'valid-token'}}
            return {'status': 401, 'error': 'Invalid credentials'}

        return {'status': 404, 'error': 'Not found'}

    def put(self, endpoint, data=None, headers=None):
        """Handle PUT request (full replacement)."""
        headers = headers or {}

        if not self.authenticate(headers):
            return {'status': 401, 'error': 'Unauthorized'}

        if endpoint.startswith('/users/'):
            user_id = int(endpoint.split('/')[-1])
            for i, user in enumerate(self.users):
                if user['id'] == user_id:
                    self.users[i] = {
                        'id': user_id,
                        'name': data.get('name', ''),
                        'email': data.get('email', '')
                    }
                    return {'status': 200, 'data': self.users[i]}
            return {'status': 404, 'error': 'User not found'}

        return {'status': 404, 'error': 'Not found'}

    def patch(self, endpoint, data=None, headers=None):
        """Handle PATCH request (partial update)."""
        headers = headers or {}

        if not self.authenticate(headers):
            return {'status': 401, 'error': 'Unauthorized'}

        if endpoint.startswith('/users/'):
            user_id = int(endpoint.split('/')[-1])
            for user in self.users:
                if user['id'] == user_id:
                    if 'name' in data:
                        user['name'] = data['name']
                    if 'email' in data:
                        user['email'] = data['email']
                    return {'status': 200, 'data': user}
            return {'status': 404, 'error': 'User not found'}

        return {'status': 404, 'error': 'Not found'}

    def delete(self, endpoint, headers=None):
        """Handle DELETE request."""
        headers = headers or {}

        if not self.authenticate(headers):
            return {'status': 401, 'error': 'Unauthorized'}

        if endpoint.startswith('/users/'):
            user_id = int(endpoint.split('/')[-1])
            for i, user in enumerate(self.users):
                if user['id'] == user_id:
                    deleted = self.users.pop(i)
                    return {'status': 200, 'data': deleted}
            return {'status': 404, 'error': 'User not found'}

        return {'status': 404, 'error': 'Not found'}


# Global API instance for examples
api = MockAPIServer()


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_post():
    """Demonstrate basic POST request."""
    print("=== Basic POST Request ===")

    # Login to get token
    response = api.post('/login', data={
        'username': 'admin',
        'password': 'secret'
    })

    if response['status'] == 200:
        token = response['data']['token']
        print(f"Got token: {token}")

        # Create user with token
        response = api.post('/users',
            data={'name': 'Carol', 'email': 'carol@example.com'},
            headers={'Authorization': f'Bearer {token}'}
        )

        if response['status'] == 201:
            print(f"Created user: {response['data']}")
    else:
        print(f"Login failed: {response.get('error')}")


def example_put_vs_patch():
    """Demonstrate PUT vs PATCH."""
    print("\n=== PUT vs PATCH ===")

    headers = {'Authorization': 'Bearer valid-token'}

    # PUT - full replacement (missing fields become empty)
    print("PUT /users/1 (full replacement):")
    response = api.put('/users/1',
        data={'name': 'Alice Updated'},  # email not provided
        headers=headers
    )
    print(f"  Result: {response['data']}")

    # PATCH - partial update (only updates provided fields)
    print("\nPATCH /users/2 (partial update):")
    response = api.patch('/users/2',
        data={'name': 'Bob Updated'},  # email unchanged
        headers=headers
    )
    print(f"  Result: {response['data']}")


def example_delete():
    """Demonstrate DELETE request."""
    print("\n=== DELETE Request ===")

    headers = {'Authorization': 'Bearer valid-token'}

    # Create a user to delete
    api.post('/users',
        data={'name': 'ToDelete'},
        headers=headers
    )

    # Delete the user
    response = api.delete('/users/3', headers=headers)

    if response['status'] == 200:
        print(f"Deleted: {response['data']}")
    else:
        print(f"Delete failed: {response.get('error')}")


def example_authentication_types():
    """Demonstrate different authentication methods."""
    print("\n=== Authentication Types ===")

    # 1. Bearer Token (most common for APIs)
    print("1. Bearer Token:")
    print("   Authorization: Bearer <token>")

    # 2. Basic Auth (username:password in base64)
    print("\n2. Basic Auth:")
    credentials = base64.b64encode(b'username:password').decode()
    print(f"   Authorization: Basic {credentials}")

    # 3. API Key in header
    print("\n3. API Key (header):")
    print("   X-API-Key: your-api-key")

    # 4. API Key in query param
    print("\n4. API Key (query param):")
    print("   ?api_key=your-api-key")


def example_json_vs_form():
    """Demonstrate JSON vs form data."""
    print("\n=== JSON vs Form Data ===")

    # JSON body (most APIs)
    print("JSON body:")
    print("  Content-Type: application/json")
    print("  Body: " + json.dumps({'name': 'Alice', 'email': 'alice@example.com'}))

    # Form data (traditional forms, some APIs)
    print("\nForm data:")
    print("  Content-Type: application/x-www-form-urlencoded")
    print("  Body: name=Alice&email=alice%40example.com")

    # Multipart form (file uploads)
    print("\nMultipart form (file upload):")
    print("  Content-Type: multipart/form-data")
    print("  Body: [file content with boundary]")


def example_error_handling():
    """Demonstrate error handling for POST requests."""
    print("\n=== Error Handling ===")

    def handle_response(response):
        """Handle API response based on status code."""
        status = response['status']

        if 200 <= status < 300:
            print(f"Success ({status}): {response.get('data')}")
            return response['data']
        elif status == 400:
            print(f"Bad Request: {response.get('error')}")
        elif status == 401:
            print("Unauthorized: Check your credentials")
        elif status == 403:
            print("Forbidden: You don't have permission")
        elif status == 404:
            print("Not Found: Resource doesn't exist")
        elif status == 409:
            print("Conflict: Resource already exists")
        elif status == 422:
            print(f"Validation Error: {response.get('error')}")
        elif status == 429:
            print("Rate Limited: Slow down!")
        elif status >= 500:
            print(f"Server Error ({status}): Try again later")

        return None

    # Test various responses
    print("Testing unauthorized request:")
    response = api.post('/users', data={'name': 'Test'})
    handle_response(response)

    print("\nTesting bad request:")
    response = api.post('/users', data={}, headers={'Authorization': 'Bearer valid-token'})
    handle_response(response)


def example_real_api():
    """Example with real API (demonstration)."""
    print("\n=== Real POST Example (demonstration) ===")

    print("""
    import requests

    # Create a resource
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json={
            'title': 'My Post',
            'body': 'Post content',
            'userId': 1
        },
        headers={
            'Content-Type': 'application/json'
        }
    )

    if response.status_code == 201:
        created = response.json()
        print(f"Created post with ID: {created['id']}")
    """)


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: CRUD API Client

    Create a class that provides full CRUD operations:

    class CRUDClient:
        def __init__(self, base_url, auth_token=None):
            pass

        def create(self, resource, data):
            '''POST /resource'''
            pass

        def read(self, resource, id=None):
            '''GET /resource or GET /resource/{id}'''
            pass

        def update(self, resource, id, data, partial=False):
            '''PUT /resource/{id} or PATCH if partial'''
            pass

        def delete(self, resource, id):
            '''DELETE /resource/{id}'''
            pass

    client = CRUDClient('https://api.example.com', auth_token='xxx')
    user = client.create('users', {'name': 'Alice'})
    client.update('users', user['id'], {'email': 'new@email.com'}, partial=True)
    client.delete('users', user['id'])
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Webhook Sender

    Create a webhook sender that:
    - Sends events to configured endpoints
    - Signs requests with HMAC
    - Retries on failure
    - Logs all attempts

    webhook = WebhookSender(
        secret='webhook-secret',
        retry_count=3,
        timeout=5
    )

    webhook.add_endpoint('https://example.com/webhook')

    webhook.send('user.created', {
        'user_id': 1,
        'name': 'Alice'
    })
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Form Submission Handler

    Create a class that handles form submissions:
    - Support both JSON and form-encoded data
    - File uploads
    - CSRF token handling
    - Validation before sending

    form = FormSubmitter(base_url='https://example.com')

    # Simple form
    form.submit('/contact', {
        'name': 'Alice',
        'message': 'Hello'
    })

    # With file upload
    form.submit('/upload', {
        'title': 'My File'
    }, files={'document': open('file.pdf', 'rb')})
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Batch Request Handler

    Create a system for batching multiple API requests:
    - Collect requests
    - Send as batch
    - Parse batch response
    - Handle partial failures

    batch = BatchRequester(api_url='https://api.example.com/batch')

    batch.add('POST', '/users', {'name': 'Alice'})
    batch.add('POST', '/users', {'name': 'Bob'})
    batch.add('PATCH', '/users/1', {'email': 'new@email.com'})

    results = batch.execute()
    # results = [
    #   {'status': 201, 'data': {...}},
    #   {'status': 201, 'data': {...}},
    #   {'status': 200, 'data': {...}}
    # ]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: REST API Client Library

    Build a complete REST API client library that could be used
    to interact with any REST API:

    1. Core features:
       - All HTTP methods (GET, POST, PUT, PATCH, DELETE)
       - JSON and form data support
       - File uploads
       - Custom headers
       - Query parameters

    2. Authentication:
       - Bearer token
       - Basic auth
       - API key (header or query)
       - OAuth2 support (bonus)

    3. Advanced features:
       - Request/response middleware
       - Automatic retry with backoff
       - Rate limiting
       - Response caching (for GET)
       - Request timeout handling

    4. Developer experience:
       - Type hints
       - Comprehensive error handling
       - Request/response logging
       - Debug mode

    Example usage:

    api = RESTClient(
        base_url='https://api.example.com/v1',
        auth=BearerAuth('your-token'),
        timeout=30,
        retry_count=3
    )

    # Add middleware
    api.add_middleware(LoggingMiddleware())
    api.add_middleware(RateLimitMiddleware(100, per_minute=True))

    # Make requests
    users = api.get('/users', params={'page': 1})
    user = api.post('/users', json={'name': 'Alice'})
    api.patch(f'/users/{user["id"]}', json={'email': 'new@email.com'})
    api.delete(f'/users/{user["id"]}')

    # File upload
    api.post('/upload', files={'file': open('doc.pdf', 'rb')})

    # Error handling
    try:
        api.get('/protected')
    except AuthenticationError:
        print("Need to re-authenticate")
    except RateLimitError as e:
        print(f"Rate limited, retry after {e.retry_after}s")
    except APIError as e:
        print(f"API error: {e.status_code} - {e.message}")
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 12: API POST Requests\n")
    print("=" * 50)

    # Run examples
    example_basic_post()
    example_put_vs_patch()
    example_delete()
    example_authentication_types()
    example_json_vs_form()
    example_error_handling()
    example_real_api()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
