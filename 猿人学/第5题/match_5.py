import time

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = execjs.compile(open('match_5.js', 'r', encoding='utf-8').read())

data = js_code.call('get_data')

session = requests.Session()

session.cookies['sessionid'] = 'oo7l1wu83aiv5jpr2387ggh616qxblpi'
session.cookies['RM4hZBv0dDon443M'] = data['cookie']

url_api = 'https://match.yuanrenxue.cn/api/match/5'
params = data['params']

arr = []
for i in range(1, 6):
	params['page'] = i

	resp = session.get(url_api, params=params)
	print(resp.text)
	data = resp.json()
	data = data['data']
	for val in data:
		v = val['value']
		arr.append(v)
print(arr)
arr.sort(reverse=True)
arr = arr[:5]
print(arr)
sum_data = 0
for i in arr:
	sum_data += int(i)

# 提交答案
# 'https://match.yuanrenxue.cn/api/answer?answer=123&id=5'
answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={sum_data}&id=5'
resp = session.get(answer_url)
print(resp.text)
