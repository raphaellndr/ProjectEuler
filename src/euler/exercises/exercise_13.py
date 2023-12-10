"""Exercise 13:

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

[...]
"""

from functools import reduce
from pathlib import Path

import typer

from ._registry import exercise

_100_50_DIGITS = Path(__file__).parent.parent.parent.parent / "data" / "_100_50_digits_numbers.txt"


def process_data() -> list[int]:
    """Processes the data needed for the exercise.

    :returns: list containing all 50 digits numbers.
    """
    with open(_100_50_DIGITS, encoding="utf-8") as stream:
        split_data = stream.read().split("\n")
    data = [int(digits) for digits in split_data]
    return data


@exercise(name="exercise-13")
def exercise_13() -> None:
    """Exercise 13: Value of the first triangle number to have over five hundred divisors."""
    data = process_data()
    sum_ = reduce(lambda x, y: x + y, data)
    first_ten_digits = str(sum_)[:9]
    print(first_ten_digits)


if __name__ == "__main__":
    typer.run(exercise_13)
