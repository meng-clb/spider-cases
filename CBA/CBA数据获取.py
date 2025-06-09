import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

# js = execjs.compile(open('CBA逆向.js', 'r', encoding='utf-8').read())
node = execjs.get()
ctx = node.compile(open('CBA逆向.js', 'r', encoding='utf-8').read())

url = ('https://data-server.cbaleague.com/api/team-match-datas/team-entirety-list?pageNumber=1'
       '&pageSize=60')
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.cbaleague.com/',
	'Content-Type': 'application/json;charset=UTF-8'
}
data = {
	"season": 2022,
	"matchTypeId": 1,
	"acrossTeamId": 'null',
	"sortStyle": "1",
	"opponentScore": 'null'
}

res = requests.post(url, headers=headers, data=json.dumps(data, separators=(',', ':')))
data = res.content.decode()
print(type(data))
fucName = 'xxx({0})'.format(data)
result = ctx.eval(fucName)
# result = js.call('main', data)
print(result)
