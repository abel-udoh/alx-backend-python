#!/usr/bin/env python3
""" More involved type annotations """
from typing import Any, Union, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
