"""Exercise 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import ceil, log
from typing import List

import typer

from ._registry import exercise


def upper_bound(number: int) -> int:
    """
    Get the greatest n-th prime number possible (approximately).

    :param number: n-th prime number possible.
    :return: greatest prime number possible.
    """
    if number >= 6:
        return ceil(number * log((number * log(number))))
    return number


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Finds all prime numbers up to any given limit.

    :param limit: greatest prime number possible.
    :return: list of prime numbers.
    """
    boolean_values = [True] * (limit + 1)
    boolean_values[0] = boolean_values[1] = False

    primes = []
    for (i, boolean_value) in enumerate(boolean_values):
        if boolean_value:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                boolean_values[j] = False

    return primes


@exercise(name="exercise-7")
def exercise_7(
    n_prime_number: int = typer.Option(0, help="The nth prime number we are looking for."),
) -> None:
    """Exercise 7: nth prime number.

    :param n_prime_number: the nth prime number we are looking for.
    """
    upp_bound: int = upper_bound(n_prime_number)
    primes: List[int] = sieve_of_eratosthenes(upp_bound)
    print(primes[n_prime_number - 1])


if __name__ == "__main__":
    typer.run(exercise_7)
