############ EXERCICE 2 ############
def fibonacci(n) :
    sum_even_numbers = 0
    n_minus_2 = 1  # first number
    n_minus_1 = 2  # second number
    for i in range(n) :
        fibo = n_minus_2 + n_minus_1
        if fibo % 2 == 0 and sum_even_numbers <= 4000000:
            sum_even_numbers += fibo
        n_minus_2 = n_minus_1
        n_minus_1 = fibo
    return sum_even_numbers + 2 # because of the first term