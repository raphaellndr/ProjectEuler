"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(n):
    """
    Function that returns the Pythagorean triplet for which a+b+c=n.

    :param n: the value we want to be equal to.
    :return: the triplet and the product of the 3 numbers.
    """
    for a in range(0, n):
        for b in range(a + 1, n):
            ab = a**2 + b**2
            for c in range(b + 1, n):
                if c**2 == ab and a + b + c == n:
                    return "the triplet is : " + str(a) + ", " + str(b) + ", " + str(
                        c
                    ), "and the product made by this triplet is : " + str(a * b * c)
                    break
