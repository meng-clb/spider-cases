import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js = execjs.compile(open('逆向.js', 'r', encoding='utf-8').read())
session = requests.Session()
session.headers[
	'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
"like Gecko) Chrome/123.0.0.0 Safari/537.36"

session.get('https://www.qimai.cn')
# print(session.cookies)

params = {
	'brand': 'paid',
	'device': 'iphone',
	'country': 'cn',
	'genre': '36',
	'date': '2024-04-15',
	'page': 4,
	'is_rank_index': 1,
	'snapshot': '09:48:06',
};

url = 'https://api.qimai.cn/rank/index'

new_url = js.call('fn', {'params': params, 'url': url})

resp = session.get(new_url, params=params)
# print(resp.request.url)
print(resp.json())
