#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
       Spawns wait_random n times with the specified max_delay
        and returns the list of all the delays (float values).
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    completed_coroutines = asyncio.as_completed(coroutines)
    delays = [await coroutine for coroutine in completed_coroutines]
    return delays
