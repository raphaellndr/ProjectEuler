"""Exercise decorator."""

from typing import Callable, MutableMapping, Optional

EXERCISES_REGISTRY: MutableMapping[str, Callable] = {}


def exercise(func: Optional[Callable] = None, *, name: Optional[str] = None) -> Callable:
    """

    :param func:
    :param name:
    :return:
    """

    def _decorator(target: Callable) -> Callable:
        nonlocal name

        name = name or target.__name__
        EXERCISES_REGISTRY[name] = target
        return target

    if func is not None:
        return _decorator(func)
    return _decorator


__all__ = ["EXERCISES_REGISTRY", "exercise"]
