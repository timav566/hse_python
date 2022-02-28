#!/usr/bin/env python

import aiohttp
import asyncio


def get_img_url(name):
    return "https://this" + str(name) + "doesnotexist.com/"


def get_file_name(name):
    return "artifacts/" + str(name) + ".png"


async def download_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def download_and_write_file(name):
    content = await download_content(get_img_url(name))
    with open(get_file_name(name), 'wb') as f:
        f.write(content)


async def main():
    file_urls = open("urls.txt", 'r')
    urls = [s[:-1] for s in file_urls.readlines()]
    file_urls.close()
    tasks = map(download_and_write_file, urls)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
