############ EXERCICE 1 ############


"""

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


def multiples_of_3_and_5(number):
    """
    Function that return the sum of all the multiples of 3 or 5 below.

    :param number: the highest number that can be a multiple of 3 or 5.
    :return:
    """
    sum_of_multiples = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples
