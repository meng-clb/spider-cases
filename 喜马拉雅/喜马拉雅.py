import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import requests
import execjs

with open('喜马拉雅.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)
sign = context.call('main')


url = 'https://www.ximalaya.com/revision/category/v2/albums'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/122.0.0.0 Safari/537.36',
	'Referer': 'https://www.ximalaya.com',
	'Xm-Sign': sign
}

data = {
	'pageNum': 2,
	'pageSize': 56,
	'sort': 1,
	'categoryId': 3,
}
resp = requests.get(url, headers=headers)
print(resp, resp.json())
