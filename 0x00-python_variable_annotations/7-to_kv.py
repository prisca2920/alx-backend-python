#!/usr/bin/env python3
"""complex types returned"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """complex types returned"""
    return (k, v * v)
