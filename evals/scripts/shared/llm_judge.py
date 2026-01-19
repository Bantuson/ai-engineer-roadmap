"""
LLM-as-Judge Evaluation Module

This module provides functions for using LLMs to evaluate AI outputs.
"""

import json
import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


# ============= Configuration =============

@dataclass
class JudgeConfig:
    """Configuration for LLM judge."""
    model: str = "deepseek-chat"
    temperature: float = 0.0
    max_tokens: int = 500
    retries: int = 2


DEFAULT_CRITERIA = [
    {
        "name": "relevance",
        "description": "How well does the response address the query?",
        "weight": 1.0
    },
    {
        "name": "accuracy",
        "description": "Is the information correct and factual?",
        "weight": 1.0
    },
    {
        "name": "clarity",
        "description": "Is the response clear and easy to understand?",
        "weight": 1.0
    },
    {
        "name": "completeness",
        "description": "Does the response fully address all aspects?",
        "weight": 1.0
    },
]


DEFAULT_RUBRIC = """
## Scoring Rubric (1-5 scale)

### Score 5 - Excellent
- Perfectly addresses the query
- All information is accurate
- Clear, well-organized, and helpful
- Comprehensive coverage

### Score 4 - Good
- Addresses the query well
- Information is mostly accurate
- Clear with minor issues
- Covers most aspects

### Score 3 - Adequate
- Addresses the main query
- Some inaccuracies or gaps
- Reasonably clear
- Missing some aspects

### Score 2 - Poor
- Partially addresses query
- Notable inaccuracies
- Unclear in places
- Significant gaps

### Score 1 - Very Poor
- Fails to address query
- Major inaccuracies
- Confusing or incoherent
- Unhelpful
"""


# ============= Prompts =============

SINGLE_CRITERION_PROMPT = """
You are an expert evaluator. Rate the following response.

Query: {query}

Response:
{response}

Criterion: {criterion_name}
Description: {criterion_description}

{rubric}

Provide your evaluation:
1. Score (1-5)
2. Brief explanation (1-2 sentences)

Format:
Score: [1-5]
Explanation: [your explanation]
"""


MULTI_CRITERIA_PROMPT = """
You are an expert evaluator. Rate the following response on multiple criteria.

Query: {query}

Response:
{response}

Evaluate on these criteria (1-5 scale each):
{criteria_list}

{rubric}

For each criterion, provide a score and brief justification.

Format your response as JSON:
{{
  "criterion_name": {{"score": X, "reason": "..."}},
  ...
}}
"""


PAIRWISE_PROMPT = """
You are comparing two responses to the same query.

Query: {query}

Response A:
{response_a}

Response B:
{response_b}

Which response is better? Consider:
- Relevance to the query
- Accuracy of information
- Clarity of explanation
- Helpfulness to the user

Important: Evaluate based on quality, not length. A concise accurate answer
is better than a verbose mediocre one.

Respond with:
- Winner: "A", "B", or "Tie"
- Confidence: "high", "medium", or "low"
- Explanation: Brief reasoning (2-3 sentences)

Format as JSON:
{{"winner": "...", "confidence": "...", "explanation": "..."}}
"""


# ============= Parsing Functions =============

def parse_score(text: str) -> Optional[int]:
    """Extract numeric score from text."""
    # Look for "Score: X" pattern
    match = re.search(r'Score:\s*(\d)', text)
    if match:
        return int(match.group(1))

    # Look for standalone number
    match = re.search(r'\b([1-5])\b', text)
    if match:
        return int(match.group(1))

    return None


def parse_json_response(text: str) -> Optional[Dict]:
    """Extract JSON from LLM response."""
    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to find JSON block
    json_match = re.search(r'\{[^{}]+\}', text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

    return None


def parse_single_evaluation(text: str) -> Dict[str, Any]:
    """Parse single criterion evaluation response."""
    result = {"score": None, "explanation": ""}

    lines = text.strip().split('\n')
    for line in lines:
        if line.lower().startswith("score:"):
            result["score"] = parse_score(line)
        elif line.lower().startswith("explanation:"):
            result["explanation"] = line.split(":", 1)[1].strip()

    # Fallback: try to find score anywhere
    if result["score"] is None:
        result["score"] = parse_score(text)

    return result


# ============= Evaluation Functions =============

def evaluate_single_criterion(
    response: str,
    query: str,
    criterion: Dict[str, str],
    llm_client,
    config: JudgeConfig = None
) -> Dict[str, Any]:
    """
    Evaluate response on a single criterion.

    Args:
        response: The response to evaluate
        query: The original query
        criterion: Dict with 'name' and 'description'
        llm_client: LLM client with generate() method
        config: Judge configuration

    Returns:
        Dict with 'score' and 'explanation'
    """
    config = config or JudgeConfig()

    prompt = SINGLE_CRITERION_PROMPT.format(
        query=query,
        response=response,
        criterion_name=criterion["name"],
        criterion_description=criterion["description"],
        rubric=DEFAULT_RUBRIC
    )

    for attempt in range(config.retries + 1):
        try:
            llm_response = llm_client.generate(prompt)
            result = parse_single_evaluation(llm_response)

            if result["score"] is not None:
                return result
        except Exception as e:
            if attempt == config.retries:
                return {"score": None, "explanation": f"Error: {e}"}

    return {"score": None, "explanation": "Failed to parse response"}


def evaluate_multi_criteria(
    response: str,
    query: str,
    criteria: List[Dict] = None,
    llm_client = None,
    config: JudgeConfig = None
) -> Dict[str, Dict]:
    """
    Evaluate response on multiple criteria.

    Args:
        response: The response to evaluate
        query: The original query
        criteria: List of criterion dicts
        llm_client: LLM client
        config: Judge configuration

    Returns:
        Dict mapping criterion names to {score, reason}
    """
    config = config or JudgeConfig()
    criteria = criteria or DEFAULT_CRITERIA

    criteria_list = "\n".join([
        f"- {c['name']}: {c['description']}"
        for c in criteria
    ])

    prompt = MULTI_CRITERIA_PROMPT.format(
        query=query,
        response=response,
        criteria_list=criteria_list,
        rubric=DEFAULT_RUBRIC
    )

    for attempt in range(config.retries + 1):
        try:
            llm_response = llm_client.generate(prompt)
            result = parse_json_response(llm_response)

            if result:
                return result
        except Exception as e:
            if attempt == config.retries:
                return {c["name"]: {"score": None, "reason": f"Error: {e}"}
                        for c in criteria}

    return {c["name"]: {"score": None, "reason": "Parse failed"}
            for c in criteria}


def pairwise_compare(
    response_a: str,
    response_b: str,
    query: str,
    llm_client,
    config: JudgeConfig = None
) -> Dict[str, Any]:
    """
    Compare two responses.

    Args:
        response_a: First response
        response_b: Second response
        query: The original query
        llm_client: LLM client
        config: Judge configuration

    Returns:
        Dict with 'winner', 'confidence', 'explanation'
    """
    config = config or JudgeConfig()

    prompt = PAIRWISE_PROMPT.format(
        query=query,
        response_a=response_a,
        response_b=response_b
    )

    for attempt in range(config.retries + 1):
        try:
            llm_response = llm_client.generate(prompt)
            result = parse_json_response(llm_response)

            if result and "winner" in result:
                return result
        except Exception as e:
            if attempt == config.retries:
                return {"winner": None, "confidence": "low",
                        "explanation": f"Error: {e}"}

    return {"winner": None, "confidence": "low",
            "explanation": "Parse failed"}


def pairwise_compare_debiased(
    response_a: str,
    response_b: str,
    query: str,
    llm_client,
    config: JudgeConfig = None
) -> Dict[str, Any]:
    """
    Compare two responses with position debiasing.

    Runs comparison in both orders and reconciles results.
    """
    # Compare A vs B
    result_ab = pairwise_compare(response_a, response_b, query, llm_client, config)

    # Compare B vs A (swapped)
    result_ba = pairwise_compare(response_b, response_a, query, llm_client, config)

    # Reconcile
    winner_ab = result_ab.get("winner", "").upper()
    winner_ba = result_ba.get("winner", "").upper()

    # Consistent results
    if winner_ab == "A" and winner_ba == "B":
        return {"winner": "A", "confidence": "high",
                "explanation": "Consistent across positions"}
    elif winner_ab == "B" and winner_ba == "A":
        return {"winner": "B", "confidence": "high",
                "explanation": "Consistent across positions"}
    elif winner_ab == "TIE" and winner_ba == "TIE":
        return {"winner": "tie", "confidence": "medium",
                "explanation": "Both comparisons resulted in tie"}
    else:
        # Inconsistent - possible position bias
        return {"winner": "uncertain", "confidence": "low",
                "explanation": f"Inconsistent: AB={winner_ab}, BA={winner_ba}"}


# ============= Aggregation =============

def calculate_judge_score(evaluation: Dict[str, Dict], weights: Dict[str, float] = None) -> float:
    """
    Calculate weighted average score from multi-criteria evaluation.

    Args:
        evaluation: Output from evaluate_multi_criteria
        weights: Optional criterion weights

    Returns:
        Weighted average score (1-5)
    """
    scores = []
    total_weight = 0

    for criterion, result in evaluation.items():
        score = result.get("score")
        if score is not None:
            weight = weights.get(criterion, 1.0) if weights else 1.0
            scores.append(score * weight)
            total_weight += weight

    if total_weight == 0:
        return 0.0

    return sum(scores) / total_weight


def normalize_score(score: float, min_val: float = 1.0, max_val: float = 5.0) -> float:
    """Normalize score to 0-1 range."""
    return (score - min_val) / (max_val - min_val)


# ============= LLM Client Wrapper =============

class SimpleLLMClient:
    """
    Simple LLM client wrapper.

    Replace with actual implementation (OpenAI, DeepSeek, etc.)
    """

    def __init__(self, model: str = "deepseek-chat", api_key: str = None):
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate response from LLM.

        This is a placeholder - implement with actual API calls.
        """
        # Example implementation for DeepSeek/OpenAI-compatible API:
        #
        # from openai import OpenAI
        # client = OpenAI(
        #     api_key=self.api_key or os.environ["DEEPSEEK_API_KEY"],
        #     base_url="https://api.deepseek.com"
        # )
        # response = client.chat.completions.create(
        #     model=self.model,
        #     messages=[{"role": "user", "content": prompt}],
        #     temperature=kwargs.get("temperature", 0.0)
        # )
        # return response.choices[0].message.content

        raise NotImplementedError("Implement with actual LLM API")


# ============= For Testing =============

if __name__ == "__main__":
    print("Testing LLM Judge module...")

    # Test parsing
    test_response = """
    Score: 4
    Explanation: The response is clear and accurate.
    """

    result = parse_single_evaluation(test_response)
    assert result["score"] == 4
    print(f"  parse_single_evaluation: OK")

    # Test JSON parsing
    test_json = '{"relevance": {"score": 4, "reason": "Good"}}'
    result = parse_json_response(test_json)
    assert result["relevance"]["score"] == 4
    print(f"  parse_json_response: OK")

    # Test score calculation
    evaluation = {
        "relevance": {"score": 4, "reason": ""},
        "accuracy": {"score": 5, "reason": ""},
    }
    avg = calculate_judge_score(evaluation)
    assert avg == 4.5
    print(f"  calculate_judge_score: {avg} OK")

    print("\nAll tests passed!")
    print("\nNote: Full testing requires implementing SimpleLLMClient.generate()")
