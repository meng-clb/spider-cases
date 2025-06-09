import re
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://movie.douban.com/subject/35357321/comments'

headers = {
	'Cookie': '',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Host': 'movie.douban.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, '
	              'like Gecko) Version/15.4 Safari/605.1.15',
	'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
	'Referer': 'https://movie.douban.com/subject/35357321/?from=showing',
	'Connection': 'keep-alive'
}
with open('comment.csv', 'a', encoding='utf-8') as f:
	for i in range(0, 600, 20):
		params = {
			'percent_type': '',
			'start': i,
			'limit': 20,
			'status': 'P',
			'sort': 'new_score',
			'comments_only': 1,
		}
		print(f'第{i}条')
		time.sleep(2)
		res = requests.get(url, headers=headers, params=params)
		html_doc = res.json()['html']
		# print(html_doc)
		# soup = BeautifulSoup(html, 'html.parser')
		html = etree.HTML(html_doc)
		items = html.xpath('//div[@class="comment-item "]')
		for item in items:
			uname = item.xpath('./div[@class="avatar"]/a/@title')[0]
			vote_count = item.xpath('.//h3//span[@class="votes vote-count"]/text()')[0]
			allstar50 = item.xpath('.//h3/span[@class="comment-info"]/span[@class="allstar50 '
			                       'rating"]/@title')
			if len(allstar50) == 0:
				continue
			allstar50 = '5星'
			comment_time = item.xpath('.//span[@class="comment-time "]/@title')[0]
			comment = item.xpath('.//p[@class=" comment-content"]/span[@class="short"]/text()')[0]
			comment = str(comment).replace('\n', '。')
			print(f'{uname}, {vote_count}, {allstar50}, {comment_time}, {comment}')

			f.write(f'{uname}, {vote_count}, {allstar50}, {comment_time}, {comment}\n')
