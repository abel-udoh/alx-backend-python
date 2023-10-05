#!/usr/bin/env python3
""" More involved type annotations """

from typing import Dict, TypeVar, Optional, Union, Mapping, Any

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
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
