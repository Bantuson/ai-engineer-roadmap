# AI Agent Frameworks Mini Projects

10 beginner-friendly projects exploring different AI agent frameworks, all powered by DeepSeek.

## Quick Start

### 1. Install Dependencies

```bash
pip install crewai langgraph langchain langchain-openai openai google-adk litellm llama-index llama-index-llms-openai pyautogen semantic-kernel pydantic-ai anthropic speechrecognition pyttsx3
```

### 2. Set Your API Key

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

### 3. Run Any Project

```bash
cd 09_pydantic_ai_calculator
python main.py
```

---

## Projects Overview

| # | Project | Framework | Pattern | Difficulty |
|---|---------|-----------|---------|------------|
| 1 | Story Writing Crew | CrewAI | Multi-Agent | Easy |
| 2 | Quiz Master | LangGraph | ReAct Loop | Medium |
| 3 | Multi-Language Translator | LangChain | Chain Composition | Easy |
| 4 | IT Helpdesk | OpenAI Agents SDK | Handoff/Routing | Medium |
| 5 | Voice Assistant | Google ADK | Tool Use + Voice | Medium |
| 6 | Study Buddy | LlamaIndex | RAG | Easy |
| 7 | Debate Club | AutoGen | Multi-Agent Chat | Medium |
| 8 | Daily Planner | Semantic Kernel | Planning + Plugins | Medium |
| 9 | Smart Calculator | Pydantic AI | Tool Use | Easy |
| 10 | Code Explainer | Claude Agents SDK | ReAct + Bash | Medium |

---

## Agent Design Patterns Demonstrated

### Multi-Agent Collaboration (Projects 1, 4, 7)
Multiple specialized agents work together, each with a specific role.

### ReAct Loop (Projects 2, 10)
Reason → Act → Observe → Repeat cycle for step-by-step problem solving.

### Chain Composition (Project 3)
Sequential processing through connected components.

### RAG - Retrieval Augmented Generation (Project 6)
Enhance responses with retrieved context from documents.

### Tool Use (Projects 5, 8, 9)
Agents use external tools to accomplish tasks.

### Handoff/Routing (Project 4)
Route conversations to specialized agents based on intent.

---

## DeepSeek Configuration

All projects use DeepSeek's `deepseek-chat` model via OpenAI-compatible API:

```python
# Base configuration pattern
base_url = "https://api.deepseek.com"
model = "deepseek-chat"
api_key = os.getenv("DEEPSEEK_API_KEY")
```

Each framework has its own configuration pattern - see individual projects for details.

---

## Prompting Techniques Used

| Technique | Projects | Description |
|-----------|----------|-------------|
| Role Personas | 1, 7 | Assign expert identities to agents |
| Chain-of-Thought | 2, 6 | Step-by-step reasoning |
| Few-Shot | 3 | Examples before the actual task |
| Routing Prompts | 4 | Instructions for agent handoffs |
| Context-First | 6 | Document context before questions |
| Structured Output | 8 | Specific format requirements |

---

## Python Skill Level

These projects use beginner-friendly Python:

**Used:**
- Functions with parameters
- `for`/`while` loops
- `if/elif/else` conditionals
- Lists and dictionaries
- f-strings
- `input()` and `print()`

**Avoided:**
- Classes and OOP
- List comprehensions
- Lambda functions
- Type hints
- Complex decorators (except framework-required)

---

## Troubleshooting

### API Key Issues
```bash
# Check if key is set
echo $DEEPSEEK_API_KEY

# Set it again if needed
export DEEPSEEK_API_KEY="your-key-here"
```

### Import Errors
```bash
# Reinstall the specific package
pip install --upgrade <package-name>
```

### Rate Limits
DeepSeek has generous rate limits, but if you hit them, wait a few seconds and try again.

---

## Project Details

### 01 - CrewAI Story Crew
Three agents (Plotter, Writer, Editor) collaborate to write a short story.
- Uses YAML configuration files
- Demonstrates sequential agent workflow

### 02 - LangGraph Quiz Master
Interactive quiz game with state management.
- StateGraph with nodes and edges
- Tracks score and provides feedback

### 03 - LangChain Translator
Translates text between multiple languages.
- LCEL pipe operator (`|`) for chains
- Few-shot prompting for quality

### 04 - OpenAI SDK Helpdesk
IT support with specialized agents.
- Triage → Password Agent or Software Agent
- Handoff pattern implementation

### 05 - Google ADK Voice Assistant
Voice-controlled assistant (speak and listen).
- Uses speech recognition and text-to-speech
- LiteLLM integration with DeepSeek

### 06 - LlamaIndex Study Buddy
Q&A over study notes.
- Simple RAG implementation
- Document loading and indexing

### 07 - AutoGen Debate Club
Two agents debate a topic with a moderator.
- Multi-agent conversation
- Persona-based arguing

### 08 - Semantic Kernel Planner
Daily task prioritization and scheduling.
- Kernel with plugins
- Structured output format

### 09 - Pydantic AI Calculator
Math operations with tool validation.
- `@agent.tool` decorator
- Clean tool definitions

### 10 - Claude Agents SDK Code Helper
Explains code and can run Python snippets.
- ReAct pattern
- Bash tool integration

---

## Learning Path

**Recommended order for beginners:**

1. **09_pydantic_ai_calculator** - Simplest tool use pattern
2. **03_langchain_translator** - Basic chain composition
3. **02_langgraph_quiz_master** - State management intro
4. **01_crewai_story_crew** - Multi-agent basics
5. **06_llamaindex_study_buddy** - RAG fundamentals
6. **07_autogen_debate_club** - Agent conversations
7. **04_openai_sdk_helpdesk** - Routing patterns
8. **05_google_adk_voice_assistant** - Voice I/O integration
9. **08_semantic_kernel_planner** - Planning with plugins
10. **10_claude_sdk_code_helper** - ReAct with real tools
