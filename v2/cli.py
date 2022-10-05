"""
Command line interface entry point
"""

import typer

from .exercises import EXERCISES_REGISTRY


def run() -> None:
    app = typer.Typer(no_args_is_help=True)
    for name, exercise in EXERCISES_REGISTRY.items():
        app.command(name=name)(exercise)

    app()
