import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

url = 'https://openapi.dataoke.com/api/goods/get-goods-list'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/122.0.0.0 Safari/537.36',
	'Referer': 'http://mmpz.ttzhuijuba.com/'
}

with open('请求参数.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

page = 1  # 要抓取的页数
parm = {
	'version': 'v1.2.4',
	'appKey': '612bcfe884763',
	'pageId': page,  # 要抓取的页数
	'pageSize': 100,
	'sort': '0',
	'cids': '9',
	'tmall': 1,
	'commissionRateLowerLimit': 3,
	'hasCoupon': 1,
	'keyWords': '',
}
sign = context.call('main', parm)
parm['sign'] = sign
print(parm)

res = requests.get(url, headers=headers, params=parm)
print(res.json())
