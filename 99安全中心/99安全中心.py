import json
import time

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

js_code = open('99安全逆向.js', 'r', encoding='utf-8').read()
js = execjs.compile(js_code)
txtPassword = js.call('getMD5Value', '123456')
url = 'https://aq.99.com/AjaxAction/AC_userlogin.ashx'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
	"Referer": "https://aq.99.com/V3/NDUser_Login.htm"
}

params = {
	"CallBack": "jQuery112405089098277902757_1713106236066",
	"siteflag": "995",
	"nduseraction": "login",
	"txtUserName": "123456",
	"txtPassword": txtPassword,
	"checkcode": "9ep6",
	"Rnd": "0.794614970358898",
	"aws": "0ab7d61be45888b94915fe40dc7bcb68",
	"_": str(int(time.time() * 1000))
}

res = requests.get(url, headers=headers, params=params)
print(res.text)
