import json

import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs

with open('Hexin-V参数逆向.js', 'r', encoding='utf-8') as f:
	js_code = f.read()

context = execjs.compile(js_code)
v = context.call('main')
url = 'https://www.iwencai.com/customized/chart/get-robot-data'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",

	'Referer': 'https://www.iwencai.com/unifiedwap/result?w=%E6%B6%A8%E8%B7%8C%E5%B9%85%E5%A4%A7'
	           '%E4'
	           '%BA%8E%E7%AD%89%E4%BA%8E0%E5%B0%8F%E4%BA%8E%E7%AD%89%E4%BA%8E5%25%EF%BC%8C'
	           '&querytype=fund&addSign=1712064372700',
	'Content-Type': 'application/json',
	'Hexin-V': v,
}

data = {
	"source": "Ths_iwencai_Xuangu",
	"version": "2.0",
	"query_area": "",
	"block_list": "",
	"add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\","
	            "\"searchInfo\":true}",
	"question": "涨跌幅大于等于0小于等于5%，",
	"perpage": 50,
	"page": 1,
	"secondary_intent": "fund",
	"log_info": "{\"input_type\":\"typewrite\"}",
	"rsh": "Ths_iwencai_Xuangu_60laz4fqllja19ihrl5hwiysewytorjm"
}

resp = requests.post(url, headers=headers, data=json.dumps(data, separators=(',', ':')))
print(resp.json())
