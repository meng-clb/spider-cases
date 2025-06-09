"""
分析:
通过个人主页爬取所有发布的文章
1. 访问接口
https://m.weibo.cn/api/container/getIndex
携带参数:
{
	'type': 'uid',
	'value': '1699432410',  # 要抓取的up的主页id
	'containerid': '1076031699432410',
	'since_id': '5019483616575645'
}
携带参数在返回json中存放
containerid = data['cardlistInfo']['containerid']
since_id = data['cardlistInfo']['since_id']


2. 返回的json中通过text可以拿到正文的详细链接
data['cards']  # 列表
列表内是文章数据: 每次请求10篇文章
评论数量 = data['mblog']['comments_count']
发布时间: data['mblog']['created_at']
文章标题: data['mblog']['page_info']['page_title']
文章url: data['mblog']['page_info']['page_url']
文章发布方式: data['mblog']['source']
简介文章: data['mblog']['text']  # 从里边可以获取到正文的后半部分url
发布者信息====>
user = data['mblog']['user']
关注数量: user['follow_count']
粉丝数量: user['followers_count']
id: user['id']
uname: user['screen_name']
主页链接: user['profile_url']
"""
import math
import random
import re
import time

import requests
from dateutil import parser
from urllib.parse import urljoin

url = 'https://m.weibo.cn/api/container/getIndex'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	# "X-Xsrf-Token": "59929b",
	"Referer": "https://m.weibo.cn/status/5019491971632145",
	"Cookie": "_T_WM=95049019167; WEIBOCN_FROM=1110103030; "
	          "SCF=AgeJM777YtkQXhBxfjXY_uVdp8KmXrjDllSZpVNUquGFUhhGK2xwYnGtwb3"
	          "-IaNmGevYeCZ2lJVbtpSlqjzct4I.; "
	          "SUB=_2A25LCtmIDeRhGeFJ6lUV8SrFzz"
	          "-IHXVoZlNArDV6PUJbktAGLVb_kW1NfJpUVSGGc58LPgjwaZZ3Pqk3SsgvTpFJ; "
	          "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFqoXFo5XoNAhasjyWTkcU5NHD95QNS02NSh2X1KB0Ws4Dqcj6i--ciK.Xi-z4i--NiKLWiKnXi--fiK.7iKy2i--4iKn0i-i2i--Xi-zRiKy2i--Ri-88i-24i--NiK.Xi-2R; SSOLoginState=1712237016; ALF=1714829016; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D5019491971632145%26luicode%3D20000061%26lfid%3D5019491971632145%26uicode%3D20000061%26fid%3D5019491971632145; XSRF-TOKEN=59929b; mweibo_short_token=6eb998903d"
}


def get_data(params):
	res = requests.get(url, headers=headers, params=params)
	data = res.json()
	# 获取下次请求的params数据
	# print(data)
	containerid = data['data']['cardlistInfo']['containerid']
	since_id = data['data']['cardlistInfo']['since_id']
	params['containerid'] = containerid
	params['since_id'] = since_id
	return data


def get_count_text(params):
	res = requests.get(url, headers=headers, params=params)
	data = res.json()
	containerid = data['data']['tabsInfo']['tabs'][1]['containerid']  # 微博的总数量
	headSubTitleText = data['data']['tabsInfo']['tabs'][1]['headSubTitleText']  # 微博的总数量
	count = re.findall('全部微博\((\d+)\)', headSubTitleText, re.S)[0]
	params['containerid'] = containerid
	return int(count)


def processing_data(data):
	data_list = data['data']['cards']  # 列表

	for data in data_list:
		try:
			comments_count = data['mblog']['comments_count']  # 评论数量
			created_at = data['mblog']['created_at']  # 发布时间
			created_at = parser.parse(created_at).strftime("%Y-%m-%d %H:%M:%S")
			page_title = data['mblog']['page_info']['page_title']  # 文章标题
			# page_url = data['mblog']['page_info']['page_url']  # 文章url
			source = data['mblog']['source']  # 文章发布方式
			text = data['mblog']['text']  # 从里边可以获取到正文的后半部分url  #简介文章
			# 通过发布方式确定文章的类型, 是属于文字类还是视频类
			if source == '微博网页版':
				id = data['mblog']['id']
				text_url = f'https://m.weibo.cn/detail/{id}'
			else:
				page_url = data['mblog']['page_info']['page_url']
				text_url = page_url
			with open('home_chapter.csv', 'a', encoding='utf-8') as f:
				f.write(f'{page_title}=>{created_at}=>{comments_count}=>{source}=>{text_url}\n')
		except Exception as e:
			print('error===>', e)


if __name__ == '__main__':
	home_page = '1699432410'  # 要抓取的主页id, 官方媒体类更适合
	params = {
		'type': 'uid',
		'value': home_page,  # 要抓取的主页id
		'containerid': f'100505{home_page}',  # 从返回的json中取到
		# 'since_id': '5019483616575645'  # 第一次请求不需要, 后续从请求回来的链接中拿到
	}
	# print('请求前====>', params)
	count = get_count_text(params)
	# print('请求后===>', params)
	# print(math.ceil(count/10))
	# page是通过文章的总数量获取需要请求多少次, 每次请求10条数据
	page = math.ceil(count/10) + 1
	for i in range(1, page):
		time.sleep(random.random())  # 控制下访问速度
		print(f'============> 开始抓取第{i}页, 共抓取了{i*10}条数据')
		data = get_data(params)
		# print(params)
		processing_data(data)
