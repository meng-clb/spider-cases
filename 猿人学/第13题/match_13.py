import re
import requests

headers = {
	'host': 'match.yuanrenxue.cn',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/124.0.0.0 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest',
}

session = requests.Session()
session.cookies['sessionid'] = 'dq8r5hxkxm4u3mikrqjk3ado9qcr65hl'
url = 'https://match.yuanrenxue.cn/match/13'
resp = session.get(url)
# print(resp.text)

cookie = re.findall(r'cookie=(.*)\+\';path=', resp.text, re.S)[0]
cookie = cookie.replace("('", '').replace("')", '').replace('+', '').split('=')[-1]
print(cookie)
session.cookies['yuanrenxue_cookie'] = cookie

session.headers = headers
sum_data = 0
for i in range(1, 6):
	url_api = f'https://match.yuanrenxue.cn/api/match/13?page={i}'
	resp = session.get(url_api)
	data = resp.json()
	# print(data)
	value_list = data['data']
	for value in value_list:
		sum_data += value['value']
print(sum_data)

# 提交答案
answer_url = f'https://match.yuanrenxue.cn/api/answers?answer={sum_data}&id=13'
resp = session.get(answer_url)
print(resp.text)
