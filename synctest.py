#!/usr/bin/env python3
# duggee.py

import uuid
import httpx
import asyncio

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = []

with open("users.txt") as file:
    for line in file:
        short_line = line.split(" ")
        urls.append(short_line[1].strip())

async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.text for resp in resps]
    for html in data:
        print(html)
        filename = str(uuid.uuid4())
        with open(filename, "w") as f:
            f.write(html)

asyncio.run(launch())
