import requests
import json


def get_location_by_address(address, api_key):
	url = f"http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak={api_key}"
	response = requests.get(url)
	data = response.json()
	if data['status'] == 0:
		location = data['result']['location']
		return location['lng'], location['lat']
	else:
		print(f"Error: {data['message']}")
		return None, None


# 使用示例
api_key = ''
address = ''
lng, lat = get_location_by_address(address, api_key)
if lng and lat:
	print(f"经度: {lng}, 纬度: {lat}")