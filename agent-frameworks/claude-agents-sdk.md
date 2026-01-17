# Claude Agents SDK: Computer Access Paradigm

## Overview

| Attribute | Details |
|-----------|---------|
| **Creator** | Anthropic |
| **License** | MIT |
| **GitHub Stars** | 8,000+ |
| **Primary Languages** | Python, TypeScript |
| **First Release** | 2024 |
| **Latest Version** | 1.0+ (2025) |
| **Documentation** | [docs.anthropic.com/claude-code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code) |
| **Repository** | [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) |

The Claude Agents SDK is Anthropic's framework for building AI agents that can interact with computers like humans do. It pioneered the "computer use" paradigm, allowing agents to control browsers, terminals, and desktop applications through vision and action.

---

## Design Pattern Support

| Pattern | Support Level | Notes |
|---------|--------------|-------|
| **ReAct** | Excellent | Native reasoning and action loops |
| **Multi-Agent** | Good | Agent handoffs supported |
| **Tool Use** | Excellent | Computer use, bash, file operations |
| **RAG** | Good | File reading, web browsing |
| **Reflection** | Good | Self-correction through observation |
| **Planning** | Moderate | Through agentic prompting |
| **Human-in-the-Loop** | Excellent | Built-in approval workflows |
| **Memory** | Good | Conversation and file-based memory |
| **MCP Support** | Excellent | Native MCP integration |

---

## Best Practices

### 1. Use MCP for Tool Integration
Leverage the Model Context Protocol for standardized tool access.

```python
from claude_code import Agent
from claude_code.mcp import MCPServer

# Connect to MCP servers for tools
agent = Agent(
    mcp_servers=[
        MCPServer("filesystem", path="/workspace"),
        MCPServer("github", token=os.environ["GITHUB_TOKEN"]),
        MCPServer("database", connection_string=os.environ["DB_URL"])
    ]
)
```

### 2. Implement Proper Sandboxing
Always sandbox computer use for security.

```python
from claude_code import Agent, Sandbox

# Create sandboxed environment
sandbox = Sandbox(
    allowed_paths=["/workspace", "/tmp"],
    network_access=["api.example.com"],
    max_execution_time=300
)

agent = Agent(
    sandbox=sandbox,
    computer_use=True
)
```

### 3. Use Visual Grounding for Accuracy
Leverage Claude's vision capabilities for precise UI interactions.

```python
from claude_code import Agent

agent = Agent(computer_use=True)

# Agent can see and interact with UI elements
result = await agent.run(
    "Open the browser, navigate to github.com, and star the anthropic/claude-code repository",
    screenshot_interval=1.0  # Take screenshots every second
)
```

### 4. Implement Checkpoints for Long Tasks
Save state periodically for long-running automation.

```python
from claude_code import Agent, Checkpoint

async def long_running_task():
    agent = Agent()

    # Create checkpoint
    checkpoint = Checkpoint("task-123")

    for step in task_steps:
        result = await agent.run(step)
        await checkpoint.save(result)

        if result.needs_human_review:
            await checkpoint.pause_for_review()
```

### 5. Use Bash Tool for System Operations
Leverage the bash tool for command-line automation.

```python
from claude_code import Agent
from claude_code.tools import BashTool

agent = Agent(
    tools=[
        BashTool(
            allowed_commands=["git", "npm", "python", "pytest"],
            working_directory="/workspace"
        )
    ]
)

result = await agent.run(
    "Clone the repository, install dependencies, and run the tests"
)
```

### 6. Handle Errors with Recovery Strategies
Implement graceful error recovery.

```python
from claude_code import Agent, ErrorStrategy

agent = Agent(
    error_strategy=ErrorStrategy(
        max_retries=3,
        retry_delay=1.0,
        on_failure="ask_human",  # or "abort", "skip"
        screenshot_on_error=True
    )
)
```

### 7. Use Structured Outputs for Automation
Get structured results from agent actions.

```python
from pydantic import BaseModel
from claude_code import Agent

class TestResult(BaseModel):
    passed: int
    failed: int
    skipped: int
    coverage: float
    errors: list[str]

agent = Agent()
result = await agent.run(
    "Run the test suite and report results",
    output_schema=TestResult
)
print(f"Tests passed: {result.passed}/{result.passed + result.failed}")
```

---

## Development Approach

### Core Concepts

1. **Computer Use**: Vision-based UI interaction
2. **Bash Tool**: Command-line execution
3. **File Operations**: Read, write, edit files
4. **MCP Integration**: Standardized tool protocol
5. **Sandboxing**: Secure execution environments
6. **Hooks**: Event-driven customization

### Project Structure

```
my_claude_agent/
├── src/
│   └── my_agent/
│       ├── __init__.py
│       ├── agent.py           # Main agent configuration
│       ├── tools/
│       │   ├── __init__.py
│       │   └── custom.py      # Custom tools
│       ├── mcp/
│       │   ├── __init__.py
│       │   └── servers.py     # MCP server configs
│       └── hooks/
│           ├── __init__.py
│           └── handlers.py    # Event hooks
├── .claude/
│   └── settings.json          # Claude Code settings
├── tests/
│   └── test_agent.py
├── .env
└── pyproject.toml
```

### Example: Code Review Agent

```python
from claude_code import Agent
from claude_code.tools import BashTool, FileTool, GitTool
from claude_code.mcp import MCPServer
from pydantic import BaseModel

class ReviewResult(BaseModel):
    summary: str
    issues: list[dict]
    suggestions: list[str]
    approval: bool
    confidence: float

# Configure agent with development tools
agent = Agent(
    name="CodeReviewer",
    instructions="""You are an expert code reviewer.
    Review code changes for:
    - Code quality and best practices
    - Security vulnerabilities
    - Performance issues
    - Test coverage

    Provide actionable feedback and suggestions.""",
    tools=[
        BashTool(allowed_commands=["git", "grep", "find"]),
        FileTool(allowed_paths=["/workspace"]),
        GitTool()
    ],
    mcp_servers=[
        MCPServer("github")
    ]
)

async def review_pull_request(pr_url: str) -> ReviewResult:
    result = await agent.run(
        f"""Review the pull request at {pr_url}:
        1. Fetch the PR changes
        2. Analyze the code diff
        3. Check for security issues
        4. Review test coverage
        5. Provide a detailed review with suggestions""",
        output_schema=ReviewResult
    )
    return result

# Run review
async def main():
    review = await review_pull_request(
        "https://github.com/example/repo/pull/123"
    )
    print(f"Approval: {review.approval}")
    print(f"Issues found: {len(review.issues)}")
    for issue in review.issues:
        print(f"  - {issue['severity']}: {issue['description']}")

import asyncio
asyncio.run(main())
```

### Example: Browser Automation Agent

```python
from claude_code import Agent
from claude_code.tools import ComputerTool

# Enable computer use for browser automation
agent = Agent(
    name="BrowserAgent",
    instructions="""You can control a web browser through screenshots and mouse/keyboard actions.
    Navigate carefully, wait for pages to load, and verify actions succeeded.""",
    tools=[
        ComputerTool(
            display_size=(1920, 1080),
            browser="chromium"
        )
    ]
)

async def scrape_and_analyze(url: str, query: str):
    result = await agent.run(
        f"""Navigate to {url} and find information about: {query}

        Steps:
        1. Open the browser to the URL
        2. Navigate the site to find relevant information
        3. Extract and summarize the findings
        4. Take a screenshot of the relevant section"""
    )
    return result

# Run browser automation
async def main():
    result = await scrape_and_analyze(
        "https://news.ycombinator.com",
        "AI agent frameworks"
    )
    print(result.output)

import asyncio
asyncio.run(main())
```

---

## Tradeoffs

### Advantages

| Advantage | Description |
|-----------|-------------|
| **Computer Use** | Unique vision-based UI automation |
| **MCP Native** | First-class Model Context Protocol support |
| **Safety First** | Built-in sandboxing and approvals |
| **Claude Optimized** | Best experience with Claude models |
| **Developer Tools** | Excellent for code-related tasks |
| **Anthropic Backing** | Strong safety research foundation |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Claude Lock-in** | Designed specifically for Claude models |
| **Computer Use Costs** | Screenshots increase token usage |
| **Newer Framework** | Smaller ecosystem than LangChain |
| **Limited Integrations** | Fewer pre-built connectors |
| **Learning Curve** | Computer use paradigm requires understanding |
| **Beta Features** | Some capabilities still evolving |

---

## Scalability

### Production Readiness

| Aspect | Status | Notes |
|--------|--------|-------|
| **Async Execution** | Excellent | Native async throughout |
| **Streaming** | Excellent | Real-time output streaming |
| **Sandboxing** | Excellent | Docker/container isolation |
| **Error Handling** | Good | Retry and recovery patterns |
| **Observability** | Good | Logging and tracing |
| **Caching** | Moderate | Screenshot caching available |

### Deployment Patterns

```python
# Docker-based deployment for computer use
from claude_code import Agent
from claude_code.deployment import DockerSandbox

sandbox = DockerSandbox(
    image="anthropic/claude-computer-use:latest",
    resources={
        "memory": "4g",
        "cpu": 2
    }
)

agent = Agent(
    sandbox=sandbox,
    computer_use=True
)
```

### Recommended Architecture

```
┌─────────────────────────────────────────────┐
│              API Gateway                    │
└───────────────────┬─────────────────────────┘
                    │
     ┌──────────────┴──────────────┐
     │                             │
┌────▼────┐                  ┌────▼────┐
│ Agent   │                  │ Agent   │
│ Worker 1│                  │ Worker N│
└────┬────┘                  └────┬────┘
     │                             │
     └──────────────┬──────────────┘
                    │
┌───────────────────▼───────────────────┐
│        Docker Sandbox Pool            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │Container│ │Container│ │Container│  │
│  │ (VNC)   │ │ (VNC)   │ │ (VNC)   │  │
│  └─────────┘ └─────────┘ └─────────┘  │
└───────────────────┬───────────────────┘
                    │
            ┌───────▼───────┐
            │  Anthropic    │
            │  Claude API   │
            └───────────────┘
```

---

## Enterprise Adoption

### Notable Users

- **Anthropic Internal**: Development automation
- **Tech Companies**: Code review and deployment automation
- **Research Labs**: Experiment automation

### Case Studies

**Automated Code Review Pipeline**
- Review 500+ PRs per week
- 60% reduction in review cycle time
- Integration with GitHub Actions

**QA Automation System**
- Browser-based testing automation
- Visual regression detection
- 80% test coverage automation

### Maturity Assessment

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Documentation** | 4 | Growing, well-structured |
| **Community** | 3 | Growing, active Discord |
| **Enterprise Support** | 4 | Anthropic enterprise tier |
| **Security** | 5 | Safety-focused design |
| **Compliance** | 4 | SOC2 available |
| **Long-term Viability** | 5 | Core Anthropic product |

---

## When to Choose Claude Agents SDK

### Ideal Use Cases

- Code-centric automation (reviews, testing, deployment)
- Browser and desktop automation
- Tasks requiring computer vision
- Development workflow automation
- Security-sensitive applications
- MCP-based tool ecosystems

### Avoid When

- Need model flexibility (use LangChain)
- Simple chatbot applications
- Heavy RAG requirements (use LlamaIndex)
- Non-visual automation tasks
- Cost-sensitive applications (computer use adds tokens)

---

## Sources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)
- [Claude Agents SDK GitHub](https://github.com/anthropics/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Computer Use Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
- [Anthropic Blog](https://www.anthropic.com/blog)

---

*Last updated: January 2026*
