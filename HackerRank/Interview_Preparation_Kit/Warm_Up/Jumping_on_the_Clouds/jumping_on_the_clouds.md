
# Jumping on the Clouds

[Go Back](/HackerRank/Interview_Preparation_Kit/Warm_Up/warm_up.md)

There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are safe (represented by `0`) and others are not safe (represented by `1`). The player can jump from one cloud to another if the cloud is safe. The player must avoid landing on clouds with `1` and can jump to a cloud that is either one or two steps away.

## Problem Statement

Given an array of integers `c` where each element represents a cloud:
- `0`: Safe cloud
- `1`: Dangerous cloud (avoid landing here)

You start at the first cloud (index `0`) and must always end at the last cloud (index `n-1`). Determine the minimum number of jumps required to get from the start to the end.

### Example

Input:
```
c = [0, 1, 0, 0, 0, 1, 0]
```

Output:
```
3
```

Explanation:

Index the array from `0...6`. The number on each cloud is its index in the list so the player must avoid the clouds at indices `1` and `5`. They could follow these two paths: 

- Jump from index `0` to index `2`
- Jump from index `2` to index `4`
- Jump from index `4` to index `6`

3 steps

or 

- Jump from index `0` to index `2`
- Jump from index `2` to index `3`
- Jump from index `3` to index `4`
- Jump from index `4` to index `6`

4 steps.

First path must be returned.

### Constraints
- \( 2 \leq n \leq 100 \)
- Each element in `c` is either `0` or `1`
- The first and last clouds are always safe (i.e., `c[0] = 0` and `c[n-1] = 0`)

### Function Signature
Implement the function as follows:
```python
def jumping_on_clouds(c):
    # code
```

### Solution

Proposed solution can be found [here](/HackerRank/Interview_Preparation_Kit/Warm_Up/Jumping_on_the_Clouds/jumping_on_the_clouds.py).
