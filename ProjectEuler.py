import math, time
from math import *

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

############ EXERCICE 12 ############
def highly_divisible_triangular_number(n) :
    sum = 0
    i = 1
    factors = 0
    while factors != n+1 and factors < n+1:
        factors = 0
        sum += i
        i += 1
        for j in range(1, int(math.sqrt(sum+1))) :
            if sum % j == 0 : factors += 1
        if factors*2 > n+1 :
            return sum
            break

############ EXERCICE 13 ############
def large_sum() :
    numbers = 37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690
    numbers_list = [int(d) for d in str(numbers)]
    numbers_of_50digits = ""
    list_of_50digits = []
    counter = 0
    large_sum = 0
    res = ""
    for i in numbers_list :
        numbers_of_50digits += str(i)
        counter += 1
        if counter % 50 == 0 :
            numbers_of_50digits = int(numbers_of_50digits)
            list_of_50digits.append(numbers_of_50digits)
            numbers_of_50digits = ""
    for i in list_of_50digits :
        large_sum += i
    large_sum_list = [int(d) for d in str(large_sum)]
    for i in large_sum_list :
        res += str(i)
        if len(res) % 10 == 0 : break
    return res

############ EXERCICE 14 ############
def longest_Collatz_sequence(n) :
    largest_length = 0
    longest_collatz_sequence = 0
    for i in range(1, n) :
        number = i
        sequence = []
        while i != 1 :
            if i % 2 == 0 :
                i = i / 2
                sequence.append(i)
            else :
                i = 3 * i + 1
                sequence.append(i)
        if len(sequence) > largest_length :
            largest_length = len(sequence)
            longest_collatz_sequence = number
            #print(largest_length, longest_collatz_sequence)
    return longest_collatz_sequence

############ EXERCICE 15 ############
def lattice_paths(grid_size,k) :
    return factorial(2*grid_size) / (factorial(k) * factorial(2*grid_size - k))

############ EXERCICE 16 ############
def power_digit_sum(number, power) :
    number_at_power = number**power
    number_list = [int(d) for d in str(number_at_power)]
    digit_sum = 0
    for i in number_list :
        digit_sum += i
    return digit_sum

############ EXERCICE 17 ############
def number_letter_counts(n) :
    units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
              'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    others = ['hundred', 'thousand', 'and']
    count = 0
    for i in range(1, n+1) :
        number = [int(d) for d in str(i)]
        if len(number) == 4 : count += len(others[1]) + len(units[0])
        if len(number) == 3 :
            count += len(units[number[0]-1]) + len(others[0])
            if i % 100 != 0 : count += len(others[2])
            if number[1] == 0 and i % 100 != 0 :
                count += len(units[number[2]-1])
            if number[1] == 1 :
                count += len(units[number[2]+9])
            if number[1] > 1 :
                count += len(tens[number[1]-2])
                if number[-1] != 0 :
                    count += len(units[number[2]-1])
        if len(number) == 2  :
            if i < 20 :
                count += len(units[i-1])
            else :
                count += len(tens[number[0]-2])
                if number[-1] != 0 :
                    count += len(units[number[1]-1])
        if len(number) == 1 :
            count += len(units[i-1])
    return count

############ EXERCICE 18 ############
def maximum_path_sum_I(max_line) :
    triangle = "75 \
                 95 64 \
                 17 47 82 \
                 18 35 87 10 \
                 20 04 82 47 65 \
                 19 01 23 75 03 34 \
                 88 02 77 73 07 63 67 \
                 99 65 04 28 06 16 70 92 \
                 41 41 26 56 83 40 80 70 33 \
                 41 48 72 33 47 32 37 16 94 29 \
                 53 71 44 65 25 43 91 52 97 51 14 \
                 70 11 33 28 77 73 17 78 39 68 17 57 \
                 91 71 52 38 17 14 91 43 58 50 27 29 48 \
                 63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
                 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    triangle_list = [int(d) for d in triangle.split()]
    penultimate_line_first_index = 0
    # get the index of the first number of the penultimate line
    for i in range(1, max_line-1) :
        penultimate_line_first_index += i
    index = penultimate_line_first_index
    line_index = max_line - 1
    for j in range(1,max_line) :
        for i in range(line_index) :
            if triangle_list[index+i] + triangle_list[index+i + (line_index)] > triangle_list[index+i] + triangle_list[index+i + (line_index+1)]:
                triangle_list[index+i] = triangle_list[index+i] + triangle_list[index+i + (line_index)]
            else:
                triangle_list[index+i] = triangle_list[index+i] + triangle_list[index+i + (line_index+1)]
            #print(triangle_list[index+i])
        index -= (line_index-1)
        line_index -= 1
    return triangle_list[0]

############ EXERCICE 19 ############
#def counting_sundays() :

































