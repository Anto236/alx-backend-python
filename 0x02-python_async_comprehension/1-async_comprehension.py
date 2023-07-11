#!/usr/bin/env python3
"""Generates a list from an async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over the async_generator coroutine and returns the list of numbers.
    """
    return [_ async for _ in async_generator()]
