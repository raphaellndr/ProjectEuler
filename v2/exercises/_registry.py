from typing import Callable, MutableMapping

EXERCISES_REGISTRY: MutableMapping[str, Callable] = {}


def exercise(func: Callable = None, *, name: str = None) -> Callable:
    def _decorator(target: Callable) -> Callable:
        nonlocal name

        name = name or target.__name__
        EXERCISES_REGISTRY[name] = target
        return target

    if func is not None:
        return _decorator(func)
    return _decorator


__all__ = ["EXERCISES_REGISTRY", "exercise"]
