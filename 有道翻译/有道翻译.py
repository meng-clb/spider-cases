import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

session = requests.Session()
with open('sign逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

headers = {
	"Referer": "https://fanyi.youdao.com/",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=715910561.6620061; '
	         'OUTFOX_SEARCH_USER_ID=682151595@39.144.24.158; _ga=GA1.2.2035400367.1703646852; '
	         'DICT_DOCTRANS_SESSION_ID=MzNmMzVlNTEtNWY3OC00YmJkLWFkZmUtMDQ4NmNkNGNmNmNm'
}

js_res = context.call('gen_sign')

data = {
	"i": "哈",
	"from": "auto",
	"to": "",
	"dictResult": "true",
	"keyid": "webfanyi",
	"sign": js_res['sign'],
	"client": "fanyideskweb",
	"product": "webfanyi",
	"appVersion": "1.0.0",
	"vendor": "web",
	"pointParam": "client,mysticTime,product",
	"mysticTime": str(js_res['mysticTime']),
	"keyfrom": "fanyi.web",
	"mid": "1",
	"screen": "1",
	"model": "1",
	"network": "wifi",
	"abtest": "0",
	"yduuid": "abcdefg"
}

url = 'https://dict.youdao.com/webtranslate'
resp = requests.post(url, headers=headers, data=data)
# 拿到返回的加密数据
data = resp.content.decode()

js_res = context.call('decrypt', data)
print(js_res)