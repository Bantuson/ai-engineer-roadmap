# DSA & LeetCode Preparation

Pattern-based approach to mastering data structures and algorithms for technical interviews.

## Philosophy

**Don't memorize solutions. Learn patterns.**

Each pattern solves a category of problems. Master the pattern, solve any problem in that category.

## Pattern Overview

| # | Pattern | Key Data Structure | Common Problems |
|---|---------|-------------------|-----------------|
| 1 | Arrays/Strings | Array, String | Two Sum, Valid Palindrome |
| 2 | Hashmaps/Sets | HashMap, HashSet | Group Anagrams, Contains Duplicate |
| 3 | Two Pointers | Array | 3Sum, Container With Water |
| 4 | Sliding Window | Array, String | Max Subarray, Min Window Substring |
| 5 | Linked Lists | LinkedList | Reverse List, Cycle Detection |
| 6 | Trees/Graphs | Tree, Graph | Level Order, Number of Islands |
| 7 | Recursion/Backtracking | Call Stack | Permutations, N-Queens |
| 8 | Dynamic Programming | Array/Table | Coin Change, Longest Subsequence |
| 9 | Sorting/Searching | Various | Binary Search, Merge Sort |

## Folder Structure

```
02-leetcode-dsa/
├── README.md (this file)
├── 01-arrays-strings/
│   ├── patterns.md
│   ├── problems/
│   │   ├── two-sum.md
│   │   ├── valid-palindrome.md
│   │   └── ...
│   └── exercises.md
├── 02-hashmaps-sets/
│   ├── patterns.md
│   └── problems/
├── ... (similar structure)
└── mental-models/
    ├── problem-decomposition.md
    ├── pattern-recognition.md
    └── complexity-analysis.md
```

## Study Plan

### Week 1: Foundation (15 problems)

**Day 1-2: Arrays & Strings**
- [ ] Two Sum (#1)
- [ ] Best Time to Buy/Sell Stock (#121)
- [ ] Contains Duplicate (#217)
- [ ] Valid Anagram (#242)

**Day 3-4: Hashmaps & Sets**
- [ ] Group Anagrams (#49)
- [ ] Top K Frequent Elements (#347)
- [ ] Valid Sudoku (#36)

**Day 5-6: Two Pointers**
- [ ] Valid Palindrome (#125)
- [ ] Two Sum II (#167)
- [ ] 3Sum (#15)
- [ ] Container With Most Water (#11)

**Day 7: Sliding Window**
- [ ] Maximum Subarray (#53)
- [ ] Longest Substring Without Repeating (#3)
- [ ] Minimum Window Substring (#76)

### Week 2: Trees & Graphs (20 problems)

**Day 8-9: Linked Lists**
- [ ] Reverse Linked List (#206)
- [ ] Merge Two Sorted Lists (#21)
- [ ] Linked List Cycle (#141)
- [ ] Remove Nth Node From End (#19)

**Day 10-12: Trees**
- [ ] Maximum Depth of Binary Tree (#104)
- [ ] Invert Binary Tree (#226)
- [ ] Binary Tree Level Order Traversal (#102)
- [ ] Validate Binary Search Tree (#98)
- [ ] Lowest Common Ancestor (#236)
- [ ] Serialize and Deserialize (#297)

**Day 13-14: Graphs**
- [ ] Number of Islands (#200)
- [ ] Clone Graph (#133)
- [ ] Course Schedule (#207)
- [ ] Pacific Atlantic Water Flow (#417)
- [ ] Word Ladder (#127)

### Week 3: Advanced (15 problems)

**Day 15-16: Recursion & Backtracking**
- [ ] Subsets (#78)
- [ ] Permutations (#46)
- [ ] Combination Sum (#39)
- [ ] Word Search (#79)

**Day 17-19: Dynamic Programming**
- [ ] Climbing Stairs (#70)
- [ ] House Robber (#198)
- [ ] Coin Change (#322)
- [ ] Longest Increasing Subsequence (#300)
- [ ] Unique Paths (#62)

**Day 20: Mixed Practice**
- [ ] Review weak areas
- [ ] Timed practice
- [ ] Mock interview problems

## Pattern Templates

### Two Pointers

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Process elements at left and right

        if condition_to_move_left:
            left += 1
        elif condition_to_move_right:
            right -= 1
        else:
            # Found solution or both pointers move
            pass

    return result
```

### Sliding Window

```python
def sliding_window(arr, k):
    window_start = 0
    window_sum = 0  # or other aggregate

    for window_end in range(len(arr)):
        # Expand window
        window_sum += arr[window_end]

        # Contract window when condition met
        while window_sum > k:  # or other condition
            window_sum -= arr[window_start]
            window_start += 1

        # Update result

    return result
```

### BFS (Trees/Graphs)

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

### DFS (Trees/Graphs)

```python
def dfs(root):
    if not root:
        return

    # Process node (preorder)
    process(root)

    # Recurse
    dfs(root.left)
    dfs(root.right)

    # Process node (postorder) - if needed
```

### Backtracking

```python
def backtrack(candidates, target, current, results, start):
    # Base case
    if is_solution(current):
        results.append(current[:])
        return

    # Explore choices
    for i in range(start, len(candidates)):
        # Skip duplicates if needed
        if should_skip(i, candidates):
            continue

        # Make choice
        current.append(candidates[i])

        # Recurse
        backtrack(candidates, target, current, results, i + 1)

        # Undo choice (backtrack)
        current.pop()
```

### Dynamic Programming

```python
def dp_bottom_up(n):
    # Initialize dp table
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = base_case_0
    dp[1] = base_case_1

    # Fill table
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # Recurrence relation

    return dp[n]
```

## Problem-Solving Framework

### 1. Understand (2-3 min)
- Restate the problem
- Identify input/output
- Clarify edge cases
- Ask questions

### 2. Plan (3-5 min)
- Identify the pattern
- Think through approach
- Consider time/space complexity
- Walk through example

### 3. Implement (10-15 min)
- Write clean code
- Use meaningful names
- Handle edge cases
- Test as you go

### 4. Verify (2-3 min)
- Trace through examples
- Check edge cases
- Analyze complexity
- Optimize if needed

## Complexity Cheat Sheet

| Operation | Array | LinkedList | HashMap | Tree (balanced) |
|-----------|-------|------------|---------|-----------------|
| Access | O(1) | O(n) | O(1) | O(log n) |
| Search | O(n) | O(n) | O(1) | O(log n) |
| Insert | O(n) | O(1) | O(1) | O(log n) |
| Delete | O(n) | O(1) | O(1) | O(log n) |

| Algorithm | Time | Space |
|-----------|------|-------|
| Binary Search | O(log n) | O(1) |
| BFS/DFS | O(V + E) | O(V) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(log n) |

## Tips for Interviews

1. **Think out loud** - Explain your reasoning
2. **Start simple** - Brute force first, then optimize
3. **Test early** - Walk through examples
4. **Ask questions** - Clarify before coding
5. **Stay calm** - It's okay to pause and think

## Next Steps

- Start with [01-arrays-strings/](01-arrays-strings/) patterns
- Use [mental-models/](mental-models/) for problem-solving
- Track progress in [../../learning-workflow/trackers/](../../learning-workflow/trackers/)
