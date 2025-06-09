import requests
from lxml import etree
from urllib.parse import urljoin

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.biquge.co/xuanhuanxiaoshuo/'
}


def get_book_info(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	book_info_list = []  # 创建空列表，用于存储书本信息

	book_lis = html.xpath('//div[@class="l"]/ul/li')
	for li in book_lis:
		book_url = li.xpath('./span[@class="s2"]/a/@href')[0]
		book_name = li.xpath('./span[@class="s2"]/a/text()')[0]
		book_author = li.xpath('./span[@class="s5"]/text()')[0]
		# Get summary
		summary_url = urljoin(url, book_url)
		summary = get_summary(summary_url)

		book_info = {
			'url': book_url,
			'name': book_name,
			'author': book_author,
			'summary': summary  # Add summary to book info
		}

		book_info_list.append(book_info)  # 将书本信息添加到列表中

	return book_info_list  # 返回书本信息的列表


def get_chapter_url(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	chapter_urls = []  # 创建空列表，用于存储章节链接

	dd_lis = html.xpath('//div[@id="list"]/dl/dd')[9:]
	if len(dd_lis) > 150:
		dd_lis = dd_lis[:151]

	for dd in dd_lis:
		href = dd.xpath('./a/@href')[0]
		chapter_name = dd.xpath('./a/text()')[0]
		chapter_url = urljoin(url, href)  # 拼接完整的章节链接
		chapter_urls.append((chapter_url, chapter_name))  # 将章节链接添加到列表中

	return chapter_urls  # 返回章节链接的列表


def get_summary(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)
	summary = html.xpath('//div[@id="intro"]/p/text()')
	return summary[0] if summary else None


def get_content(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)
	content = html.xpath('//div[@id="content"]//text()')
	content = ''.join(content)
	return content


if __name__ == '__main__':
	# 通过首页获取到小说信息
	# https://www.biquge.co/chuanyuexiaoshuo/4_{变化}.html
	for i in range(1, 6):
		if i == 1:
			url = 'https://www.biquge.co/chuanyuexiaoshuo/'
		else:
			url = f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html'
		book_list = get_book_info(url)
		for book in book_list:
			# print(book_list)
			# 通过小说链接, 进去详情页, 获取小说的章节和url
			url = book['url']
			chapter_urls = get_chapter_url(url)
			for chapter_url in chapter_urls:
				url = chapter_url[0]
				# 通过小说章节链接, 获取所有的内容
				content = get_content(url)
