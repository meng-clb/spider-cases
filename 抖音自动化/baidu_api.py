import base64
import urllib
import requests


# "access_token":"24.2ed0e20c119c2d9818e858115745c3db.2592000.1718614712.282335-72053907"
def get_tag(path):
	url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=24" \
	      ".2ed0e20c119c2d9818e858115745c3db.2592000.1718614712.282335-72053907"

	# image 可以通过 get_file_content_as_base64("C:\fakepath\yadang.png",True) 方法获取
	payload = f'image={get_file_content_as_base64(path + ".png", True)}' \
	          f'&detect_direction=false&detect_language=false&paragraph=false&probability=false'

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	resp = response.json()
	tags = resp['words_result']
	with open(path + '.csv', 'w', encoding='utf-8') as f:
		for tag in tags:
			f.write(tag['words'])
			f.write('\n')
	# print(resp)
	print('图片解析完成')


def get_file_content_as_base64(path, urlencoded=False):
	"""
	获取文件base64编码
	:param path: 文件路径
	:param urlencoded: 是否对结果进行urlencoded
	:return: base64编码信息
	"""
	with open(path, "rb") as f:
		content = base64.b64encode(f.read()).decode("utf8")
		if urlencoded:
			content = urllib.parse.quote_plus(content)
	return content


if __name__ == '__main__':
	path = '亚当'
	get_tag(path)
