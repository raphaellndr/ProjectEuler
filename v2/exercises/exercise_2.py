"""
Exercise 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

import typer

from typing import List

subcommand = typer.Typer(help="")
app = typer.Typer(no_args_is_help=True)
app.add_typer(subcommand, name="")


@subcommand.command(help="")
def exercise_2(
    limit: int = typer.Option(
        2, help="Highest number that can be a multiple of 3 or 5."
    ),
) -> None:
    """
    Function that returns the sum of the even-valued terms in the Fibonacci sequence
    that are lower than the limit.

    :param limit: value that can't be exceeded by the Fibonacci sequence's terms.
    :return: sum of even-valued terms.
    """
    fibo: List = [1, 2]
    while True:
        next_fibo: int = sum(fibo[-2:])
        if next_fibo >= limit:
            print(sum([i for i in fibo if i % 2 == 0]))
        fibo.append(next_fibo)


if __name__ == "__main__":
    typer.run(exercise_2)
