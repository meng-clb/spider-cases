import time

import requests
from lxml import etree

headers = {
	'Referer': 'https://movie.douban.com/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

url = 'https://movie.douban.com/chart'


def get_detail_url():
	resp = requests.get(url, headers=headers)

	text = resp.text
	html = etree.HTML(text)
	url_list = html.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
	return url_list


def get_title(detail_url):
	resp = requests.get(detail_url, headers=headers)

	text = resp.text
	html = etree.HTML(text)
	title = html.xpath('//h1//text()')
	title = ''.join(title).replace('\n', '').strip()
	print(title)


if __name__ == '__main__':
	t1 = time.time()
	url_list = get_detail_url()
	for url in url_list:
		get_title(url)
	print(time.time() - t1)
