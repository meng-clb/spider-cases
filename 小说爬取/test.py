# -*- coding: utf-8 -*-

import requests
from lxml import etree
from urllib.parse import urljoin
import pymysql.cursors
import time
from threading import Thread

# MySQL数据库连接信息


# 全局变量，用于控制线程访问速度
DELAY = 1


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
			# 获取插入后的自增ID
			book_info['bid'] = cursor.lastrowid
			print(book_info['bid'])
			print(f"书本信息已插入: {book_info['name']}")

	except Exception as e:
		print(f"插入书本信息时出错: {e}")


# 插入章节信息到vv_book_episodes表
def insert_chapter_info(connection, chapter_info):
	print(chapter_info)
	try:
		with connection.cursor() as cursor:
			sql_query = """INSERT INTO vv_book_episodes (id,bid, title, ji_no, info, readnums,
            likes,previous, following,  create_time, update_time)
                           VALUES (null, %s, %s, %s, %s, %s, 0, 0, 0, UNIX_TIMESTAMP(), 
                           UNIX_TIMESTAMP())"""
			print(chapter_info['bid'], chapter_info['title'], chapter_info['ji_no'],
			      chapter_info['info'], chapter_info['readnums'])
			cursor.execute(sql_query, (
				chapter_info['bid'], chapter_info['title'], chapter_info['ji_no'], chapter_info[
					'info'],
				chapter_info['readnums']))
			print(sql_query)
			connection.commit()
			print(f"章节信息已插入: {chapter_info['title']}")
	except Exception as e:
		print(f"插入章节信息时出错: {e}")


# 获取书本信息
def get_book_info(url, connection):
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
			'summary': summary,
			'bid': None  # 用于存储书本ID
		}

		# 插入书本信息
		insert_book_info(connection, book_info)

		# 获取章节信息并插入数据库
		chapter_urls = get_chapter_url(urljoin(url, book_url))
		for idx, chapter_url in enumerate(chapter_urls, start=1):
			chapter_info = {
				'bid': book_info['bid'],  # 使用书本ID
				'title': chapter_url[1],
				'ji_no': idx,  # 章节编号暂时使用索引
				'info': get_content(chapter_url[0]),
				'readnums': 0  # 暂时设定阅读人数为0
			}
			insert_chapter_info(connection, chapter_info)

	print("正在获取书本信息...")  # 输出提示信息


# 获取章节链接
def get_chapter_url(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	chapter_urls = []

	dd_lis = html.xpath('//div[@id="list"]/dl/dd')[9:]
	if len(dd_lis) > 150:
		dd_lis = dd_lis[:151]

	for dd in dd_lis:
		href = dd.xpath('./a/@href')[0]
		chapter_name = dd.xpath('./a/text()')[0]
		chapter_url = urljoin(url, href)
		chapter_urls.append((chapter_url, chapter_name))

	return chapter_urls


# 获取书本简介
def get_summary(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)
	summary = html.xpath('//div[@id="intro"]/p/text()')
	return summary[0] if summary else None


# 获取章节内容
def get_content(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)
	content = html.xpath('//div[@id="content"]//text()')
	# content = ''.join(content)
	print(content)
	return content


if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
		              'like Gecko) Chrome/123.0.0.0 Safari/537.36',
		'Referer': 'https://www.biquge.co/xuanhuanxiaoshuo/'
	}

	connection = connect_to_mysql()
	if connection:
		try:
			for i in range(1, 6):
				if i == 1:
					url = 'https://www.biquge.co/chuanyuexiaoshuo/'
				else:
					url = f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html'
				# 在单独的线程中获取书本信息
				t = Thread(target=get_book_info, args=(url, connection))
				t.start()
				time.sleep(DELAY)  # 控制线程访问速度
		finally:
			connection.close()
