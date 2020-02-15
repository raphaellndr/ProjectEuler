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

############ EXERCICE 11 ############
def largest_product() :
    grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    grid_list = [int(i) for i in grid.split()]
    products = []
    for i in range(400) :
        if i % 20 < 17 :
            products.append(grid_list[i] * grid_list[i+1] * grid_list[i+2] * grid_list[i+3])
        if i < 340 :
            products.append(grid_list[i] * grid_list[i+20] * grid_list[i+40] * grid_list[i+60])
        if i % 20 < 17 and i < 340 :
            products.append(grid_list[i] * grid_list[i + 21] * grid_list[i + 42] * grid_list[i + 63])
        if i % 20 > 3 and i < 340 :
            products.append(grid_list[i] * grid_list[i + 19] * grid_list[i + 38] * grid_list[i + 57])
    return max(products)



































