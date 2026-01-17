# LlamaIndex: Best-in-Class RAG Framework

## Overview

| Attribute | Details |
|-----------|---------|
| **Creator** | LlamaIndex Inc (formerly GPT Index) |
| **License** | MIT |
| **GitHub Stars** | 40,000+ |
| **Primary Languages** | Python, TypeScript |
| **First Release** | 2022 |
| **Latest Version** | 0.11+ (2025) |
| **Documentation** | [docs.llamaindex.ai](https://docs.llamaindex.ai) |
| **Repository** | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) |

LlamaIndex is the leading framework for building RAG (Retrieval-Augmented Generation) applications. It excels at connecting LLMs with external data sources, offering sophisticated indexing, retrieval, and query capabilities that go far beyond simple vector search.

---

## Design Pattern Support

| Pattern | Support Level | Notes |
|---------|--------------|-------|
| **ReAct** | Good | Through agent module |
| **Multi-Agent** | Moderate | Basic multi-agent support |
| **Tool Use** | Good | Tool integration for agents |
| **RAG** | Excellent | Core strength - best-in-class |
| **Reflection** | Good | Query refinement patterns |
| **Planning** | Good | Query planning and decomposition |
| **Human-in-the-Loop** | Moderate | Callback-based intervention |
| **Memory** | Excellent | Chat memory and index memory |
| **MCP Support** | Good | Growing integration support |

---

## Best Practices

### 1. Choose the Right Index Type
Select index types based on your data and query patterns.

```python
from llama_index.core import VectorStoreIndex, SummaryIndex, TreeIndex

# Vector index for semantic search
vector_index = VectorStoreIndex.from_documents(documents)

# Summary index for full document understanding
summary_index = SummaryIndex.from_documents(documents)

# Tree index for hierarchical data
tree_index = TreeIndex.from_documents(documents)
```

### 2. Use Node Parsers for Optimal Chunking
Configure chunking based on your document types.

```python
from llama_index.core.node_parser import (
    SentenceSplitter,
    SemanticSplitterNodeParser,
    MarkdownNodeParser
)

# For general text
splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=200)

# For semantic coherence
semantic_splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95,
    embed_model=embed_model
)

# For markdown documents
markdown_parser = MarkdownNodeParser()
```

### 3. Implement Hybrid Search
Combine vector and keyword search for better retrieval.

```python
from llama_index.core.retrievers import VectorIndexRetriever, KeywordTableRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import get_response_synthesizer

# Create hybrid retriever
vector_retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=5)
keyword_retriever = KeywordTableRetriever(index=keyword_index, top_k=5)

# Combine results
from llama_index.core.retrievers import QueryFusionRetriever

fusion_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, keyword_retriever],
    similarity_top_k=10,
    num_queries=4,  # Query expansion
    mode="reciprocal_rerank"
)
```

### 4. Use Query Transformations
Transform queries for better retrieval accuracy.

```python
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core.query_engine import CustomQueryEngine

# HyDE: Hypothetical Document Embeddings
from llama_index.core.indices.query.query_transform import HyDEQueryTransform

hyde = HyDEQueryTransform(llm=llm, include_original=True)
query_engine = TransformQueryEngine(base_query_engine, hyde)
```

### 5. Implement Evaluation
Use built-in evaluation tools to measure RAG quality.

```python
from llama_index.core.evaluation import (
    FaithfulnessEvaluator,
    RelevancyEvaluator,
    CorrectnessEvaluator
)

# Evaluate responses
faithfulness = FaithfulnessEvaluator(llm=eval_llm)
relevancy = RelevancyEvaluator(llm=eval_llm)

result = faithfulness.evaluate_response(query=query, response=response)
print(f"Faithfulness score: {result.score}")
```

### 6. Use Observability Tools
Track retrieval and generation quality.

```python
from llama_index.core import set_global_handler

# Use LlamaTrace for observability
set_global_handler("arize_phoenix")

# Or use callback handlers
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler

debug_handler = LlamaDebugHandler()
callback_manager = CallbackManager([debug_handler])
```

### 7. Optimize for Production
Configure caching and performance optimizations.

```python
from llama_index.core import Settings
from llama_index.core.storage import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Use production vector store
vector_store = QdrantVectorStore(
    collection_name="my_collection",
    url="http://localhost:6333"
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Configure global settings
Settings.chunk_size = 1024
Settings.chunk_overlap = 200
Settings.llm = llm
Settings.embed_model = embed_model
```

---

## Development Approach

### Core Concepts

1. **Documents**: Raw data containers
2. **Nodes**: Chunked document pieces
3. **Indices**: Organized node structures
4. **Retrievers**: Node retrieval strategies
5. **Query Engines**: End-to-end query processing
6. **Response Synthesizers**: Answer generation

### Project Structure

```
my_rag_project/
├── src/
│   └── my_rag/
│       ├── __init__.py
│       ├── indexing/
│       │   ├── __init__.py
│       │   ├── loaders.py
│       │   ├── parsers.py
│       │   └── indices.py
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── retrievers.py
│       │   └── rerankers.py
│       ├── synthesis/
│       │   ├── __init__.py
│       │   └── synthesizers.py
│       ├── agents/
│       │   ├── __init__.py
│       │   └── rag_agent.py
│       └── evaluation/
│           ├── __init__.py
│           └── metrics.py
├── data/
│   └── documents/
├── storage/
│   └── indices/
├── tests/
├── .env
└── pyproject.toml
```

### Example: Advanced RAG System

```python
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    StorageContext,
    load_index_from_storage
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import (
    SimilarityPostprocessor,
    LongContextReorder
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Configure settings
Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=200)

# Load documents
documents = SimpleDirectoryReader(
    input_dir="./data/documents",
    recursive=True,
    filename_as_id=True
).load_data()

# Create or load index
try:
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
except:
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./storage")

# Configure retriever with postprocessors
retriever = VectorIndexRetriever(index=index, similarity_top_k=10)

postprocessors = [
    SimilarityPostprocessor(similarity_cutoff=0.7),
    LongContextReorder()  # Reorder to avoid "lost in the middle"
]

# Create query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=postprocessors
)

# Query
response = query_engine.query("What are the key findings about AI agents?")
print(response)

# Access source nodes
for node in response.source_nodes:
    print(f"Score: {node.score:.3f} - {node.node.metadata['file_name']}")
```

### Example: RAG Agent with Tools

```python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, FunctionTool
from llama_index.core import VectorStoreIndex

# Create multiple indices for different document types
research_index = VectorStoreIndex.from_documents(research_docs)
code_index = VectorStoreIndex.from_documents(code_docs)

# Create query engine tools
research_tool = QueryEngineTool.from_defaults(
    query_engine=research_index.as_query_engine(),
    name="research_search",
    description="Search research papers and academic content"
)

code_tool = QueryEngineTool.from_defaults(
    query_engine=code_index.as_query_engine(),
    name="code_search",
    description="Search code documentation and examples"
)

# Create function tools
@FunctionTool.from_defaults(
    name="calculate",
    description="Perform mathematical calculations"
)
def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Create agent
agent = ReActAgent.from_tools(
    tools=[research_tool, code_tool, calculate],
    llm=Settings.llm,
    verbose=True
)

# Run agent
response = agent.chat(
    "Find research on AI agent architectures and calculate the average "
    "number of citations if 3 papers have 150, 200, and 175 citations"
)
print(response)
```

---

## Tradeoffs

### Advantages

| Advantage | Description |
|-----------|-------------|
| **RAG Excellence** | Best-in-class retrieval and indexing |
| **Data Connectors** | 160+ data source integrations |
| **Flexible Indexing** | Multiple index types for different needs |
| **Evaluation Tools** | Built-in RAG evaluation metrics |
| **Query Optimization** | Advanced query transformation techniques |
| **Active Development** | Weekly releases, rapid innovation |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Agent Limitations** | Agent module less mature than dedicated frameworks |
| **Complexity** | Many concepts to learn for advanced usage |
| **Documentation Gaps** | Advanced patterns less documented |
| **Performance Tuning** | Requires expertise for optimal performance |
| **Breaking Changes** | Rapid development leads to API churn |
| **Memory Usage** | Large indices can consume significant memory |

---

## Scalability

### Production Readiness

| Aspect | Status | Notes |
|--------|--------|-------|
| **Async Execution** | Excellent | Native async support |
| **Streaming** | Excellent | Response streaming |
| **Vector Store Integration** | Excellent | All major vector DBs |
| **Caching** | Good | Index and response caching |
| **Observability** | Excellent | LlamaTrace, Phoenix integration |
| **Deployment** | Good | LlamaCloud for managed hosting |

### Production Vector Store Setup

```python
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone

# Initialize Pinecone
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
pinecone_index = pc.Index("my-index")

# Create vector store
vector_store = PineconeVectorStore(
    pinecone_index=pinecone_index,
    namespace="production"
)

# Build index with production vector store
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)
```

### Recommended Architecture

```
┌─────────────────────────────────────────────┐
│              Load Balancer                  │
└───────────────────┬─────────────────────────┘
                    │
     ┌──────────────┴──────────────┐
     │                             │
┌────▼────┐                  ┌────▼────┐
│ Query   │                  │ Query   │
│ Worker 1│                  │ Worker N│
└────┬────┘                  └────┬────┘
     │                             │
     └──────────────┬──────────────┘
                    │
┌───────────────────▼───────────────────┐
│           Vector Database             │
│  (Pinecone / Qdrant / Weaviate)       │
└───────────────────┬───────────────────┘
                    │
┌───────────────────▼───────────────────┐
│          Document Storage             │
│    (S3 / GCS / Local filesystem)      │
└───────────────────┬───────────────────┘
                    │
         ┌──────────▼──────────┐
         │    LlamaTrace       │
         │  (Observability)    │
         └─────────────────────┘
```

---

## Enterprise Adoption

### Notable Users

- **Uber**: Knowledge base search
- **Notion**: AI-powered features
- **Multiple Fortune 500**: Document Q&A systems (under NDA)

### Case Studies

**Legal Document Analysis**
- RAG over 1M+ legal documents
- 95% accuracy on complex legal queries
- 10x faster document research

**Enterprise Knowledge Base**
- Unified search across 50+ data sources
- 100K queries/day
- Multi-language support

### Maturity Assessment

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Documentation** | 4 | Comprehensive, well-organized |
| **Community** | 5 | Large, active Discord and forums |
| **Enterprise Support** | 4 | LlamaCloud enterprise tier |
| **Security** | 3 | Basic, improving |
| **Compliance** | 3 | SOC2 through LlamaCloud |
| **Long-term Viability** | 5 | Strong funding, market leader in RAG |

---

## When to Choose LlamaIndex

### Ideal Use Cases

- Document Q&A and knowledge bases
- Enterprise search applications
- Multi-source data retrieval
- Complex RAG pipelines
- Semantic search applications
- Data-heavy AI applications

### Avoid When

- Need advanced multi-agent (use CrewAI or LangGraph)
- Simple chatbot without retrieval
- Focus on workflow automation (use LangGraph)
- Need computer/browser use (use Claude Agents SDK)

---

## Sources

- [LlamaIndex Documentation](https://docs.llamaindex.ai)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)
- [LlamaCloud](https://cloud.llamaindex.ai/)
- [LlamaIndex Blog](https://www.llamaindex.ai/blog)
- [LlamaHub - Data Loaders](https://llamahub.ai/)

---

*Last updated: January 2026*
