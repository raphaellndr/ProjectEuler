"""
Exercise 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import functools
import itertools
from typing import List

import typer

from ._registry import exercise


def greatest_palindromic_product(numbers_length: int):
    """Function that returns the largest palindromic number that the product of 2 'nb-digits'
    numbers can make.

    :param numbers_length: length (numbers of digits) of the numbers.
    :return: largest palindromic number.
    """
    numbers: list[int] = list(range(10 ** (numbers_length - 1), 10**numbers_length))

    palindromic_products: List = []
    for couple in itertools.product(numbers, repeat=2):
        product: int = functools.reduce(lambda x, y: x * y, couple)
        reversed_product: int = int("".join(list(str(product))[::-1]))

        if product == reversed_product:
            palindromic_products.append(product)

    return max(palindromic_products)


@exercise(name="exercise-4")
def exercise_4(
    numbers_length: int = typer.Option(2, help="Length (numbers of digits) of the numbers.")
) -> None:
    """Exercise 4: largest palindromic number that the product of 2 3-digit numbers can make.

    :param numbers_length: length (numbers of digits) of the numbers.
    """
    result: int = greatest_palindromic_product(numbers_length)
    print(result)


if __name__ == "__main__":
    typer.run(exercise_4)
