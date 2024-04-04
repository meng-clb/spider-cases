import requests

url = 'https://m.weibo.cn/api/container/getIndex'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	'Referer': 'https://m.weibo.cn/p/index?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1'
	           '%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C'
	           '&show_cache_when_error=1&extparam=seat%3D1%26dgr%3D0%26filter_type%3Drealtimehot'
	           '%26cate%3D10103%26region_relas_conf%3D0%26pos%3D0_0%26lcate%3D1001%26mi_cid'
	           '%3D100103%26c_type%3D30%26display_time%3D1712116738%26pre_seqid'
	           '%3D171211673805607371183&luicode=20000174'
}

params = {
	'containerid': '106003type=25&t=3&disable_hot=1&filter_type=realtimehot',
	'title': '微博热搜',
	'show_cache_when_error': 1,
	'extparam': 'seat=1&dgr=0&filter_type=realtimehot&cate=10103&region_relas_conf=0&pos=0_0&lcate'
	            '=1001&mi_cid=100103&c_type=30&display_time=1712116738&pre_seqid'
	            '=171211673805607371183',
	'luicode': '20000174',
}

resp = requests.get(url, headers=headers, params=params)
data = resp.json()['data']['cards']

# 微博实时热搜
print('======================实时热搜================')
hot_word_list = data[0]['card_group']
with open('hot_word.csv', 'w', encoding='utf-8') as f:
	for hot in hot_word_list:
		title = hot['desc']
		href = hot['scheme']
		f.write(f'{title}=>{href}')
		f.write('\n')
print(hot_word_list)
# print('======================上升热搜================')
# time_hot_list = data[1]
# for hot in time_hot_list:
# 	title = hot['desc']
# 	href = hot['scheme']
# print(time_hot_list)
