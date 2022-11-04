"""Exercise 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

import typer
from tqdm import tqdm

from ._registry import exercise


def is_prime(k: int):
    """Returns True if given number is prime.

    :param k: number to check if prime or not.
    :return: boolean.
    """
    for j in range(2, k):
        if k % j == 0:
            return False
    return True


def greatest_prime_factor(number: int) -> int:
    """Function that returns the largest prime factor of a number.

    :param number: the number that will be divided in order to find its greatest
    prime divisor.
    :return: largest prime divisor.
    """
    greatest_pf: int = 0
    for factor in tqdm(range(1, int(math.ceil(math.sqrt(number))) + 2)):
        if number % factor == 0 and is_prime(factor):
            greatest_pf = factor

    return greatest_pf


@exercise(name="exercise-3")
def exercise_3(
    number: int = typer.Option(0, help=""),
) -> None:
    """Exercise 3: largest prime factor of a number.

    :param number: the number that will be divided in order to find its greatest
    prime divisor.
    """
    result: int = greatest_prime_factor(number)
    print(result)


if __name__ == "__main__":
    typer.run(exercise_3)
