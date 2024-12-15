# Left Rotation

## Problem Statement

A left rotation operation on an array shifts each of the array's elements `1` unit to the left. For example, if `2` left rotations are performed on array `arr = [1, 2, 3, 4, 5]`, then the array would become `[3, 4, 5, 1, 2]`.

Given an array `arr` of integers and a number, `d`, perform `d` left rotations on the array. Return the updated array.

## Example

### Input

```
n = 5
arr = [1, 2, 3, 4, 5]
d = 2
```

### Output

```
[3, 4, 5, 1, 2]
```

## Function Signature

The function should have the following signature:

```python
def left_rotate(arr: List[int], d: int) -> List[int]:
```

## Input Format

- The first line contains two integers, `n` (the size of the array) and `d` (the number of left rotations).
- The second line contains `n` space-separated integers, the elements of the array `arr`.

## Output Format

- The function should return the updated array after `d` left rotations.

## Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ d ≤ n`
- `1 ≤ arr[i] ≤ 10^6`

## Explanation

Performing `d = 2` left rotations on the array `arr = [1, 2, 3, 4, 5]`:

1. After the 1st rotation: `[2, 3, 4, 5, 1]`
2. After the 2nd rotation: `[3, 4, 5, 1, 2]`

The final array is `[3, 4, 5, 1, 2]`.

## Solution

A proposed solution can be found [here](/HackerRank/Interview_Preparation_Kit/Arrays/Left_Rotation/list_left_rotation.py).