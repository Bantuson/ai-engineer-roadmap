"""
OpenAI Agents SDK IT Helpdesk
==============================
Pattern: Handoff Pattern (Agent-to-Agent Routing)
Framework: OpenAI Agents SDK with Agent and handoff

IT support system with specialized agents:
1. Triage Agent - Categorizes issues and routes to specialists
2. Password Agent - Handles password reset requests
3. Software Agent - Handles software installation questions
"""

import os
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, handoff, RunContextWrapper

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Create DeepSeek client via OpenAI-compatible API
client = AsyncOpenAI(
    base_url="https://api.deepseek.com",
    api_key=api_key
)


# =====================================================
# Specialist Agents
# =====================================================

# Password Reset Agent
password_agent = Agent(
    name="Password Specialist",
    instructions="""You are a password reset specialist for IT support.

Your responsibilities:
1. Guide users through password reset procedures
2. Explain security requirements for new passwords
3. Help with account lockout issues

Password Reset Steps:
1. Verify the user knows their username
2. Ask them to go to the password reset portal
3. They'll receive a reset link via email
4. New password must be 8+ characters with letters and numbers

Security reminders:
- Never share passwords
- Don't reuse old passwords
- Enable two-factor authentication

Be helpful and patient. If the issue isn't about passwords, let the user
know they should describe their issue again for proper routing.""",
    model="deepseek-chat"
)

# Software Support Agent
software_agent = Agent(
    name="Software Specialist",
    instructions="""You are a software installation and troubleshooting specialist.

Your responsibilities:
1. Help with software installation questions
2. Troubleshoot common software issues
3. Explain how to request new software

Common software we support:
- Microsoft Office (Word, Excel, PowerPoint)
- Web browsers (Chrome, Firefox, Edge)
- Video conferencing (Zoom, Teams)
- Development tools (VS Code, Python)

For installation issues:
1. Check if the software is in the company software center
2. Verify system requirements are met
3. Try restarting the application
4. Clear cache/temp files if needed

For new software requests:
- Submit a ticket to IT with the software name and business justification
- Approval usually takes 2-3 business days

Be helpful and provide step-by-step guidance.""",
    model="deepseek-chat"
)


# =====================================================
# Triage Agent (Main Router)
# =====================================================

# Define handoff functions
def handoff_to_password_agent():
    """Transfer to password specialist for password-related issues."""
    return handoff(password_agent)


def handoff_to_software_agent():
    """Transfer to software specialist for software-related issues."""
    return handoff(software_agent)


# Triage Agent
triage_agent = Agent(
    name="IT Helpdesk Triage",
    instructions="""You are the IT Helpdesk triage agent. Your job is to:
1. Greet the user professionally
2. Understand their IT issue
3. Route them to the appropriate specialist

Routing rules:
- Password issues (reset, forgot, locked out) → Use handoff_to_password_agent
- Software issues (install, update, crash, error) → Use handoff_to_software_agent
- For other issues, help if you can or explain you'll create a ticket

Always be professional and helpful. Ask clarifying questions if the
issue isn't clear. Start by asking how you can help today.""",
    model="deepseek-chat",
    tools=[handoff_to_password_agent, handoff_to_software_agent]
)


# =====================================================
# Main Functions
# =====================================================

async def run_helpdesk_session():
    """Run an interactive helpdesk session."""
    print("\n" + "-" * 60)
    print("Connected to IT Helpdesk")
    print("-" * 60)

    # Create runner with triage agent
    runner = Runner(
        agent=triage_agent,
        client=client
    )

    # Conversation history
    messages = []

    # Initial greeting
    print("\nIT Helpdesk: Hello! Welcome to IT Support. How can I help you today?")
    print()

    while True:
        # Get user input
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            print("\nIT Helpdesk: Thank you for contacting IT Support. Have a great day!")
            break

        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Run the agent
            result = await runner.run(messages)

            # Get the response
            response = result.final_output

            # Print the response
            print(f"\nIT Helpdesk: {response}")
            print()

            # Add assistant response to history
            messages.append({
                "role": "assistant",
                "content": response
            })

            # Check if there was a handoff
            if result.last_agent.name != "IT Helpdesk Triage":
                print(f"[Transferred to: {result.last_agent.name}]")
                print()

        except Exception as error:
            print(f"\nError: {error}")
            print("Please try again or type 'quit' to exit.")


async def main_async():
    """Async main function."""
    print("=" * 60)
    print("  IT Helpdesk (OpenAI Agents SDK + DeepSeek)")
    print("=" * 60)
    print()
    print("Welcome to the IT Helpdesk Demo!")
    print()
    print("This system demonstrates the agent handoff pattern:")
    print("  - Triage Agent: Routes your issue to specialists")
    print("  - Password Specialist: Handles password resets")
    print("  - Software Specialist: Handles software issues")
    print()
    print("Try asking about:")
    print("  - Resetting your password")
    print("  - Installing Microsoft Office")
    print("  - Fixing a software crash")
    print()
    print("Type 'quit' to exit.")
    print("=" * 60)

    await run_helpdesk_session()


def main():
    """Main entry point."""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\nSession ended.")


if __name__ == "__main__":
    main()
