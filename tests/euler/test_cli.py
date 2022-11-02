"""Cli tests."""

from subprocess import PIPE, run


def test_help():
    res = run(["euler", "--help"], stdout=PIPE, stderr=PIPE)
    assert res.returncode == 0
    assert res.stdout.startswith(b"Usage: euler [OPTIONS] COMMAND [ARGS]...")
