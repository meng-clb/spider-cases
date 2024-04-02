import json
import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

headers = {
	"X-Requested-With": "XMLHttpRequest",
	"Referer": "https://www.kanzhun.com/search?",
	"Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

url = 'https://www.kanzhun.com/api_to/search/salary.json'

data = {
	'query': '操作员',
	'cityCode': 42,
	'industryCodes': '',
	'pageNum': 1,
	'limit': 15,
}

data = context.call('encrypt', data)


params = {
	'b': data['b'],
	'kiv': data['kiv']
}

# 返回加密的数据
res = requests.get(url, headers=headers, params=params)
en_data = res.content.decode()

de_data = context.call('decrypt', en_data, data['kiv'])
print(de_data)
