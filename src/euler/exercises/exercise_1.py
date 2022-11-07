"""Exercise 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import typer

from ._registry import exercise


def sum_of_multiples(number: int) -> int:
    """Function that returns the sum of all the multiples of 3 or 5 below the
    parameter 'number'.

    :param number: the highest number that can be a multiple of 3 or 5.
    :return: sum of all the multiples.
    """
    mltp_sum: int = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            mltp_sum += i
    return mltp_sum


@exercise(name="exercise-1")
def exercise_1(
    number: int = typer.Option(0, help="Highest number that can be a multiple of 3 or 5."),
) -> None:
    """Exercise 1: sum of all the multiples of 3 or 5 below the parameter 'number'.

    :param number: the highest number that can be a multiple of 3 or 5.
    """
    result: int = sum_of_multiples(number)
    print(result)


if __name__ == "__main__":
    typer.run(exercise_1)
