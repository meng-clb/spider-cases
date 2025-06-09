import os.path
import requests
from concurrent.futures import ThreadPoolExecutor, wait

headers = {
	'accept': 'application/json, text/plain, */*',
	'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
	'cache-control': 'no-cache',
	'origin': 'https://www.doutub.com',
	'pragma': 'no-cache',
	'priority': 'u=1, i',
	'referer': 'https://www.doutub.com/',
	'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


def get_img_src(page):
	for i in range(1, page):
		params = {
			'isShowIndex': 'false',
			'typeId': '1',
			'curPage': str(i),
			'pageSize': '50',
		}
		url = 'https://api.doutub.com/api/bq/queryNewBq'
		print(f'开始获取第{i}页数据')
		resp = requests.get(url, params=params, headers=headers)
		data = resp.json()
		data = data['data']['rows']
		img_list = []
		for img in data:
			img_list.append(img['path'])
		yield img_list


def save_img(url):
	# print(f'开始获取{url}图片')
	path = 'img'
	if not os.path.exists(path):
		os.mkdir(path)
	img_name = url.split('-')[-1]
	with open(os.path.join(path, img_name), 'wb') as f:
		img_resp = requests.get(url, headers=headers)
		f.write(img_resp.content)


if __name__ == '__main__':
	pool = ThreadPoolExecutor()
	"""
	for url_list in get_img_src(5):
		p1 = pool.map(save_img, url_list)
	"""
	task_list = []
	for url_list in get_img_src(5):
		task_list.extend(pool.submit(save_img, url) for url in url_list)
	wait(task_list)
	print('over')
