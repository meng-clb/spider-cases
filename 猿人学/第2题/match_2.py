import subprocess
import time
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests

session = requests.Session()
# session.cookies['sessionid'] = 'cezhfxpx1km6vabxhdp0qfr09vuntnyz'
js_code = execjs.compile(open('match_2.js', 'r', encoding='utf-8').read())
cookie = js_code.call('get_cookie')
cookie = cookie.split('=')[1].split(' ')[0].split(';')[0]
print(cookie)
headers = {
	"Referer": "https://match.yuanrenxue.cn/match/2",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/124.0.0.0 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"
}

cookies = {
	"sessionid": "cezhfxpx1km6vabxhdp0qfr09vuntnyz",
	"yuanrenxue_cookie": "1714992000|l9g33BhppfNCsZf4ATu1OdWkl0moIYtjn2yALyd5neTss07",
	"m": cookie,
}
# url = 'https://match.yuanrenxue.cn/match/2'
sum_data = 0
for page in range(1, 6):
	url = f'https://match.yuanrenxue.cn/api/match/2?page={page}'
	print(url)

	resp = session.get(url, headers=headers, cookies=cookies)
	# print(headers['Cookie'])
	page = resp.json()
	print(page)
	for data in page['data']:
		sum_data += data['value']

print(sum_data)

answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={sum_data}&id=2'
resp = session.get(answer_url, headers=headers, cookies=cookies)
print(resp.text)
