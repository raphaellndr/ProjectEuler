"""Cli tests."""

from subprocess import PIPE, run


def test_help() -> None:
    res = run(["euler", "--help"], stdout=PIPE, stderr=PIPE, shell=True)
    assert res.returncode == 0
    assert res.stdout.startswith(b"Usage: euler [OPTIONS] COMMAND [ARGS]...")
