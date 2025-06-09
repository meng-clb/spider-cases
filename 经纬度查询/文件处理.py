import re
import time

import requests

path = '未处理/起亚.csv'
manage_path = '未处理/location起亚.csv'

with open(path, 'r', encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		try:
			id = re.findall('\d+', line, re.S)[0]
			uname = str(re.findall('[a-zA-Z].*|[\u4e00-\u9fa5].*', line, re.S)[0]).strip()
			api_url = (f'https://api.map.baidu.com/geocoding/v3/?address={uname}&'
			       'output=json&ak=ZbFnW8vTS3WWQQ17wJowxvOnYlhp4NIY')
			# 发送请求并获取响应
			time.sleep(0.3)
			response = requests.get(api_url)
			result = response.json()
			print(result)
			# print(result)
			location = result.get('result', {}).get('location')
			# print(location)
			lng = location['lng']
			lat = location['lat']
			location = (f'{lng}, {lat}' or {})
			print(location)

			with open(manage_path, 'a', encoding='utf-8') as f:
				f.write(f'{id}, {uname}, {location}\n')

		except Exception as e:
			# print('获取失败')
			with open('log.txt', 'a', encoding='utf-8') as f:
				f.write(f'{id} {uname} 获取失败 ====> {e}\n')
