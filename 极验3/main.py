import subprocess
import time
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests
from until import *

session = requests.Session()
session.headers[
	'Agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36')

with open('first_w.js', 'r', encoding='utf-8') as f:
	first_js = f.read()

with open('第二次w.js', 'r', encoding='utf-8') as f:
	second_js = f.read()

with open('third_w.js', 'r', encoding='utf-8') as f:
	third_w = f.read()

# 第一次请求
print('===============第一次请求===================')
first_url = f'https://www.geetest.com/demo/gt/register-slide?t={get_now()}'
first_res = session.get(first_url)
first_data = first_res.json()
# 一次请求返回的所需参数
gt = first_data['gt']
challenge = first_data['challenge']
time.sleep(1)
# 第二次请求
print('===============第二次请求===================')

second_url = 'https://apiv6.geetest.com/gettype.php'
# 携带参数
params = {
	'gt': gt,
	'callback': f'geetest_{get_now()}'
}
session.headers['Referer'] = 'https://www.geetest.com/'
resp = session.get(second_url, params=params)
# print(resp.text)
time.sleep(1)

# 第三次请求
print('===============第三次请求===================')
three_url = 'https://apiv6.geetest.com/get.php'
content = execjs.compile(first_js)
first_w_res = content.call('first_w', gt, challenge)
# print(first_w_res)
params = first_w_res['params']
# print(params)
aeskey = first_w_res['aeskey']
# print(aeskey)
params['callback'] = f'geetest_{get_now()}'
resp = session.get(three_url, params=params)
third_data = manger_jsonp(resp.text)
cc = third_data['data']['c']
ss = third_data['data']['s']
# print(third_data)
time.sleep(1)

# 第四次请求
print('===============第四次请求===================')
fourth_url = 'https://api.geetest.com/ajax.php'
content = execjs.compile(second_js)
# second_w_res = content.call('second_w', gt, challenge, cc, ss, aeskey)
second_w_res = content.call('second_w', gt, challenge, cc, ss, aeskey)
print(second_w_res)
params = {
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"pt": "0",
	"client_type": "web",
	# "w": second_w_res['$_CEAR'],
	"w": second_w_res['$_CEEg'],
	"callback": f"geetest_{get_now()}"
}
# print(second_w_res['$_CEAR'])
resp = session.get(fourth_url, params=params)
# print(resp.text)
time.sleep(1)

print('===============第五次请求===================')
five_url = 'https://api.geetest.com/get.php'
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

resp = session.get(five_url, params=params)
five_data = manger_jsonp(resp.text)
# print(five_data)
challenge = five_data['challenge']  # 返回新的challenge
# 下载滑块图片
print('======> 开始下载图片 ')
bg_url = five_data['bg']
download_img('bg.jpg', bg_url, session)
fullbg_url = five_data['fullbg']
download_img('fullbg.jpg', bg_url, session)
slice_url = five_data['slice']
download_img('slice.jpg', bg_url, session)
# 处理滑块图片
print('======> 处理图片 ')
manger_back('bg.jpg')
manger_back('fullbg.jpg')

print('======> 处理滑块距离和轨迹 ')
juli = get_x()

guiji, shijian = get_slide_track(juli)
# print(jvli)
# print(guiji)
# print(shijian)
time.sleep(1)

print('===============第六次请求===================')
last_url = 'https://api.geetest.com/ajax.php'
content = execjs.compile(third_w)
third_w_res = content.call('third_w', gt, challenge, juli, guiji, shijian, cc, ss)
# third_w_res = content.call('three_w', guiji, gt, challenge, juli, shijian, cc, ss)
params['callback'] = f'geetest_{get_now()}'
resp = session.get(last_url, params=params)
last_data = manger_jsonp(resp.text)
print(last_data)
