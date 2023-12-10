"""Exercise 6:

The sum of the squares of the first ten natural numbers is, 1²+2²+...+10²=385.

The square of the sum of the first ten natural numbers is, (1+2+...+10)²=55²=3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the
square of the sum.
"""

import operator
from functools import reduce

import typer

from ._registry import exercise


def sum_of_squares(limit: int) -> int:
    """Computes the sum of squares until reaching the given limit.

    :param limit: last square added.
    :return: sum of squares.
    """
    return reduce(operator.add, [x * x for x in list(range(1, limit + 1))])


def square_of_sum(limit: int) -> int:
    """Computes the square of the sum until reaching the given limit.

    :param limit: last number added to the sum.
    :return: square of the sum.
    """
    return sum(list(range(1, limit + 1))) ** 2


@exercise(name="exercise-6")
def exercise_6(
    limit: int = typer.Option(1, help="Natural number where we want to stop the sum."),
) -> None:
    """Exercise 6: difference between the sum of the squares and the square of the sum, from one to
    'limit'.

    :param limit: the natural number where we want to stop the sum.
    """
    print(square_of_sum(limit) - sum_of_squares(limit))


if __name__ == "__main__":
    typer.run(exercise_6)
