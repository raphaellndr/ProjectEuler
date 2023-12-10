"""Exercise 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

import itertools
from typing import NamedTuple, Optional

import typer

from ._registry import exercise


class Triplet(NamedTuple):
    """Definition of a triplet."""

    a: int
    b: int
    c: int


def _pythagorean_triplet(triplet: Triplet) -> bool:
    """Returns True if given triplet is Pythagorean.

    :param triplet: triplet to evaluate.
    :return: boolean.
    """
    if not triplet.a < triplet.b < triplet.c:
        return False
    if triplet.a**2 + triplet.b**2 == triplet.c**2:
        return True
    return False


def _sum_of_triplet(triplet: Triplet) -> int:
    """ """
    return triplet.a + triplet.b + triplet.c


def _find_triplet(goal: int) -> Optional[Triplet]:
    """Function that returns the Pythagorean triplet for which a+b+c=goal.

    :param goal: the value we want to be equal to.
    :return: the triplet and the product of the 3 numbers.
    """
    for couple in itertools.combinations(range(goal), 2):
        triplet = Triplet(couple[0], couple[1], goal - (sum(couple)))

        if _pythagorean_triplet(triplet):
            if _sum_of_triplet(triplet) == goal:
                return triplet
    return None


@exercise(name="exercise-9")
def exercise_9(
    goal: int = typer.Option(0, help="The value we want to be equal to."),
) -> None:
    """Exercise 9: Pythagorean triplet for which a+b+c=goal.

    :param goal: the value we want to be equal to.
    """
    triplet = _find_triplet(goal)
    if triplet is not None:
        print(triplet)
        print(triplet.a * triplet.b * triplet.c)


if __name__ == "__main__":
    typer.run(exercise_9)
