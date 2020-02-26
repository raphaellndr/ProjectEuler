############ EXERCICE 14 ############


"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def longest_Collatz_sequence(n):
    """
    Function that return the longest sequence made by a starting number under n.

    :param n: limit of the starting number.
    :return: starting number and length of the sequence
    """
    largest_length = 0
    longest_collatz_sequence = 0
    for i in range(1, n):
        number = i
        sequence = []
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                sequence.append(i)
            else:
                i = 3 * i + 1
                sequence.append(i)
        if len(sequence) > largest_length:
            largest_length = len(sequence)
            longest_collatz_sequence = number
            # print(largest_length, longest_collatz_sequence)
    return "the starting number is : " + str(longest_collatz_sequence) + "and his associated length is " \
           + str(largest_length)
