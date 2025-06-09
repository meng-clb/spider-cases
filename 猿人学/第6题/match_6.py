import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = execjs.compile(open('match_6.js', 'r', encoding='utf-8').read())

headers = {

}
cookie = {
	'sessionid': 'oo7l1wu83aiv5jpr2387ggh616qxblpi'
}
session = requests.Session()
session.cookies['sessionid'] = 'oo7l1wu83aiv5jpr2387ggh616qxblpi'
arr = []
for i in range(1, 6):
	params = js_code.call('get_params', i)  # TODO page是页数
	url = 'https://match.yuanrenxue.cn/api/match/6'
	resp = session.get(url, headers=headers, params=params)
	data = resp.json()
	data = data['data']
	for val in data:
		v = val['value']
		arr.append(int(v))
		two = int(v) * 8  # 二等奖
		one = int(v) * 15  # 一等奖
		arr.append(two)
		arr.append(one)

sum_data = 0
for val in arr:
	sum_data += val

print(sum_data)
# 提交答案
answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={sum_data}&id=6'
resp = session.get(answer_url)
print(resp.text)