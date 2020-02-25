import math

############ EXERCICE 10 ############
def summation_of_prime(n) :
    sum_of_primes = 0
    def is_prime(k) :
        for j in range(2, int(math.sqrt(k))+1) :
            if k % j == 0 : return False
        return True
    for i in range(2, n) :
        if is_prime(i) : sum_of_primes += i
    return sum_of_primes