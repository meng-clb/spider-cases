import requests

headers = {
	"Host": "match.yuanrenxue.cn",
	"Connection": "keep-alive",
	"Content-Length": "0",
	"Pragma": "no-cache",
	"Cache-Control": "no-cache",
	"sec-ch-ua": "Google Chrome;v=125, Chromium;v=125, Not.A/Brand;v=24",
	"sec-ch-ua-mobile": "?0",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/125.0.0.0 Safari/537.36",
	"sec-ch-ua-platform": "Windows",
	"Accept": "*/*",
	"Origin": "https://match.yuanrenxue.cn",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://match.yuanrenxue.cn/match/3",
	"Accept-Encoding": "gzip, deflate, br, zstd",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cookie": "Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1716470137; "
	          "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1716470137; tk=-317852247875011854; "
	          "sessionid=rva3d7b0hu3dwkrsh4zzb6u4l9sd83nd; "
	          "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1716470154; "
	          "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1716470176"
}

cookie = {
	'sessionid': 'rva3d7b0hu3dwkrsh4zzb6u4l9sd83nd'
}
session = requests.Session()
session.headers = headers

# res = session.post('https://match.yuanrenxue.cn/jssm', cookies=cookie, verify=False)
# print(res)
# print(res.cookies)

arr = []
for page in range(1, 6):
	session.post('https://match.yuanrenxue.cn/jssm', cookies=cookie)
	url = f'https://match.yuanrenxue.cn/api/match/3?page={page}'
	resp = session.get(url, cookies=cookie)
	data = resp.json()
	data = data['data']
	for val in data:
		v = val['value']
		arr.append(v)
print(arr)
some_data = max(arr, key=arr.count)

# 提交答案
answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={some_data}&id=3'
resp = session.get(answer_url)
print(resp.text)
