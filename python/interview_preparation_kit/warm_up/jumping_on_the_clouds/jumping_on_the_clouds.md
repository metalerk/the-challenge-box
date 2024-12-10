
# Jumping on the Clouds

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
- Jump from index `0` to index `2`
- Jump from index `2` to index `4`
- Jump from index `4` to index `6`

### Constraints
- \( 2 \leq n \leq 100 \)
- Each element in `c` is either `0` or `1`
- The first and last clouds are always safe (i.e., `c[0] = 0` and `c[n-1] = 0`)

### Function Signature
Implement the function as follows:
```python
def jumpingOnClouds(c):
    # Your code here
```
