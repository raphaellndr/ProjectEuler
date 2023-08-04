"""Exercise 16:

2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 +8 = 26.

What is the sum of the digits of the number 2**100?
?
"""

import functools
import typer

from ._registry import exercise


def compute_sum_of_digits(exponent: int) -> int:
    """Computes the sum of the digits of 2**``exponent``.

    :param exponent: exponent of the number 2.
    :returns:
    """
    digits = [int(d) for d in str(2**exponent)]
    sum_of_digits = functools.reduce(lambda x, y: x + y, digits)
    return sum_of_digits


@exercise(name="exercise-16")
def exercise_16(exponent: int = typer.Option(2, help="Exponent of the number 2.")) -> None:
    """Exercise 15: Find the sum of the digits of 2 at the power of ``exponent``.

    :param exponent: exponent of the number 2.
    """
    sum_of_digits = compute_sum_of_digits(exponent)
    print(sum_of_digits)


if __name__ == "__main__":
    typer.run(exercise_16)
