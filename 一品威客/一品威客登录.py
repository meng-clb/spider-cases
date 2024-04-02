import base64
import json
import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

session = requests.Session()

with open('逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)

headers = context.call('main')
# print(headers)
headers['X-Request-Id'] = '855dce6b87a95fb2d89f7d44d341d167'
headers['Referer'] = 'https://www.epwk.com/login.html'
headers['Timestemp'] = str(headers['Timestemp'])
headers['User-Agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/123.0.0.0 Safari/537.36')

check_url = 'https://www.epwk.com/api/epwk/v1/captcha/show?channel=common_channel&base64=1'
res = session.get(check_url, headers=headers)
with open('code.jpg', 'wb') as f:
	f.write(base64.b64decode(res.json()['data']['base64']))


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


result = base64_api(uname='账号', pwd='密码', img='code.jpg', typeid=3)
print(result)

data = {
	'username': '账号',
	'password': '喵喵',
	'code': result,
	'hdn_refer': 'https://www.epwk.com/',
}

headers = context.call('main', data)
headers['X-Request-Id'] = '855dce6b87a95fb2d89f7d44d341d167'
headers['Referer'] = 'https://www.epwk.com/login.html'
headers['Timestemp'] = str(headers['Timestemp'])
headers['User-Agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/123.0.0.0 Safari/537.36')
login_url = 'https://www.epwk.com/api/epwk/v1/user/login'
resp = session.post(login_url, headers=headers, data=data)
print(resp.json())
