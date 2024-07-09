#!/usr/bin/env python3
"""coroutine that takes no arg"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine that takes no arg"""
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
