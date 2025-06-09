import pymysql
import asyncio
import aiohttp
from lxml import etree
from urllib.parse import urljoin

# 数据库连接配置
db_config = {

}

# 获取页面内容的异步函数
async def fetch(url):
    print(f"正在获取页面内容：{url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# 获取书籍信息的异步函数
async def get_book_info(url):
    data = await fetch(url)
    html = etree.HTML(data)
    book_info_list = []

    book_lis = html.xpath('//div[@class="l"]/ul/li')
    for li in book_lis:
        book_url = li.xpath('./span[@class="s2"]/a/@href')[0]
        book_name = li.xpath('./span[@class="s2"]/a/text()')[0]
        book_author = li.xpath('./span[@class="s5"]/text()')[0]
        summary_url = urljoin(url, book_url)
        summary = await get_summary(summary_url)

        book_info = {
            'name': book_name,
            'author': book_author,
            'summary': summary
        }
        book_info_list.append(book_info)

    return book_info_list

# 获取章节链接的异步函数
async def get_chapter_url(url):
    data = await fetch(url)
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

# 获取书籍简介的异步函数
async def get_summary(url):
    data = await fetch(url)
    html = etree.HTML(data)
    summary = html.xpath('//div[@id="intro"]/p/text()')
    return summary[0] if summary else None

# 获取章节内容的异步函数
async def get_content(url):
    data = await fetch(url)
    html = etree.HTML(data)
    content = html.xpath('//div[@id="content"]//text()')
    content = ''.join(content)
    return content

# 将书籍数据插入 vv_book 表的异步函数
async def insert_book_data(book_info):
    print(f"正在插入书籍数据：{book_info['name']}")
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    sql = "INSERT INTO vv_book (title, author, summary) VALUES (%s, %s, %s)"
    cursor.execute(sql, (book_info['name'], book_info['author'], book_info['summary']))

    conn.commit()
    conn.close()

# 将分集数据插入 vv_book_episodes 表的异步函数
async def insert_episode_data(book_id, episode_data):
    print(f"正在插入分集数据：{episode_data['title']}")
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    sql = "INSERT INTO vv_book_episodes (bid, title, ji_no, info) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (book_id, episode_data['title'], episode_data['ji_no'], episode_data['content']))

    conn.commit()
    conn.close()

# 处理书籍的异步函数
async def process_books(url):
    book_list = await get_book_info(url)
    for book in book_list:
        print(f"正在处理书籍：{book['name']}")
        await insert_book_data(book)
        url = book['url']
        chapter_urls = await get_chapter_url(url)
        for index, chapter_url in enumerate(chapter_urls):
            url = chapter_url[0]
            content = await get_content(url)
            episode_data = {
                'title': chapter_url[1],
                'ji_no': index + 1,
                'content': content
            }
            await insert_episode_data(book_id, episode_data)

# 主函数
async def main():
    tasks = []
    for i in range(1, 6):
        if i == 1:
            url = 'https://www.biquge.co/chuanyuexiaoshuo/'
        else:
            url = f'https://www.biquge.co/chuanyuexiaoshuo/4_{i}.html'
        tasks.append(process_books(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
