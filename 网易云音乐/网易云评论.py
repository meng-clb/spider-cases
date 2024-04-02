import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests
from lxml import etree

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/122.0.0.0 Safari/537.36',
	'Referer': 'https://music.163.com/song?id=2136351674',
}


# 获取评论的接口
url = ('https://music.163.com/weapi/comment/resource/comments/get?csrf_token'
       '=7f841d17d5a1cc2672e080979b2dc659')

# 读取js代码
with open('网易云评论.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

# 执行js代码
compile = execjs.compile(js_code)

res = compile.call('comment')

data = {
	'params': res['encText'],
	'encSecKey': res['encSecKey']
}

resp = requests.post(url, headers=headers, data=data)
print(resp.json())
