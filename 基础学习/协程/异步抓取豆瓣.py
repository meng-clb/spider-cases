import asyncio
import time
import aiohttp
import requests
from lxml import etree
import aiofiles

headers = {
	'Referer': 'https://movie.douban.com/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

url = 'https://movie.douban.com/chart'


async def get_detail_url():
	async with aiohttp.ClientSession(headers=headers) as session:
		async with session.get(url) as resp:
			text = await resp.text()
			html = etree.HTML(text)
			url_list = html.xpath(
				'//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
	return url_list


async def get_title(detail_url):
	async with aiohttp.ClientSession(headers=headers) as session:
		async with session.get(detail_url) as resp:
			text = await resp.text()
			html = etree.HTML(text)
			title = html.xpath('//h1//text()')
			title = ''.join(title).replace('\n', '').strip()
		# print(title)
		return title


if __name__ == '__main__':
	t1 = time.time()
	# 新版的写法
	url_list = asyncio.run(get_detail_url())
	tasks = [get_title(url) for url in url_list]
	asyncio.run(asyncio.wait(tasks))

	"""
	# 老版本, 兼容性的写法
	loop = asyncio.get_event_loop()
	url_list = loop.run_until_complete(get_detail_url())
	tasks = [get_title(url) for url in url_list]
	loop.run_until_complete(asyncio.gather(*tasks))
	"""

	print(time.time() - t1)
