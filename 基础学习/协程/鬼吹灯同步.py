import os.path
import re

import requests
from lxml import etree

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


def get_book_url():
	url = 'https://www.51shucheng.net/daomu/guichuideng'
	resp = requests.get(url, headers=headers)
	html = resp.content.decode()

	html = etree.HTML(html)
	book_url = html.xpath('//div[@class="sbut"]/a/@href')
	return book_url


def get_chapter_url(url):
	book = {}
	resp = requests.get(url, headers=headers)
	html = resp.content.decode()

	html = etree.HTML(html)
	book_name = html.xpath('//div[@class="mulu-title"][1]/h2/text()')[0]
	book_name = book_name.replace(' ', '_')
	book['name'] = book_name
	# print(book_name)
	chapter_url_list = html.xpath('//div[@class="mulu-list"]/ul/li/a/@href')
	book['chapter_url'] = chapter_url_list
	# print(chapter_url_list)
	return book


def get_content(url):
	chapter = {}
	resp = requests.get(url, headers=headers)
	html = resp.content.decode()

	html = etree.HTML(html)
	info = html.xpath('//div[@class="content book-content"]')[0]
	title = info.xpath('./h1/text()')[0]
	title = title.replace(' ', '').replace(':', '_')
	print(title)
	content = html.xpath('//div[@id="neirong"]//text()')
	# print(content)
	content = '  '.join(content).replace('\t', '')
	if '(adsbygoogle = window.adsbygoogle || []).push({});' in content:
		s = re.findall(r'\(adsbygoogle = window.adsbygoogle \|\| \[\]\)\.push\({}\);', content)[0]
		content = content.replace(s, '')
	# print(content)
	chapter['title'] = title
	chapter['content'] = content
	return chapter


def save_file(chapter):
	file_path = os.path.join(path, chapter['title'])
	with open(f'{file_path}.txt', 'w', encoding='utf-8') as f:
		f.write(chapter['content'])


if __name__ == '__main__':
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
			save_file(chapter)
# print(chapter)
