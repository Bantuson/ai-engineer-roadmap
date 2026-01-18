"""
Semantic Kernel Daily Planner
==============================
Pattern: Planning with Plugins
Framework: Semantic Kernel with Kernel + Plugins + Functions

A daily planner that:
- Takes user's tasks for the day
- Prioritizes and schedules them
- Suggests time blocks
- Provides productivity tips
"""

import os
import asyncio
from datetime import datetime, timedelta
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions import kernel_function
from openai import AsyncOpenAI

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)


# =====================================================
# Plugin: Task Manager
# =====================================================

class TaskManagerPlugin:
    """Plugin for managing and organizing tasks."""

    def __init__(self):
        self.tasks = []
        self.schedule = []

    @kernel_function(
        name="add_task",
        description="Add a new task to the list with estimated duration and priority"
    )
    def add_task(
        self,
        task_name: str,
        duration_minutes: int = 30,
        priority: str = "medium"
    ) -> str:
        """Add a task to the task list.

        Args:
            task_name: Name of the task
            duration_minutes: Estimated duration in minutes
            priority: Priority level (high, medium, low)
        """
        task = {
            "name": task_name,
            "duration": duration_minutes,
            "priority": priority.lower(),
            "completed": False
        }
        self.tasks.append(task)
        return f"Added task: '{task_name}' ({duration_minutes} min, {priority} priority)"

    @kernel_function(
        name="list_tasks",
        description="List all current tasks"
    )
    def list_tasks(self) -> str:
        """List all tasks in the current list."""
        if not self.tasks:
            return "No tasks in the list yet."

        result = "Current Tasks:\n"
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            result = result + f"{i+1}. {status} {task['name']} "
            result = result + f"({task['duration']} min, {task['priority']})\n"

        return result

    @kernel_function(
        name="prioritize_tasks",
        description="Sort tasks by priority (high first, then medium, then low)"
    )
    def prioritize_tasks(self) -> str:
        """Sort tasks by priority level."""
        priority_order = {"high": 0, "medium": 1, "low": 2}

        self.tasks.sort(key=lambda t: priority_order.get(t["priority"], 1))

        return "Tasks have been prioritized. " + self.list_tasks()

    @kernel_function(
        name="create_schedule",
        description="Create a time-blocked schedule starting from the given hour"
    )
    def create_schedule(self, start_hour: int = 9) -> str:
        """Create a schedule with time blocks for all tasks.

        Args:
            start_hour: Hour to start the schedule (24-hour format)
        """
        if not self.tasks:
            return "No tasks to schedule. Add some tasks first."

        # Sort by priority first
        priority_order = {"high": 0, "medium": 1, "low": 2}
        sorted_tasks = sorted(
            self.tasks,
            key=lambda t: priority_order.get(t["priority"], 1)
        )

        # Create schedule
        self.schedule = []
        current_time = datetime.now().replace(
            hour=start_hour, minute=0, second=0, microsecond=0
        )

        result = f"\n📅 Daily Schedule (starting at {start_hour}:00)\n"
        result = result + "=" * 45 + "\n"

        for task in sorted_tasks:
            end_time = current_time + timedelta(minutes=task["duration"])

            time_str = current_time.strftime("%H:%M")
            end_str = end_time.strftime("%H:%M")

            schedule_item = {
                "task": task["name"],
                "start": time_str,
                "end": end_str,
                "priority": task["priority"]
            }
            self.schedule.append(schedule_item)

            priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}
            icon = priority_icon.get(task["priority"], "⚪")

            result = result + f"{time_str} - {end_str} | {icon} {task['name']}\n"

            # Add 5 min break between tasks
            current_time = end_time + timedelta(minutes=5)

        # Calculate total time
        total_minutes = sum(t["duration"] for t in sorted_tasks)
        hours = total_minutes // 60
        mins = total_minutes % 60
        result = result + "=" * 45 + "\n"
        result = result + f"Total work time: {hours}h {mins}m\n"

        return result

    @kernel_function(
        name="complete_task",
        description="Mark a task as completed by its number"
    )
    def complete_task(self, task_number: int) -> str:
        """Mark a task as completed.

        Args:
            task_number: The number of the task to complete (1-based)
        """
        index = task_number - 1
        if index < 0 or index >= len(self.tasks):
            return f"Invalid task number. You have {len(self.tasks)} tasks."

        self.tasks[index]["completed"] = True
        task_name = self.tasks[index]["name"]
        return f"✓ Completed: '{task_name}'"

    @kernel_function(
        name="clear_tasks",
        description="Clear all tasks from the list"
    )
    def clear_tasks(self) -> str:
        """Clear all tasks."""
        self.tasks = []
        self.schedule = []
        return "All tasks have been cleared."


# =====================================================
# Plugin: Productivity Tips
# =====================================================

class ProductivityPlugin:
    """Plugin for productivity advice."""

    @kernel_function(
        name="get_productivity_tip",
        description="Get a productivity tip based on the context"
    )
    def get_productivity_tip(self, context: str = "general") -> str:
        """Get a productivity tip.

        Args:
            context: Type of tip needed (focus, energy, breaks, general)
        """
        tips = {
            "focus": [
                "Use the Pomodoro Technique: 25 min work, 5 min break.",
                "Put your phone in another room while working on important tasks.",
                "Block distracting websites during focus time.",
            ],
            "energy": [
                "Schedule your most important tasks during your peak energy hours.",
                "Take a short walk after lunch to boost afternoon energy.",
                "Stay hydrated - dehydration reduces mental performance.",
            ],
            "breaks": [
                "Step away from screens during breaks - look at something far away.",
                "Do some light stretching during breaks to prevent stiffness.",
                "A 10-minute power nap can boost afternoon productivity.",
            ],
            "general": [
                "Start your day with the hardest task (Eat That Frog!).",
                "Break large tasks into smaller, manageable chunks.",
                "Review your accomplishments at the end of each day.",
            ],
        }

        import random
        context_lower = context.lower()
        if context_lower in tips:
            tip = random.choice(tips[context_lower])
        else:
            tip = random.choice(tips["general"])

        return f"💡 Productivity Tip: {tip}"


# =====================================================
# Main Functions
# =====================================================

async def setup_kernel():
    """Set up the Semantic Kernel with plugins."""
    # Create kernel
    kernel = Kernel()

    # Create DeepSeek client
    client = AsyncOpenAI(
        base_url="https://api.deepseek.com",
        api_key=api_key
    )

    # Add chat completion service
    chat_service = OpenAIChatCompletion(
        ai_model_id="deepseek-chat",
        async_client=client,
        service_id="deepseek"
    )
    kernel.add_service(chat_service)

    # Add plugins
    task_plugin = TaskManagerPlugin()
    productivity_plugin = ProductivityPlugin()

    kernel.add_plugin(task_plugin, "task_manager")
    kernel.add_plugin(productivity_plugin, "productivity")

    return kernel, task_plugin


async def run_planner_session(kernel, task_plugin):
    """Run an interactive planner session."""
    print("\n" + "-" * 60)
    print("Daily Planner Ready!")
    print("-" * 60)

    # Get the chat service
    chat_service = kernel.get_service("deepseek")

    # Chat history
    history = ChatHistory()
    history.add_system_message("""You are a helpful daily planner assistant.

Your job is to help users:
1. Add and manage their tasks for the day
2. Create a prioritized schedule
3. Provide productivity tips

Available tools:
- add_task: Add a new task with duration and priority
- list_tasks: Show all current tasks
- prioritize_tasks: Sort tasks by priority
- create_schedule: Generate a time-blocked schedule
- complete_task: Mark a task as done
- clear_tasks: Clear all tasks
- get_productivity_tip: Get a productivity tip

Always use the appropriate tools. Be encouraging and helpful.
When users describe tasks, extract the task name, estimate duration, and determine priority.

Response format:
TIME - TASK - PRIORITY

Be concise but friendly.""")

    print("\nHow can I help you plan your day?")
    print("Commands: 'show' (list tasks), 'schedule', 'tip', 'quit'")

    # Configure function calling
    settings = kernel.get_prompt_execution_settings_from_service_id("deepseek")
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    while True:
        print()
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "q"]:
            print("\nPlanner: Have a productive day! Goodbye!")
            break

        # Shortcuts
        if user_input.lower() == "show":
            print("\n" + task_plugin.list_tasks())
            continue

        if user_input.lower() == "schedule":
            print(task_plugin.create_schedule())
            continue

        if user_input.lower() == "tip":
            productivity = ProductivityPlugin()
            print("\n" + productivity.get_productivity_tip())
            continue

        # Add user message to history
        history.add_user_message(user_input)

        try:
            # Get response from kernel
            result = await chat_service.get_chat_message_content(
                chat_history=history,
                settings=settings,
                kernel=kernel
            )

            response = str(result)
            print(f"\nPlanner: {response}")

            # Add assistant response to history
            history.add_assistant_message(response)

        except Exception as error:
            print(f"\nError: {error}")
            print("Please try again.")


async def main_async():
    """Async main function."""
    print("=" * 60)
    print("  Daily Planner (Semantic Kernel + DeepSeek)")
    print("=" * 60)
    print()
    print("This planner will help you organize your day!")
    print()
    print("Features:")
    print("  - Add tasks with duration and priority")
    print("  - Get a prioritized schedule")
    print("  - Receive productivity tips")
    print()
    print("Example inputs:")
    print('  - "Add a meeting at 10am for 1 hour, high priority"')
    print('  - "I need to write a report, about 2 hours"')
    print('  - "Create my schedule starting at 8am"')
    print()
    print("=" * 60)

    # Setup kernel
    kernel, task_plugin = await setup_kernel()

    # Run session
    await run_planner_session(kernel, task_plugin)


def main():
    """Main entry point."""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\nSession ended.")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Install semantic-kernel: pip install semantic-kernel")
        print("2. Check your DEEPSEEK_API_KEY")


if __name__ == "__main__":
    main()
