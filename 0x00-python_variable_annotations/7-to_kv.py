#!/usr/bin/env python3
""" Takes a string k and an int OR float, returns a tuple """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Tuple[str, float]: A tuple with the string k as the
        first element and the square of v as the second
        element (annotated as a float)
       """
    squared_value = float(v) ** 2
    return k, squared_value
