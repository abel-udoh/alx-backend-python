#!/usr/bin/env python3
""" More involved type annotations """

from typing import Dict, TypeVar, Optional

K = TypeVar('K')  # Type variable for dictionary keys
V = TypeVar('V')  # Type variable for dictionary values

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely get a value from a dictionary by key, with an optional
    default value.

    Returns:
        V: The value associated with the key in the dictionary, or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
