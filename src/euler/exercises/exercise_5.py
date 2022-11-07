"""Exercise 5:

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers
from 1 to 20 ?
"""

import typer

from ._registry import exercise


def smallest_number() -> int:
    """Function that returns the smallest positive number that is evenly divisible by all
    numbers from 1 to 20.

    :return: smallest positive number evenly divisible.
    """
    number = 20
    while True:
        dividers = [20, 19, 18, 17, 16, 14, 13, 11]
        rest = int(sum(number % divider for divider in dividers))
        if rest == 0:
            return number
        number += 20


@exercise(name="exercise-5")
def exercise_5() -> None:
    """Exercise 5: smallest positive number that is evenly divisible by all
    numbers from 1 to 20.
    """
    result: int = smallest_number()
    print(result)


if __name__ == "__main__":
    typer.run(exercise_5)
