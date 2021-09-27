import aiohttp
import asyncio
import time
import requests
from difflib import SequenceMatcher


def spider(base_url,):
    urls = []
    if base_url[-1] != '/': base_url += '/'  #append "/" to the end of the base url

    not_found = requests.get(base_url+"something_that_shows_this_is_a_not_found_page")
    not_found_text = not_found.text

    print('finding interesting files...')
    with open('common.txt','r') as wordlist:
        for w in wordlist:
            word = w[:-1]
            url = base_url + word
            urls.append(url)

    async def get_url(session, url):
        async with session.get(url) as resp:
            resp_text = await resp.text()
            if SequenceMatcher(None, not_found_text, resp_text).ratio() < 0.9 :
                print('found this url, might be interesting:  '+ url)

    async def main():

        async with aiohttp.ClientSession() as session:

            tasks = []
            for url in urls:
                tasks.append(asyncio.ensure_future(get_url(session, url)))

            original_request = await asyncio.gather(*tasks)

    asyncio.run(main())




