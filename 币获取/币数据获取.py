import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

url = 'https://api.mytokenapi.com/ticker/currencyranklist'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"Referer": "https://www.mytokencap.com/",
	'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
}

data = context.call('main')

params = {
	"pages": "1,1",
	"sizes": "100,100",
	"subject": "market_cap",
	"language": "en_US",
	"timestamp": data['timestamp'],
	"code": data['code'],
	"platform": "web_pc",
	"v": "0.1.0",
	"legal_currency": "USD",
	"international": "1"
}

print(params)
res = requests.get(url, headers=headers, params=params)
print(res.json())
