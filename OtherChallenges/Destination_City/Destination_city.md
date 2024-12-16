# Destination City Problem Statement

## Problem Description

You are given a list of direct paths between cities in the form of pairs `paths[i] = [A, B]`, where `A` is the **starting city** and `B` is the **destination city**. A city is defined as a **destination city** if it does not appear as a starting city in any path.

Your task is to find the **destination city**.

It is guaranteed that there will always be exactly one destination city.

---

## Input Format

- `n` (1 ≤ n ≤ 100): The number of paths.
- An array of `n` paths, where each path is represented as a pair of strings `[A, B]`.

---

## Output Format

- A single string representing the destination city.

---

## Example

### Input:
```
paths = [["London", "Paris"], ["Paris", "Tokyo"], ["Tokyo", "New York"]]
```

### Output:
```
"New York"
```

### Explanation:
- "London" is a starting city but not a destination.
- "Paris" is a starting city and a destination, so it is not the final destination.
- "Tokyo" is a starting city and a destination, so it is not the final destination.
- "New York" does not appear as a starting city, making it the destination city.

---

## Constraints

- All cities have unique names.
- The input is a valid list of paths with no cycles.

---

## Function Signature

You can implement your solution with the following function signature:
```python
def find_destination_city(paths: List[List[str]]) -> str:
    pass
```

## Solution

### Layton Burchell at HackSussex Coder's Cup 2024

I found interesting the Layton Burchell's proposed solution to this challenge in [HackSussex Coder's Cup 2024](https://www.youtube.com/live/VixYfv0UEyE?si=ATP8LrPdFv8HECiP&t=738) and I **recreated** it here:

### `test.py` (Recreated)

```python
import unittest


class DestinationCityTestCase(unittest.TestCase):
    def __init__(self, solution_func, *args, **kwargs):
        self.solution_func = solution_func

        return super().__init__(*args, **kwargs)

    def test_solution(self):
        test_input = [
            ["London", "Paris"],
            ["Paris", "Tokyo"],
            ["Tokyo", "New York"]
        ]
        expected_output = "New York"
        self.assertEquals(
            self.solution_func(test_input),
            expected_output
        )


def runTests(solution):
    suite = unittest.TestSuite()
    suite.addTest(DestinationCityTestCase(solution_func=solution))
    runner = unittest.TextTestRunner()
    runner.run(suite)

```

### `main.py`

```python
from typing import List
import test


def Solution(paths: List[List[str]]) -> str:
    outs = set()
    ins = set()

    for a, b in paths:
        outs.insert(a)
        ins.insert(b)

    return [b for b in ins if b not in outs][0]

# testing
test.runTests(Solution)

```
