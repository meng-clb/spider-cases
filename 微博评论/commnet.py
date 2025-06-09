import random
import re
import time

import pandas as pd
import requests
from datetime import datetime
from openpyxl import Workbook
from datetime import datetime

# 读取 Excel 文件
excel_file = '微博.xlsx'  # 替换为你的 Excel 文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名
column_name = '微博链接'  # 替换为你要读取的列名

# 使用 pandas 读取 Excel 文件
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# 提取指定列数据
column_data = data[column_name]

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"X-Xsrf-Token": "59929b",
	"Referer": "https://m.weibo.cn/detail/4985092973790250",
	}

csv_path = ''
excel_path = ''


def get_id(mid):
	"""
	传递url携带的mid,
	:param mid: url的后半部分
	:return: 返回评论请求参数携带的id
	"""
	url = 'https://weibo.com/ajax/statuses/show'
	# 请求参数
	params = {
		'id': mid,
		'locale': 'zh-CN'
	}
	res = requests.get(url, headers=headers, params=params)
	return res.json()['id']


def write_multiple_to_excel(data):
	wb = Workbook()
	ws = wb.active

	# 写入表头
	ws.append(["名字", "时间", "点赞", "评论"])

	# 循环写入数据
	for item in data:
		name = item["name"]
		time_str = item["time"]
		likes = item["likes"]
		comment = item["comment"]
		ws.append([name, time_str, likes, comment])

	# 保存Excel文件
	wb.save(excel_path)


def convert_to_normal_time(time_str):
	# 解析时间字符串
	time_format = "%a %b %d %H:%M:%S %z %Y"
	parsed_time = datetime.strptime(time_str, time_format)
	# 格式化成正常时间格式
	normal_time = parsed_time.strftime("%Y-%m-%d %H:%M:%S")
	return normal_time


def get_comment(data):
	i = 0
	data_list = data['data']['data']
	max_id = data['data']['max_id']
	max_id_list.append(max_id)
	for data in data_list:
		# Turl_x += 1ODO 一级评论
		# print('==========一级评论=========')
		i += 1
		time.sleep(random.uniform(0, 0.5))
		created_at = data['created_at']  # 发布时间
		created_at = convert_to_normal_time(created_at)
		text = data['text']  # 评论内容
		try:
			text.index('<a')
			a = re.findall("<a.*</a>", text)[0]
			b = re.findall(">@(.*?)</a>", text)[0]
			text = text.replace(a, b)
		except Exception as e:
			pass
		user = data['user']
		uname = user['screen_name']  # name
		like_count = data['like_count']  # 点赞数量
		# print(f'=======>开始抓取第{i}条评论')
		com_data = {'name': uname, 'time': created_at, 'likes': like_count, 'comment': text}
		excel_data.append(com_data)
		write_multiple_to_excel(excel_data)
		with open(csv_path, 'a', encoding='utf-8') as f:
			f.write(f'{uname}=>{created_at}=>{like_count}=>{text}\n')


if __name__ == '__main__':
	max_id_list = []
	url_x = 0
	for url in column_data:
		url_x += 1
		# print(url_x)
		if url_x < 149:
			continue

		url_u = url
		print(f'第{url_x}条连接获取=======================')
		with open('url_list.csv', 'a', encoding='utf-8') as f:
			f.write(f'{url}\n')
		excel_data = []
		mid = str(url).split('/')[-1]
		csv_path = f'./comment/{mid}.csv'
		excel_path = f'./excel/{mid}.xlsx'
		id = get_id(mid)
		headers['Referer'] = f'https://m.weibo.cn/detail/{id}'
		# print(headers['Referer'])
		params = {
			'id': id,
			'mid': id,
			'max_id_type': 0
		}
		# print(params)
		for i in range(1, 1000):
			url = 'https://m.weibo.cn/comments/hotflow'
			print(f'开始抓取第{i}页数据')
			res = requests.get(url, headers=headers, params=params)
			data = res.json()
			# print(data)
			try:
				get_comment(data)
			except Exception as e:
				with open('log.txt', 'a', encoding='utf-8') as f:
					f.write(f'{url_u}抓取到{i}页数据\n{e}\n\n')
				break
			if max_id_list[-1] == 0:
				break
			params['max_id'] = max_id_list[-1]
			print(max_id_list)
			max_id_list.clear()
