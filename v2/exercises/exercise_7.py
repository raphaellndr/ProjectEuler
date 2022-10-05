"""
Exercise 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from typing import List

import typer
from math import ceil, log

subcommand = typer.Typer(help="")
app = typer.Typer(no_args_is_help=True)
app.add_typer(subcommand, name="")


def _upper_bound(n: int) -> int:
    """
    Get the greatest n-th prime number possible.

    :param n: n-th prime number possible.
    :return: greatest prime number possible.
    """
    if n >= 6:
        return ceil(n * (log(n) + log(log(n))))
    return 100


def _sieve_of_eratosthenes(limit: int) -> List[int]:
    boolean_values = [True] * (limit + 1)
    boolean_values[0] = boolean_values[1] = False

    primes = []
    for (i, boolean_value) in enumerate(boolean_values):
        if boolean_value:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                boolean_values[j] = False

    return primes


@subcommand.command(help="")
def exercise_7(
    n_prime_number: int = typer.Option(0, help="The nth prime number we are looking for."),
) -> None:
    """
    Function that returns the nth prime number.

    :param n_prime_number: the nth prime number we are looking for.
    :return: nth prime number.
    """
    upper_bound: int = _upper_bound(n_prime_number)
    primes: List[int] = _sieve_of_eratosthenes(upper_bound)
    print(primes[-1])


if __name__ == "__main__":
    typer.run(exercise_7)
