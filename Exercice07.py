############ EXERCICE 7 ############
def find_prime_number(n):
    a = 1
    n_prime = 2
    i = 3
    def is_prime(k) :
        for j in range(2, k) :
            if k % j == 0 : return False
        return True
    while (a < n) :
        if is_prime(i) :
            a += 1
            n_prime = i
        i += 1
    return n_prime