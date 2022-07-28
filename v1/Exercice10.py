"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def summation_of_prime(limit):
    """
    Function that returns the sum of all the primes below n.

    :param limit: the greatest prime number we can reach (not necessarily one). .
    :return: sum of the prime numbers.
    """
    sum_of_primes = 0

    def is_prime(k):  # check if the number k is prime or not
        for j in range(2, int(math.sqrt(k)) + 1):
            if k % j == 0:
                return False
        return True

    for i in range(2, limit):
        if is_prime(i):
            sum_of_primes += i
    return sum_of_primes
