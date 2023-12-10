import pytest

from src.euler.exercises.exercise_8 import greatest_product


@pytest.mark.parametrize(
    "limit,result",
    [
        (1, 9),
        (2, 81),
        (4, 5832),
    ],
)
def test_exercise_8(limit: int, result: list[int]):
    assert greatest_product(limit) == result
