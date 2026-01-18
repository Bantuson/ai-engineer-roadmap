"""
LangGraph Quiz Master
======================
Pattern: ReAct Loop with State
Framework: LangGraph StateGraph with nodes and edges

An interactive quiz game that:
- Generates questions on a chosen topic
- Checks answers with explanation
- Tracks score and provides feedback
- Uses Chain-of-Thought for evaluation
"""

import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Get API key from environment
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: Please set DEEPSEEK_API_KEY environment variable")
    print("  export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Initialize DeepSeek model
model = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key,
    temperature=0.7
)

output_parser = StrOutputParser()


# =====================================================
# State Definition
# =====================================================

# Using TypedDict for state (framework requirement, not OOP)
class QuizState(TypedDict):
    topic: str
    current_question: str
    correct_answer: str
    user_answer: str
    is_correct: bool
    explanation: str
    score: int
    questions_asked: int
    max_questions: int
    should_continue: bool


# =====================================================
# Node Functions
# =====================================================

def generate_question(state):
    """Generate a new quiz question based on the topic."""
    topic = state["topic"]
    questions_asked = state["questions_asked"]

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a quiz master creating educational questions.
Generate ONE trivia question about the given topic.

Requirements:
- Make the question clear and unambiguous
- It should have a definite correct answer
- Vary difficulty (mix easy and medium questions)
- Don't repeat previous questions in the session

Format your response EXACTLY like this:
QUESTION: [Your question here]
ANSWER: [The correct answer]"""),
        ("human", "Topic: {topic}\nThis is question #{number}. Generate a fresh question.")
    ])

    chain = prompt | model | output_parser
    result = chain.invoke({"topic": topic, "number": questions_asked + 1})

    # Parse the response
    lines = result.strip().split("\n")
    question = ""
    answer = ""

    for line in lines:
        if line.startswith("QUESTION:"):
            question = line.replace("QUESTION:", "").strip()
        if line.startswith("ANSWER:"):
            answer = line.replace("ANSWER:", "").strip()

    # Update state
    new_state = dict(state)
    new_state["current_question"] = question
    new_state["correct_answer"] = answer
    new_state["questions_asked"] = questions_asked + 1

    return new_state


def get_user_answer(state):
    """Get the user's answer (happens outside the graph)."""
    # This node just marks that we need user input
    # The actual input happens in the main loop
    return state


def check_answer(state):
    """Check if the user's answer is correct using CoT reasoning."""
    user_answer = state["user_answer"]
    correct_answer = state["correct_answer"]
    question = state["current_question"]

    # Chain-of-Thought prompt for evaluation
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a fair quiz judge. Evaluate if the user's answer is correct.

Use step-by-step reasoning:
1. Consider the correct answer
2. Consider what the user answered
3. Check if they match (allow minor spelling variations, synonyms)
4. Provide a helpful explanation

Format your response EXACTLY like this:
THINKING: [Your step-by-step reasoning]
CORRECT: [YES or NO]
EXPLANATION: [Brief explanation for the user]"""),
        ("human", """Question: {question}
Correct Answer: {correct_answer}
User's Answer: {user_answer}

Evaluate this answer.""")
    ])

    chain = prompt | model | output_parser
    result = chain.invoke({
        "question": question,
        "correct_answer": correct_answer,
        "user_answer": user_answer
    })

    # Parse response
    is_correct = False
    explanation = ""

    lines = result.strip().split("\n")
    for line in lines:
        if line.startswith("CORRECT:"):
            is_correct = "YES" in line.upper()
        if line.startswith("EXPLANATION:"):
            explanation = line.replace("EXPLANATION:", "").strip()

    # Update state
    new_state = dict(state)
    new_state["is_correct"] = is_correct
    new_state["explanation"] = explanation

    if is_correct:
        new_state["score"] = state["score"] + 1

    return new_state


def give_feedback(state):
    """Provide feedback to the user."""
    is_correct = state["is_correct"]
    explanation = state["explanation"]
    correct_answer = state["correct_answer"]
    score = state["score"]
    questions_asked = state["questions_asked"]

    print()
    if is_correct:
        print("✓ CORRECT!")
    else:
        print("✗ Not quite...")
        print(f"  The correct answer was: {correct_answer}")

    print(f"\n  {explanation}")
    print(f"\n  Score: {score}/{questions_asked}")

    return state


def should_continue(state):
    """Decide whether to continue the quiz or end."""
    questions_asked = state["questions_asked"]
    max_questions = state["max_questions"]

    if questions_asked >= max_questions:
        return "end_quiz"

    # Ask user if they want to continue
    print()
    choice = input("Continue? (y/n): ").strip().lower()

    if choice in ["n", "no", "quit", "q"]:
        return "end_quiz"

    return "next_question"


def end_quiz(state):
    """End the quiz and show final results."""
    score = state["score"]
    total = state["questions_asked"]

    print()
    print("=" * 50)
    print("  QUIZ COMPLETE!")
    print("=" * 50)
    print()
    print(f"  Final Score: {score}/{total}")

    # Calculate percentage
    if total > 0:
        percentage = (score / total) * 100
        print(f"  Percentage: {percentage:.0f}%")

        # Give rating
        if percentage == 100:
            print("\n  Rating: PERFECT! You're a master!")
        elif percentage >= 80:
            print("\n  Rating: Excellent work!")
        elif percentage >= 60:
            print("\n  Rating: Good job!")
        elif percentage >= 40:
            print("\n  Rating: Keep practicing!")
        else:
            print("\n  Rating: Study more and try again!")

    print()

    new_state = dict(state)
    new_state["should_continue"] = False
    return new_state


# =====================================================
# Build the Graph
# =====================================================

def build_quiz_graph():
    """Build the LangGraph state machine for the quiz."""
    # Create the graph
    workflow = StateGraph(QuizState)

    # Add nodes
    workflow.add_node("generate_question", generate_question)
    workflow.add_node("check_answer", check_answer)
    workflow.add_node("give_feedback", give_feedback)
    workflow.add_node("end_quiz", end_quiz)

    # Set the entry point
    workflow.set_entry_point("generate_question")

    # Add edges
    workflow.add_edge("generate_question", "check_answer")
    workflow.add_edge("check_answer", "give_feedback")

    # Conditional edge based on whether to continue
    workflow.add_conditional_edges(
        "give_feedback",
        should_continue,
        {
            "next_question": "generate_question",
            "end_quiz": "end_quiz"
        }
    )

    workflow.add_edge("end_quiz", END)

    return workflow.compile()


# =====================================================
# Main Function
# =====================================================

def get_user_input_for_answer(question):
    """Get user's answer for a question."""
    print()
    print("-" * 50)
    print(f"Q: {question}")
    print("-" * 50)
    answer = input("\nYour answer: ").strip()
    return answer


def main():
    """Main function to run the quiz."""
    print("=" * 50)
    print("  Quiz Master (LangGraph + DeepSeek)")
    print("=" * 50)
    print()

    # Get quiz settings from user
    print("What topic would you like to be quizzed on?")
    print("Examples: Science, History, Movies, Sports, Music, Geography")
    print()
    topic = input("Topic: ").strip()

    if not topic:
        topic = "General Knowledge"

    print()
    print("How many questions? (1-10)")
    max_q_input = input("Number of questions: ").strip()

    try:
        max_questions = int(max_q_input)
        if max_questions < 1:
            max_questions = 1
        if max_questions > 10:
            max_questions = 10
    except:
        max_questions = 5

    print()
    print(f"Starting quiz on '{topic}' with {max_questions} questions!")
    print("=" * 50)

    # Build the graph
    quiz_graph = build_quiz_graph()

    # Initialize state
    state = {
        "topic": topic,
        "current_question": "",
        "correct_answer": "",
        "user_answer": "",
        "is_correct": False,
        "explanation": "",
        "score": 0,
        "questions_asked": 0,
        "max_questions": max_questions,
        "should_continue": True
    }

    # Run the quiz loop manually to handle user input
    while state["should_continue"] and state["questions_asked"] < state["max_questions"]:
        # Generate question
        print("\nGenerating question...")
        state = generate_question(state)

        # Get user answer
        user_answer = get_user_input_for_answer(state["current_question"])
        state["user_answer"] = user_answer

        # Check answer
        print("\nChecking answer...")
        state = check_answer(state)

        # Give feedback
        state = give_feedback(state)

        # Check if should continue
        if state["questions_asked"] < state["max_questions"]:
            result = should_continue(state)
            if result == "end_quiz":
                break

    # End quiz
    end_quiz(state)

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
