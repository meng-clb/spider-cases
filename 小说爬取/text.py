# -*- coding: utf-8 -*-

import requests
from lxml import etree
from urllib.parse import urljoin
import pymysql.cursors
import time
import threading

# MySQL数据库连接信息



# 连接MySQL数据库
def connect_to_mysql():
	connection = pymysql.connect(host=DB_HOST,
	                             user=DB_USER,
	                             password=DB_PASSWORD,
	                             database=DB_NAME,
	                             port=3306,
	                             cursorclass=pymysql.cursors.DictCursor)
	return connection


# 插入书本信息到vv_book表
def insert_book_info(connection, book_info):
	try:
		with connection.cursor() as cursor:
			sql_query = """INSERT INTO vv_book (title, author, summary, create_time, update_time)
                           VALUES (%s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())"""
			cursor.execute(sql_query,
			               (book_info['name'], book_info['author'], book_info['summary']))
			connection.commit()
			print(f"书本信息已插入: {book_info['name']}")
	except Exception as e:
		print(f"插入书本信息时出错: {e}")


# 插入章节信息到vv_book_episodes表
def insert_chapter_info(connection, book_id, chapter_info):
	try:
		with connection.cursor() as cursor:
			sql_query = """INSERT INTO vv_book_episodes (bid, title, ji_no, info, create_time, 
			update_time)
                           VALUES (%s, %s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())"""
			cursor.execute(sql_query, (
				book_id, chapter_info['chapter_name'], chapter_info['chapter_no'],
				chapter_info['content']))
			connection.commit()
			print(f"章节信息已插入: {chapter_info['chapter_name']}")
	except Exception as e:
		print(f"插入章节信息时出错: {e}")


# 获取书本信息
def get_book_info(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	book_info_list = []

	book_lis = html.xpath('//div[@class="l"]/ul/li')
	for li in book_lis:
		book_url = li.xpath('./span[@class="s2"]/a/@href')[0]
		book_name = li.xpath('./span[@class="s2"]/a/text()')[0]
		book_author = li.xpath('./span[@class="s5"]/text()')[0]

		summary_url = urljoin(url, book_url)
		summary = get_summary(summary_url)

		book_info = {
			'url': book_url,
			'name': book_name,
			'author': book_author,
			'summary': summary
		}

		book_info_list.append(book_info)

	print("正在获取书本信息...")
	return book_info_list


# 获取章节信息
def get_chapter_info(book_url):
	resp = requests.get(book_url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	chapter_urls = []

	dd_lis = html.xpath('//div[@id="list"]/dl/dd')[9:]
	if len(dd_lis) > 150:
		dd_lis = dd_lis[:151]

	for dd in dd_lis:
		href = dd.xpath('./a/@href')[0]
		chapter_name = dd.xpath('./a/text()')[0]
		chapter_url = urljoin(book_url, href)
		chapter_urls.append((chapter_url, chapter_name))

	return chapter_urls


# 获取作品简介
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


# 处理书本信息
def process_book_info(book_info):
	connection = connect_to_mysql()
	if connection:
		try:
			for book in book_info:
				insert_book_info(connection, book)
				time.sleep(1)  # 等待1秒，防止过快请求被封IP
				chapter_urls = get_chapter_info(book['url'])
				for chapter_url, chapter_name in chapter_urls:
					chapter_content = get_content(chapter_url)
					chapter_info = {
						'chapter_name': chapter_name,
						'chapter_no': chapter_urls.index((chapter_url, chapter_name)) + 1,
						# 章节编号从1开始
						'content': chapter_content
					}
					insert_chapter_info(connection, book['id'], chapter_info)
					time.sleep(1)  # 等待1秒，防止过快请求被封IP
		finally:
			connection.close()


if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
		              'like Gecko) Chrome/123.0.0.0 Safari/537.36',
		'Referer': 'https://www.biquge.co/xuanhuanxiaoshuo/'
	}

	# 通过首页获取到小说信息
	# https://www.biquge.co/chuanyuexiaoshuo/4_{变化}.html
	book_info_list = []
	for i in range(1, 6):
		if i == 1:
			url = 'https://www.biquge.co/chuanyuexiaoshuo/'
		else:
			url = f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html'
		book_list = get_book_info(url)
		book_info_list.extend(book_list)

	# 多线程处理书本信息
	threads = []
	for book_info in book_info_list:
		t = threading.Thread(target=process_book_info, args=(book_info,))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	print("所有书本信息已处理完成")
