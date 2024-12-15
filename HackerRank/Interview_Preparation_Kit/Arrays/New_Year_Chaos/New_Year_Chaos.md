# New Year Chaos

## Problem Statement

It's New Year's Day, and people are in line for the Wonderland rollercoaster ride. Each person has a unique ticket number, and the initial queue is ordered sequentially, starting with the ticket number `1`. Some people have decided to bribe the person directly in front of them to swap places. One person can bribe at most two others. Determine the minimum number of bribes that took place to get the queue into its current state.

If the queue state is invalid (i.e., any person has bribed more than two others), print "Too chaotic".

## Example

### Input

```
2
5
2 1 5 3 4
5
2 5 1 3 4
```

### Output

```
3
Too chaotic
```

## Explanation

1. For the first test case, the initial state of the queue is `[1, 2, 3, 4, 5]`.
    - Person `5` bribed two people to move ahead of `3` and `4`.
    - Person `3` bribed one person to move ahead of `4`.
    - Total bribes: `3`.

2. For the second test case, person `5` has bribed more than two people, making the state "Too chaotic".

## Input Format

- The first line contains an integer `t`, the number of test cases.
- Each of the next `t` test cases is described as:
  - An integer `n`, the number of people in the queue.
  - A line of `n` space-separated integers, the current state of the queue.

## Output Format

- For each test case, print an integer representing the minimum number of bribes, or "Too chaotic" if the state is invalid.

## Constraints

- `1 ≤ t ≤ 10`
- `1 ≤ n ≤ 10^5`
- The integers in the queue are a permutation of the first `n` natural numbers.

## Function Signature

The function should have the following signature:

```python
def minimum_bribes(q: List[int]) -> None:
```

## Notes

- The function should print the result for each test case on a new line.
- The goal is to determine the minimum number of bribes in `O(n)` time per test case for efficiency.

## Solution

A Proposed solution can be found [here](/HackerRank/Interview_Preparation_Kit/Arrays/New_Year_Chaos/new_year_chaos.py).
