############ EXERCICE 5 ############


"""

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""


def smallest_number(n):
    """

    :param n:
    :return:
    """
    smallest_number = 0
    for i in range(n - 10, n + 10):
        rest = 0
        for j in range(1, 21):
            rest = rest + i % j
        if rest == 0 and i > smallest_number:
            smallest_number = i
    return smallest_number


print(smallest_number(232792560))
