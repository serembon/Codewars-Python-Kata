"""Your task is to write a function which returns the sum of following series upto nth term(parameter).

```Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...```

Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:

```SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"```

NOTE: In PHP the function is called ```series_sum().```
"""


def series_sum1(n):  # My solution
    x = 0
    for i in range(n):
        x += 1/(1+(3*i))
    return format(x, '.2f')


def series_sum(n):  # Best way
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
