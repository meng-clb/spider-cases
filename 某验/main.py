import subprocess
import time
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests
from until import *

session = requests.Session()
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/124.0.0.0 Safari/537.36'
}
session.get('https://www.geetest.com/demo/slide-popup.html', headers=headers)

first_js = open('first_w_.js', 'r', encoding='utf-8').read()
second_js = open('second_w_.js', 'r', encoding='utf-8').read()
# third_js = open('third_w_.js', 'r', encoding='utf-8').read()
third_js = open('第三次w.js', 'r', encoding='utf-8').read()

print('============== 第一次请求 =================')
url = f'https://www.geetest.com/demo/gt/register-slide?t={get_now()}'
resp = session.get(url, headers=headers)
data = resp.json()
gt = data['gt']
challenge = data['challenge']

print('============== 第二次请求 =================')
url = 'https://apiv6.geetest.com/gettype.php'
params = {
	'gt': gt,
	'callback': f'geetest_{get_now()}'
}

resp = session.get(url, headers=headers, params=params)

manger_jsonp(resp.text)
# print(resp.text)

print('============== 第三次请求 =================')
url = 'https://apiv6.geetest.com/get.php'
js_code = execjs.compile(first_js)
js_res = js_code.call('first_w', gt, challenge)
# print(js_res['w'])
# exit()
params = {
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"pt": "0",
	"client_type": "web",
	"w": js_res['w'],
	"callback": f"geetest_{get_now()}"
}

resp = session.get(url, headers=headers, params=params)
data = manger_jsonp(resp.text)
# print(data)
aeskey = js_res['aeskey']
c = data['data']['c']
s = data['data']['s']
print(aeskey)
print(c, s)

print('============== 第四次请求 =================')
url = 'https://api.geetest.com/ajax.php'
js_code = execjs.compile(second_js)
js_res = js_code.call('get_second_w', gt, challenge, c, s, aeskey)
params = {
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"pt": "0",
	"client_type": "web",
	"w": js_res['$_CEAR'],
	"callback": f"geetest_{get_now()}"
}
resp = session.get(url, headers=headers, params=params)
print(resp.text)

print('============== 第五次请求 =================')
url = 'https://api.geetest.com/get.php'
params = {
	"is_next": "true",
	"type": "slide3",
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"https": "true",
	"protocol": "https://",
	"offline": "false",
	"product": "popup",
	"api_server": "api.geetest.com",
	"isPC": "true",
	"autoReset": "true",
	"width": "100%",
	"callback": f"geetest_{get_now()}"
}

resp = session.get(url, headers=headers, params=params)
data = manger_jsonp(resp.text)
print(data)
challenge = data['challenge']
s = data['s']
bg = data['bg']
fullbg = data['fullbg']
slice = data['slice']

print('============== 下载图片 =================')
download_img('bg.jpg', bg, session)
download_img('fullbg.jpg', bg, session)
download_img('slice.jpg', bg, session)

print('============== 处理图片 =================')
manger_back('bg.jpg')
manger_back('fullbg.jpg')

jvli = get_x()
guiji, shijian = get_slide_track(jvli)
# print(guiji, shijian)
# exit()
print('============== 第六次请求 =================')
url = 'https://api.geetest.com/ajax.php'
js_code = execjs.compile(third_js)
# js_res = js_code.call('third_w', gt, challenge, jvli, guiji, shijian, c, s)
js_res = js_code.call('three_w', guiji, gt, challenge, jvli, shijian, c, s)
params = {
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"$_BCN": "0",
	"client_type": "web",
	"w": js_res['w'],
	"callback": f"geetest_{get_now()}"
}

resp = session.get(url, headers=headers, params=params)
print(resp.text)
