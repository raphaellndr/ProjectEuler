"""Import all exercises."""

import importlib
import re
from pathlib import Path

from ._registry import EXERCISES_REGISTRY

EXERCISE_PATTERN = re.compile(r"exercise_[0-9]+")

__all__ = ["EXERCISES_REGISTRY"]


for module in Path(__file__).parent.iterdir():
    if not module.is_file():
        continue

    module_name: str = str(module.stem)
    if not EXERCISE_PATTERN.fullmatch(module_name):
        continue

    importlib.import_module(f"euler.exercises.{module_name}")
    __all__.append(module_name)
