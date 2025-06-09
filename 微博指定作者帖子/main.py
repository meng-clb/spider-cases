import json
import os.path

import re

import requests
from dateutil import parser

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	}

count = 0  # 计算共抓取了多少ID
chapter_csv_path = 'chapter_info_csv'  # 文章的信息csv文件夹
chapter_json_path = 'chapter_info_json'  # 文章的信息json文件夹
comment_csv_path = 'comment_csv_path'  # 评论csv文件夹
comment_json_path = 'comment_json_path'  # 评论json文件夹
if not os.path.exists(chapter_csv_path):
	os.makedirs(chapter_csv_path)

if not os.path.exists(chapter_json_path):
	os.makedirs(chapter_json_path)

if not os.path.exists(comment_csv_path):
	os.makedirs(comment_csv_path)

if not os.path.exists(comment_json_path):
	os.makedirs(comment_json_path)


def get_data(params):
	url = 'https://weibo.com/ajax/statuses/mymblog'
	res = requests.get(url, headers=headers, params=params)
	data = res.json()
	since_id = data['data']['since_id']
	params['since_id'] = since_id
	# print(params)
	return data


def processing_data(data):
	global count
	data_list = data['data']['list']  # 列表
	count += len(data_list)
	print(f'本次抓取请求{len(data_list)}个ID')
	print(f'累计抓取了{count}个ID')
	for data in data_list:
		try:
			attitudes_count = data['attitudes_count']  # 点赞数量
			comments_count = data['comments_count']  # 评论数量
			reposts_count = data['reposts_count']  # 转发数量
			created_at = data['created_at']  # 发布时间
			created_at = parser.parse(created_at).strftime("%Y-%m-%d %H:%M:%S")
			mid = data['mid']  # 文章的mid, 通过mid去到详细的界面
			try:
				region_name = data['region_name']  # 发布ip地址
			except:
				region_name = '空'
			with open(f'{os.path.join(chapter_csv_path, mid)}.csv', 'w', encoding='utf-8') as f:
				f.write(f'帖子ID=>发布时间=>点赞数量=>转发数量=>评论数量=>发布ip\n')
				f.write(f'{mid}=>{created_at}=>{attitudes_count}=>{reposts_count}=>'
				        f'{comments_count}=>{region_name}\n')
			with open(f'{os.path.join(chapter_json_path, mid)}.json', 'w', encoding='utf-8') as f:
				info = str({
					"帖子ID": f"{mid}",
					"发布时间": f"{created_at}",
					"点赞数量": f"{attitudes_count}",
					"转发数量": f"{reposts_count}",
					"评论数量": f"{comments_count}",
					"发布ip": f"{region_name}"
				})
				f.write(info.replace("'", '"'))
			with open('all_mid.csv', 'a', encoding='utf-8') as f:
				f.write(mid)
				f.write('\n')
		except Exception as e:
			print('error===>', e)


def get_comment(mid):
	info = {}
	print(f'开始获取ID:{mid}的评论')
	headers['Referer'] = f"https://m.weibo.cn/detail/{mid}"
	url = 'https://m.weibo.cn/comments/hotflow'
	params = {
		'id': mid,
		'mid': mid,
		'max_id_type': 0,
	}
	resp = requests.get(url, headers=headers, params=params, timeout=60)
	try:
		data = resp.json()
		# print(data)
		data_list = data['data']['data']
		max_id = data['data']['max_id']  # 进行下次请求评论的参数
		# TODO 一般请求一次刚好是20条评论, 如果不是, 请查看帖子评论是否够20条,
		#  如果够, 可获取到maxid,携带maxid进行下次请求
		with open(f'{os.path.join(comment_csv_path, mid)}.csv', 'w', encoding='utf-8') as f:
			f.write(f'作者=>发布时间=>发布ip=>点赞数量=>评论内容\n')
			for data in data_list:
				content = data['text']  # 评论内容
				ls = re.findall('<(.*?)>', content)
				for li in ls:
					content = content.replace(f'<{li}>', '_')  # 处理评论的信息, 去除特殊符号
				like_count = data['like_count']  # 点赞数量
				created_at = data['created_at']  # 评论时间
				created_at = parser.parse(created_at).strftime("%Y-%m-%d %H:%M:%S")
				ip = data['source']  # 评论ip
				user = data['user']['screen_name']  # 发布者名字
				# print(f'{user}=>{created_at}=>{ip}=>{like_count}=>{content}')
				f.write(f'{user}=>{created_at}=>{ip}=>{like_count}=>{content}\n')
				info[f'{user}'] = {
					"作者": f"{user}",
					"发布时间": f"{created_at}",
					"发布ip": f"{ip}",
					"点赞数量": f"{like_count}",
					"评论内容": f"{content}",

				}
			with open(f'{os.path.join(comment_json_path, mid)}.json', 'w', encoding='utf-8') as \
					file:
				file.write(str(info).replace("'", '"'))
		return True
	except Exception as e:
		print(f'error ==> {mid} 请求错误, 请更新cookie或者查找别的问题')
		return False


if __name__ == '__main__':
	if os.path.exists('all_mid.csv'):
		os.remove('all_mid.csv')
	params = {
		'uid': 5652018762,
		'page': 1,  # 获取的页数
		'feature': 0,
	}
	# 获取到要抓取评论的帖子ID
	for i in range(1, 3):
		params['page'] = i
		data = get_data(params)
		processing_data(data)
	with open('all_mid.csv', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	for line in lines:
		while True:
			if get_comment(line.strip()):
				break
