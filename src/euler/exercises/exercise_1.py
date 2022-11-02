"""
Exercise 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import typer

from ._registry import exercise


@exercise(name="exercise-1")
def exercise_1(
    number: int = typer.Option(0, help="Highest number that can be a multiple of 3 or 5."),
) -> None:
    """
    Function that returns the sum of all the multiples of 3 or 5 below the
    parameter 'number'.

    :param number: the highest number that can be a multiple of 3 or 5.
    :return: sum of all the multiples.
    """
    sum_of_multiples: int = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    print(sum_of_multiples)


if __name__ == "__main__":
    typer.run(exercise_1)
