import aiohttp
import asyncio
import time


def spider(base_url,not_found_text):
    urls = []
    if base_url[-1] != '/': base_url += '/'  #append "/" to the end of the base url
    print('finding interesting files...')
    with open('common.txt','r') as wordlist:
        for w in wordlist:
            word = w[:-1]
            url = base_url + word
            urls.append(url)

    async def get_url(session, url):
        async with session.get(url) as resp:
            resp_text = await resp.text()
            if not_found_text not in resp_text :
                print('find this url, might be interesting:  '+ url)

    async def main():

        async with aiohttp.ClientSession() as session:

            tasks = []
            for url in urls:
                tasks.append(asyncio.ensure_future(get_url(session, url)))

            original_request = await asyncio.gather(*tasks)

    asyncio.run(main())




