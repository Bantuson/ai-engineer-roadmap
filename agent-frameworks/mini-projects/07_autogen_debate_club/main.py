"""
AutoGen Debate Club
====================
Pattern: Multi-Agent Conversation
Framework: AutoGen with AssistantAgent and GroupChat

Three agents debate a topic:
1. Pro Agent - Argues FOR the topic
2. Con Agent - Argues AGAINST the topic
3. Moderator - Guides discussion and declares winner
"""

import os
from autogen import AssistantAgent, GroupChat, GroupChatManager

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# DeepSeek configuration for AutoGen
llm_config = {
    "config_list": [
        {
            "model": "deepseek-chat",
            "base_url": "https://api.deepseek.com",
            "api_key": api_key,
        }
    ],
    "temperature": 0.7,
}


def create_agents(topic):
    """Create the debate agents with the given topic."""

    # Pro Agent - Argues FOR the topic
    pro_agent = AssistantAgent(
        name="Pro_Debater",
        system_message=f"""You are a skilled debater arguing IN FAVOR of: "{topic}"

Your role:
- Present compelling arguments supporting this position
- Use logic, evidence, and persuasive rhetoric
- Respond to the opposing side's points with counterarguments
- Stay respectful but assertive

Rules:
- Keep each response to 2-3 paragraphs maximum
- Start your first response with your opening argument
- Address the Con_Debater's points directly when responding
- Never switch sides or agree with the opposition

Remember: You MUST argue FOR this position, even if you personally disagree.""",
        llm_config=llm_config,
    )

    # Con Agent - Argues AGAINST the topic
    con_agent = AssistantAgent(
        name="Con_Debater",
        system_message=f"""You are a skilled debater arguing AGAINST: "{topic}"

Your role:
- Present compelling arguments opposing this position
- Use logic, evidence, and persuasive rhetoric
- Respond to the supporting side's points with counterarguments
- Stay respectful but assertive

Rules:
- Keep each response to 2-3 paragraphs maximum
- Start your first response with your opening argument
- Address the Pro_Debater's points directly when responding
- Never switch sides or agree with the opposition

Remember: You MUST argue AGAINST this position, even if you personally agree.""",
        llm_config=llm_config,
    )

    # Moderator - Guides the debate
    moderator = AssistantAgent(
        name="Moderator",
        system_message=f"""You are the moderator for a debate on: "{topic}"

Your role:
- Keep the debate focused and civil
- After 2-3 exchanges, summarize key points from both sides
- Declare a winner based on argument quality, not personal opinion

Structure:
1. First, let Pro_Debater make their opening argument
2. Then let Con_Debater respond
3. Allow 2 more exchanges
4. Finally, summarize and declare a winner

When declaring a winner:
- Evaluate argument strength, evidence, and rebuttals
- Be fair and explain your reasoning
- End with "DEBATE CONCLUDED" when finished

Keep the debate moving and ensure both sides get equal time.""",
        llm_config=llm_config,
    )

    return pro_agent, con_agent, moderator


def run_debate(topic, max_rounds):
    """Run a debate on the given topic."""
    print("\n" + "=" * 60)
    print("  DEBATE CLUB")
    print("=" * 60)
    print(f"\nTopic: {topic}")
    print(f"Rounds: {max_rounds}")
    print("\n" + "-" * 60)
    print("The debate is about to begin...")
    print("-" * 60 + "\n")

    # Create agents
    pro_agent, con_agent, moderator = create_agents(topic)

    # Create group chat
    group_chat = GroupChat(
        agents=[moderator, pro_agent, con_agent],
        messages=[],
        max_round=max_rounds,
        speaker_selection_method="round_robin"
    )

    # Create manager
    manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=llm_config
    )

    # Start the debate
    opening_message = f"""Welcome to today's debate!

Topic: "{topic}"

We have two debaters today:
- Pro_Debater will argue IN FAVOR
- Con_Debater will argue AGAINST

Let's begin. Pro_Debater, please make your opening argument."""

    # Initiate chat
    moderator.initiate_chat(
        manager,
        message=opening_message
    )

    print("\n" + "=" * 60)
    print("  DEBATE ENDED")
    print("=" * 60)


def get_debate_topic():
    """Get a debate topic from the user."""
    print("\nEnter a debate topic (a statement that can be argued for or against):")
    print()
    print("Examples:")
    print("  - Remote work is better than office work")
    print("  - Social media does more harm than good")
    print("  - AI will create more jobs than it destroys")
    print("  - Homework should be banned in schools")
    print("  - Electric cars should replace all gas cars by 2030")
    print()

    topic = input("Your topic: ").strip()

    if not topic:
        topic = "Artificial intelligence will benefit humanity more than harm it"
        print(f"\nUsing default topic: {topic}")

    return topic


def get_max_rounds():
    """Get the number of debate rounds."""
    print("\nHow many exchanges? (3-10, default is 6)")
    rounds_input = input("Rounds: ").strip()

    try:
        rounds = int(rounds_input)
        if rounds < 3:
            rounds = 3
        if rounds > 10:
            rounds = 10
    except:
        rounds = 6

    return rounds


def main():
    """Main function to run the debate club."""
    print("=" * 60)
    print("  AutoGen Debate Club (DeepSeek)")
    print("=" * 60)
    print()
    print("Welcome to the AI Debate Club!")
    print("Watch two AI agents debate any topic you choose.")
    print()
    print("Agents:")
    print("  - Pro_Debater: Argues FOR the topic")
    print("  - Con_Debater: Argues AGAINST the topic")
    print("  - Moderator: Keeps order and declares winner")
    print()
    print("-" * 60)

    while True:
        # Get topic
        topic = get_debate_topic()

        # Get rounds
        max_rounds = get_max_rounds()

        try:
            # Run the debate
            run_debate(topic, max_rounds)

        except Exception as error:
            print(f"\nError during debate: {error}")
            print("\nTroubleshooting:")
            print("  1. Check your DEEPSEEK_API_KEY")
            print("  2. Ensure pyautogen is installed: pip install pyautogen")

        # Ask to continue
        print()
        again = input("Start another debate? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break

    print("\nThanks for visiting the Debate Club!")


if __name__ == "__main__":
    main()
