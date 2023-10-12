#!/usr/bin/env python3
""" Import async_comprehension from the previous file
    and write a measure_runtime coroutine that will execute
    async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the total runtime and return it
    """
    i = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for x in range(4)]
    await asyncio.gather(*task)
    elapsed = perf_counter() - i
    return elapsed
