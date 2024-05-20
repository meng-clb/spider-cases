import time

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = execjs.compile(open('match_5.js', 'r', encoding='utf-8').read())

data = js_code.call('get_data')


session = requests.Session()

session.cookies['sessionid'] = 'xpun7h7ejow0r61za8wyz673jqcioozk'
session.cookies['RM4hZBv0dDon443M'] = data['cookie']

url_api = 'https://match.yuanrenxue.cn/api/match/5'
params = data['params']
params['page'] = 2

resp = session.get(url_api, params=params)
print(resp.text)