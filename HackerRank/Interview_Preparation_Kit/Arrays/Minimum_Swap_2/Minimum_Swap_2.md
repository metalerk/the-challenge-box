# Minimum Swaps 2

## Problem Statement

You are given an unordered array consisting of consecutive integers `[1, 2, 3, ..., n]` without any duplicates. You are allowed to swap any two elements. Find the **minimum number of swaps** required to sort the array in ascending order.

## Example

### Example 1

**Input**  
```
arr = [4, 3, 1, 2]
```

**Output**  
```
3
```

**Explanation**  
Perform the following swaps:
1. Swap `4` and `1`. `arr = [1, 3, 4, 2]`
2. Swap `3` and `2`. `arr = [1, 2, 4, 3]`
3. Swap `4` and `3`. `arr = [1, 2, 3, 4]`

### Example 2

**Input**  
```
arr = [2, 3, 4, 1, 5]
```

**Output**  
```
3
```

**Explanation**  
Perform the following swaps:
1. Swap `2` and `1`. `arr = [1, 3, 4, 2, 5]`
2. Swap `3` and `2`. `arr = [1, 2, 4, 3, 5]`
3. Swap `4` and `3`. `arr = [1, 2, 3, 4, 5]`

### Example 3

**Input**  
```
arr = [1, 3, 5, 2, 4, 6, 7]
```

**Output**  
```
3
```

**Explanation**  
Perform the following swaps:
1. Swap `3` and `2`. `arr = [1, 2, 5, 3, 4, 6, 7]`
2. Swap `5` and `3`. `arr = [1, 2, 3, 5, 4, 6, 7]`
3. Swap `5` and `4`. `arr = [1, 2, 3, 4, 5, 6, 7]`

## Constraints

- `1 <= n <= 10^5`
- The array contains consecutive integers from `1` to `n`, inclusive.
- No integer is repeated in the array.

## Function Signature

```python
def minimumSwaps(arr: List[int]) -> int:
    pass
```

## Notes

- Your function should be optimized for large inputs to run within a reasonable time frame.
