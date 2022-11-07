import pytest

from src.euler.exercises.exercise_7 import sieve_of_eratosthenes, upper_bound


@pytest.mark.parametrize(
    "limit,result",
    [(6, [2, 3, 5, 7, 11, 13]), (15, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])],
)
def test_exercise_7(limit: int, result: list[int]):
    upp_bound: int = upper_bound(limit)
    assert sieve_of_eratosthenes(upp_bound)[:limit] == result
