# Pydantic AI: Type-Safe Agent Development

## Overview

| Attribute | Details |
|-----------|---------|
| **Creator** | Pydantic (Samuel Colvin) |
| **License** | MIT |
| **GitHub Stars** | 5,000+ |
| **Primary Language** | Python |
| **First Release** | 2024 |
| **Latest Version** | 0.1+ (2025) |
| **Documentation** | [ai.pydantic.dev](https://ai.pydantic.dev) |
| **Repository** | [github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) |

Pydantic AI is a Python agent framework built by the creators of Pydantic. It emphasizes type safety, validation, and developer experience, leveraging Pydantic's powerful data validation capabilities to create reliable, well-structured AI agents with the fastest execution speeds among agent frameworks.

---

## Design Pattern Support

| Pattern | Support Level | Notes |
|---------|--------------|-------|
| **ReAct** | Excellent | Native tool use with validation |
| **Multi-Agent** | Moderate | Basic agent composition |
| **Tool Use** | Excellent | Type-safe tool definitions |
| **RAG** | Good | Integration with retrieval systems |
| **Reflection** | Good | Through result validators |
| **Planning** | Moderate | Via prompt engineering |
| **Human-in-the-Loop** | Good | Validation-based intervention |
| **Memory** | Moderate | Conversation history |
| **MCP Support** | Moderate | Community integrations |

---

## Best Practices

### 1. Define Typed Result Models
Use Pydantic models for all agent outputs to ensure type safety.

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class ResearchResult(BaseModel):
    """Structured research output."""
    title: str = Field(description="Research title")
    summary: str = Field(description="Executive summary")
    key_findings: list[str] = Field(description="List of key findings")
    confidence: float = Field(ge=0, le=1, description="Confidence score")
    sources: list[str] = Field(description="Source references")

agent = Agent(
    "openai:gpt-4o",
    result_type=ResearchResult,
    system_prompt="You are a research analyst. Provide structured research findings."
)

result = await agent.run("Research AI agent frameworks in 2025")
print(f"Confidence: {result.data.confidence}")
for finding in result.data.key_findings:
    print(f"- {finding}")
```

### 2. Use Type-Safe Tools
Define tools with full type annotations for validation.

```python
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

class OrderDetails(BaseModel):
    order_id: str
    status: str
    items: list[str]
    total: float

class Dependencies(BaseModel):
    db_connection: str
    api_key: str

agent = Agent(
    "openai:gpt-4o",
    deps_type=Dependencies,
    result_type=str
)

@agent.tool
async def get_order(
    ctx: RunContext[Dependencies],
    order_id: str
) -> OrderDetails:
    """Fetch order details from the database."""
    # Type-safe access to dependencies
    db = ctx.deps.db_connection
    # Fetch from database
    return OrderDetails(
        order_id=order_id,
        status="shipped",
        items=["Widget A", "Widget B"],
        total=99.99
    )

result = await agent.run(
    "Get details for order #12345",
    deps=Dependencies(db_connection="postgres://...", api_key="...")
)
```

### 3. Implement Result Validators
Add validation logic to ensure result quality.

```python
from pydantic_ai import Agent, ModelRetry

class AnalysisResult(BaseModel):
    analysis: str
    confidence: float

agent = Agent(
    "openai:gpt-4o",
    result_type=AnalysisResult
)

@agent.result_validator
async def validate_analysis(ctx: RunContext, result: AnalysisResult) -> AnalysisResult:
    """Validate analysis quality."""
    if result.confidence < 0.7:
        raise ModelRetry("Confidence too low. Please provide more detailed analysis.")
    if len(result.analysis) < 100:
        raise ModelRetry("Analysis too brief. Please elaborate.")
    return result
```

### 4. Use Dependency Injection
Leverage the dependency injection pattern for testable code.

```python
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class AppDependencies:
    database: DatabaseConnection
    cache: CacheClient
    logger: Logger

agent = Agent(
    "openai:gpt-4o",
    deps_type=AppDependencies
)

@agent.tool
async def search_database(
    ctx: RunContext[AppDependencies],
    query: str
) -> list[dict]:
    """Search the database."""
    ctx.deps.logger.info(f"Searching for: {query}")

    # Check cache first
    cached = await ctx.deps.cache.get(query)
    if cached:
        return cached

    # Query database
    results = await ctx.deps.database.search(query)
    await ctx.deps.cache.set(query, results)
    return results

# Easy to test with mock dependencies
async def test_agent():
    mock_deps = AppDependencies(
        database=MockDatabase(),
        cache=MockCache(),
        logger=MockLogger()
    )
    result = await agent.run("Find all orders", deps=mock_deps)
```

### 5. Use Streaming for Real-Time Output
Implement streaming for better user experience.

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", result_type=str)

async def stream_response(query: str):
    async with agent.run_stream(query) as response:
        async for text in response.stream():
            print(text, end="", flush=True)

        # Get final validated result
        final_result = await response.get_data()
        return final_result
```

### 6. Handle Errors Gracefully
Use Pydantic's validation for robust error handling.

```python
from pydantic import BaseModel, ValidationError
from pydantic_ai import Agent
from pydantic_ai.exceptions import UnexpectedModelBehavior

class SafeResult(BaseModel):
    success: bool
    data: str | None = None
    error: str | None = None

agent = Agent("openai:gpt-4o", result_type=SafeResult)

async def safe_run(query: str) -> SafeResult:
    try:
        result = await agent.run(query)
        return result.data
    except ValidationError as e:
        return SafeResult(success=False, error=f"Validation error: {e}")
    except UnexpectedModelBehavior as e:
        return SafeResult(success=False, error=f"Model error: {e}")
```

### 7. Use Model Configuration
Configure model behavior for different use cases.

```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# Custom model configuration
model = OpenAIModel(
    "gpt-4o",
    api_key="...",
    base_url="https://custom-endpoint.com",
    http_client=custom_http_client
)

agent = Agent(
    model,
    result_type=str,
    retries=3,
    model_settings={
        "temperature": 0.7,
        "max_tokens": 1000
    }
)
```

---

## Development Approach

### Core Concepts

1. **Agents**: Type-safe LLM interaction wrappers
2. **Tools**: Functions agents can call with validation
3. **Dependencies**: Injected context for tools
4. **Result Types**: Pydantic models for outputs
5. **Validators**: Result quality checks
6. **Streaming**: Real-time output generation

### Project Structure

```
my_pydantic_ai_project/
├── src/
│   └── my_agent/
│       ├── __init__.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── research.py
│       │   └── support.py
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── database.py
│       │   └── api.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── requests.py
│       │   └── responses.py
│       ├── validators/
│       │   ├── __init__.py
│       │   └── quality.py
│       └── dependencies.py
├── tests/
│   ├── test_agents.py
│   └── test_tools.py
├── .env
└── pyproject.toml
```

### Example: Customer Support Agent

```python
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

# Define response models
class CustomerInfo(BaseModel):
    id: str
    name: str
    email: str
    tier: str  # "basic", "premium", "enterprise"

class SupportResponse(BaseModel):
    message: str = Field(description="Response to the customer")
    ticket_created: bool = Field(description="Whether a ticket was created")
    ticket_id: str | None = Field(default=None, description="Ticket ID if created")
    escalated: bool = Field(default=False, description="Whether issue was escalated")

# Define dependencies
@dataclass
class SupportDependencies:
    customer_db: CustomerDatabase
    ticket_system: TicketSystem
    knowledge_base: KnowledgeBase

# Create agent
support_agent = Agent(
    "openai:gpt-4o",
    deps_type=SupportDependencies,
    result_type=SupportResponse,
    system_prompt="""You are a customer support agent for TechCorp.
    Be helpful, professional, and empathetic.
    Use available tools to look up information and create tickets when needed.
    Escalate complex issues to human support."""
)

# Define tools
@support_agent.tool
async def get_customer(
    ctx: RunContext[SupportDependencies],
    customer_id: str
) -> CustomerInfo:
    """Get customer information by ID."""
    return await ctx.deps.customer_db.get(customer_id)

@support_agent.tool
async def search_knowledge_base(
    ctx: RunContext[SupportDependencies],
    query: str
) -> list[str]:
    """Search the knowledge base for relevant articles."""
    results = await ctx.deps.knowledge_base.search(query)
    return [r.content for r in results[:5]]

@support_agent.tool
async def create_ticket(
    ctx: RunContext[SupportDependencies],
    customer_id: str,
    subject: str,
    description: str,
    priority: str = "normal"
) -> str:
    """Create a support ticket. Returns ticket ID."""
    ticket = await ctx.deps.ticket_system.create(
        customer_id=customer_id,
        subject=subject,
        description=description,
        priority=priority
    )
    return ticket.id

# Add result validator
@support_agent.result_validator
async def validate_response(
    ctx: RunContext[SupportDependencies],
    result: SupportResponse
) -> SupportResponse:
    """Ensure response quality."""
    if len(result.message) < 20:
        raise ModelRetry("Response too brief. Please provide more detail.")
    if result.escalated and not result.ticket_created:
        raise ModelRetry("Escalated issues must have a ticket created.")
    return result

# Usage
async def handle_support_request(
    customer_id: str,
    message: str
) -> SupportResponse:
    deps = SupportDependencies(
        customer_db=CustomerDatabase(),
        ticket_system=TicketSystem(),
        knowledge_base=KnowledgeBase()
    )

    result = await support_agent.run(
        f"Customer {customer_id} says: {message}",
        deps=deps
    )
    return result.data
```

### Example: Data Analysis Agent

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent
import pandas as pd

class AnalysisResult(BaseModel):
    summary: str = Field(description="Summary of findings")
    statistics: dict[str, float] = Field(description="Key statistics")
    insights: list[str] = Field(description="Key insights")
    recommendations: list[str] = Field(description="Actionable recommendations")

@dataclass
class AnalysisDeps:
    dataframe: pd.DataFrame

analyst = Agent(
    "openai:gpt-4o",
    deps_type=AnalysisDeps,
    result_type=AnalysisResult,
    system_prompt="You are a data analyst. Analyze data and provide insights."
)

@analyst.tool
def get_statistics(ctx: RunContext[AnalysisDeps]) -> dict:
    """Get basic statistics about the dataset."""
    df = ctx.deps.dataframe
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "numeric_summary": df.describe().to_dict()
    }

@analyst.tool
def query_data(
    ctx: RunContext[AnalysisDeps],
    column: str,
    operation: str
) -> float:
    """Perform operation on a column. Operations: mean, sum, min, max, std."""
    df = ctx.deps.dataframe
    if column not in df.columns:
        raise ValueError(f"Column {column} not found")

    ops = {
        "mean": df[column].mean,
        "sum": df[column].sum,
        "min": df[column].min,
        "max": df[column].max,
        "std": df[column].std
    }
    return float(ops[operation]())

# Usage
async def analyze_data(df: pd.DataFrame, question: str) -> AnalysisResult:
    result = await analyst.run(
        question,
        deps=AnalysisDeps(dataframe=df)
    )
    return result.data
```

---

## Tradeoffs

### Advantages

| Advantage | Description |
|-----------|-------------|
| **Type Safety** | Full Pydantic validation on all I/O |
| **Fastest Execution** | Minimal overhead, optimized performance |
| **Developer Experience** | IDE support, autocompletion, refactoring |
| **Testability** | Dependency injection, easy mocking |
| **Validation** | Built-in input/output validation |
| **Pydantic Ecosystem** | Works with existing Pydantic models |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Newer Framework** | Smaller ecosystem and community |
| **Limited Multi-Agent** | Basic agent composition |
| **Fewer Integrations** | Less pre-built connectors than LangChain |
| **Python Only** | No TypeScript/Java support |
| **Less Documentation** | Growing but not comprehensive |
| **Limited Ecosystem** | Fewer examples and tutorials |

---

## Scalability

### Production Readiness

| Aspect | Status | Notes |
|--------|--------|-------|
| **Async Execution** | Excellent | Native async support |
| **Streaming** | Excellent | Built-in streaming |
| **Type Safety** | Excellent | Full Pydantic validation |
| **Error Handling** | Excellent | Structured exceptions |
| **Observability** | Good | Logfire integration |
| **Performance** | Excellent | Fastest among frameworks |

### Performance Optimization

```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
import httpx

# Use connection pooling for better performance
limits = httpx.Limits(max_connections=100, max_keepalive_connections=20)
timeout = httpx.Timeout(60.0, connect=10.0)
http_client = httpx.AsyncClient(limits=limits, timeout=timeout)

model = OpenAIModel(
    "gpt-4o",
    http_client=http_client
)

agent = Agent(model, result_type=str)

# Batch processing with concurrency control
import asyncio
from asyncio import Semaphore

async def batch_process(queries: list[str], max_concurrent: int = 10):
    semaphore = Semaphore(max_concurrent)

    async def process_one(query: str):
        async with semaphore:
            return await agent.run(query)

    results = await asyncio.gather(*[
        process_one(q) for q in queries
    ])
    return results
```

### Recommended Architecture

```
┌─────────────────────────────────────────────┐
│              FastAPI Application            │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼───────────────────┐
│          Pydantic AI Agents           │
│   ┌─────────┐  ┌─────────┐            │
│   │Research │  │Support  │            │
│   │ Agent   │  │ Agent   │            │
│   └────┬────┘  └────┬────┘            │
│        │            │                 │
│   ┌────▼────────────▼────┐            │
│   │   Tool Functions     │            │
│   │  (Type-Safe Tools)   │            │
│   └──────────────────────┘            │
└───────────────────┬───────────────────┘
                    │
     ┌──────────────┴──────────────┐
     │                             │
┌────▼────┐                  ┌────▼────┐
│   LLM   │                  │ Database│
│   API   │                  │  Cache  │
└─────────┘                  └─────────┘
```

---

## Enterprise Adoption

### Notable Users

- **Pydantic Users**: Organizations already using Pydantic
- **Type-Safety Focused Teams**: Engineering teams prioritizing reliability
- **Performance-Critical Applications**: Low-latency requirements

### Case Studies

**Financial Data Analysis**
- Type-safe financial calculations
- Validated output reports
- 50% fewer runtime errors

**API Automation**
- Structured API responses
- Automatic validation
- Easy integration testing

### Maturity Assessment

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Documentation** | 3 | Growing, well-structured |
| **Community** | 3 | Smaller but active |
| **Enterprise Support** | 2 | Community support primarily |
| **Security** | 4 | Validation prevents many issues |
| **Compliance** | 2 | Limited enterprise features |
| **Long-term Viability** | 4 | Backed by Pydantic team |

---

## When to Choose Pydantic AI

### Ideal Use Cases

- Type-safety focused teams
- Performance-critical applications
- Teams already using Pydantic
- Projects requiring strong validation
- Python-native development
- Rapid, reliable prototyping

### Avoid When

- Need extensive integrations (use LangChain)
- Complex multi-agent systems (use CrewAI or AutoGen)
- Non-Python environments
- Need large community support
- Enterprise compliance requirements

---

## Sources

- [Pydantic AI Documentation](https://ai.pydantic.dev)
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [Logfire (Observability)](https://pydantic.dev/logfire)

---

*Last updated: January 2026*
