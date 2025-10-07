import asyncio
from project.generator_load import start_generator_load
from my import MY_URL

URL = MY_URL

if __name__ == "__main__":
    asyncio.run(start_generator_load(URL, total=300, concurrency=50))
