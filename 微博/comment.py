import time

import requests

url = 'https://m.weibo.cn/comments/hotflow'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"X-Xsrf-Token": "59929b",
	"Referer": "https://m.weibo.cn/status/5019491971632145",
	"Cookie": "_T_WM=95049019167; WEIBOCN_FROM=1110103030; "
	          "SCF=AgeJM777YtkQXhBxfjXY_uVdp8KmXrjDllSZpVNUquGFUhhGK2xwYnGtwb3"
	          "-IaNmGevYeCZ2lJVbtpSlqjzct4I.; "
	          "SUB=_2A25LCtmIDeRhGeFJ6lUV8SrFzz"
	          "-IHXVoZlNArDV6PUJbktAGLVb_kW1NfJpUVSGGc58LPgjwaZZ3Pqk3SsgvTpFJ; "
	          "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFqoXFo5XoNAhasjyWTkcU5NHD95QNS02NSh2X1KB0Ws4Dqcj6i--ciK.Xi-z4i--NiKLWiKnXi--fiK.7iKy2i--4iKn0i-i2i--Xi-zRiKy2i--Ri-88i-24i--NiK.Xi-2R; SSOLoginState=1712237016; ALF=1714829016; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D5019491971632145%26luicode%3D20000061%26lfid%3D5019491971632145%26uicode%3D20000061%26fid%3D5019491971632145; XSRF-TOKEN=59929b; mweibo_short_token=6eb998903d"
}
# 让max_id依次递减
params = {
	'id': '5019491971632145',
	'mid': '5019491971632145',
	'max_id': '0',  # 在返回的信息中保存有
	'max_id_type': 0
}

res = requests.get(url, headers=headers, params=params)
data = res.json()
i = 0
data_list = data['data']['data']
for data in data_list:
	# TODO 一级评论
	# print('==========一级评论=========')
	i += 1
	time.sleep(0.3)
	created_at = data['created_at']  # 发布时间
	text = data['text']  # 评论内容
	source = data['source']  # 用户ip
	user = data['user']
	id = user['id']  # 用户id
	uname = user['screen_name']  # name
	profile_url = user['profile_url']  # 用户主页
	# print(created_at, text, source, id, uname, profile_url)
	print(f'=======>开始抓取第{i}条评论')
	with open('comment.csv', 'a', encoding='utf-8')as f:
		f.write(f'{uname} {id} {created_at} {source} {profile_url} \n{text}\n')
	# TODO 二级评论
	# print('==========二级评论=========')
	try:
		comment_list = data['comments']
		for comment in comment_list:
			created_at = comment['created_at']  # 发布时间
			text = comment['text']  # 评论内容
			source = comment['source']  # 用户ip
			user = comment['user']
			id = user['id']  # 用户id
			uname = user['screen_name']  # name
			profile_url = user['profile_url']  # 用户主页
			# print(created_at, text, source, id, uname, profile_url)
			with open('comment.csv', 'a', encoding='utf-8') as f:
				f.write(f'{uname} {id} {created_at} {source} {profile_url} \n{text}\n')
	except Exception as e:
		print(e)