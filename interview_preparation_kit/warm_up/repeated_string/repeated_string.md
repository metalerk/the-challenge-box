
# Repeated String

You have a string, `s`, and you want to determine how many times the letter `a` appears in the first `n` characters of the infinite repetition of the string.

## Example

Input:
```
s = "aba"
n = 10
```

Output:
```
7
```

Explanation:
- The substring of the first 10 characters is "abaabaabaa".
- The letter `a` appears 7 times.

### Constraints
- \( 1 \leq |s| \leq 100 \)
- \( 1 \leq n \leq 10^{12} \)
- The string `s` contains only lowercase English letters.

### Function Signature
Implement the function as follows:
```python
def repeatedString(s, n):
    # Your code here
```
