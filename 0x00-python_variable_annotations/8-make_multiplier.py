#!/usr/bin/env python3
"""complex types functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """complex types functions"""
    def multiples(i: float) -> float:
        return i * multiplier
    return make_multiplier
