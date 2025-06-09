import time
import requests

url = 'https://m.weibo.cn/comments/hotflow'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	"X-Xsrf-Token": "59929b",
	"Referer": "https://m.weibo.cn/detail/4985092973790250",
	"Cookie": "_T_WM=95049019167; WEIBOCN_FROM=1110103030; "
	          "SCF=AgeJM777YtkQXhBxfjXY_uVdp8KmXrjDllSZpVNUquGFUhhGK2xwYnGtwb3"
	          "-IaNmGevYeCZ2lJVbtpSlqjzct4I.; "
	          "SUB=_2A25LCtmIDeRhGeFJ6lUV8SrFzz"
	          "-IHXVoZlNArDV6PUJbktAGLVb_kW1NfJpUVSGGc58LPgjwaZZ3Pqk3SsgvTpFJ; "
	          "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFqoXFo5XoNAhasjyWTkcU5NHD95QNS02NSh2X1KB0Ws4Dqcj6i--ciK.Xi-z4i--NiKLWiKnXi--fiK.7iKy2i--4iKn0i-i2i--Xi-zRiKy2i--Ri-88i-24i--NiK.Xi-2R; SSOLoginState=1712237016; ALF=1714829016; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D5019491971632145%26luicode%3D20000061%26lfid%3D5019491971632145%26uicode%3D20000061%26fid%3D5019491971632145; XSRF-TOKEN=59929b; mweibo_short_token=6eb998903d"
}
# 让max_id依次递减
params = {
	'id': '4985092973790250',
	'mid': '4985092973790250',
	'max_id_type': 0
}

max_id_list = []


def get_comment(data):
	i = 0
	data_list = data['data']['data']
	max_id = data['data']['max_id']
	max_id_list.append(max_id)
	for data in data_list:
		# TODO 一级评论
		# print('==========一级评论=========')
		i += 1
		time.sleep(0.3)
		created_at = data['created_at']  # 发布时间
		text = data['text']  # 评论内容
		user = data['user']
		uname = user['screen_name']  # name
		like_count = data['like_count']  # 点赞数量
		# print(f'=======>开始抓取第{i}条评论')
		with open('comment.csv', 'a', encoding='utf-8') as f:
			f.write(f'名字: {uname} 时间: {created_at}  点赞: {like_count} \n{text}  \n \n')



for i in range(1, 20):
	print(f'开始抓取第{i}页数据')
	res = requests.get(url, headers=headers, params=params)
	data = res.json()
	print(data)

	get_comment(data)
	print(max_id_list)
	# exit()
	# print('max_id==>', max_id_list[-1])
	params['max_id'] = max_id_list[-1]
	print(params)
