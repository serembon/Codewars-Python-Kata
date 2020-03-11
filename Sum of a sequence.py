"""Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: `begin, end, step`.

If begin value is greater than the end, function should returns `0`"""


# My solution


def sequence_sum1(begin_number, end_number, step):

    # begin_number is greater than the end_number(it`s not required, sum function returns 0 by default).
    if begin_number > end_number:
        return 0

    # Using sum function for calculation.
    else:
        return sum(x for x in range(begin_number, end_number + 1, step))


# Best way


def sequence_sum2(begin_number, end_number, step):

    return sum(range(begin_number, end_number + 1, step))
