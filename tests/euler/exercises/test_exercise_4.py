import pytest

from src.euler.exercises.exercise_4 import greatest_palindromic_product


@pytest.mark.parametrize(
    "length,result",
    [
        (2, 9009),
        (3, 906609),
    ],
)
def test_exercise_4(length: int, result: int):
    assert greatest_palindromic_product(length) == result
