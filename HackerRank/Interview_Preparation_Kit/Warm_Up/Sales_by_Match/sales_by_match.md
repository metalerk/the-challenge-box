
# Sales by Match

There is a collection of socks in various colors. Each sock is represented by an integer, identifying its color. Your task is to find the number of pairs of socks with matching colors.

## Example

Input:
```
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
```

Output:
```
2
```

Explanation:
- There are two pairs of socks: one pair of color `1` and one pair of color `2`.

## Additional Test Cases

### Test Case 1
Input:
```
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
```
Output:
```
3
```

### Test Case 2
Input:
```
n = 4
ar = [1, 1, 1, 1]
```
Output:
```
2
```

### Constraints
- \( 1 \leq n \leq 100 \)
- \( 1 \leq 	ext{ar}[i] \leq 100 \)

### Function Signature
Implement the function as follows:
```python
def sockMerchant(n, ar):
    # Your code here
```
