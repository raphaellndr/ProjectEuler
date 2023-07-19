"""Exercise 14:

The following iterative sequence is defined for the set of positive integers:
    n -> n / 2 (n is even)
    n -> 3 * n + 1 (n is odd)

Using the rule above and starting with, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although
it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from typing import NamedTuple

import typer

from ._registry import exercise


class CollatzNumber(NamedTuple):
    """Defines a tuple containing a number and its chain length."""

    number: int
    chain_length: int


def apply_collatz_rules(number: int) -> int:
    """Applies Collatz rules to given number until it becomes one and stores its chain length

    :param number: number to apply rules on.
    :returns: chain length.
    """
    chain_length = 1
    while number != 1:
        chain_length += 1
        if number % 2 == 0:
            number = number // 2
            continue
        number = 3 * number + 1
    return chain_length


@exercise(name="exercise-14")
def exercise_14() -> None:
    """Exercise 14: Find which number, under one million, produces the longest chain."""
    max_ = CollatzNumber(number=1, chain_length=1)
    for number in range(2, 1000000):
        chain_length = apply_collatz_rules(number)
        if max_.chain_length < chain_length:
            max_ = CollatzNumber(number=number, chain_length=chain_length)
    print(max_)


if __name__ == "__main__":
    typer.run(exercise_14)
