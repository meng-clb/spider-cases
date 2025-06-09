import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('空气质量.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

hXhY1B2Kd = context.call('params', '信阳')

url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
data = {
	'hXhY1B2Kd': hXhY1B2Kd
}

headers = {
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.aqistudy.cn/html/city_realtime.php?v=2.3'
}

resp = requests.post(url, headers=headers, data=data)
# print(resp.content.decode())
data = resp.content.decode()

data = context.call('decrypt', data)

print(json.loads(data))
