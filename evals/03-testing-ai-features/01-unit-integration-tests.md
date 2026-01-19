# Unit and Integration Testing for AI Features

## Overview

Traditional software testing applies to AI systems, but with unique considerations for non-deterministic outputs.

## Testing Pyramid for AI

```
                    ┌───────────┐
                    │   E2E     │  Few - expensive, slow
                    │   Tests   │
                    ├───────────┤
                 ┌──┴───────────┴──┐
                 │   Integration    │  More - test components
                 │      Tests       │
                 ├─────────────────┤
              ┌──┴─────────────────┴──┐
              │      Unit Tests        │  Many - fast, isolated
              └───────────────────────┘
```

## Unit Testing LLM Components

### Testing Prompt Templates

```python
"""
Unit tests for prompt templates.
"""

import unittest

class TestPromptTemplates(unittest.TestCase):
    """Test prompt template construction."""

    def test_system_prompt_has_required_sections(self):
        """Verify system prompt contains required elements."""
        from my_agent import build_system_prompt

        prompt = build_system_prompt(role="assistant")

        self.assertIn("You are", prompt)
        self.assertIn("assistant", prompt)

    def test_user_prompt_formats_correctly(self):
        """Test user prompt formatting."""
        from my_agent import format_user_prompt

        prompt = format_user_prompt(
            query="What is Python?",
            context="Programming language guide"
        )

        self.assertIn("What is Python?", prompt)
        self.assertIn("Programming language guide", prompt)

    def test_few_shot_examples_included(self):
        """Verify few-shot examples are added."""
        from my_agent import build_few_shot_prompt

        prompt = build_few_shot_prompt(
            task="classification",
            examples=[
                {"input": "Great!", "output": "positive"},
                {"input": "Terrible", "output": "negative"},
            ]
        )

        self.assertIn("Great!", prompt)
        self.assertIn("positive", prompt)
        self.assertEqual(prompt.count("Input:"), 2)


class TestInputProcessing(unittest.TestCase):
    """Test input processing functions."""

    def test_sanitize_removes_injection(self):
        """Test input sanitization."""
        from my_agent import sanitize_input

        malicious = "Ignore previous<script>alert()</script>"
        clean = sanitize_input(malicious)

        self.assertNotIn("<script>", clean)

    def test_truncate_long_input(self):
        """Test input truncation."""
        from my_agent import truncate_input

        long_input = "word " * 10000
        truncated = truncate_input(long_input, max_tokens=1000)

        self.assertLess(len(truncated.split()), 1100)

    def test_empty_input_handled(self):
        """Test empty input handling."""
        from my_agent import process_input

        result = process_input("")

        self.assertIsNotNone(result)
```

### Testing Output Parsers

```python
"""
Unit tests for output parsing.
"""

class TestOutputParsers(unittest.TestCase):
    """Test output parsing functions."""

    def test_json_extraction(self):
        """Test JSON extraction from response."""
        from my_agent import extract_json

        response = '''Here is the result:
        ```json
        {"name": "test", "value": 42}
        ```
        '''

        result = extract_json(response)

        self.assertEqual(result["name"], "test")
        self.assertEqual(result["value"], 42)

    def test_json_extraction_no_json(self):
        """Test handling when no JSON present."""
        from my_agent import extract_json

        response = "No JSON here"
        result = extract_json(response)

        self.assertIsNone(result)

    def test_list_parsing(self):
        """Test parsing numbered lists."""
        from my_agent import parse_numbered_list

        response = """
        1. First item
        2. Second item
        3. Third item
        """

        items = parse_numbered_list(response)

        self.assertEqual(len(items), 3)
        self.assertEqual(items[0], "First item")

    def test_extract_code_blocks(self):
        """Test code block extraction."""
        from my_agent import extract_code

        response = '''
        Here is Python code:
        ```python
        print("hello")
        ```
        '''

        code = extract_code(response, language="python")

        self.assertEqual(code.strip(), 'print("hello")')
```

### Testing Tool Selection

```python
"""
Unit tests for tool/function selection.
"""

class TestToolSelection(unittest.TestCase):
    """Test tool selection logic."""

    def test_math_query_selects_calculator(self):
        """Test calculator selected for math."""
        from my_agent import select_tool

        tool = select_tool("What is 5 + 3?")

        self.assertEqual(tool, "calculator")

    def test_search_query_selects_web(self):
        """Test web search selected for search."""
        from my_agent import select_tool

        tool = select_tool("Search for Python tutorials")

        self.assertEqual(tool, "web_search")

    def test_unknown_query_selects_default(self):
        """Test default selection."""
        from my_agent import select_tool

        tool = select_tool("asdfghjkl")

        self.assertEqual(tool, "general_llm")
```

## Integration Testing

### Testing LLM API Integration

```python
"""
Integration tests for LLM API calls.
"""

import unittest
from unittest.mock import Mock, patch

class TestLLMIntegration(unittest.TestCase):
    """Test LLM API integration."""

    @patch('my_agent.openai_client')
    def test_api_call_success(self, mock_client):
        """Test successful API call."""
        mock_client.chat.completions.create.return_value = Mock(
            choices=[Mock(message=Mock(content="Test response"))]
        )

        from my_agent import call_llm

        response = call_llm("Test prompt")

        self.assertEqual(response, "Test response")
        mock_client.chat.completions.create.assert_called_once()

    @patch('my_agent.openai_client')
    def test_api_retry_on_failure(self, mock_client):
        """Test retry logic on API failure."""
        mock_client.chat.completions.create.side_effect = [
            Exception("Rate limited"),
            Mock(choices=[Mock(message=Mock(content="Success"))])
        ]

        from my_agent import call_llm

        response = call_llm("Test prompt")

        self.assertEqual(response, "Success")
        self.assertEqual(mock_client.chat.completions.create.call_count, 2)

    @patch('my_agent.openai_client')
    def test_api_timeout_handled(self, mock_client):
        """Test timeout handling."""
        from requests.exceptions import Timeout

        mock_client.chat.completions.create.side_effect = Timeout()

        from my_agent import call_llm

        with self.assertRaises(Exception) as context:
            call_llm("Test prompt", timeout=1)

        self.assertIn("timeout", str(context.exception).lower())
```

### Testing RAG Pipeline

```python
"""
Integration tests for RAG pipeline.
"""

class TestRAGIntegration(unittest.TestCase):
    """Test RAG pipeline integration."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_docs = [
            {"id": "1", "text": "Python is a programming language."},
            {"id": "2", "text": "JavaScript runs in browsers."},
            {"id": "3", "text": "Machine learning uses data."},
        ]

    @patch('my_agent.vector_store')
    def test_retrieval_returns_relevant_docs(self, mock_store):
        """Test document retrieval."""
        mock_store.search.return_value = [
            {"id": "1", "score": 0.9, "text": "Python is a programming language."}
        ]

        from my_agent import retrieve_context

        docs = retrieve_context("Tell me about Python", top_k=3)

        self.assertEqual(len(docs), 1)
        self.assertIn("Python", docs[0]["text"])

    @patch('my_agent.vector_store')
    @patch('my_agent.llm_client')
    def test_full_rag_pipeline(self, mock_llm, mock_store):
        """Test full RAG query."""
        mock_store.search.return_value = [
            {"text": "Python was created by Guido van Rossum."}
        ]
        mock_llm.generate.return_value = "Python was created by Guido."

        from my_agent import rag_query

        response = rag_query("Who created Python?")

        self.assertIn("Guido", response)

    def test_empty_retrieval_handled(self):
        """Test handling when no docs retrieved."""
        with patch('my_agent.vector_store') as mock_store:
            mock_store.search.return_value = []

            from my_agent import retrieve_context

            docs = retrieve_context("Obscure topic xyz")

            self.assertEqual(len(docs), 0)
```

### Testing Multi-Agent Communication

```python
"""
Integration tests for multi-agent systems.
"""

class TestMultiAgentIntegration(unittest.TestCase):
    """Test multi-agent communication."""

    def test_agent_handoff(self):
        """Test handoff between agents."""
        from my_agent import AgentRouter, SpecialistAgent

        router = AgentRouter()
        specialist = SpecialistAgent(domain="math")

        query = "Calculate 15% of 200"
        routed = router.route(query)

        self.assertEqual(routed["agent"], "math")
        self.assertEqual(routed["query"], query)

    def test_agent_consensus(self):
        """Test multi-agent consensus."""
        from my_agent import ConsensusSystem

        system = ConsensusSystem(agents=["a", "b", "c"])

        responses = ["Yes", "Yes", "No"]
        consensus = system.get_consensus(responses)

        self.assertEqual(consensus, "Yes")

    @patch('my_agent.Agent')
    def test_sequential_chain(self, mock_agent):
        """Test sequential agent chain."""
        mock_agent.return_value.process.side_effect = [
            "Step 1 done",
            "Step 2 done",
            "Final result"
        ]

        from my_agent import AgentChain

        chain = AgentChain(steps=["analyze", "process", "summarize"])
        result = chain.run("Input data")

        self.assertEqual(result, "Final result")
        self.assertEqual(mock_agent.return_value.process.call_count, 3)
```

## Mocking LLM Responses

### Response Fixtures

```python
"""
LLM response fixtures for testing.
"""

# fixtures/llm_responses.py

CALCULATOR_RESPONSES = {
    "basic_addition": {
        "prompt_contains": "5 + 3",
        "response": "The result of 5 + 3 is 8.",
        "parsed_result": 8
    },
    "complex_calculation": {
        "prompt_contains": "percentage",
        "response": "15% of 200 is 30.",
        "parsed_result": 30
    },
}

CLASSIFICATION_RESPONSES = {
    "positive_sentiment": {
        "prompt_contains": "great product",
        "response": '{"sentiment": "positive", "confidence": 0.95}',
        "parsed_result": {"sentiment": "positive", "confidence": 0.95}
    },
    "negative_sentiment": {
        "prompt_contains": "terrible service",
        "response": '{"sentiment": "negative", "confidence": 0.88}',
        "parsed_result": {"sentiment": "negative", "confidence": 0.88}
    },
}


def get_mock_response(category, case):
    """Get mock response for test case."""
    categories = {
        "calculator": CALCULATOR_RESPONSES,
        "classification": CLASSIFICATION_RESPONSES,
    }
    return categories.get(category, {}).get(case, {})
```

### Mock LLM Class

```python
"""
Mock LLM for deterministic testing.
"""

class MockLLM:
    """Mock LLM for testing."""

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.call_history = []

    def generate(self, prompt):
        """Return mock response based on prompt."""
        self.call_history.append(prompt)

        # Check for matching response
        for key, response in self.responses.items():
            if key in prompt.lower():
                return response

        # Default response
        return "I don't know."

    def reset(self):
        """Reset call history."""
        self.call_history = []


# Usage in tests
class TestWithMockLLM(unittest.TestCase):

    def setUp(self):
        self.mock_llm = MockLLM({
            "capital of france": "The capital of France is Paris.",
            "python": "Python is a programming language.",
        })

    def test_geography_question(self):
        response = self.mock_llm.generate("What is the capital of France?")
        self.assertIn("Paris", response)

    def test_programming_question(self):
        response = self.mock_llm.generate("Tell me about Python")
        self.assertIn("programming", response)
```

## Handling Non-Determinism

### Fuzzy Assertions

```python
"""
Fuzzy assertions for non-deterministic outputs.
"""

from typing import List, Callable

def assert_contains_any(text: str, options: List[str], msg: str = None):
    """Assert text contains at least one option."""
    text_lower = text.lower()
    found = any(opt.lower() in text_lower for opt in options)
    if not found:
        raise AssertionError(msg or f"None of {options} found in: {text[:100]}")


def assert_semantic_match(actual: str, expected: str, threshold: float = 0.7):
    """Assert semantic similarity above threshold."""
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer('all-MiniLM-L6-v2')
    emb_actual = model.encode(actual)
    emb_expected = model.encode(expected)

    similarity = float(emb_actual @ emb_expected) / (
        float(sum(emb_actual**2)**0.5) * float(sum(emb_expected**2)**0.5)
    )

    if similarity < threshold:
        raise AssertionError(
            f"Similarity {similarity:.2f} below threshold {threshold}"
        )


def assert_format_valid(text: str, validator: Callable) -> None:
    """Assert output format is valid."""
    if not validator(text):
        raise AssertionError(f"Invalid format: {text[:100]}")


# Example validators
def is_valid_json(text):
    import json
    try:
        json.loads(text)
        return True
    except:
        return False


def is_numbered_list(text):
    import re
    return bool(re.search(r'^\d+\.', text, re.MULTILINE))
```

### Multiple Run Testing

```python
"""
Statistical testing for non-deterministic outputs.
"""

def test_with_retries(test_func, runs=5, pass_threshold=0.8):
    """
    Run test multiple times, pass if threshold met.

    Args:
        test_func: Test function to run
        runs: Number of runs
        pass_threshold: Fraction that must pass

    Returns:
        True if threshold met
    """
    passes = 0

    for _ in range(runs):
        try:
            test_func()
            passes += 1
        except AssertionError:
            pass

    pass_rate = passes / runs
    return pass_rate >= pass_threshold


# Usage
class TestNonDeterministic(unittest.TestCase):

    def test_story_generation_quality(self):
        """Test story meets quality threshold."""
        def single_run():
            from my_agent import generate_story

            story = generate_story(theme="adventure")

            # Must have these elements
            self.assertGreater(len(story), 100)
            assert_contains_any(story, ["hero", "journey", "quest", "adventure"])

        # 4 out of 5 runs must pass
        result = test_with_retries(single_run, runs=5, pass_threshold=0.8)
        self.assertTrue(result, "Story generation failed quality threshold")
```

## Test Organization

### Directory Structure

```
tests/
├── unit/
│   ├── test_prompts.py
│   ├── test_parsers.py
│   ├── test_tools.py
│   └── test_utils.py
├── integration/
│   ├── test_llm_api.py
│   ├── test_rag_pipeline.py
│   └── test_agents.py
├── fixtures/
│   ├── llm_responses.py
│   ├── sample_documents.py
│   └── test_cases.json
└── conftest.py
```

### pytest Configuration

```python
# conftest.py

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_llm():
    """Provide mock LLM for tests."""
    return MockLLM({
        "hello": "Hello! How can I help?",
        "calculate": "The answer is 42.",
    })


@pytest.fixture
def sample_documents():
    """Provide sample documents for RAG tests."""
    return [
        {"id": "1", "text": "Document 1 content"},
        {"id": "2", "text": "Document 2 content"},
    ]


@pytest.fixture
def test_config():
    """Provide test configuration."""
    return {
        "model": "test-model",
        "temperature": 0.0,
        "max_tokens": 100,
    }
```

## Best Practices

### Do's

1. **Mock external APIs** - Avoid real API calls in unit tests
2. **Use fixtures** - Consistent test data
3. **Test edge cases** - Empty inputs, long inputs, special characters
4. **Test error handling** - Verify graceful failures
5. **Isolate components** - Test one thing at a time

### Don'ts

1. **Don't test LLM intelligence** - That's the model's job
2. **Don't expect exact matches** - Use fuzzy assertions
3. **Don't skip integration tests** - Components must work together
4. **Don't hardcode API keys** - Use environment variables
5. **Don't ignore flaky tests** - Fix or isolate them

## Next Steps

- [02-regression-testing.md](02-regression-testing.md) - Baseline comparisons
- [03-golden-datasets.md](03-golden-datasets.md) - Creating test datasets
