"""
Shared Evaluation Metrics

This module provides common metrics used across evaluation scripts.
"""

import math
import statistics
from typing import List, Dict, Any, Set
from collections import Counter


# ============= Basic Metrics =============

def exact_match(prediction: str, reference: str, case_sensitive: bool = False) -> float:
    """
    Check if prediction exactly matches reference.

    Args:
        prediction: Model output
        reference: Expected output
        case_sensitive: Whether comparison is case-sensitive

    Returns:
        1.0 if match, 0.0 otherwise
    """
    pred = prediction.strip()
    ref = reference.strip()

    if not case_sensitive:
        pred = pred.lower()
        ref = ref.lower()

    return 1.0 if pred == ref else 0.0


def contains_match(prediction: str, reference: str, case_sensitive: bool = False) -> float:
    """
    Check if reference is contained in prediction.

    Returns:
        1.0 if contained, 0.0 otherwise
    """
    pred = prediction.strip()
    ref = reference.strip()

    if not case_sensitive:
        pred = pred.lower()
        ref = ref.lower()

    return 1.0 if ref in pred else 0.0


# ============= Token-Based Metrics =============

def tokenize(text: str) -> List[str]:
    """Simple whitespace tokenization."""
    return text.lower().split()


def precision(prediction_tokens: List[str], reference_tokens: List[str]) -> float:
    """
    Calculate precision: correct_tokens / predicted_tokens

    Returns:
        Precision score (0-1)
    """
    if not prediction_tokens:
        return 0.0

    pred_set = set(prediction_tokens)
    ref_set = set(reference_tokens)
    overlap = pred_set & ref_set

    return len(overlap) / len(pred_set)


def recall(prediction_tokens: List[str], reference_tokens: List[str]) -> float:
    """
    Calculate recall: correct_tokens / reference_tokens

    Returns:
        Recall score (0-1)
    """
    if not reference_tokens:
        return 0.0

    pred_set = set(prediction_tokens)
    ref_set = set(reference_tokens)
    overlap = pred_set & ref_set

    return len(overlap) / len(ref_set)


def f1_score(prediction_tokens: List[str], reference_tokens: List[str]) -> float:
    """
    Calculate F1 score: harmonic mean of precision and recall

    Returns:
        F1 score (0-1)
    """
    p = precision(prediction_tokens, reference_tokens)
    r = recall(prediction_tokens, reference_tokens)

    if p + r == 0:
        return 0.0

    return 2 * (p * r) / (p + r)


def f1_score_text(prediction: str, reference: str) -> float:
    """Calculate F1 score on text strings."""
    return f1_score(tokenize(prediction), tokenize(reference))


# ============= N-gram Metrics =============

def get_ngrams(tokens: List[str], n: int) -> List[tuple]:
    """Extract n-grams from token list."""
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]


def bleu_score(candidate: str, reference: str, max_n: int = 4) -> float:
    """
    Calculate BLEU score for translation quality.

    Args:
        candidate: Generated text
        reference: Reference text
        max_n: Maximum n-gram size

    Returns:
        BLEU score (0-1)
    """
    cand_tokens = tokenize(candidate)
    ref_tokens = tokenize(reference)

    if len(cand_tokens) == 0:
        return 0.0

    precisions = []

    for n in range(1, max_n + 1):
        cand_ngrams = Counter(get_ngrams(cand_tokens, n))
        ref_ngrams = Counter(get_ngrams(ref_tokens, n))

        if not cand_ngrams:
            precisions.append(0.0)
            continue

        overlap = sum((cand_ngrams & ref_ngrams).values())
        total = sum(cand_ngrams.values())

        precisions.append(overlap / total if total > 0 else 0.0)

    # Avoid log(0)
    if min(precisions) == 0:
        return 0.0

    # Geometric mean
    log_precisions = [math.log(p) for p in precisions]
    geo_mean = math.exp(sum(log_precisions) / len(log_precisions))

    # Brevity penalty
    bp = min(1.0, math.exp(1 - len(ref_tokens) / len(cand_tokens)))

    return bp * geo_mean


def rouge_l(candidate: str, reference: str) -> float:
    """
    Calculate ROUGE-L score using longest common subsequence.

    Returns:
        ROUGE-L F1 score (0-1)
    """
    cand_tokens = tokenize(candidate)
    ref_tokens = tokenize(reference)

    if not cand_tokens or not ref_tokens:
        return 0.0

    # LCS length via dynamic programming
    m, n = len(cand_tokens), len(ref_tokens)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if cand_tokens[i-1] == ref_tokens[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs = dp[m][n]

    p = lcs / len(cand_tokens)
    r = lcs / len(ref_tokens)

    if p + r == 0:
        return 0.0

    return 2 * p * r / (p + r)


# ============= Quality Metrics =============

def keyword_coverage(text: str, keywords: List[str]) -> float:
    """
    Calculate what fraction of keywords appear in text.

    Args:
        text: Text to check
        keywords: Required keywords

    Returns:
        Coverage score (0-1)
    """
    if not keywords:
        return 1.0

    text_lower = text.lower()
    covered = sum(1 for k in keywords if k.lower() in text_lower)

    return covered / len(keywords)


def length_ratio(text: str, target_length: int) -> float:
    """
    Calculate how close text length is to target.

    Returns:
        Score (0-1), 1.0 means exactly target length
    """
    actual_length = len(text.split())
    if target_length == 0:
        return 0.0 if actual_length > 0 else 1.0

    ratio = actual_length / target_length
    # Penalize both too short and too long
    return max(0.0, 1.0 - abs(1.0 - ratio))


def calculate_quality_score(scores: Dict[str, float], weights: Dict[str, float] = None) -> float:
    """
    Calculate weighted average quality score.

    Args:
        scores: Dictionary of metric scores
        weights: Optional weights for each metric

    Returns:
        Weighted average score
    """
    if not scores:
        return 0.0

    if weights is None:
        weights = {k: 1.0 for k in scores}

    total_weight = sum(weights.get(k, 1.0) for k in scores)
    weighted_sum = sum(scores[k] * weights.get(k, 1.0) for k in scores)

    return weighted_sum / total_weight


# ============= Aggregation Functions =============

def aggregate_scores(results: List[Dict[str, float]], metric: str) -> Dict[str, float]:
    """
    Aggregate scores for a single metric across results.

    Args:
        results: List of result dictionaries
        metric: Metric name to aggregate

    Returns:
        Dictionary with mean, std, min, max
    """
    scores = [r.get(metric, 0.0) for r in results if metric in r]

    if not scores:
        return {"mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0}

    return {
        "mean": statistics.mean(scores),
        "std": statistics.stdev(scores) if len(scores) > 1 else 0.0,
        "min": min(scores),
        "max": max(scores),
    }


def pass_rate(results: List[Dict], threshold: float, metric: str) -> float:
    """
    Calculate percentage of results passing threshold.

    Args:
        results: List of result dictionaries
        threshold: Minimum passing score
        metric: Metric to check

    Returns:
        Pass rate (0-1)
    """
    if not results:
        return 0.0

    passed = sum(1 for r in results if r.get(metric, 0.0) >= threshold)
    return passed / len(results)


# ============= Statistical Functions =============

def confidence_interval(scores: List[float], confidence: float = 0.95) -> tuple:
    """
    Calculate confidence interval for scores.

    Args:
        scores: List of scores
        confidence: Confidence level (default 0.95)

    Returns:
        Tuple of (lower, upper) bounds
    """
    if len(scores) < 2:
        return (0.0, 0.0)

    n = len(scores)
    mean = statistics.mean(scores)
    std = statistics.stdev(scores)

    # Z-score for 95% confidence
    z = 1.96 if confidence == 0.95 else 2.576  # 99%

    margin = z * (std / math.sqrt(n))

    return (mean - margin, mean + margin)


def is_significant(scores_a: List[float], scores_b: List[float], alpha: float = 0.05) -> bool:
    """
    Simple t-test for significance (two-tailed).

    Note: For production, use scipy.stats.ttest_ind

    Args:
        scores_a: First group scores
        scores_b: Second group scores
        alpha: Significance level

    Returns:
        True if difference is significant
    """
    if len(scores_a) < 2 or len(scores_b) < 2:
        return False

    mean_a = statistics.mean(scores_a)
    mean_b = statistics.mean(scores_b)
    var_a = statistics.variance(scores_a)
    var_b = statistics.variance(scores_b)
    n_a = len(scores_a)
    n_b = len(scores_b)

    # Pooled standard error
    se = math.sqrt(var_a/n_a + var_b/n_b)

    if se == 0:
        return mean_a != mean_b

    # T-statistic
    t = abs(mean_a - mean_b) / se

    # Rough critical value for large samples
    critical = 1.96 if alpha == 0.05 else 2.576

    return t > critical


# ============= For Testing =============

if __name__ == "__main__":
    # Test metrics
    print("Testing metrics...")

    # Exact match
    assert exact_match("Paris", "paris") == 1.0
    assert exact_match("Paris", "London") == 0.0
    print("  exact_match: OK")

    # F1 score
    f1 = f1_score_text("the cat sat", "a cat sat down")
    assert 0 < f1 < 1
    print(f"  f1_score: {f1:.3f} OK")

    # BLEU
    bleu = bleu_score("the cat sat on the mat", "the cat is on the mat")
    assert 0 < bleu < 1
    print(f"  bleu_score: {bleu:.3f} OK")

    # ROUGE-L
    rouge = rouge_l("the cat sat on mat", "the cat sat on the mat")
    assert 0 < rouge < 1
    print(f"  rouge_l: {rouge:.3f} OK")

    # Keyword coverage
    kw = keyword_coverage("Python is great for ML", ["python", "ml"])
    assert kw == 1.0
    print(f"  keyword_coverage: {kw:.3f} OK")

    print("\nAll tests passed!")
