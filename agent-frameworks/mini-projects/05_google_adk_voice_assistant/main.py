"""
Google ADK Voice Assistant
===========================
Pattern: Tool Use + Voice I/O
Framework: Google ADK with LiteLLM integration

A voice-controlled assistant that:
- Records voice from microphone
- Converts speech to text
- Processes with DeepSeek agent
- Responds with text-to-speech

Voice Options:
- FREE: speech_recognition + pyttsx3 (local)
- PAID: Google Cloud Speech APIs
"""

import os
import asyncio
from google.adk.agents import Agent
from google.adk.tools import Tool
from google.adk.runners import Runner

# Optional: Voice libraries (install with pip install speechrecognition pyttsx3)
try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Set up for LiteLLM (used by Google ADK for DeepSeek)
os.environ["DEEPSEEK_API_KEY"] = api_key


# =====================================================
# Voice Tools
# =====================================================

def initialize_speech_engine():
    """Initialize the text-to-speech engine."""
    if not TTS_AVAILABLE:
        return None

    try:
        engine = pyttsx3.init()
        # Adjust speech rate (default is usually 200)
        engine.setProperty('rate', 175)
        return engine
    except:
        return None


def listen_to_microphone():
    """Record audio from microphone and convert to text."""
    if not SPEECH_RECOGNITION_AVAILABLE:
        return None

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... (speak now)")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen for speech
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        print("🔄 Processing speech...")
        # Use Google's free speech recognition
        text = recognizer.recognize_google(audio)
        return text

    except sr.WaitTimeoutError:
        print("⏱️ No speech detected (timeout)")
        return None
    except sr.UnknownValueError:
        print("❓ Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"🔴 Speech recognition error: {e}")
        return None
    except Exception as e:
        print(f"🔴 Microphone error: {e}")
        return None


def speak_text(engine, text):
    """Convert text to speech and play it."""
    if not engine or not text:
        return False

    try:
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"🔴 TTS error: {e}")
        return False


# =====================================================
# Agent Tools (using Google ADK @Tool decorator)
# =====================================================

@Tool
def get_time():
    """Get the current time.

    Returns:
        str: The current time in readable format.
    """
    from datetime import datetime
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}"


@Tool
def get_date():
    """Get the current date.

    Returns:
        str: The current date in readable format.
    """
    from datetime import datetime
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}"


@Tool
def calculate(expression: str):
    """Calculate a mathematical expression.

    Args:
        expression: A math expression like "2 + 2" or "10 * 5"

    Returns:
        str: The result of the calculation.
    """
    import math
    safe_functions = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi,
        "abs": abs,
        "round": round,
    }

    try:
        result = eval(expression, {"__builtins__": {}}, safe_functions)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Sorry, I couldn't calculate that: {e}"


@Tool
def set_reminder(message: str):
    """Set a reminder (simulated - just confirms the reminder).

    Args:
        message: The reminder message.

    Returns:
        str: Confirmation of the reminder.
    """
    return f"I've set a reminder for you: '{message}'"


@Tool
def tell_joke():
    """Tell a random joke.

    Returns:
        str: A joke to brighten your day.
    """
    import random
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because he used up all his cache!",
        "What's a computer's favorite snack? Microchips!",
        "Why do Java developers wear glasses? Because they can't C#!",
        "What do you call a computer that sings? A-Dell!",
    ]
    return random.choice(jokes)


# =====================================================
# Voice Assistant Agent
# =====================================================

def create_voice_agent():
    """Create the voice assistant agent."""
    agent = Agent(
        name="voice_assistant",
        model="litellm/deepseek/deepseek-chat",
        instructions="""You are a friendly voice assistant. You help users with various tasks.

Your capabilities:
- Tell the current time and date
- Perform calculations
- Set reminders
- Tell jokes

Response style:
- Keep responses concise (1-2 sentences) since they will be spoken aloud
- Be friendly and conversational
- Don't use special characters or formatting
- Speak naturally as if talking to a friend

If the user says goodbye, farewell, or exit, respond with a friendly goodbye.""",
        tools=[get_time, get_date, calculate, set_reminder, tell_joke]
    )
    return agent


# =====================================================
# Main Functions
# =====================================================

async def run_voice_session(agent, speech_engine, use_voice):
    """Run an interactive voice session."""
    print("\n" + "-" * 60)
    print("Voice Assistant Ready!")
    print("-" * 60)

    if use_voice:
        print("\n🎤 Voice mode enabled!")
        print("   Say 'type' to switch to typing mode")
        print("   Say 'goodbye' or 'exit' to quit")
    else:
        print("\n⌨️  Text mode (voice libraries not available)")
        print("   Type your questions")
        print("   Type 'voice' to try voice mode")
        print("   Type 'quit' to exit")

    runner = Runner(agent=agent)

    # Initial greeting
    greeting = "Hello! I'm your voice assistant. How can I help you today?"
    print(f"\n🤖 Assistant: {greeting}")
    if use_voice and speech_engine:
        speak_text(speech_engine, greeting)

    while True:
        # Get user input
        if use_voice and SPEECH_RECOGNITION_AVAILABLE:
            print("\n[Press Enter to speak, or type your message]")
            typed = input().strip()

            if typed.lower() == "type":
                use_voice = False
                print("Switched to text mode")
                continue
            elif typed.lower() in ["quit", "exit"]:
                break
            elif typed:
                user_input = typed
            else:
                # Use voice input
                user_input = listen_to_microphone()
                if not user_input:
                    continue
        else:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() == "voice":
                if SPEECH_RECOGNITION_AVAILABLE:
                    use_voice = True
                    print("Switched to voice mode")
                else:
                    print("Voice libraries not installed.")
                    print("Install with: pip install speechrecognition pyttsx3")
                continue

        # Check for exit
        if user_input.lower() in ["quit", "exit", "goodbye", "bye"]:
            farewell = "Goodbye! Have a great day!"
            print(f"\n🤖 Assistant: {farewell}")
            if use_voice and speech_engine:
                speak_text(speech_engine, farewell)
            break

        print(f"\n👤 You: {user_input}")

        try:
            # Run the agent
            result = await runner.run(user_input)

            # Get response
            response = result.output

            # Display and speak response
            print(f"\n🤖 Assistant: {response}")

            if use_voice and speech_engine:
                speak_text(speech_engine, response)

        except Exception as error:
            error_msg = f"Sorry, I encountered an error: {error}"
            print(f"\n🤖 Assistant: {error_msg}")


async def main_async():
    """Async main function."""
    print("=" * 60)
    print("  Voice Assistant (Google ADK + DeepSeek)")
    print("=" * 60)
    print()

    # Check voice capabilities
    print("Checking voice capabilities...")
    voice_available = SPEECH_RECOGNITION_AVAILABLE and TTS_AVAILABLE

    if voice_available:
        print("✅ Speech recognition: Available")
        print("✅ Text-to-speech: Available")
    else:
        if not SPEECH_RECOGNITION_AVAILABLE:
            print("❌ Speech recognition: Not installed")
            print("   Install with: pip install speechrecognition")
        if not TTS_AVAILABLE:
            print("❌ Text-to-speech: Not installed")
            print("   Install with: pip install pyttsx3")

    print()
    print("Voice Assistant Capabilities:")
    print("  - Tell time and date")
    print("  - Perform calculations")
    print("  - Set reminders")
    print("  - Tell jokes")
    print()

    # Initialize speech engine
    speech_engine = None
    if TTS_AVAILABLE:
        speech_engine = initialize_speech_engine()

    # Create agent
    agent = create_voice_agent()

    # Ask about voice mode
    use_voice = False
    if voice_available:
        choice = input("Enable voice mode? (y/n): ").strip().lower()
        use_voice = choice in ["y", "yes"]

    # Run session
    await run_voice_session(agent, speech_engine, use_voice)


def main():
    """Main entry point."""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\nSession ended.")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Install google-adk: pip install google-adk")
        print("2. Install litellm: pip install litellm")
        print("3. For voice: pip install speechrecognition pyttsx3")


if __name__ == "__main__":
    main()
