""""
1. 创建一个函数, 处理完热搜链接之后,
2. 把数据传递到hot_info内获取详细信息
3. 把详细信息传递出来, 拿着后半段url和title传递到join_url内, 进行正文详情页的信息获取
"""

from processing_url import processing_url
from hot_info import processing_info
from join_url import join_url

path = 'hot_word.csv'
url_list = processing_url(path)
for url in url_list:
	data = processing_info(url)
	print(data)
	try:
		join_url(data['title'], data['url'])
	except Exception as e:
		with open('log.txt', 'a', encoding='utf-8') as f:
			f.write(f'写入错误 => {e} => {data}')
