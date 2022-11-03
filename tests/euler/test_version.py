"""Euler version check."""

from src import euler


def test_version_info():
    """Euler version test."""
    assert euler.__version__ is not None
