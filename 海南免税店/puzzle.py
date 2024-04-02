import base64
import json
import requests

"""
识别验证码图片 图鉴
"""


def base64_api(uname, pwd, img, watermark, typeid):
	with open(img, 'rb') as f:
		base64_data = base64.b64encode(f.read())
		b64 = base64_data.decode()
	with open(watermark, 'rb') as f:
		base64_data = base64.b64encode(f.read())
		b64_imageback = base64_data.decode()
	data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64,
	        'imageback': b64_imageback}
	result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
	if result['success']:
		return result["data"]["result"]
	else:
		# ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
		return result["message"]
	return ""


def axis():
	watermark = "watermark.jpg"
	puzzle = "puzzle.jpg"
	result = base64_api(uname='账号', pwd='密码', img=puzzle, watermark=watermark,
	                    typeid=18)
	# print(result)
	# print(type(result))
	# 拼凑验证码的滑动后的值
	# position = str(result.split(',')[0]) + '_' + str(1)
	# print(position)
	return result
