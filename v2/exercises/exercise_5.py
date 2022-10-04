"""
Exercise 5:

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20 ?
"""
import typer

subcommand = typer.Typer(help="")
app = typer.Typer(no_args_is_help=True)
app.add_typer(subcommand, name="")


@subcommand.command(help="")
def exercise_5() -> None:
    """
    Function that returns the smallest positive number that is evenly divisible by all
    numbers from 1 to 20.

    :param n:
    :return: smallest positive number evenly divisible.
    """
    n = 20
    while True:
        dividers = [20, 19, 18, 17, 16, 14, 13, 11]
        rest = int(sum([n % divider for divider in dividers]))
        if rest == 0:
            print(n)
            break
        n += 20


if __name__ == "__main__":
    typer.run(exercise_5)
