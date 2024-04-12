"""
1. 验证码获取
url = 'https://user.qunar.com/captcha/api/image'
请求参数:
params = {
	'k': '{en7mni(z',
	'p': 'ucenter_login',
	'c': 'ef7d278eca6d25aa6aec7272d57f0a9a',
	't': ''  # 时间戳
}

2. 登录请求
login_url = 'https://user.qunar.com/webApi/logins.jsp'  post
请求参数:
data = {
	'username': '17538263267',
	'password': 'abc123456',
	'remember': '1',
	'prenum': '86',
	'isHalfLogin': 'false',
	'vcode': code
}
"""
import time
import base64
import json

import requests

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"Referer": "https://hotel.qunar.com/"
}

session = requests.Session()
session.get('https://www.qunar.com/')


def base64_api(uname, pwd, img, typeid):
	with open(img, 'rb') as f:
		base64_data = base64.b64encode(f.read())
		b64 = base64_data.decode()
	data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
	result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
	if result['success']:
		return result["data"]["result"]
	else:
		# ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
		return result["message"]
	return ""


captcha_url = 'https://user.qunar.com/captcha/api/image'

params = {
	'k': '{en7mni(z',
	'p': 'ucenter_login',
	'c': 'ef7d278eca6d25aa6aec7272d57f0a9a',
	't': str(int(time.time() * 1000))
}
resp = session.get(captcha_url, headers=headers, params=params)
with open('code.jpg', 'wb') as f:
	f.write(resp.content)
img_path = "code.jpg"
code = base64_api(uname='账号', pwd='密码', img=img_path, typeid=3)

login_url = 'https://user.qunar.com/webApi/logins.jsp'
data = {
	'username': '账号',
	'password': '密码',
	'remember': '1',
	'prenum': '86',
	'isHalfLogin': 'false',
	'vcode': code
}
resp = session.post(login_url, headers=headers, data=data)
print(resp.json())
data = resp.json()
user_name = data['data']['qcookie'].split('.')[-1]
uuid = data['data']['scookie']
print(user_name, uuid)

# post请求
address = 'hangzhou'
from_data = '2024-04-12'
to_data = '2024-04-13'
t = int(time.time() * 1000)
url = (f'https://hotel.qunar.com/napi/hotHotelList?size=50&city={address}&fromDate={from_data}'
       f'&toDate={to_data}&time={t}')

data = {
	'bizVersion': "17",
	'userName': user_name,
	'uuid': uuid
}

resp = session.post(url, headers={
	'Content-Type': 'application/json;charset=UTF-8'
}, data=json.dumps(data, separators=(',', ':')))

print(resp.json())