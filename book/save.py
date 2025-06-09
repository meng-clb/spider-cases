import asyncio
from lxml import etree
import aiohttp
from urllib.parse import urljoin
import pymysql.cursors

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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 获取书籍信息的函数
async def get_info(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()

    book_infos = []

    for book in data:
        book_info = {
            'title': book['articlename'],
            'author': book['author'],
            'summary': book['intro'],
            'cover_pic': book['url_img'],
            'status': 1 if book['is_end'] == '连载' else 2,
            'free_type': 1 if book['is_free'] == '免费' else 2,
            'episodes': book['last_chap'],
            'reader': book['read_count'],
            'likes': book['zannum'],
            'create_time': book['create_time'],
            'update_time': book['update_time']
        }
        book_infos.append(book_info)
    return book_infos

# 获取章节内容的函数
async def get_content(session, url):
    async with session.get(url, headers=headers) as response:
        data = await response.text()

    html = etree.HTML(data)

    title = html.xpath('//div[@class="content"]/h1/text()')
    content = html.xpath('//div[@id="chaptercontent"]//text()')
    return {
        'title': title[0],
        'content': ''.join(content)
    }

# 用于向数据库中添加数据的函数
async def insert_data(book_info, episode_info):
    async with conn.cursor() as cursor:
        await cursor.execute("INSERT INTO vv_book (title, author, summary, cover_pic, status, free_type, episodes, reader, likes, create_time, update_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                             (book_info['title'], book_info['author'], book_info['summary'], book_info['cover_pic'], book_info['status'], book_info['free_type'], book_info['episodes'], book_info['reader'], book_info['likes'], book_info['create_time'], book_info['update_time']))
        await cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = (await cursor.fetchone())['LAST_INSERT_ID()']
        await cursor.execute("INSERT INTO vv_book_episodes (bid, title, ji_no, info, readnums, likes, create_time, update_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                             (last_id, episode_info['title'], episode_info['ji_no'], episode_info['info'], episode_info['readnums'], episode_info['likes'], episode_info['create_time'], episode_info['update_time']))
    conn.commit()

# 处理书籍信息并添加到数据库的函数
async def process_book(session, book_info):
    episode_url = book_info['url']
    async with session.get(episode_url, headers=headers) as response:
        data = await response.json()

    episode_infos = []

    for episode in data:
        episode_info = {
            'title': episode['chapname'],
            'ji_no': episode['sort'],
            'info': episode['content'],
            'readnums': episode['read_count'],
            'likes': episode['zannum'],
            'create_time': episode['create_time'],
            'update_time': episode['update_time']
        }
        episode_infos.append(episode_info)

    for episode_info in episode_infos:
        await insert_data(book_info, episode_info)

# 主函数
async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 10):
            url = f'https://www.bq60.cc/json?sortid=1&page={i}'
            book_infos = await get_info(url)
            for book_info in book_infos:
                task = asyncio.create_task(process_book(session, book_info))
                tasks.append(task)
        await asyncio.gather(*tasks)

# 运行主函数
if __name__ == "__main__":
    asyncio.run(main())

# 关闭数据库连接
conn.close()
