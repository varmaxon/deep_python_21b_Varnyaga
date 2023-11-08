import os
import time
import argparse
from collections import Counter
import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup


class Fetcher:
    """Fetcher Class for async fetch urls"""

    num_check = 0
    status_OK = 200

    def __init__(self, n_workers, file_name, k_top=5):
        if n_workers < 1:
            raise ValueError("Workers number must be greater than 1")

        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"File {file_name} not found")

        self.n_workers = n_workers
        self.file_name = file_name
        self.k_top = k_top

    def _find_frequent_words(self, str_words):
        return Counter(str_words.split()).most_common(self.k_top)

    async def _get_url_info(self, response):
        text = await response.text()
        str_words = BeautifulSoup(text, 'html.parser').get_text()
        return self._find_frequent_words(str_words)

    async def fetch_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == self.status_OK:
                    result = await self._get_url_info(resp)
                    print(self.num_check, result)
                    self.num_check += 1

                else:
                    raise Exception("failed to connect")

    async def fetch_worker(self, que):
        while True:
            url = await que.get()
            try:
                await self.fetch_url(url)

            finally:
                que.task_done()

    async def batch_fetch(self):
        que = asyncio.Queue(maxsize=self.n_workers * 2)

        workers = [
            asyncio.create_task(self.fetch_worker(que))
            for _ in range(self.n_workers)
        ]

        async with aiofiles.open(self.file_name,
                                 mode='r',
                                 encoding='UTF-8') as file:
            async for line in file:
                await que.put(line)

        await que.join()

        for worker in workers:
            worker.cancel()

    def run(self):

        start = time.time()
        asyncio.get_event_loop().run_until_complete(self.batch_fetch())
        end = time.time()

        print("Timing:", end - start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse input string')
    parser.add_argument("-c", type=int, default=10)
    parser.add_argument("-filename", type=str, default="random_urls.txt")
    args = parser.parse_args()
    fetcher = Fetcher(args.c, args.filename)
    fetcher.run()
