#!/usr/bin/env python3
""" Annotates the below function’s parameters """

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains a string from the input list and its
        corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
