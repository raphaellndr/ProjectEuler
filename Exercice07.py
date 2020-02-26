############ EXERCICE 7 ############


"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


def find_prime_number(n):
    """
    Function that return the nth prime number.

    :param n: the nth prime number we are looking for.
    :return:
    """
    a = 1
    n_prime = 2
    i = 3

    def is_prime(k):
        for j in range(2, k):
            if k % j == 0: return False
        return True

    while a < n:
        if is_prime(i):
            a += 1
            n_prime = i
        i += 1
    return n_prime
