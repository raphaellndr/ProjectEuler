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