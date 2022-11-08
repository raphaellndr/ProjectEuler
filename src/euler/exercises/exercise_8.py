"""Exercise 8:

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 =
5832.

[...]

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is
the value of this product?
"""

import operator
from functools import reduce
from typing import List

import typer

from ._registry import exercise


def greatest_product(n_digits: int):
    """Function that returns the greatest product made by n adjacent digits.

    :param n_digits: number of adjacent digits.
    :return: greatest product.
    """
    with open("src/euler/data/thousand_digits.txt", "r", encoding="utf-8") as file:
        thousand_digits: str = file.read()

    thousand_digits_list: List[int] = [int(d) for d in thousand_digits]

    sliced_list: List[List[int]] = [
        thousand_digits_list[i : i + n_digits]
        for i in range(0, len(thousand_digits_list) - n_digits)
    ]

    max_product: int = 0
    for l_slice in sliced_list:
        product: int = reduce(operator.mul, l_slice)

        if product == 9**n_digits:
            return product

        max_product = max(max_product, product)

    return max_product


@exercise(name="exercise-8")
def exercise_8(
    n_digits: int = typer.Option(1, help="Number of adjacent digits"),
) -> None:
    """Exercise 8: greatest product made by n adjacent digits.

    :param n_digits: number of adjacent digits.
    """
    result: int = greatest_product(n_digits)
    print(result)


if __name__ == "__main__":
    typer.run(exercise_8)
