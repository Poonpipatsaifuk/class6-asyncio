import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Use asyncio.gather to run two coroutines concurrently:
    await asyncio.gather(
        print_after("world!", 2),
        print_after("Hello", 1)
    )

    asyncio.run(main())
