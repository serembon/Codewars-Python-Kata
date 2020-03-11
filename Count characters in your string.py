"""
The main idea is to count all the occurring characters (UTF-8) in string. If you have string like this aba then the result should be `{ 'a': 2, 'b': 1 }`

What if the string is empty ? Then the result should be empty object literal `{ }`
"""

# My solution


def count1(string):
    if string == '':    # Check for empty string
        return {}

    d = {}

    for word in string:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


# Best way


def count2(string):
    return {i: string.count(i) for i in string}
