"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once in
the original string. Ignore capitalization when determining if a character is a duplicate.
```
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```
"""


# My solution


def duplicate_encode1(word):
    iter_word = str(word.lower())
    check_list = []
    formatted_list = []
    position = 0

    for i in iter_word.lower():
        position += 1
        if i not in check_list and i not in (iter_word[position:]):
            check_list.append(i)
            i = '('
            formatted_list.append(i)
        else:
            check_list.append(i)
            i = ')'
            formatted_list.append(i)
    return ''.join(map(str, formatted_list))


# Best way


def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
