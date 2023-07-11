#!/usr/bin/rnv python3
"""Creates a generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Each time asynchronously waits 1 second,
       then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
