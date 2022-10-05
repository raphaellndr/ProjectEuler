"""
Exercise 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

import typer
from tqdm import tqdm

from ._registry import exercise


def _is_prime(k: int):
    """

    :param k:
    :return:
    """
    for j in range(2, k):
        if k % j == 0:
            return False
    return True


@exercise(name="exercise-3")
def exercise_3(
    number: int = typer.Option(0, help=""),
) -> None:
    """
    Function that returns the largest prime factor of a number.

    :param number: the number that will be divided in order to find its greatest
    prime divisor.
    :return: largest prime divisor.
    """
    greatest_prime_factor: int = 0
    for factor in tqdm(range(1, int(math.ceil(math.sqrt(number))) + 2)):
        if number % factor == 0 and _is_prime(factor):
            greatest_prime_factor = factor
    print(greatest_prime_factor)


if __name__ == "__main__":
    typer.run(exercise_3)
