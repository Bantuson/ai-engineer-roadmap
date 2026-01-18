"""
CrewAI Story Writing Crew
==========================
Pattern: Multi-Agent Collaboration
Framework: CrewAI with YAML configuration

Three agents collaborate to write a story:
1. Plotter - Creates the story outline
2. Writer - Writes the prose
3. Editor - Polishes the final story
"""

import os
import yaml
from crewai import Agent, Task, Crew, LLM

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))


def load_yaml_config(filename):
    """Load a YAML configuration file."""
    filepath = os.path.join(script_dir, filename)
    with open(filepath, "r") as file:
        return yaml.safe_load(file)


def create_llm():
    """Create the DeepSeek LLM instance for CrewAI."""
    return LLM(
        model="deepseek/deepseek-chat",
        base_url="https://api.deepseek.com",
        api_key=api_key
    )


def create_agents(agents_config, llm):
    """Create agent instances from YAML configuration."""
    agents = {}

    for agent_name, config in agents_config.items():
        agent = Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            verbose=config.get("verbose", True),
            allow_delegation=config.get("allow_delegation", False),
            llm=llm
        )
        agents[agent_name] = agent

    return agents


def create_tasks(tasks_config, agents, story_premise):
    """Create task instances from YAML configuration."""
    tasks = []
    task_objects = {}

    for task_name, config in tasks_config.items():
        # Get the agent for this task
        agent_name = config["agent"]
        agent = agents[agent_name]

        # Format description with variables
        description = config["description"]
        description = description.replace("{story_premise}", story_premise)

        # Handle context (dependencies on other tasks)
        context = []
        if "context" in config:
            for ctx_name in config["context"]:
                if ctx_name in task_objects:
                    context.append(task_objects[ctx_name])

        # Create the task
        task = Task(
            description=description,
            expected_output=config["expected_output"],
            agent=agent,
            context=context if context else None
        )

        tasks.append(task)
        task_objects[task_name] = task

    return tasks


def run_story_crew(story_premise):
    """Run the story writing crew with the given premise."""
    print("\n" + "=" * 60)
    print("  STORY WRITING CREW")
    print("=" * 60)
    print(f"\nPremise: {story_premise}")
    print("\n" + "-" * 60)
    print("Starting the crew... This may take a few minutes.")
    print("-" * 60 + "\n")

    # Create LLM
    llm = create_llm()

    # Load configurations
    agents_config = load_yaml_config("agents.yaml")
    tasks_config = load_yaml_config("tasks.yaml")

    # Create agents and tasks
    agents = create_agents(agents_config, llm)
    tasks = create_tasks(tasks_config, agents, story_premise)

    # Create and run the crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    return result


def get_story_premise():
    """Get a story premise from the user."""
    print("Enter a story premise or idea.")
    print("Examples:")
    print("  - A lonely robot discovers emotions on a distant planet")
    print("  - A baker finds a mysterious recipe that grants wishes")
    print("  - A detective must solve a crime they committed")
    print()

    premise = input("Your premise: ").strip()

    if not premise:
        premise = "A time traveler accidentally changes history and must fix it before they disappear"
        print(f"\nUsing default premise: {premise}")

    return premise


def main():
    """Main function to run the story writing crew."""
    print("=" * 60)
    print("  CrewAI Story Writing Crew (DeepSeek)")
    print("=" * 60)
    print()
    print("This crew of AI agents will collaborate to write a story:")
    print("  1. Plotter - Creates the story outline")
    print("  2. Writer - Writes the prose")
    print("  3. Editor - Polishes the final story")
    print()
    print("-" * 60)

    # Get premise from user
    story_premise = get_story_premise()

    try:
        # Run the crew
        result = run_story_crew(story_premise)

        # Display the final result
        print("\n" + "=" * 60)
        print("  FINAL STORY")
        print("=" * 60)
        print()
        print(result)
        print()
        print("=" * 60)
        print("  Story complete!")
        print("=" * 60)

    except Exception as error:
        print(f"\nError: {error}")
        print("\nTroubleshooting:")
        print("  1. Check your DEEPSEEK_API_KEY is correct")
        print("  2. Ensure you have crewai installed: pip install crewai")
        print("  3. Make sure agents.yaml and tasks.yaml are in the same directory")


if __name__ == "__main__":
    main()
