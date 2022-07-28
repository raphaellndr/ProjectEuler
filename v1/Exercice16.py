"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

what is the sum of the digits of the number 2^1000?
"""


def power_digit_sum(number, power):
    """
    Function that returns the sum of the digit of 'number' to the power of 'power'.

    :param number: the number we want to raise to the power 'power'.
    :param power: the exponent.
    :return: the sum of the digit.
    """
    number_at_power = number**power
    number_list = [int(d) for d in str(number_at_power)]
    digit_sum = 0
    for i in number_list:
        digit_sum += i
    return digit_sum
