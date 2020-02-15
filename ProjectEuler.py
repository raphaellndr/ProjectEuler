import math

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

############ EXERCICE 8 ############
def largest_product(n) :
    thousand_digits = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    thousand_digits_list = [int(d) for d in str(thousand_digits)]
    greatest_product = 0
    for i in range(0, len(thousand_digits_list)-n) :
        product = 1
        for j in range(i, i+n) :
            product *= thousand_digits_list[j]
            if product > greatest_product : greatest_product = product
    return greatest_product

############ EXERCICE 9 ############
def pythagorean_triplet(n) :
    for a in range(0, n) :
        for b in range(a+1, n) :
            ab = a**2 + b**2
            for c in range(b+1, n) :
                if c**2 == ab and a + b + c == n :
                    return a, b, c
                    break

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

############ EXERCICE 10 ############




































