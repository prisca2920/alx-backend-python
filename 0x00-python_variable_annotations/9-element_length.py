#!/usr/bin/env python3
""" duck type iterable obj"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck type iterable obj"""
    return [(i, len(i)) for i in lst]
