import pytest

from src.euler.exercises.exercise_3 import greatest_prime_factor, is_prime


@pytest.mark.parametrize("number,result", [(13, True), (10, False), (37, True)])
def test_is_prime(number: int, result: bool):
    assert is_prime(number) == result


@pytest.mark.parametrize("number,result", [(50, 5), (13195, 29), (600851475143, 6857)])
def test_exercise_3(number: int, result: int):
    assert greatest_prime_factor(number) == result
