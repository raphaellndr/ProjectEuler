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

    :param n:
    :return:
    """

    def are_amicable(a, b):
        sum_a = 0
        sum_b = 0
        for i in range(1, a):
            if a % i == 0:
                sum_a += i
        for i in range(1, b):
            if b % i == 0:
                sum_b += i
        if sum_a == b and sum_b == a:
            return True
        return False

    sum_amicable = 0
    for a in range(n):
        for b in range(n):
            print(str(a) + ", " + str(b))
            if a != b:
                if are_amicable(a, b):
                    sum_amicable += a + b
    return sum_amicable


print(amicable_number(10000))
