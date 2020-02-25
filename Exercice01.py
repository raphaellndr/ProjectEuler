############ EXERCICE 1 ############
def multiples_of_3_and_5() :
    sum_of_multiples = 0
    for i in range(1000) :
        if i % 3 == 0 or i % 5 == 0 : sum_of_multiples += i
    return sum_of_multiples