"""Euler version check."""

from src import euler


def test_version() -> None:
    """Euler version test."""
    assert euler.__version__ is not None


def test_program_name() -> None:
    assert euler.PROGRAM_NAME is not None
