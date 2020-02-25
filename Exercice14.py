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