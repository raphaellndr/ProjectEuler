import pytest

from src.euler.exercises.exercise_2 import fibo_sum


@pytest.mark.parametrize(
    "limit,result",
    [
        (100, 44),
        (4000000, 4613732),
    ],
)
def test_exercise_2(limit: int, result: int):
    assert fibo_sum(limit) == result
