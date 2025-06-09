import re

import pymysql.cursors
from lxml import etree
import requests
from urllib.parse import urljoin

# 建立数据库连接
conn = pymysql.connect(
	host='8.137.88.254',
	user='yule7_yuanshiwan',
	password='18215675631hxj',
	database='yule7_yuanshiwan',
	charset='utf8mb4'
)

# 请求头信息
headers = {
	'Referer': 'https://www.bq60.cc/xuanhuan/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/123.0.0.0 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}


def get_info(url):
	res = requests.get(url, headers=headers)
	data = res.json()

	book_infos = []

	for book in data:
		book_info = {
			'url': urljoin('https://www.bq60.cc/xuanhuan/', book['url_list']),
			'url_img': book['url_img'],
			'book_name': book['articlename'],
			'author': book['author'],
			'summary': book['intro']
		}
		book_infos.append(book_info)
	return book_infos


def get_chapter_url(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode()
	html = etree.HTML(data)

	chapter_urls = []

	dd_lis = html.xpath('//div[@class="listmain"]/dl/span[@class="dd_hide"]/dd')[:150]

	for dd in dd_lis:
		href = dd.xpath('./a/@href')[0]
		chapter_name = dd.xpath('./a/text()')[0]
		chapter_url = urljoin(url, href)
		chapter_urls.append((chapter_url, chapter_name))

	return chapter_urls


def get_content(url):
	resp = requests.get(url, headers=headers)
	data = resp.content.decode()
	html = etree.HTML(data)

	title = html.xpath('//div[@class="content"]/h1/text()')
	content = html.xpath('//div[@id="chaptercontent"]//text()')
	book = {
		'title': title[0],
		'content': ''.join(content)
	}
	return book


def insert_to_database(book_info, chapter_info):
	try:
		with conn.cursor() as cursor:
			# 检查书籍是否已存在
			sql = "SELECT id FROM vv_book WHERE title = %s"
			cursor.execute(sql, (book_info['book_name'],))
			result = cursor.fetchone()

			if result:  # 书籍已存在，无需再次插入
				book_id = result[0]
			else:  # 如果不存在，插入书籍信息
				sql = ("INSERT INTO vv_book (title, author, summary, cover_pic, create_time, "
				       "update_time) VALUES (%s, %s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())")
				cursor.execute(sql, (
					book_info['book_name'], book_info['author'], book_info['summary'],
					book_info['url_img']))
				# 获取新插入书籍的 ID
				book_id = cursor.lastrowid

			# 插入章节信息
			sql = ("INSERT INTO vv_book_episodes (bid, title, ji_no, info, create_time, "
			       "update_time) VALUES (%s, %s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())")
			cursor.execute(sql, (
				book_id, chapter_info['title'], book_info['ji_no'], chapter_info['content']))

		# 提交事务
		conn.commit()
		print("数据插入成功！")
	except Exception as e:
		print(f"数据插入失败: {e}")


if __name__ == '__main__':
	for i in range(1, 10):
		url = f'https://www.bq60.cc/json?sortid=1&page={i}'
		book_infos = get_info(url)
		for book_info in book_infos:
			print(book_info)
			chapter_urls = get_chapter_url(book_info['url'])
			for chapter_url, chapter_name in chapter_urls:
				print(chapter_url)
				print(chapter_name)
				try:
					book_info['ji_no'] = re.findall('第(\d+)章', chapter_name)[0]
					print(book_info['ji_no'])
				except Exception as e:
					book_info['ji_no'] = 0
				print('============')
				content = get_content(chapter_url)
				print(content)
				insert_to_database(book_info, content)

# 关闭数据库连接
conn.close()
