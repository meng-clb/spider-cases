import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('请求头.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

url = 'https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details?cid=508&param=%7B' \
      '%22cityId%22%3A%221004%22%2C%22serialId%22%3A%221661%22%7D'
cookie = "CIGUID=f5c1d33c1f0134b77967b272e1a83bea; isWebP=true; locatecity=411500; "
"auto_id=424c017777b43b4880682591fa8930a7; "
"UserGuid=f5c1d33c1f0134b77967b272e1a83bea; "
"Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1711883882; selectcity=411500; "
"selectcityid=1004; selectcityName=%E4%BF%A1%E9%98%B3; "
"bitauto_ipregion=125.45.144.25%3A%E6%B2%B3%E5%8D%97%E7%9C%81%E4%BF%A1%E9%98%B3%E5"
"%B8%82%3B1004%2C%E4%BF%A1%E9%98%B3%E5%B8%82%2Cxinyang; "
"Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1711895083"
data = context.call('main', cookie)

headers = {
	"Cid": "508",
	"Content-Type": "application/json;charset=UTF-8",

	"Origin": "https://car.yiche.com",
	"Pragma": "no-cache",
	"Referer": "https://car.yiche.com/siyucivic/peizhi/",
	"Sec-Ch-Ua": "Google Chrome;v=123, Not:A-Brand;v=8, Chromium;v=123",
	"Sec-Ch-Ua-Mobile": "?0",
	"Sec-Ch-Ua-Platform": "Windows",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-site",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"X-City-Id": "1004",
	"X-Ip-Address": "125.45.144.25",
	"X-Platform": "pc",
	"X-Sign": str(data['X-Sign']),
	"X-Timestamp": str(data['X-Timestamp']),  # str(data['X-Timestamp'])
	"X-User-Guid": data['X-User-Guid']
}
res = requests.get(url, headers=headers)

print(res.json())
