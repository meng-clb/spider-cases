import os.path
import requests

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	}

count = 0  # 计算共抓取了多少ID


def get_data(params):
	url = 'https://weibo.com/ajax/statuses/mymblog'
	res = requests.get(url, headers=headers, params=params)
	data = res.json()
	since_id = data['data']['since_id']
	params['since_id'] = since_id
	# print(params)
	return data


def processing_data(data):
	global count
	data_list = data['data']['list']  # 列表
	count += len(data_list)
	print(f'本次抓取请求{len(data_list)}个ID')
	print(f'累计抓取了{count}个ID')
	for data in data_list:
		try:
			mid = data['mid']  # 文章的mid, 通过mid去到详细的界面
			with open('all_mid.csv', 'a', encoding='utf-8') as f:
				f.write(mid)
				f.write('\n')
		except Exception as e:
			print('error===>', e)


if __name__ == '__main__':
	if os.path.exists('all_mid.csv'):
		os.remove('all_mid.csv')
	params = {
		'uid': 5652018762,
		'page': 1,  # 获取的页数
		'feature': 0,
	}
	# 获取到要抓取评论的帖子ID
	for i in range(1, 3):
		params['page'] = i
		data = get_data(params)
		processing_data(data)
