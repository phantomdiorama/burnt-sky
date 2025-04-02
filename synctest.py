#!/usr/bin/env python3
# duggee.py

import httpx
import uuid
import asyncio
import feedparser
#########################
# sync stuff
#########################

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)

urls = []
blusers = []

with open("users.txt") as file:
    for line in file:
        short_line = line.split(" ")
        urls.append(short_line[1].strip())

async def launch():
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp for resp in resps]
    for html in data:
        print(html)
        blusers.append(html)
        # filename = str(uuid.uuid4())
        # with open(dump_path / filename, "w") as f:
        #     f.write(html)

asyncio.run(launch())

for i in blusers:
    d = feedparser.parse(i)
    k = d.feed.title
    print(k)
#########################
#########################
