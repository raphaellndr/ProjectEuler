from math import factorial

############ EXERCICE 15 ############
def lattice_paths(grid_size,k) :
    return factorial(2*grid_size) / (factorial(k) * factorial(2*grid_size - k))