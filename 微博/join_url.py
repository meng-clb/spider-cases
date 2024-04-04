from urllib.parse import urljoin
import os

# 存储热搜榜的完整url
path = 'hot_url.csv'


def join_url(title, s):
	"""
	拼接url
	:param title: 对应的标题
	:param s: 要拼接url的后半部分
	:return: 保存到hot_url文件内
	"""
	url = urljoin('https://m.weibo.cn', s)
	with open(path, 'a', encoding='utf-8') as f:
		f.write(f'{title}=>{url}\n')




if __name__ == '__main__':
	s = 'status/5019393010699549'
	join_url('测试', s)
