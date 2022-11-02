"""
Exercise 4:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import functools
import itertools
from typing import List

import typer

from ._registry import exercise


@exercise(name="exercise-4")
def exercise_4() -> None:
    """
    Function that returns the largest palindromic number that the product of
    2 3-digit numbers can make.

    :return: largest palindromic number.
    """
    three_digits_numbers = list(range(100, 1000))
    palindromic_number: List = []
    for couple in itertools.product(three_digits_numbers, repeat=2):
        product: int = functools.reduce(lambda x, y: x * y, couple)
        reversed_product: int = int("".join(list(str(product))[::-1]))

        if product == reversed_product:
            palindromic_number.append(product)

    print(max(palindromic_number))


if __name__ == "__main__":
    typer.run(exercise_4)
