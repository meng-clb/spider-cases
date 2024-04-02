import base64
import json
from puzzle import axis
import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('登录逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

headers = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 ('
	              'KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
	'Referer': 'https://m.hltmsp.com/',
}


def save_img(str, path):
	byte = base64.b64decode(str.split(',')[1])
	with open(f'{path}.jpg', 'wb') as f:
		f.write(byte)


# 第一次请求
data = context.call('one')
login_url = 'https://api.hltmsp.com/user/index/login'
res = requests.post(login_url, headers=headers, data=data)
print('第一次 ', data)
print(res.json())

# 第二次请求
data = context.call('two')
get_code_url = 'https://api.hltmsp.com/slider/index/get-code'
res = requests.get(get_code_url, headers=headers, params=data)
ident = res.json()['data']['ident']  # 传入下一个请求使用
puzzle = res.json()['data']['puzzle']  # 图片
save_img(puzzle, 'puzzle')  # 保存滑动验证码的图片
watermark = res.json()['data']['watermark']  # 图片
save_img(watermark, 'watermark')  # 保存滑动验证码的图片
y = res.json()['data']['y']  # 拿到验证码返回的y轴坐标
x = axis().split(',')[0]  # 通过图鉴拿到x轴坐标
position = f'{x}_{y}'  # 拼接滑动验证的坐标
print('第二次 ', data)
# print(res.json())

# 第三次请求
parm = context.call('three', ident, position)
check_url = 'https://api.hltmsp.com/slider/index/check'
resp = requests.get(check_url, headers=headers, params=parm)
print('第三次 ', data)
print(resp.json())

# 第四次请求
data = context.call('four', ident)
login_url = 'https://api.hltmsp.com/user/index/login'
res = requests.post(login_url, headers=headers, data=data)
print('第四次 ', data)
print(res.json())
