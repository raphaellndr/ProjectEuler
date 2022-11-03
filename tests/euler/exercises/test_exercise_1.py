import pytest

from src.euler.exercises.exercise_1 import sum_of_multiples


@pytest.mark.parametrize(
    "number,result",
    [
        (1, 0),
        (10, 23),
        (25, 143),
    ],
)
def test_exercise_1(number: int, result: int):
    mltp_sum: int = sum_of_multiples(number)
    assert mltp_sum == result
