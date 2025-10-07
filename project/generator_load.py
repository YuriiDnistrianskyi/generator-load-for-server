import aiohttp
import asyncio
import time
import statistics

async def do_request(session, url, timeout=10):
    start = time.perf_counter()
    try:
        async with session.get(url, timeout=timeout) as response:
            await response.text()
            elapsed = time.perf_counter() - start
            return elapsed, response.status, None
    except Exception as ex:
        return time.perf_counter() - start, None, str(ex)

async def start_generator_load(url, total=100, concurrency=10):
    latencies = []
    errors = []
    semaphore = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession() as session:
        async def worker():
            async with semaphore:
                elapsed_time, status, error = await do_request(session, url)
                latencies.append(elapsed_time)
                if error or (status and status >= 400):
                    errors.append((status, error))

        tasks = [asyncio.create_task(worker()) for _ in range(total)]
        start = time.perf_counter()
        await asyncio.gather(*tasks)
        total_time = time.perf_counter() - start

    print("Done")
    print("Total: ", total_time, "Done: ", len(latencies), "Errors: ", len(errors))
    print("Avg: ", statistics.mean(latencies))
    print("")
