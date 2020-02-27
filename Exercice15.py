from math import factorial

############ EXERCICE 15 ############


"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""


def lattice_paths(grid_size, k):
    """
    Function that returns the number of routes in a 'grid_size' grid.

    :param grid_size: size of the grid.
    :param k:
    :return: number of routes in the grid.
    """
    return factorial(2 * grid_size) / (factorial(k) * factorial(2 * grid_size - k))
