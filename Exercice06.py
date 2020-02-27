############ EXERCICE 6 ############


"""

The sum of the squares of the first ten natural numbers is, 1²+2²+...+10²=385.

The square of the sum of the first ten natural numbers is, (1+2+...+10)²=55²=3025.

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""


def sum_square_difference(limit):
    """
    Function that returns the difference between the sum of the squares and the
    square of the sum, from one to 'limit'.

    :param limit: the natural number where we want to stop the sum.
    :return: the difference.
    """
    sum = 0
    sum_of_squares = 0
    for i in range(1, limit + 1):
        sum += i
        sum_of_squares += i ** 2
    difference = sum ** 2 - sum_of_squares
    return difference
