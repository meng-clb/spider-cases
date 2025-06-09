import json
import re
import asyncio
import aiomysql
import aiohttp
from lxml import etree
from urllib.parse import urljoin

# 请求头信息
headers = {
    'Referer': 'https://www.bq60.cc/xuanhuan/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

async def get_info(url, session):
    async with session.get(url, headers=headers) as res:
        data = await res.text()
        # print(data)
        # print(data.json())
        # print(type(data))
        data = json.loads(data)
        print(data)
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

async def get_chapter_url(url, session):
    async with session.get(url, headers=headers) as resp:
        data = await resp.text()
        html = etree.HTML(data)

        chapter_urls = []

        dd_lis = html.xpath('//div[@class="listmain"]/dl/span[@class="dd_hide"]/dd')[:150]

        for dd in dd_lis:
            href = dd.xpath('./a/@href')[0]
            chapter_name = dd.xpath('./a/text()')[0]
            chapter_url = urljoin(url, href)
            chapter_urls.append((chapter_url, chapter_name))

        return chapter_urls

async def get_content(url, session):
    async with session.get(url, headers=headers) as resp:
        data = await resp.text()
        html = etree.HTML(data)

        title = html.xpath('//div[@class="content"]/h1/text()')
        content = html.xpath('//div[@id="chaptercontent"]//text()')
        book = {
            'title': title[0],
            'content': ''.join(content)
        }
        return book

async def insert_to_database(pool, book_info, chapter_info):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            # 检查书籍是否已存在
            sql = "SELECT id FROM vv_book WHERE title = %s"
            await cursor.execute(sql, (book_info['book_name'],))
            result = await cursor.fetchone()

            if result:  # 书籍已存在，无需再次插入
                book_id = result[0]
            else:  # 如果不存在，插入书籍信息
                sql = ("INSERT INTO vv_book (title, author, summary, cover_pic, create_time, "
                       "update_time) VALUES (%s, %s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())")
                await cursor.execute(sql, (
                    book_info['book_name'], book_info['author'], book_info['summary'],
                    book_info['url_img']))
                # 获取新插入书籍的 ID
                book_id = cursor.lastrowid

            # 插入章节信息
            sql = ("INSERT INTO vv_book_episodes (bid, title, ji_no, info, create_time, "
                   "update_time) VALUES (%s, %s, %s, %s, UNIX_TIMESTAMP(), UNIX_TIMESTAMP())")
            await cursor.execute(sql, (
                book_id, chapter_info['title'], book_info['ji_no'], chapter_info['content']))

        # 提交事务
        await conn.commit()
        print("数据插入成功！")

async def main():
    pool = await aiomysql.create_pool(
        host='8.137.88.254',
        user='yule7_yuanshiwan',
        password='18215675631hxj',
        db='yule7_yuanshiwan',
        charset='utf8mb4',
        autocommit=True,
    )

    async with aiohttp.ClientSession() as session:
        for i in range(17, 19):
            url = f'https://www.bq60.cc/json?sortid=1&page={i}'
            book_infos = await get_info(url, session)
            for book_info in book_infos:
                print(book_info)
                chapter_urls = await get_chapter_url(book_info['url'], session)
                for chapter_url, chapter_name in chapter_urls:
                    print(chapter_url)
                    print(chapter_name)
                    try:
                        book_info['ji_no'] = re.findall('第(\d+)章', chapter_name)[0]
                        print(book_info['ji_no'])
                    except Exception as e:
                        book_info['ji_no'] = 0
                    print('============')
                    content = await get_content(chapter_url, session)
                    print(content)
                    await insert_to_database(pool, book_info, content)

    # 关闭数据库连接池
    pool.close()
    await pool.wait_closed()

# 运行异步主函数
asyncio.run(main())
