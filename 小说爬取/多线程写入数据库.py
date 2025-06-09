import pymysql
import requests
from lxml import etree
from urllib.parse import urljoin
import threading

# 数据库连接配置
db_config = {

}

# 数据库连接
conn = pymysql.connect(**db_config)
cursor = conn.cursor()


# 从代理API获取代理列表
def get_proxy():
	# 获取代理IP的API
	api = "https://dps.kdlapi.com/api/getdps"
	# 请求参数
	params = {
		"secret_id": "o97gfimgt220wbilkisx",
		"signature": "fy4geb8b3u24a3oi12b9up193u0lbr9f",
		"num": 1,  # 提取数量
	}
	# 发送请求获取代理IP
	response = requests.get(api, params=params)
	data = response.json()
	# 提取代理IP
	proxy = data['data']['proxy_list'][0]
	return proxy


# 函数用于获取当前要使用的代理
def get_current_proxy():
	proxy = get_proxy()
	# 将用户名和密码添加到代理IP地址中
	proxy_with_auth = f"http://17538263287:ameng123456@{proxy}"
	return {"http": proxy_with_auth, "https": proxy_with_auth}


def get_book_info(url):
	proxy = get_current_proxy()  # 获取当前代理
	resp = requests.get(url, headers=headers, proxies=proxy)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)

	book_info_list = []

	book_lis = html.xpath('//div[@class="l"]/ul/li')
	for li in book_lis:
		book_url = li.xpath('./span[@class="s2"]/a/@href')[0]
		book_name = li.xpath('./span[@class="s2"]/a/text()')[0]
		book_author = li.xpath('./span[@class="s5"]/text()')[0]

		book_info = {
			'url': book_url,
			'name': book_name,
			'author': book_author
		}

		book_info_list.append(book_info)

	return book_info_list


def get_chapter_url(url):
	proxy = get_current_proxy()  # 获取当前代理
	resp = requests.get(url, headers=headers, proxies=proxy)
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


def get_content(url):
	proxy = get_current_proxy()  # 获取当前代理
	resp = requests.get(url, headers=headers, proxies=proxy)
	data = resp.content.decode('gbk')
	html = etree.HTML(data)
	content = html.xpath('//div[@id="content"]//text()')
	content = ''.join(content)
	return content


def insert_book(book_info):
	# 插入 vv_book 表数据的 SQL 语句
	insert_book_sql = """
        INSERT INTO vv_book (title, author) 
        VALUES (%s, %s)
    """
	# 执行插入操作
	cursor.execute(insert_book_sql, (book_info['name'], book_info['author']))
	# 提交事务
	conn.commit()
	# 获取插入数据的自增主键值
	book_id = cursor.lastrowid
	return book_id


def insert_chapter(book_id, chapter_url):
	content = get_content(chapter_url)
	# 插入 vv_book_episodes 表数据的 SQL 语句
	insert_chapter_sql = """
        INSERT INTO vv_book_episodes (bid, title, info) 
        VALUES (%s, %s, %s)
    """
	# 执行插入操作
	cursor.execute(insert_chapter_sql, (book_id, chapter_url[1], content))
	# 提交事务
	conn.commit()


def crawl_book(book_info):
	book_id = insert_book(book_info)
	chapter_urls = get_chapter_url(book_info['url'])
	for chapter_url in chapter_urls:
		insert_chapter(book_id, chapter_url)


if __name__ == '__main__':
	urls = []
	for i in range(1, 6):
		if i == 1:
			urls.append('https://www.biquge.co/chuanyuexiaoshuo/')
		else:
			urls.append(f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html')

	threads = []
	for url in urls:
		book_list = get_book_info(url)
		for book in book_list:
			thread = threading.Thread(target=crawl_book, args=(book,))
			thread.start()
			threads.append(thread)

	for thread in threads:
		thread.join()

	# 关闭数据库连接
	cursor.close()
	conn.close()
