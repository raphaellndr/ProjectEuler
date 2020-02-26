############ EXERCICE 17 ############


"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?
"""


def number_letter_counts(n):
    """
    
    :param n:
    :return:
    """
    units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
             'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    others = ['hundred', 'thousand', 'and']
    count = 0
    for i in range(1, n + 1):
        number = [int(d) for d in str(i)]
        if len(number) == 4: count += len(others[1]) + len(units[0])
        if len(number) == 3:
            count += len(units[number[0] - 1]) + len(others[0])
            if i % 100 != 0: count += len(others[2])
            if number[1] == 0 and i % 100 != 0:
                count += len(units[number[2] - 1])
            if number[1] == 1:
                count += len(units[number[2] + 9])
            if number[1] > 1:
                count += len(tens[number[1] - 2])
                if number[-1] != 0:
                    count += len(units[number[2] - 1])
        if len(number) == 2:
            if i < 20:
                count += len(units[i - 1])
            else:
                count += len(tens[number[0] - 2])
                if number[-1] != 0:
                    count += len(units[number[1] - 1])
        if len(number) == 1:
            count += len(units[i - 1])
    return count
