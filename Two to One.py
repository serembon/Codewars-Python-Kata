"""Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
containing distinct letters, each taken only once - coming from `s1` or `s2`.

Examples:
```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```
"""


# My solution


def longest1(s1, s2):
    x = list(set(s1).union(set(s2)))
    return ''.join(sorted(x))


# Best way


def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))
