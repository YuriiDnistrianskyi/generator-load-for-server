import asyncio
from project.generator_load import start_generarur_load
from my import url

if __name__ == "__main__":
    asyncio.run(start_generarur_load(url, total=200, concurrency=50))
