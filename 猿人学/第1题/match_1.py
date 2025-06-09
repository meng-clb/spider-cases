import json
import time

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = execjs.compile(open('match_1.js', 'r', encoding='utf-8').read())
# m = js_code.call('get_m')
# print(m)

headers = {
	'host': 'match.yuanrenxue.cn',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/124.0.0.0 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest',
}

session = requests.Session()
session.headers = headers
session.cookies['sessionid'] = 'dq8r5hxkxm4u3mikrqjk3ado9qcr65hl'
sum_data = 0
air_data = 0
for page in range(1, 6):
	m = js_code.call('get_m')
	print(m)
	api_url = f'https://match.yuanrenxue.cn/api/match/1?page={page}&m={m}'
	resp = session.get(api_url)
	data = resp.json()
	print(data)
	data_list = data['data']
	air_data = len(data_list)
	for data in data_list:
		sum_data += int(data['value'])

avg = int(sum_data / (air_data * 5))
print(avg)
# 提交答案
answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={avg}&id=1'
resp = session.get(answer_url)
print(resp.text)
