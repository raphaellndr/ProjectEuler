############ EXERCICE 21 ############


"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


def amicable_number(n):
    """
    Function that returns the sum of all the amicable numbers under n.

    :param n: greatest amicable number reachable.
    :return: sum of the amicable numbers.
    """

    def d(k):
        return sum(x for x in range(1, k // 2 + 1) if not (k % x))

    amicable_number = set()
    for i in range(1, n):
        a = d(i)
        b = d(a)
        if (i == b) and (a != b):
            amicable_number.add(a)
    return sum(amicable_number)