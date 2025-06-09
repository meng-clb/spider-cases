import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

url = 'https://capi.jiansheku.com/nationzj/enterprice/expire'
with open('建设库逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

for page in range(1, 5):
	res = context.call('main', page)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
		              'like Gecko) Chrome/122.0.0.0 Safari/537.36',
		'Referer': 'https://www.jiansheku.com/',
		'Content-Type': 'application/json;charset=UTF-8',
		'Sign': res['sign'],
		'Timestamp': str(res['timestamp']),
	}

	data = {
		'eid': '',
		'achievementQueryType': 'and',
		'achievementQueryDto': [],
		'personnelQueryDto': {
			'queryType': 'and',
		},
		'aptitudeQueryDto': {
			'hasAptitude': 1,
			'startAptitudeValidityDate': '2024-03-25',
			'endAptitudeValidityDate': '2024-04-25',
			'aptitudeDtoList': [
				{
					'codeStr': '',
					'queryType': 'and',
					'aptitudeType': 'qualification',
				},
			],
			'aptitudeSource': 'new',
		},
		'page': {
			'page': page,
			'limit': '20',
			'order': 'desc',
		},
	}

	resp = requests.post(url, headers=headers, data=json.dumps(data, separators=(',', ':')))
	# resp = requests.post(url, headers=headers)
	print(f'第{page}页数据=============>\n', resp.json())
