############ EXERCICE 5 ############
def smallest_number(n) :
    smallest_number = 0
    for i in range(n-10, n+10) :
        reste = 0
        for j in range(1,21) :
            reste = reste + i % j
        if reste == 0 and i > smallest_number :
            smallest_number = i
    return smallest_number