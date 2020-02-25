############ EXERCICE 6 ############
def sum_square_difference(n) :
    sum = 0
    sum_of_squares = 0
    for i in range(1, n+1) :
        sum += i
        sum_of_squares += i**2
    difference = sum**2 - sum_of_squares
    return difference