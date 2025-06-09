import pymysql
import requests
from lxml import etree
from urllib.parse import urljoin
import threading

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.biquge.co/xuanhuanxiaoshuo/'
}

# 建立数据库连接
conn = pymysql.connect(

)

# 创建游标对象
cursor = conn.cursor()


# 爬取书本信息的线程类
class BookInfoThread(threading.Thread):
	def __init__(self, url):
		threading.Thread.__init__(self)
		self.url = url

	def run(self):
		book_info_list = get_book_info(self.url)
		for book_info in book_info_list:
			book_id = save_book_to_db(book_info)
			chapter_thread = ChapterUrlThread(book_info['url'], book_id)
			chapter_thread.start()


# 爬取章节链接的线程类
class ChapterUrlThread(threading.Thread):
	def __init__(self, url, book_id):
		threading.Thread.__init__(self)
		self.url = url
		self.book_id = book_id

	def run(self):
		chapter_urls = get_chapter_url(self.url)
		for index, chapter_url in enumerate(chapter_urls, start=1):
			content = get_content(chapter_url[0])
			chapter_name = chapter_url[1]
			save_chapter_to_db(self.book_id, chapter_name, index, content)


def save_book_to_db(book_info):
	sql = ("INSERT INTO vv_book (title, author, summary, create_time, update_time) VALUES (%s, "
	       "%s, "
	       "%s, %s, %s)")
	cursor.execute(sql, (book_info['name'], book_info['author'], book_info['summary'], 0, 0))
	conn.commit()

	print(f"已插入书本信息：{book_info['name']}")  # 添加插入书本信息的提示信息
	return cursor.lastrowid


def save_chapter_to_db(book_id, chapter_name, ji_no, content):
	try:
		cursor = conn.cursor()  # 创建新的游标
		sql = (
			"INSERT INTO vv_book_episodes (bid, title, ji_no, info, create_time, update_time) "
			"VALUES "
			"(%s, %s, %s, %s, %s, %s)")
		cursor.execute(sql, (book_id, chapter_name, ji_no, content, 0, 0))
		conn.commit()
	finally:
		cursor.close()  # 在插入完数据后关闭游标
	print(f"已插入章节信息：{chapter_name}")  # 添加插入章节信息的提示信息


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
		book_summary = get_summary(urljoin(url, book_url))

		book_info = {
			'url': book_url,
			'name': book_name,
			'author': book_author,
			'summary': book_summary  # 添加摘要信息
		}

		book_info_list.append(book_info)  # 将书本信息添加到列表中
	print(f'已爬取书本信息：{url}')  # 添加爬取书本信息的提示信息
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
	print(f'已获取章节链接：{url}')  # 添加获取章节链接的提示信息
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
	# 创建并启动爬取书本信息的线程
	threads = []
	for i in range(1, 6):
		if i == 1:
			url = 'https://www.biquge.co/chuanyuexiaoshuo/'
		else:
			url = f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html'
		thread = BookInfoThread(url)
		thread.start()
		threads.append(thread)

	# 等待所有线程完成
	for thread in threads:
		thread.join()

	# 关闭游标和数据库连接
	cursor.close()
	conn.close()
