"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    """
    Function that returns the largest palindromic number that the product of
    2 3-digit numbers can make.

    :return: largest palindromic number.
    """
    largest_palindrome = 0
    for j in range(100, 999):
        for i in range(100, 999):
            product = i * j
            a = [int(d) for d in str(product)]
            b = a[::-1]
            if a == b:
                largest_palindrome = product
    return largest_palindrome
