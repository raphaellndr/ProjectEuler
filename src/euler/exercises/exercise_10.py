"""Exercise 10:

The sum of the prime numbers below 10 is 2 + 3 + 5 + 1 = 17.

Find the sum of all the prime numbers below 2 million.
"""

import typer

from ._registry import exercise
from .exercise_7 import sieve_of_eratosthenes


@exercise(name="exercise-10")
def exercise_10(
    limit: int = typer.Option(10, help="Max value of the prime number to add to the sum."),
) -> None:
    """Exercise 10: Sum of all the prime numbers below given limit.

    :param limit: max value of the prime number to add to the sum.
    """
    print(sum(sieve_of_eratosthenes(limit)))


if __name__ == "__main__":
    typer.run(exercise_10)
