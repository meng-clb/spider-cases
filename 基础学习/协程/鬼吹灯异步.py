import asyncio
import os.path
import re

import aiofiles
import requests
from lxml import etree
import aiohttp

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


async def get_book_url():
	url = 'https://www.51shucheng.net/daomu/guichuideng'
	async with aiohttp.ClientSession(headers=headers) as session:
		async with session.get(url) as resp:
			html = await resp.text(encoding='utf-8')
			html = etree.HTML(html)
			book_url = html.xpath('//div[@class="sbut"]/a/@href')
	return book_url


async def get_chapter_url(url):
	async with aiohttp.ClientSession(headers=headers) as session:
		async with session.get(url) as resp:
			book = {}
			html = await resp.text(encoding='utf-8')
			html = etree.HTML(html)
			book_name = html.xpath('//div[@class="mulu-title"][1]/h2/text()')[0]
			book_name = book_name.replace(' ', '_')
			book['name'] = book_name
			# print(book_name)
			chapter_url_list = html.xpath('//div[@class="mulu-list"]/ul/li/a/@href')
			book['chapter_url'] = chapter_url_list
	# print(chapter_url_list)
	return book


async def get_content(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			chapter = {}
			html = await resp.text(encoding='utf-8')
			html = etree.HTML(html)
			info = html.xpath('//div[@class="content book-content"]')[0]
			title = info.xpath('./h1/text()')[0]
			title = title.replace(' ', '').replace(':', '_')
			print(title)
			content = html.xpath('//div[@id="neirong"]//text()')
			# print(content)
			content = '  '.join(content).replace('\t', '')
			if '(adsbygoogle = window.adsbygoogle || []).push({});' in content:
				s = re.findall(r'\(adsbygoogle = window.adsbygoogle \|\| \[\]\)\.push\({}\);',
				               content)[0]
				content = content.replace(s, '')
			# print(content)
			chapter['title'] = title
			chapter['content'] = content
	return chapter


async def save_file(path, chapter):
	# print(chapter)
	file_path = os.path.join(path, chapter['title'])
	# path = f'{file_path}.txt'
	async with aiofiles.open(f'{file_path}.txt', 'w', encoding='utf-8') as f:
		await f.write(chapter['content'])


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	book_url = loop.run_until_complete(get_book_url())
	tasks = [get_chapter_url(url) for url in book_url]
	book_list = loop.run_until_complete(asyncio.gather(*tasks))
	for book in book_list:
		book_name = book['name']
		if not os.path.exists(book_name):
			os.mkdir(book_name)
		tasks = [get_content(chapter_url) for chapter_url in book['chapter_url']]
		chapter_list = loop.run_until_complete(asyncio.gather(*tasks))
		tasks = [save_file(book_name, chapter) for chapter in chapter_list]
		loop.run_until_complete(asyncio.gather(*tasks))

	"""
	book_url = get_book_url()
	# print(book_url)
	for url in book_url:
		book = get_chapter_url(url)
		path = book['name']
		if not os.path.exists(path):
			os.mkdir(path)
		chapter_url_list = book['chapter_url']
		for chapter_url in chapter_url_list:
			chapter = get_content(chapter_url)
			save_file(path,chapter)
			# print(chapter)
	"""
