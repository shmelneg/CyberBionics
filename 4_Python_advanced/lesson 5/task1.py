import aiohttp
import asyncio
from urllib import request
import time

urls = ['https://jsonplaceholder.typicode.com/', 'https://jsonplaceholder.typicode.com/',
        'https://jsonplaceholder.typicode.com/', 'https://jsonplaceholder.typicode.com/',
        'https://jsonplaceholder.typicode.com/', 'https://jsonplaceholder.typicode.com/']


async def request_aiohttp(session, url):
    async with session.get(url) as response:
        return await response.text()


async def test_aiohttp(urls):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            response = await request_aiohttp(session, url)


start = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_aiohttp(urls))
loop.close()

print("Elapsed Time aiohttp (with asyncio): %s" % (time.time() - start))


start = time.time()

for url in urls:
    response = request.urlopen(url)

print("Elapsed Time URLLib (without concurrency): %s" % (time.time() - start))
