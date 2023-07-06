"""Exercise 11:

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right,
or diagonally) in the 20×20 grid?
"""

import functools
from pathlib import Path

import numpy as np
import typer

from ._registry import exercise

PRODUCT_GRID = Path(__file__).parent.parent.parent.parent / "data/product_grid.txt"


def process_data() -> np.ndarray:
    """Processes the data needed for the exercise.

    :returns: ``numpy.ndarray`` containing processed data.
    """
    with open(PRODUCT_GRID, encoding="utf-8") as stream:
        split_data = stream.read().split("\n")
    data = [line.split(" ") for line in split_data]
    int_data = [[int(number) for number in line] for line in data]
    array_data = np.asarray(int_data)
    return array_data


def get_largest_product(data: np.ndarray, nb_adjacent_digits: int) -> int:
    """Computes products in every direction in the grid.

    :param data: ``np.ndarray`` containing processed data
    :param nb_adjacent_digits: number of adjacent numbers to compute products from.
    :returns: largest products amongst every direction.
    """
    transposed_data = data.transpose()
    horizontally_flipped_data = np.flip(data, 0)

    product = 0
    for i in range(len(data) - nb_adjacent_digits + 1):
        for j in range(len(data) - nb_adjacent_digits + 1):
            # compute horizontal product
            horizontal_product: int = functools.reduce(
                lambda x, y: x * y, data[i][j : j + nb_adjacent_digits]
            )
            # compute vertical product
            vertical_product: int = functools.reduce(
                lambda x, y: x * y, transposed_data[i][j : j + nb_adjacent_digits]
            )
            # compute diagonal products
            downwards_diagonal_digits: list[int] = [
                data[i + k][j + k] for k in range(nb_adjacent_digits)
            ]
            downwards_diagonal_product = functools.reduce(
                lambda x, y: x * y, downwards_diagonal_digits
            )
            upwards_diagonal_digits: list[int] = [
                horizontally_flipped_data[i + k][j + k] for k in range(nb_adjacent_digits)
            ]
            upwards_diagonal_product = functools.reduce(lambda x, y: x * y, upwards_diagonal_digits)

            product = max(
                product,
                horizontal_product,
                vertical_product,
                downwards_diagonal_product,
                upwards_diagonal_product,
            )

    return product


@exercise(name="exercise-11")
def exercise_11(
    nb_adjacent_digits: int = typer.Option(1, help=""),
) -> None:
    """Exercise 11: Greatest product of four adjacent numbers in the same direction in the grid.

    :param nb_adjacent_digits: .
    """
    data = process_data()
    diagonal_product = get_largest_product(data, nb_adjacent_digits)
    print(diagonal_product)


if __name__ == "__main__":
    typer.run(exercise_11)
