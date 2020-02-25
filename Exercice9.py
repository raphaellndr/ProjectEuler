############ EXERCICE 9 ############
def pythagorean_triplet(n) :
    for a in range(0, n) :
        for b in range(a+1, n) :
            ab = a**2 + b**2
            for c in range(b+1, n) :
                if c**2 == ab and a + b + c == n :
                    return a, b, c
                    break