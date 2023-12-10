"""Exercise 15:

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import math
import typer

from ._registry import exercise


def compute_lattice_paths(grid_size: int) -> int:
    """Computes number of paths in the grid.

    :param grid_size: size of each side of the grid.
    :returns: number of paths.
    """
    nb_path = math.factorial(2 * grid_size) // (
        math.factorial(grid_size) * math.factorial(grid_size)
    )
    return nb_path


@exercise(name="exercise-15")
def exercise_15(grid_size: int = typer.Option(2, help="Size of the grid.")) -> None:
    """Exercise 15: Find how many routes there are in a grid of size ``grid_size``.

    :param grid_size: size of each side of the grid.
    """
    lattice_paths = compute_lattice_paths(grid_size)
    print(lattice_paths)


if __name__ == "__main__":
    typer.run(exercise_15)
