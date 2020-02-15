def multiples_of_3_and_5() :
    sum_of_multiples = 0
    for i in range(1000) :
        if i % 3 == 0 or i % 5 == 0 : sum_of_multiples += i
    return sum_of_multiples


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


def smallest_number(n) :
    smallest_number = 0
    for i in range(n-10, n+10) :
        reste = 0
        for j in range(1,21) :
            reste = reste + i % j
        if reste == 0 and i > smallest_number :
            smallest_number = i
    return smallest_number
