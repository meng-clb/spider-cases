import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('数据获取.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

url = 'https://www.endata.com.cn/API/GetData.ashx'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

data = {
	'year': '2024',
	'MethodName': 'BoxOffice_GetYearInfoData'
}

res = requests.post(url, headers=headers,data=data)
data = res.content.decode()
# print(data)

resp = context.call('shell', data)
print(resp)
