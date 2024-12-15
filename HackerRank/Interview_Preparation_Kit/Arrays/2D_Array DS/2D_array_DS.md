# 2D Array - DS

## Problem Statement

Given a 6x6 2D array, `arr`:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

An **hourglass** in `arr` is a subset of values with indices falling in this pattern:

```
a b c
  d
e f g
```

There are **16 hourglasses** in a 6x6 array. An hourglass sum is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in `arr`, then print the maximum hourglass sum.

## Example

Given the 2D array:

```
-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
```

The hourglass sums are:

```
-63, -34, -9, 12, 16, 2, ...
```

The maximum hourglass sum is `28`.

## Input Format

- A 6x6 2D array, `arr`, of integers.

## Output Format

- Print the maximum hourglass sum in the array.

## Constraints

- `-9 ≤ arr[i][j] ≤ 9`
- `0 ≤ i, j ≤ 5`

## Solution

Proposed solution can be found [here](/HackerRank/Interview_Preparation_Kit/Arrays/2D_Array_DS/2D_array_DS.py).
