"""
1. 从csv文件内拿到链接
2. 这个链接就是referer
所有信息请求的url
info_url = 'https://m.weibo.cn/api/container/getIndex'
参数全部在referer内
3. 返回的json数据, 需要的信息都在返回的数据内
正文的详细链接, 新闻原来地址, 发布者主页
"""
import requests
import re
from urllib.parse import unquote

session = requests.Session()

# 请求一次, 保持一个cookie
session.get('https://m.weibo.cn/')

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
}


def processing_info(url):
	headers['Referer'] = url
	try:
		# 请求头参数获取
		s = unquote(headers['Referer'].split('?')[1])  # url解码
		containerid = re.findall('containerid=(.*)#', s, re.S)[0]
		print(containerid)
		stream_entry_id = re.findall('stream_entry_id=(\d+)', s, re.S)[0]
		isnewpage = re.findall('isnewpage=(\d+)', s, re.S)[0]
		extparam = re.findall('extparam=(.*)', s, re.S)[0]
		params = {
			'containerid': containerid + '#',  # 需要url解码
			'stream_entry_id': stream_entry_id,
			'isnewpage': isnewpage,
			'extparam': extparam,
			'luicode': '10000011',
			'lfid': '',
			'page_type': 'searchall',
		}
		# print(params)
	except Exception as e:
		with open('log.txt', 'a', encoding='utf-8') as f:
			f.write(f'params====> {e}\n')
	# url携带的参数全部在referer中保存
	url = 'https://m.weibo.cn/api/container/getIndex'
	try:
		res = session.get(url, headers=headers, params=params).json()

		# 热搜标题
		title = res['data']['cardlistInfo']['cardlist_title']
		# print(title)
		# 阅读量/讨论量
		midtext = res['data']['cardlistInfo']['cardlist_head_cards'][0]['head_data']['midtext']
		# print(midtext)
		# 主持人
		downtext = res['data']['cardlistInfo']['cardlist_head_cards'][0]['head_data']['downtext']
		# print(downtext)
		# 发布时间
		created_at = res['data']['cards'][0]['mblog']['created_at']
		# print(created_at)
		# 发布地址
		status_city = res['data']['cards'][0]['mblog']['status_city']
		# print(status_city)
		# 正文信息 需要处理
		text = res['data']['cards'][0]['mblog']['text']
		# 详细内容的url后半部分
		content_url = re.findall('href="/(.*)">全文</a>', text)[0]
		# join_url(title, content_url)
		# print(text)
		# print('============>', content_url)
		# 发布者用户信息
		user = res['data']['cards'][0]['mblog']['user']
		# 账户名
		screen_name = user['screen_name']
		# print(screen_name)
		# id
		id = user['id']
		# print(id)
		# 主页
		profile_url = user['profile_url']
		# print(profile_url)
		# 关注
		follow_count = user['follow_count']
		# print(follow_count)
		# 粉丝
		followers_count = user['followers_count']
		# print(followers_count)
		return {
			'title': title,
			'url': content_url
		}
	except Exception as e:
		with open('log.txt', 'a', encoding='utf-8') as f:
			f.write(f'error====> {e}\n')


if __name__ == '__main__':
	url = ('https://m.weibo.cn/search?containerid=100103type%3D1%26t%3D10%26q%3D%2312306%E5%9B%9E'
	       '%E5%BA%94%E9%AB%98%E9%93%81%E8%B5%B0%E5%88%B0%E5%8D%8A%E8%B7%AF%E4%B8%A4%E8%BD%A6%E4'
	       '%B9%98%E5%AE%A2%E4%BA%92%E6%8D%A2%23&stream_entry_id=31&isnewpage=1&extparam=seat%3D1'
	       '%26pos%3D0%26flag%3D2%26q%3D%252312306%25E5%259B%259E%25E5%25BA%2594%25E9%25AB%2598'
	       '%25E9%2593%2581%25E8%25B5%25B0%25E5%2588%25B0%25E5%258D%258A%25E8%25B7%25AF%25E4%25B8'
	       '%25A4%25E8%25BD%25A6%25E4%25B9%2598%25E5%25AE%25A2%25E4%25BA%2592%25E6%258D%25A2%2523'
	       '%26dgr%3D0%26c_type%3D31%26cate%3D5001%26band_rank%3D1%26stream_entry_id%3D31%26lcate'
	       '%3D5001%26filter_type%3Drealtimehot%26realpos%3D1%26display_time%3D1712231111'
	       '%26pre_seqid%3D171223111153600559203')
	data = processing_info(url)
	print(data)
