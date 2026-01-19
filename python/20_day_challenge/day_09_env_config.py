"""
Day 9: Environment Variables and Configuration
==============================================
Learn to manage configuration and environment variables properly.

Key concepts:
- os.environ for environment variables
- python-dotenv for .env files
- Configuration patterns
- Secrets management basics
"""

import os
import json

# =============================================================================
# CONCEPT: Environment Variables
# =============================================================================

# Read environment variable
def get_env(key, default=None):
    """Get environment variable with optional default."""
    return os.environ.get(key, default)


# Read required environment variable
def get_required_env(key):
    """Get required environment variable, raise if missing."""
    value = os.environ.get(key)
    if value is None:
        raise EnvironmentError(f"Required environment variable '{key}' is not set")
    return value


# Set environment variable (for current process only)
def set_env(key, value):
    """Set environment variable."""
    os.environ[key] = str(value)


# =============================================================================
# CONCEPT: Configuration Classes
# =============================================================================

class Config:
    """Base configuration class."""

    def __init__(self):
        self.debug = self._get_bool('DEBUG', False)
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.app_name = os.environ.get('APP_NAME', 'MyApp')

    def _get_bool(self, key, default=False):
        """Get boolean from environment."""
        value = os.environ.get(key, str(default)).lower()
        return value in ('true', '1', 'yes')

    def _get_int(self, key, default=0):
        """Get integer from environment."""
        return int(os.environ.get(key, default))

    def _get_list(self, key, default=None):
        """Get comma-separated list from environment."""
        value = os.environ.get(key)
        if value is None:
            return default or []
        return [item.strip() for item in value.split(',')]


class DevelopmentConfig(Config):
    """Development configuration."""

    def __init__(self):
        super().__init__()
        self.debug = True
        self.database_url = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')


class ProductionConfig(Config):
    """Production configuration."""

    def __init__(self):
        super().__init__()
        self.debug = False
        self.database_url = get_required_env('DATABASE_URL')


# =============================================================================
# EXAMPLES
# =============================================================================

def example_basic_env():
    """Demonstrate basic environment variable usage."""
    print("=== Basic Environment Variables ===")

    # Set some variables for demo
    os.environ['MY_APP_DEBUG'] = 'true'
    os.environ['MY_APP_PORT'] = '8080'

    # Read variables
    debug = os.environ.get('MY_APP_DEBUG', 'false')
    port = os.environ.get('MY_APP_PORT', '3000')
    missing = os.environ.get('NONEXISTENT', 'default_value')

    print(f"DEBUG: {debug}")
    print(f"PORT: {port}")
    print(f"MISSING: {missing}")

    # Check if variable exists
    if 'MY_APP_DEBUG' in os.environ:
        print("MY_APP_DEBUG is set")


def example_dotenv_simulation():
    """Simulate dotenv behavior (without the package)."""
    print("\n=== Simulated .env Loading ===")

    # Create a sample .env file
    env_content = """
# Database settings
DATABASE_URL=postgresql://localhost/myapp
DATABASE_POOL_SIZE=5

# API Keys (don't commit real keys!)
API_KEY=your-api-key-here
SECRET_KEY=super-secret-key

# Feature flags
FEATURE_NEW_UI=true
ALLOWED_HOSTS=localhost,127.0.0.1
"""

    with open('.env.example', 'w') as f:
        f.write(env_content)

    # Simple .env parser
    def load_dotenv(filepath):
        """Load environment variables from file."""
        if not os.path.exists(filepath):
            return False

        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                # Parse key=value
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    os.environ[key] = value

        return True

    # Load and verify
    load_dotenv('.env.example')

    print(f"DATABASE_URL: {os.environ.get('DATABASE_URL')}")
    print(f"DATABASE_POOL_SIZE: {os.environ.get('DATABASE_POOL_SIZE')}")
    print(f"FEATURE_NEW_UI: {os.environ.get('FEATURE_NEW_UI')}")

    # Cleanup
    os.remove('.env.example')


def example_config_class():
    """Demonstrate configuration class usage."""
    print("\n=== Configuration Class ===")

    # Set up environment
    os.environ['DEBUG'] = 'true'
    os.environ['LOG_LEVEL'] = 'DEBUG'
    os.environ['APP_NAME'] = 'TestApp'

    # Use config
    config = Config()
    print(f"App: {config.app_name}")
    print(f"Debug: {config.debug}")
    print(f"Log Level: {config.log_level}")


def example_config_by_environment():
    """Demonstrate environment-based configuration."""
    print("\n=== Environment-Based Config ===")

    def get_config():
        """Get config based on environment."""
        env = os.environ.get('ENVIRONMENT', 'development')

        configs = {
            'development': DevelopmentConfig,
            'production': ProductionConfig,
        }

        config_class = configs.get(env, DevelopmentConfig)
        return config_class()

    # Development
    os.environ['ENVIRONMENT'] = 'development'
    config = get_config()
    print(f"Development DB: {config.database_url}")

    # Production (would need DATABASE_URL set)
    os.environ['ENVIRONMENT'] = 'production'
    os.environ['DATABASE_URL'] = 'postgresql://prod-server/app'
    config = get_config()
    print(f"Production DB: {config.database_url}")


def example_secrets_pattern():
    """Demonstrate secrets handling pattern."""
    print("\n=== Secrets Handling ===")

    class Secrets:
        """Handle sensitive configuration separately."""

        def __init__(self):
            self._api_key = None
            self._db_password = None

        @property
        def api_key(self):
            if self._api_key is None:
                self._api_key = get_required_env('API_KEY')
            return self._api_key

        @property
        def db_password(self):
            if self._db_password is None:
                self._db_password = get_required_env('DB_PASSWORD')
            return self._db_password

        def __repr__(self):
            """Don't expose secrets in repr."""
            return "Secrets(***)"

    os.environ['API_KEY'] = 'secret-api-key'
    os.environ['DB_PASSWORD'] = 'secret-password'

    secrets = Secrets()
    print(f"Secrets object: {secrets}")
    print(f"API Key loaded: {'*' * len(secrets.api_key)}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Config Validator

    Create a function that validates required configuration is present.

    schema = {
        'DATABASE_URL': {'required': True},
        'PORT': {'required': False, 'default': '8080', 'type': int},
        'DEBUG': {'required': False, 'default': 'false', 'type': bool},
        'ALLOWED_HOSTS': {'required': False, 'default': '', 'type': list}
    }

    config = validate_config(schema)
    # Returns validated config dict or raises ConfigError with all issues
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Multi-Environment Config

    Create a configuration system that:
    1. Loads base config from config.json
    2. Overrides with environment-specific config (config.{env}.json)
    3. Overrides with environment variables

    Priority: env vars > env config > base config

    Example:
    config.json: {"port": 3000, "debug": false}
    config.development.json: {"debug": true}
    PORT=8080 (env var)

    Result: {"port": 8080, "debug": true}
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Secrets Manager

    Create a secrets manager that:
    1. Loads secrets from environment variables
    2. Can also load from a secrets file (for local dev)
    3. Masks secrets in logs (shows only first/last 2 chars)
    4. Validates all required secrets are present at startup

    secrets = SecretsManager(['API_KEY', 'DB_PASSWORD', 'JWT_SECRET'])
    secrets.validate()  # Raises if any missing
    print(secrets.masked('API_KEY'))  # "ab...xy"
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Feature Flags

    Create a feature flag system using environment variables.

    flags = FeatureFlags(prefix='FEATURE_')

    # Set FEATURE_NEW_UI=true, FEATURE_DARK_MODE=false

    flags.is_enabled('new_ui')  # True
    flags.is_enabled('dark_mode')  # False
    flags.is_enabled('unknown')  # False (default)

    # Support percentage rollout
    # FEATURE_NEW_CHECKOUT=50 (50% of users)
    flags.is_enabled_for_user('new_checkout', user_id='123')
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Complete Configuration System

    Build a production-ready configuration system with:

    1. Multiple sources (in priority order):
       - Command-line arguments
       - Environment variables
       - .env file
       - Config file (JSON/YAML)
       - Defaults

    2. Features:
       - Type coercion (string -> int, bool, list, etc.)
       - Validation with custom validators
       - Required vs optional settings
       - Nested configuration support
       - Secrets handling (separate from regular config)
       - Environment-based overrides

    3. Usage patterns:
       - Singleton access: config.get('database.host')
       - Dot notation: config.database.host
       - Dictionary access: config['database']['host']

    4. Additional features:
       - Config reloading (for dev mode)
       - Config export (for debugging)
       - Config diff between environments

    Example usage:

    # Define schema
    schema = {
        'server': {
            'host': {'type': str, 'default': 'localhost'},
            'port': {'type': int, 'default': 8080, 'env': 'PORT'},
        },
        'database': {
            'url': {'type': str, 'required': True, 'env': 'DATABASE_URL'},
            'pool_size': {'type': int, 'default': 5},
        },
        'features': {
            'debug': {'type': bool, 'default': False, 'env': 'DEBUG'},
        }
    }

    # Initialize
    config = ConfigSystem(schema)
    config.load_file('.env')
    config.load_file('config.json')
    config.validate()

    # Use
    print(config.server.host)  # localhost
    print(config.database.url)  # from env or config file
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 9: Environment Variables and Configuration\n")
    print("=" * 50)

    # Run examples
    example_basic_env()
    example_dotenv_simulation()
    example_config_class()
    example_config_by_environment()
    example_secrets_pattern()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
