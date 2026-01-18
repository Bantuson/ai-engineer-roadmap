"""
LangChain Multi-Language Translator
====================================
Pattern: Chain Composition (LCEL)
Framework: LangChain with pipe operator |

Translates text between multiple languages using:
- Language detection
- Few-shot prompting for quality translations
- LCEL chain composition
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Initialize DeepSeek model via OpenAI-compatible API
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key,
    temperature=0.3  # Lower temperature for consistent translations
)

# Output parser
output_parser = StrOutputParser()

# Supported languages
SUPPORTED_LANGUAGES = [
    "English", "Spanish", "French", "German", "Italian",
    "Portuguese", "Chinese", "Japanese", "Korean", "Russian",
    "Arabic", "Hindi", "Dutch", "Swedish", "Polish"
]

# =====================================================
# Chain 1: Language Detection
# =====================================================

detect_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a language detection expert.
Identify the language of the given text.
Respond with ONLY the language name (e.g., "English", "Spanish", "French").
Do not include any other text or explanation."""),
    ("human", "{text}")
])

# LCEL chain: prompt | model | parser
detect_chain = detect_prompt | model | output_parser


# =====================================================
# Chain 2: Translation with Few-Shot Examples
# =====================================================

# Few-shot examples for high-quality translation
translation_examples = [
    {
        "source": "Hello, how are you today?",
        "source_lang": "English",
        "target_lang": "Spanish",
        "translation": "Hola, ¿cómo estás hoy?"
    },
    {
        "source": "The weather is beautiful this morning.",
        "source_lang": "English",
        "target_lang": "French",
        "translation": "Le temps est magnifique ce matin."
    },
    {
        "source": "Ich liebe Programmierung.",
        "source_lang": "German",
        "target_lang": "English",
        "translation": "I love programming."
    },
]

# Template for each example
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "Translate from {source_lang} to {target_lang}: {source}"),
    ("assistant", "{translation}")
])

# Create few-shot prompt
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=translation_examples,
)

# Main translation prompt with few-shot examples
translate_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional translator.
Translate the text accurately while preserving:
- The original meaning and tone
- Idiomatic expressions (adapt them naturally)
- Proper grammar and punctuation

Respond with ONLY the translated text. No explanations."""),
    few_shot_prompt,
    ("human", "Translate from {source_lang} to {target_lang}: {text}")
])

# LCEL chain for translation
translate_chain = translate_prompt | model | output_parser


# =====================================================
# Chain 3: Format Output
# =====================================================

format_prompt = ChatPromptTemplate.from_messages([
    ("system", """Format the translation result nicely.
Include the original text, detected language, target language, and translation.
Use a clean, readable format."""),
    ("human", """Original ({source_lang}): {original}
Target Language: {target_lang}
Translation: {translation}

Format this nicely for display.""")
])

format_chain = format_prompt | model | output_parser


# =====================================================
# Main Functions
# =====================================================

def detect_language(text):
    """Detect the language of the input text."""
    result = detect_chain.invoke({"text": text})
    return result.strip()


def translate_text(text, source_lang, target_lang):
    """Translate text from source language to target language."""
    result = translate_chain.invoke({
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })
    return result.strip()


def format_result(original, source_lang, target_lang, translation):
    """Format the translation result for display."""
    result = format_chain.invoke({
        "original": original,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "translation": translation
    })
    return result


def show_languages():
    """Display supported languages."""
    print("\nSupported Languages:")
    print("-" * 40)

    # Display in columns
    for i in range(0, len(SUPPORTED_LANGUAGES), 3):
        row = SUPPORTED_LANGUAGES[i:i+3]
        formatted_row = ""
        for lang in row:
            formatted_row = formatted_row + f"  {lang:<15}"
        print(formatted_row)

    print()


def get_target_language():
    """Prompt user to select target language."""
    print("\nEnter target language (or 'list' to see options):")

    while True:
        choice = input("> ").strip()

        if choice.lower() == "list":
            show_languages()
            continue

        # Check if valid language
        for lang in SUPPORTED_LANGUAGES:
            if choice.lower() == lang.lower():
                return lang

        # Accept the input even if not in list (model can handle it)
        if choice:
            return choice

        print("Please enter a language name.")


def main():
    """Main function to run the translator."""
    print("=" * 50)
    print("  Multi-Language Translator (LangChain + DeepSeek)")
    print("=" * 50)
    print()
    print("Enter text to translate. I'll detect the language")
    print("and translate it for you.")
    print()
    print("Commands:")
    print("  'languages' - Show supported languages")
    print("  'quit' - Exit the program")
    print("-" * 50)

    while True:
        print()
        print("Enter text to translate:")
        user_input = input("> ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        if user_input.lower() in ["languages", "langs", "list"]:
            show_languages()
            continue

        try:
            # Step 1: Detect language
            print("\nDetecting language...")
            source_lang = detect_language(user_input)
            print(f"Detected: {source_lang}")

            # Step 2: Get target language
            target_lang = get_target_language()

            if source_lang.lower() == target_lang.lower():
                print(f"\nText is already in {target_lang}!")
                continue

            # Step 3: Translate
            print(f"\nTranslating to {target_lang}...")
            translation = translate_text(user_input, source_lang, target_lang)

            # Step 4: Display result
            print()
            print("=" * 50)
            print(f"Original ({source_lang}):")
            print(f"  {user_input}")
            print()
            print(f"Translation ({target_lang}):")
            print(f"  {translation}")
            print("=" * 50)

        except Exception as error:
            print(f"\nError: {error}")
            print("Please try again.")


if __name__ == "__main__":
    main()
