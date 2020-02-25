import math

############ EXERCICE 12 ############
def highly_divisible_triangular_number(n) :
    sum = 0
    i = 1
    factors = 0
    while factors != n+1 and factors < n+1:
        factors = 0
        sum += i
        i += 1
        for j in range(1, int(math.sqrt(sum+1))) :
            if sum % j == 0 : factors += 1
        if factors*2 > n+1 :
            return sum
            break