"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def largest_prime_factors(number):
    """
    Function that returns the largest prime factor of a number.

    :param number: the number that will be divided in order to find its largest
    prime divisor.
    :return: largest prime divisor.
    """
    largest_factor = 0

    def is_prime(k):
        for j in range(2, k):
            if k % j == 0:
                return False
        return True

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            if i > largest_factor:
                largest_factor = i
    return largest_factor


print(largest_prime_factors(600851475143))
