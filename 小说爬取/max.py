import pymysql
import requests
from lxml import etree
from urllib.parse import urljoin
import threading
import time
import random


class ProxyPool():

    def __init__(self, secretid, signature, proxy_count):
        self.secretid = secretid
        self.signature = signature
        self.proxy_count = proxy_count if proxy_count < 50 else 50
        self.alive_proxy_list = []

    def _fetch_proxy_list(self, count):
        try:
            res = requests.get("https://dps.kdlapi.com/api/getdps/?secret_id=%s&signature=%s&num=%s&pt=1&sep=1&f_et=1&format=json" % (self.secretid, self.signature, count))
            return [proxy.split(',') for proxy in res.json().get('data').get('proxy_list')]
        except Exception as e:
            print("API获取IP异常，请检查订单:", e)
        return []

    def _init_proxy(self):
        self.alive_proxy_list = self._fetch_proxy_list(self.proxy_count)

    def add_alive_proxy(self, add_count):
        self.alive_proxy_list.extend(self._fetch_proxy_list(add_count))

    def get_proxy(self):
        return random.choice(self.alive_proxy_list)[0] if self.alive_proxy_list else ""

    def run(self):
        sleep_seconds = 1
        self._init_proxy()
        while True:
            for proxy in self.alive_proxy_list:
                proxy[1] = float(proxy[1]) - sleep_seconds
                if proxy[1] <= 3:
                    self.alive_proxy_list.remove(proxy)
            if len(self.alive_proxy_list) < self.proxy_count:
                self.add_alive_proxy(self.proxy_count - len(self.alive_proxy_list))
            time.sleep(sleep_seconds)

    def start(self):
        t = threading.Thread(target=self.run)
        t.setDaemon(True)
        t.start()


# 数据库连接配置
db_config = {

}

# 数据库连接
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) '
                  'Chrome/123.0.0.0 Safari/537.36',
    'Referer': 'https://www.biquge.co/xuanhuanxiaoshuo/'
}

# 实例化代理池对象
proxy_pool = ProxyPool('o97gfimgt220wbilkisx', 'fy4geb8b3u24a3oi12b9up193u0lbr9f', 30)
proxy_pool.start()


def get_book_info(url):
    # 获取当前代理
    proxy = proxy_pool.get_proxy()
    resp = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
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
    proxy = proxy_pool.get_proxy()  # 获取当前代理
    resp = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
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
    proxy = proxy_pool.get_proxy()  # 获取当前代理
    resp = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
    data = resp.content.decode('gbk')
    html = etree.HTML(data)
    content = html.xpath('//div[@id="content"]//text()')
    content = ''.join(content)
    return content


def insert_book(book_info):
    insert_book_sql = """
        INSERT INTO vv_book (title, author) 
        VALUES (%s, %s)
    """
    cursor.execute(insert_book_sql, (book_info['name'], book_info['author']))
    conn.commit()
    book_id = cursor.lastrowid
    return book_id


def insert_chapter(book_id, chapter_url):
    content = get_content(chapter_url)
    insert_chapter_sql = """
        INSERT INTO vv_book_episodes (bid, title, info) 
        VALUES (%s, %s, %s)
    """
    cursor.execute(insert_chapter_sql, (book_id, chapter_url[1], content))
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

    cursor.close()
    conn.close()
