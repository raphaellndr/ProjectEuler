import pytest

from src.euler.exercises.exercise_6 import square_of_sum, sum_of_squares


@pytest.mark.parametrize("limit,result", [(10, 2640), (100, 25164150)])
def test_exercise_6(limit: int, result: int):
    assert square_of_sum(limit) - sum_of_squares(limit) == result
