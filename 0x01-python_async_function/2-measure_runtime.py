#!/usr/bin/env python3
"""measuring the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()

    total_time = stop - start
    return (total_time/n)
