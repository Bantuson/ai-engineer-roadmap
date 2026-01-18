"""
LlamaIndex Study Buddy
=======================
Pattern: RAG (Retrieval Augmented Generation)
Framework: LlamaIndex with SimpleDirectoryReader and VectorStoreIndex

A study assistant that:
- Loads text files (study notes)
- Answers questions about the content
- Explains concepts in simple terms
"""

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
notes_dir = os.path.join(script_dir, "notes")


def setup_llm():
    """Configure DeepSeek as the LLM for LlamaIndex."""
    # Configure DeepSeek via OpenAI-compatible API
    llm = OpenAI(
        model="deepseek-chat",
        api_base="https://api.deepseek.com",
        api_key=api_key,
        temperature=0.3
    )

    # For embeddings, we'll use a simple approach
    # Note: DeepSeek doesn't provide embeddings, so we use a basic splitter
    Settings.llm = llm
    Settings.embed_model = "local"  # Use local embeddings
    Settings.chunk_size = 512
    Settings.chunk_overlap = 50

    return llm


def create_sample_notes():
    """Create sample study notes if they don't exist."""
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    sample_file = os.path.join(notes_dir, "python_basics.txt")

    if not os.path.exists(sample_file):
        sample_content = """# Python Programming Basics

## Variables and Data Types

Python has several basic data types:

1. Integers (int): Whole numbers like 1, 42, -7
   - Example: age = 25
   - You can do math: result = 10 + 5

2. Floats: Decimal numbers like 3.14, -0.5
   - Example: price = 19.99
   - Be careful with precision: 0.1 + 0.2 might not equal 0.3 exactly

3. Strings (str): Text enclosed in quotes
   - Example: name = "Alice"
   - Can use single or double quotes
   - Concatenation: "Hello " + "World" gives "Hello World"

4. Booleans (bool): True or False values
   - Example: is_student = True
   - Used in conditions and comparisons

## Control Flow

### If Statements
If statements let you run code conditionally:

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm")
else:
    print("It's cool")

### For Loops
For loops iterate over sequences:

for number in range(5):
    print(number)  # Prints 0, 1, 2, 3, 4

for letter in "hello":
    print(letter)  # Prints each letter

### While Loops
While loops run until a condition is false:

count = 0
while count < 5:
    print(count)
    count = count + 1

## Functions

Functions are reusable blocks of code:

def greet(name):
    message = "Hello, " + name + "!"
    return message

result = greet("Bob")
print(result)  # Prints: Hello, Bob!

Functions can have multiple parameters:

def add_numbers(a, b):
    return a + b

sum = add_numbers(5, 3)  # sum is 8

## Lists

Lists store multiple items:

fruits = ["apple", "banana", "cherry"]

Accessing items (index starts at 0):
first_fruit = fruits[0]  # "apple"
last_fruit = fruits[-1]  # "cherry"

Adding items:
fruits.append("orange")

List length:
count = len(fruits)  # 4

## Dictionaries

Dictionaries store key-value pairs:

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

Accessing values:
name = student["name"]  # "Alice"

Adding or updating:
student["email"] = "alice@example.com"

## Common Mistakes to Avoid

1. Indentation errors - Python uses indentation for code blocks
2. Forgetting colons after if, for, while, def
3. Using = instead of == for comparison
4. Index out of range - remember lists start at 0
5. Modifying a list while iterating over it
"""
        with open(sample_file, "w") as f:
            f.write(sample_content)

        print(f"Created sample notes: {sample_file}")
        return True

    return False


def load_documents():
    """Load documents from the notes directory."""
    if not os.path.exists(notes_dir):
        create_sample_notes()

    # Check if directory has files
    files = os.listdir(notes_dir)
    text_files = []
    for f in files:
        if f.endswith(".txt") or f.endswith(".md"):
            text_files.append(f)

    if not text_files:
        create_sample_notes()

    print(f"\nLoading notes from: {notes_dir}")

    # Load all documents
    reader = SimpleDirectoryReader(notes_dir)
    documents = reader.load_data()

    print(f"Loaded {len(documents)} document(s)")

    return documents


def create_index(documents):
    """Create a vector store index from documents."""
    print("Creating search index...")

    # Create index
    index = VectorStoreIndex.from_documents(
        documents,
        show_progress=True
    )

    print("Index created successfully!")

    return index


def create_query_engine(index):
    """Create a query engine with custom prompt."""
    # Custom prompt for the study buddy
    system_prompt = """You are a helpful study buddy assistant.
Your job is to help students understand their study materials.

When answering questions:
1. Use the context provided from the study notes
2. Explain concepts in simple, easy-to-understand terms
3. Give examples when helpful
4. If something isn't in the notes, say so but try to help anyway
5. Encourage the student and be supportive

Context from study notes:
{context_str}

Question: {query_str}
"""

    query_engine = index.as_query_engine(
        similarity_top_k=3,
        response_mode="compact"
    )

    return query_engine


def main():
    """Main function to run the study buddy."""
    print("=" * 60)
    print("  Study Buddy (LlamaIndex + DeepSeek)")
    print("=" * 60)
    print()
    print("I'll help you study by answering questions about your notes!")
    print()

    # Setup LLM
    print("Setting up AI...")
    setup_llm()

    # Load documents
    documents = load_documents()

    # Create index
    index = create_index(documents)

    # Create query engine
    query_engine = create_query_engine(index)

    print()
    print("-" * 60)
    print("Ready! Ask me anything about your study notes.")
    print("Commands:")
    print("  'topics' - See what topics are covered")
    print("  'quiz' - Get a practice question")
    print("  'quit' - Exit the program")
    print("-" * 60)

    while True:
        print()
        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() in ["quit", "exit", "q"]:
            print("\nGood luck with your studies! Goodbye!")
            break

        if question.lower() == "topics":
            print("\nLet me check what topics are covered...")
            response = query_engine.query(
                "What are all the main topics and subtopics covered in these notes? List them clearly."
            )
            print(f"\nStudy Buddy: {response}")
            continue

        if question.lower() == "quiz":
            print("\nGenerating a practice question...")
            response = query_engine.query(
                "Generate one practice question based on the study notes. Make it a good test of understanding, not just memorization. Format: Question, then wait for answer."
            )
            print(f"\nStudy Buddy: {response}")
            continue

        # Regular question
        try:
            response = query_engine.query(question)
            print(f"\nStudy Buddy: {response}")
        except Exception as error:
            print(f"\nError: {error}")
            print("Try rephrasing your question.")


if __name__ == "__main__":
    main()
