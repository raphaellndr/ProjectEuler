############ EXERCICE 1 ############
def multiples_of_3_and_5() :
    sum_of_multiples = 0
    for i in range(1000) :
        if i % 3 == 0 or i % 5 == 0 : sum_of_multiples += i
    return sum_of_multiples

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

############ EXERCICE 4 ############
def largest_palindrome() :
    largest_palindrome = 0
    for j in range(100,999) :
        for i in range(100,999) :
            product = i * j
            a = [int(d) for d in str(product)]
            b = a[::-1]
            if a == b :
                largest_palindrome = product
    return largest_palindrome

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

############ EXERCICE 6 ############
def sum_square_difference(n) :
    sum = 0
    sum_of_squares = 0
    for i in range(1, n+1) :
        sum += i
        sum_of_squares += i**2
    difference = sum**2 - sum_of_squares
    return difference

print(sum_square_difference(100))

















