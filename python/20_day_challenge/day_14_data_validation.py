"""
Day 14: Data Validation
=======================
Learn to validate and sanitize input data properly.

Key concepts:
- Input validation patterns
- Type checking
- Constraint validation
- Sanitization
- Error reporting
"""

import re
from typing import Any

# =============================================================================
# CONCEPT: Validation Fundamentals
# =============================================================================

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, errors):
        self.errors = errors if isinstance(errors, list) else [errors]
        super().__init__(str(self.errors))


class Validator:
    """Base validator class."""

    def validate(self, value):
        """Validate value, return (is_valid, error_message)."""
        raise NotImplementedError


class Required(Validator):
    """Validate that value is present."""

    def validate(self, value):
        if value is None or value == '':
            return False, "This field is required"
        return True, None


class TypeValidator(Validator):
    """Validate value type."""

    def __init__(self, expected_type):
        self.expected_type = expected_type

    def validate(self, value):
        if not isinstance(value, self.expected_type):
            return False, f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
        return True, None


class Range(Validator):
    """Validate numeric range."""

    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def validate(self, value):
        if self.min_val is not None and value < self.min_val:
            return False, f"Value must be at least {self.min_val}"
        if self.max_val is not None and value > self.max_val:
            return False, f"Value must be at most {self.max_val}"
        return True, None


class Length(Validator):
    """Validate string/list length."""

    def __init__(self, min_len=None, max_len=None):
        self.min_len = min_len
        self.max_len = max_len

    def validate(self, value):
        length = len(value)
        if self.min_len is not None and length < self.min_len:
            return False, f"Length must be at least {self.min_len}"
        if self.max_len is not None and length > self.max_len:
            return False, f"Length must be at most {self.max_len}"
        return True, None


class Pattern(Validator):
    """Validate against regex pattern."""

    def __init__(self, pattern, message=None):
        self.pattern = re.compile(pattern)
        self.message = message or f"Value must match pattern: {pattern}"

    def validate(self, value):
        if not self.pattern.match(str(value)):
            return False, self.message
        return True, None


class OneOf(Validator):
    """Validate value is one of allowed values."""

    def __init__(self, choices):
        self.choices = choices

    def validate(self, value):
        if value not in self.choices:
            return False, f"Value must be one of: {', '.join(map(str, self.choices))}"
        return True, None


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_validation():
    """Demonstrate basic validation."""
    print("=== Basic Validation ===")

    def validate_user(data):
        errors = []

        # Name validation
        name = data.get('name')
        if not name:
            errors.append(('name', 'Name is required'))
        elif len(name) < 2:
            errors.append(('name', 'Name must be at least 2 characters'))

        # Age validation
        age = data.get('age')
        if age is not None:
            if not isinstance(age, int):
                errors.append(('age', 'Age must be an integer'))
            elif age < 0 or age > 150:
                errors.append(('age', 'Age must be between 0 and 150'))

        # Email validation
        email = data.get('email')
        if email:
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(email_pattern, email):
                errors.append(('email', 'Invalid email format'))

        return errors

    # Test with valid data
    valid_user = {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
    errors = validate_user(valid_user)
    print(f"Valid user errors: {errors}")

    # Test with invalid data
    invalid_user = {'name': 'A', 'age': -5, 'email': 'not-an-email'}
    errors = validate_user(invalid_user)
    print(f"Invalid user errors: {errors}")


def example_validator_classes():
    """Demonstrate using validator classes."""
    print("\n=== Validator Classes ===")

    # Define validation rules
    validators = {
        'name': [Required(), TypeValidator(str), Length(min_len=2, max_len=50)],
        'age': [TypeValidator(int), Range(min_val=0, max_val=150)],
        'role': [Required(), OneOf(['admin', 'user', 'guest'])],
    }

    def validate(data, validators):
        errors = {}
        for field, field_validators in validators.items():
            value = data.get(field)
            for validator in field_validators:
                # Skip other validators if Required fails
                if isinstance(validator, Required):
                    valid, error = validator.validate(value)
                    if not valid:
                        errors[field] = error
                        break
                elif value is not None:
                    valid, error = validator.validate(value)
                    if not valid:
                        errors[field] = error
                        break
        return errors

    # Test
    data = {'name': 'Alice', 'age': 30, 'role': 'admin'}
    errors = validate(data, validators)
    print(f"Valid data errors: {errors}")

    data = {'name': 'A', 'age': 200, 'role': 'superuser'}
    errors = validate(data, validators)
    print(f"Invalid data errors: {errors}")


def example_nested_validation():
    """Demonstrate validating nested data."""
    print("\n=== Nested Validation ===")

    def validate_order(order):
        errors = {}

        # Validate customer
        customer = order.get('customer', {})
        if not customer.get('name'):
            errors['customer.name'] = 'Customer name is required'
        if not customer.get('email'):
            errors['customer.email'] = 'Customer email is required'

        # Validate items
        items = order.get('items', [])
        if not items:
            errors['items'] = 'At least one item is required'
        else:
            for i, item in enumerate(items):
                if not item.get('product_id'):
                    errors[f'items.{i}.product_id'] = 'Product ID is required'
                quantity = item.get('quantity', 0)
                if quantity < 1:
                    errors[f'items.{i}.quantity'] = 'Quantity must be at least 1'

        return errors

    order = {
        'customer': {'name': 'Alice'},  # Missing email
        'items': [
            {'product_id': 1, 'quantity': 2},
            {'quantity': 0}  # Missing product_id, invalid quantity
        ]
    }

    errors = validate_order(order)
    print("Order validation errors:")
    for field, error in errors.items():
        print(f"  {field}: {error}")


def example_sanitization():
    """Demonstrate input sanitization."""
    print("\n=== Input Sanitization ===")

    def sanitize_string(value):
        """Sanitize string input."""
        if not isinstance(value, str):
            return str(value)
        # Strip whitespace
        value = value.strip()
        # Remove control characters
        value = ''.join(c for c in value if ord(c) >= 32)
        return value

    def sanitize_html(value):
        """Remove/escape HTML tags."""
        # Simple approach - for production use a library like bleach
        import html
        value = html.escape(value)
        return value

    def sanitize_phone(value):
        """Normalize phone number."""
        # Keep only digits
        digits = re.sub(r'\D', '', value)
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return value

    # Test sanitization
    print(f"String: {repr(sanitize_string('  Hello World  '))}")
    print(f"HTML: {sanitize_html('<script>alert(1)</script>')}")
    print(f"Phone: {sanitize_phone('555-123-4567')}")


def example_coercion():
    """Demonstrate type coercion during validation."""
    print("\n=== Type Coercion ===")

    def coerce(value, target_type, default=None):
        """Coerce value to target type."""
        if value is None:
            return default

        try:
            if target_type == bool:
                if isinstance(value, str):
                    return value.lower() in ('true', '1', 'yes')
                return bool(value)
            elif target_type == int:
                return int(float(value))  # Handle "3.0" -> 3
            elif target_type == float:
                return float(value)
            elif target_type == str:
                return str(value)
            elif target_type == list:
                if isinstance(value, str):
                    return [v.strip() for v in value.split(',')]
                return list(value)
            else:
                return target_type(value)
        except (ValueError, TypeError):
            return default

    # Test coercion
    print(f"'123' -> int: {coerce('123', int)}")
    print(f"'3.14' -> float: {coerce('3.14', float)}")
    print(f"'true' -> bool: {coerce('true', bool)}")
    print(f"'a,b,c' -> list: {coerce('a,b,c', list)}")
    print(f"'invalid' -> int: {coerce('invalid', int, default=0)}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Schema Validator

    Create a schema-based validator:

    schema = {
        'name': {'type': str, 'required': True, 'min_length': 2},
        'age': {'type': int, 'min': 0, 'max': 150},
        'email': {'type': str, 'pattern': r'^[\w\.-]+@[\w\.-]+\.\w+$'},
        'role': {'type': str, 'choices': ['admin', 'user']},
        'tags': {'type': list, 'item_type': str}
    }

    validator = SchemaValidator(schema)
    result = validator.validate(data)
    # result.is_valid, result.errors, result.data (coerced)
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Chained Validators

    Create validators that can be chained:

    username_validator = (
        StringValidator()
        .required()
        .min_length(3)
        .max_length(20)
        .pattern(r'^[a-z0-9_]+$', 'Username can only contain lowercase letters, numbers, and underscores')
    )

    result = username_validator.validate('john_doe')
    # (True, None)

    result = username_validator.validate('JohnDoe!')
    # (False, 'Username can only contain...')
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Form Validator

    Create a form validator for web forms:

    form = FormValidator()
    form.field('email').required().email()
    form.field('password').required().min_length(8).has_uppercase().has_digit()
    form.field('confirm_password').required().equals('password')
    form.field('age').optional().integer().range(18, 100)

    result = form.validate(request_data)
    if not result.is_valid:
        return {'errors': result.errors}
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: API Request Validator

    Create a decorator for validating API requests:

    @validate_request({
        'body': {
            'title': {'type': str, 'required': True, 'max_length': 100},
            'content': {'type': str, 'required': True}
        },
        'query': {
            'format': {'type': str, 'choices': ['json', 'xml']}
        },
        'headers': {
            'X-API-Key': {'required': True}
        }
    })
    def create_post(request):
        # request.validated_body, request.validated_query, etc.
        pass
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Complete Validation Framework

    Build a full-featured validation framework:

    1. Core Validators:
       - Type validators (str, int, float, bool, list, dict)
       - String validators (min/max length, pattern, email, url, uuid)
       - Number validators (min/max, positive, negative, integer)
       - Collection validators (min/max items, unique, item validator)
       - Date validators (format, min/max date, before/after)

    2. Features:
       - Nested object validation
       - Array item validation
       - Cross-field validation (field A depends on field B)
       - Conditional validation (if field A == X, require field B)
       - Custom validators
       - Error message customization
       - Internationalization support

    3. Schema Definition:
       - JSON Schema-like syntax
       - Decorator syntax for functions
       - Class-based schemas

    4. Output:
       - Detailed error messages with field paths
       - Coerced/sanitized data
       - Validation metadata (which fields passed/failed)

    Example usage:

    # Schema definition
    UserSchema = Schema({
        'username': String(required=True, min_length=3, max_length=20,
                          pattern=r'^[a-z0-9_]+$'),
        'email': Email(required=True),
        'password': String(required=True, min_length=8,
                          validators=[HasUppercase(), HasDigit(), HasSpecial()]),
        'profile': Nested({
            'age': Integer(min=13),
            'bio': String(max_length=500),
            'website': URL(optional=True)
        }),
        'roles': Array(String(choices=['admin', 'user']), min_items=1),
        'settings': Dict(key_type=String(), value_type=Any())
    })

    # With conditions
    OrderSchema = Schema({
        'type': String(choices=['pickup', 'delivery']),
        'address': String().when('type', '==', 'delivery', required=True),
        'pickup_time': DateTime().when('type', '==', 'pickup', required=True)
    })

    # Validation
    result = UserSchema.validate(data)

    if result.is_valid:
        user = result.data  # Coerced and sanitized
    else:
        for error in result.errors:
            print(f"{error.path}: {error.message}")
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 14: Data Validation\n")
    print("=" * 50)

    # Run examples
    example_basic_validation()
    example_validator_classes()
    example_nested_validation()
    example_sanitization()
    example_coercion()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
