import time

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = execjs.compile(open('match_5.js', 'r', encoding='utf-8').read())

session = requests.Session()
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/124.0.0.0 Safari/537.36',
	'Referer':'https://match.yuanrenxue.cn/match/5',
	'X-Requested-With':'XMLHttpRequest'
}
session.headers = headers
session.cookies['sessionid'] = 'ar3ego7x9t7rgon4rdupvui57zheocko'
cookie = js_code.call('get_cookie')
# session.cookies['m'] = cookie
session.cookies['tk'] = '-8733569097663512141'
params = js_code.call('get_params')
api_url = 'https://match.yuanrenxue.cn/api/match/5'

for page in range(1, 6):
	params['page'] = page
	print(params)

	resp = session.get(api_url)
	print(resp.request.headers)
	print(resp.json())
