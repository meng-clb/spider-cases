import base64
import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

session = requests.Session()
login_url = 'https://www.to8to.com/new_login.php'
session.get(login_url)
captcha_url = 'https://apigwc2.to8to.com/cgi/user/pic/captcha/info'
data = {"type": '1'}

res = session.post(captcha_url, headers={
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}, data=json.dumps(data, separators=(',', ':')))
img_uid = res.json()['result']['verifyKey']
img_code = str(res.json()['result']['img']).split(',')[1]
with open('code.jpg', 'wb') as f:
	f.write(base64.b64decode(img_code))


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


img_path = "code.jpg"
code = base64_api(uname='账号', pwd='密码', img=img_path, typeid=3)

with open('参数逆向.js', 'r') as f:
	js_code = f.read()

context = execjs.compile(js_code)
# 账号密码
user = {
	'name': '账号',
	'pwd': '密码',
}
user = context.call('main', user['name'], user['pwd'])

data = {
	'referer': 'https://www.to8to.com/new_login.php',
	'msgCode': '',
	'val': user['name'],
	'password': user['pwd'],
	'imgCode': code,
	'imgUuid': img_uid
}

login_url = 'https://www.to8to.com/new_login.php'
resp = session.post(login_url, headers={
	'Content-Type':'application/x-www-form-urlencoded'
}, data=data)

print(resp.content.decode())
