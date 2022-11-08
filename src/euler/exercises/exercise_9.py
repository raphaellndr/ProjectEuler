"""Exercise 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

from typing import List, NamedTuple

import typer

from ._registry import exercise


class Triplet(NamedTuple):
    """Definition of a triplet."""

    a: int
    b: int
    c: int


def pythagorean_triplet(triplet: Triplet) -> bool:
    """Returns True if given triplet is Pythagorean.

    :param triplet: triplet to evaluate.
    :return: boolean.
    """
    if not triplet.a < triplet.b < triplet.c:
        raise ValueError("a < b < c is not verified: cannot be a Pythagorean triplet.")

    if triplet.a**2 + triplet.b**2 == triplet.c**2:
        return True
    return False


def tmp(goal: int):
    """Function that returns the Pythagorean triplet for which a+b+c=goal.

    :param goal: the value we want to be equal to.
    :return: the triplet and the product of the 3 numbers.
    """
    numbers: List[int] = list(range(1, 998))
    print(numbers, goal)


@exercise(name="exercise-9")
def exercise_8(
    goal: int = typer.Option(0, help="Number of adjacent digits"),
) -> None:
    """Exercise 9: Pythagorean triplet for which a+b+c=goal.

    :param goal: the value we want to be equal to.
    """
    tmp(goal)


if __name__ == "__main__":
    typer.run(exercise_8)
