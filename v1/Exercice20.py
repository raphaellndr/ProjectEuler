"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial_digit_sum(number):
    """
    Function that returns the sum of the digit of a factorial number.

    :param number: factorial number.
    :return: sum of the digit
    """

    def factorial(n):
        facto = 1
        for j in range(1, n + 1):
            facto *= j
        return facto

    factorial = factorial(number)
    factorial_digit = [int(d) for d in str(factorial)]
    sum = 0
    for i in range(len(factorial_digit)):
        sum += factorial_digit[i]
    return sum


print(factorial_digit_sum(100))
