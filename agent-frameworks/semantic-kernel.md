# Semantic Kernel: Enterprise .NET Integration

## Overview

| Attribute | Details |
|-----------|---------|
| **Creator** | Microsoft |
| **License** | MIT |
| **GitHub Stars** | 22,000+ |
| **Primary Languages** | C#, Python, Java |
| **First Release** | 2023 |
| **Latest Version** | 1.0+ (2025) |
| **Documentation** | [learn.microsoft.com/semantic-kernel](https://learn.microsoft.com/en-us/semantic-kernel/) |
| **Repository** | [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) |

Semantic Kernel is Microsoft's SDK for integrating AI into enterprise applications. It's designed for organizations already invested in the Microsoft ecosystem, offering first-class C#/.NET support with enterprise patterns like dependency injection, strong typing, and Azure service integration.

---

## Design Pattern Support

| Pattern | Support Level | Notes |
|---------|--------------|-------|
| **ReAct** | Excellent | Auto function calling |
| **Multi-Agent** | Good | Agent framework integration |
| **Tool Use** | Excellent | Native plugins and functions |
| **RAG** | Good | Memory and connector patterns |
| **Reflection** | Good | Planner reflection patterns |
| **Planning** | Good | Handlebars and Stepwise planners |
| **Human-in-the-Loop** | Good | Filter-based intervention |
| **Memory** | Good | Multiple memory connectors |
| **MCP Support** | Good | Community integration |

---

## Best Practices

### 1. Use Dependency Injection
Leverage .NET's DI container for proper service management.

```csharp
using Microsoft.SemanticKernel;
using Microsoft.Extensions.DependencyInjection;

var builder = Kernel.CreateBuilder();

builder.Services.AddAzureOpenAIChatCompletion(
    deploymentName: "gpt-4o",
    endpoint: Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!,
    apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!
);

// Register plugins as services
builder.Services.AddSingleton<WeatherPlugin>();
builder.Services.AddSingleton<CalendarPlugin>();

var kernel = builder.Build();
```

### 2. Create Typed Plugins
Use strongly-typed plugins for maintainability and testability.

```csharp
using Microsoft.SemanticKernel;
using System.ComponentModel;

public class OrderPlugin
{
    private readonly IOrderRepository _repository;

    public OrderPlugin(IOrderRepository repository)
    {
        _repository = repository;
    }

    [KernelFunction, Description("Get order details by order ID")]
    public async Task<OrderDetails> GetOrderAsync(
        [Description("The order ID")] string orderId)
    {
        return await _repository.GetOrderAsync(orderId);
    }

    [KernelFunction, Description("Create a new order")]
    public async Task<Order> CreateOrderAsync(
        [Description("Customer ID")] string customerId,
        [Description("List of product IDs")] List<string> productIds)
    {
        return await _repository.CreateOrderAsync(customerId, productIds);
    }
}
```

### 3. Use Prompt Templates
Leverage the Handlebars template engine for complex prompts.

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.PromptTemplates.Handlebars;

var templateFactory = new HandlebarsPromptTemplateFactory();

var template = """
    <message role="system">
    You are a helpful assistant specializing in {{specialty}}.
    </message>

    <message role="user">
    {{#each context}}
    Previous context: {{this}}
    {{/each}}

    Current question: {{question}}
    </message>
    """;

var function = kernel.CreateFunctionFromPrompt(
    new PromptTemplateConfig
    {
        Template = template,
        TemplateFormat = "handlebars"
    },
    templateFactory
);

var result = await kernel.InvokeAsync(function, new()
{
    ["specialty"] = "customer support",
    ["context"] = new[] { "User is premium member", "Previous order was delayed" },
    ["question"] = "Where is my order?"
});
```

### 4. Implement Filters for Cross-Cutting Concerns
Use filters for logging, validation, and security.

```csharp
using Microsoft.SemanticKernel;

public class AuditFilter : IFunctionInvocationFilter
{
    private readonly ILogger<AuditFilter> _logger;

    public AuditFilter(ILogger<AuditFilter> logger)
    {
        _logger = logger;
    }

    public async Task OnFunctionInvocationAsync(
        FunctionInvocationContext context,
        Func<FunctionInvocationContext, Task> next)
    {
        _logger.LogInformation(
            "Function {Name} invoked with {Arguments}",
            context.Function.Name,
            context.Arguments);

        var startTime = DateTime.UtcNow;
        await next(context);
        var duration = DateTime.UtcNow - startTime;

        _logger.LogInformation(
            "Function {Name} completed in {Duration}ms",
            context.Function.Name,
            duration.TotalMilliseconds);
    }
}

// Register filter
builder.Services.AddSingleton<IFunctionInvocationFilter, AuditFilter>();
```

### 5. Use Memory for RAG
Implement semantic memory for document retrieval.

```csharp
using Microsoft.SemanticKernel.Connectors.AzureAISearch;
using Microsoft.SemanticKernel.Memory;

var memoryBuilder = new MemoryBuilder();

memoryBuilder.WithAzureOpenAITextEmbeddingGeneration(
    deploymentName: "text-embedding-3-small",
    endpoint: Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!,
    apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!
);

memoryBuilder.WithAzureAISearchMemoryStore(
    endpoint: Environment.GetEnvironmentVariable("AZURE_SEARCH_ENDPOINT")!,
    apiKey: Environment.GetEnvironmentVariable("AZURE_SEARCH_KEY")!
);

var memory = memoryBuilder.Build();

// Store documents
await memory.SaveInformationAsync(
    collection: "documents",
    text: "Important company policy about refunds...",
    id: "policy-refunds"
);

// Retrieve relevant documents
var results = await memory.SearchAsync(
    collection: "documents",
    query: "What is the refund policy?",
    limit: 5
).ToListAsync();
```

### 6. Use Auto Function Calling
Let the model decide which functions to call.

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

// Import plugins
kernel.ImportPluginFromType<OrderPlugin>();
kernel.ImportPluginFromType<CustomerPlugin>();

// Enable auto function calling
var settings = new OpenAIPromptExecutionSettings
{
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
};

var result = await kernel.InvokePromptAsync(
    "Check the status of order #12345 and get the customer details",
    new(settings)
);
```

### 7. Implement Retry and Resilience
Use Polly for production resilience.

```csharp
using Polly;
using Polly.Retry;

builder.Services.AddResiliencePipeline("llm-pipeline", builder =>
{
    builder
        .AddRetry(new RetryStrategyOptions
        {
            MaxRetryAttempts = 3,
            Delay = TimeSpan.FromSeconds(2),
            BackoffType = DelayBackoffType.Exponential
        })
        .AddTimeout(TimeSpan.FromMinutes(2));
});
```

---

## Development Approach

### Core Concepts

1. **Kernel**: Central orchestration object
2. **Plugins**: Collections of functions
3. **Functions**: Semantic (prompts) or Native (code)
4. **Memory**: Semantic memory for RAG
5. **Planners**: Task decomposition and planning
6. **Filters**: Cross-cutting concerns

### Project Structure

```
MySemanticKernelApp/
├── src/
│   └── MyApp/
│       ├── Program.cs
│       ├── Plugins/
│       │   ├── OrderPlugin.cs
│       │   ├── CustomerPlugin.cs
│       │   └── SearchPlugin.cs
│       ├── Prompts/
│       │   ├── CustomerService/
│       │   │   ├── config.json
│       │   │   └── skprompt.txt
│       │   └── Summarization/
│       │       ├── config.json
│       │       └── skprompt.txt
│       ├── Filters/
│       │   ├── AuditFilter.cs
│       │   └── SecurityFilter.cs
│       ├── Memory/
│       │   └── MemoryConfiguration.cs
│       └── Services/
│           └── AgentService.cs
├── tests/
│   └── MyApp.Tests/
├── appsettings.json
└── MyApp.csproj
```

### Example: Customer Service Agent

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

// Build kernel with services
var builder = Kernel.CreateBuilder();

builder.AddAzureOpenAIChatCompletion(
    deploymentName: "gpt-4o",
    endpoint: Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!,
    apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!
);

// Add plugins
builder.Plugins.AddFromType<OrderPlugin>();
builder.Plugins.AddFromType<CustomerPlugin>();
builder.Plugins.AddFromType<RefundPlugin>();

var kernel = builder.Build();

// Create chat service
var chatService = kernel.GetRequiredService<IChatCompletionService>();
var history = new ChatHistory();

history.AddSystemMessage("""
    You are a helpful customer service agent for TechCorp.
    You can help customers with:
    - Order status inquiries
    - Refund requests
    - Product information

    Always be polite and professional.
    Use the available tools to look up accurate information.
    """);

// Chat loop
var settings = new OpenAIPromptExecutionSettings
{
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
};

while (true)
{
    Console.Write("Customer: ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input)) break;

    history.AddUserMessage(input);

    var response = await chatService.GetChatMessageContentAsync(
        history,
        settings,
        kernel
    );

    history.AddAssistantMessage(response.Content!);
    Console.WriteLine($"Agent: {response.Content}");
}
```

### Example: Python Integration

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.core_plugins import TextPlugin

# Create kernel
kernel = sk.Kernel()

# Add Azure OpenAI service
kernel.add_service(
    AzureChatCompletion(
        deployment_name="gpt-4o",
        endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_KEY"]
    )
)

# Add plugins
kernel.add_plugin(TextPlugin(), "text")

# Define custom plugin
class CustomerPlugin:
    @sk.kernel_function(
        name="get_customer",
        description="Get customer information by ID"
    )
    async def get_customer(self, customer_id: str) -> str:
        # Implementation
        return f"Customer {customer_id}: John Doe, Premium Member"

kernel.add_plugin(CustomerPlugin(), "customer")

# Create prompt function
prompt = """
Given this customer information: {{customer.get_customer $customer_id}}

Answer the following question: {{$question}}
"""

result = await kernel.invoke_prompt(
    prompt,
    customer_id="12345",
    question="What is their membership status?"
)
print(result)
```

---

## Tradeoffs

### Advantages

| Advantage | Description |
|-----------|-------------|
| **Enterprise .NET** | First-class C# support, familiar patterns |
| **Azure Native** | Deep Azure service integration |
| **Strong Typing** | Type safety, IntelliSense, refactoring |
| **Dependency Injection** | Standard .NET DI patterns |
| **Multi-Language** | C#, Python, Java support |
| **Microsoft Support** | Enterprise support options |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| **Learning Curve** | Many concepts to learn |
| **Azure Preference** | Best experience on Azure |
| **Less Ecosystem** | Fewer integrations than LangChain |
| **Verbose** | More code than Python alternatives |
| **Documentation Gaps** | Advanced patterns less covered |
| **Java/Python Secondary** | C# is the primary focus |

---

## Scalability

### Production Readiness

| Aspect | Status | Notes |
|--------|--------|-------|
| **Async Execution** | Excellent | Native async/await |
| **Streaming** | Excellent | IAsyncEnumerable support |
| **Dependency Injection** | Excellent | .NET DI integration |
| **Error Handling** | Excellent | .NET exception patterns |
| **Observability** | Excellent | OpenTelemetry support |
| **Caching** | Good | Through Azure services |

### Enterprise Deployment

```csharp
// appsettings.json for production
{
  "SemanticKernel": {
    "AzureOpenAI": {
      "DeploymentName": "gpt-4o",
      "Endpoint": "https://your-resource.openai.azure.com/",
      "ApiKey": "${AZURE_OPENAI_KEY}"
    },
    "AzureAISearch": {
      "Endpoint": "https://your-search.search.windows.net",
      "ApiKey": "${AZURE_SEARCH_KEY}"
    }
  },
  "ApplicationInsights": {
    "ConnectionString": "${APPINSIGHTS_CONNECTION}"
  }
}
```

### Recommended Architecture

```
┌─────────────────────────────────────────────┐
│           Azure API Management              │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼───────────────────┐
│          Azure App Service            │
│     (ASP.NET Core + Semantic Kernel)  │
└───────────────────┬───────────────────┘
                    │
     ┌──────────────┴──────────────┐
     │                             │
┌────▼────┐                  ┌────▼────┐
│ Azure   │                  │  Azure  │
│ OpenAI  │                  │   AI    │
│ Service │                  │ Search  │
└─────────┘                  └─────────┘
                    │
         ┌──────────▼──────────┐
         │ Application Insights│
         │   (Observability)   │
         └─────────────────────┘
```

---

## Enterprise Adoption

### Notable Users

- **Microsoft Internal**: Microsoft 365, Dynamics
- **Enterprise Customers**: Financial services, healthcare
- **Government**: Public sector applications

### Case Studies

**Enterprise Document Search**
- RAG over 5M+ documents
- Azure AI Search integration
- 99.9% uptime SLA

**Customer Service Platform**
- Multi-channel support automation
- Integration with Dynamics 365
- 40% cost reduction

### Maturity Assessment

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Documentation** | 4 | Microsoft Learn integration |
| **Community** | 4 | Active GitHub, Microsoft community |
| **Enterprise Support** | 5 | Full Microsoft support |
| **Security** | 5 | Azure security infrastructure |
| **Compliance** | 5 | Azure compliance certifications |
| **Long-term Viability** | 5 | Core Microsoft AI platform |

---

## When to Choose Semantic Kernel

### Ideal Use Cases

- .NET/C# enterprise applications
- Azure-first organizations
- Integration with Microsoft 365/Dynamics
- Enterprise compliance requirements
- Teams with .NET expertise
- Multi-language enterprise (C#, Python, Java)

### Avoid When

- Python-only team (use LangChain)
- Need maximum flexibility (use LangChain)
- Non-Azure cloud preference
- Startup/rapid prototyping (use CrewAI)
- Heavy multi-agent needs (use AutoGen)

---

## Sources

- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [Semantic Kernel Blog](https://devblogs.microsoft.com/semantic-kernel/)
- [Azure AI Documentation](https://docs.microsoft.com/azure/ai-services/)
- [Microsoft Learn - AI](https://learn.microsoft.com/en-us/training/browse/?products=azure-openai)

---

*Last updated: January 2026*
