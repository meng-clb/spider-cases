import base64
import json
import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

url = 'https://user.wangxiao.cn/apis//login/passwordLogin'

session = requests.Session()
session.headers = {
	'User-Agent':
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/120.0.0.0 Safari/537.36'
}
# 使用session保持cookie
session.get('https://user.wangxiao.cn/login')
code_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
# 设置请求头格式  大坑
res = session.post(code_url, headers={
	'Content-Type': 'application/json;charset=UTF-8'
})
img_code = str(res.json()['data']).split(',')[1]
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
print('验证码是: ', code)

with open('中大网校密码逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

data = {
	'imageCaptchaCode': code,
	'password': '密码',
	'userName': '账号'
}
pwd = context.call('main', data['password'])
data['password'] = pwd
print(data)
# 请求头格式,大坑
res = session.post(url, headers={'Content-Type':'application/json;charset=UTF-8'},
                   data=json.dumps(data, separators=(',', ':')))
print(res.content.decode())
