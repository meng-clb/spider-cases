import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests
from lxml import etree

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/122.0.0.0 Safari/537.36',
	'Referer': 'https://music.163.com/',
}

# 获取排行榜的歌曲id
url = 'https://music.163.com/discover/toplist?id=3779629'
resp = requests.get(url, headers=headers)
html = etree.HTML(resp.content.decode())
li_list = html.xpath('//ul[@class="f-hide"]/li')
songs_id_list = []  # 保存所有的歌曲id
for li in li_list:
	song_id = li.xpath('./a/@href')[0].split('=')[-1]
	songs_id_list.append(song_id)

# 获取歌曲url链接
url = ('https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token'
       '=7f841d17d5a1cc2672e080979b2dc659')

# 读取js代码
with open('网易云歌曲链接逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

# 执行js代码
compile = execjs.compile(js_code)

for song_id in songs_id_list:
	res = compile.call('main', song_id)

	data = {
		'params': res['encText'],
		'encSecKey': res['encSecKey']
	}

	resp = requests.post(url, headers=headers, data=data)
	song_url = resp.json()['data'][0]['url']  # 获取到歌曲的url, 可以进行下载
	print(song_url)
