"""
Exercise 6:

The sum of the squares of the first ten natural numbers is, 1²+2²+...+10²=385.

The square of the sum of the first ten natural numbers is, (1+2+...+10)²=55²=3025.

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
import operator
from functools import reduce

import typer

subcommand = typer.Typer(help="")
app = typer.Typer(no_args_is_help=True)
app.add_typer(subcommand, name="")


@subcommand.command(help="")
def exercise_6(
    limit: int = typer.Option(0, help="Natural number where we want to stop the sum."),
) -> None:
    """
    Function that returns the difference between the sum of the squares and the
    square of the sum, from one to 'limit'.

    :param limit: the natural number where we want to stop the sum.
    :return: the difference.
    """
    sum_of_the_squares = reduce(operator.add, [x * x for x in list(range(1, limit + 1))])

    square_of_the_sum = sum(list(range(1, limit + 1))) ** 2

    print(square_of_the_sum - sum_of_the_squares)


if __name__ == "__main__":
    typer.run(exercise_6)
