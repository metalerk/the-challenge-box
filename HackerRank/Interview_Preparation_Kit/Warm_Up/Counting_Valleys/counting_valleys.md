
# Counting Valleys

[Go Up](/HackerRank/Interview_Preparation_Kit/Warm_Up/warm_up.md)

A hiker starts at sea level and records their path as a string of steps. Each step is either uphill (`U`) or downhill (`D`). A valley is a sequence of consecutive steps below sea level, starting with a step down and ending with a step up.

## Example

Input:
```
steps = 8
path = "UDDDUDUU"
```

Output:
```
1
```

Explanation:
- The hiker enters one valley during the hike.

## Additional Test Cases

### Test Case 1
Input:
```
steps = 12
path = "DDUUDDUDUUUD"
```
Output:
```
2
```

### Test Case 2
Input:
```
steps = 10
path = "UDUUUDUDDD"
```
Output:
```
0
```

### Constraints
- \( 2 \leq 	ext{steps} \leq 10^6 \)
- The `path` string will consist of `U` and `D` characters only.

### Function Signature
Implement the function as follows:
```python
def countingValleys(steps, path):
    # Your code here
```
