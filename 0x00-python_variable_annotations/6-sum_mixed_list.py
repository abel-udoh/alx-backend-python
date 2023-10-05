#!/usr/bin/env python3
""" Takes list input of of integers and floats, returns float """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
