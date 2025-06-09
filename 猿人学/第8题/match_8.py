import base64

import requests
from lxml import etree
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os
import urllib

session = requests.Session()
session.cookies['sessionid'] = '9a4a0jq8dfjnoaqwigo4p2noqrazvitx'


def get_chapter():
	chapter_url = 'https://match.yuanrenxue.cn/api/match/8_verify'
	resp = session.get(chapter_url)
	# print(resp.json())
	data = resp.json()
	data = data['html']
	html = etree.HTML(data)
	p = html.xpath('//p//text()')
	# print(p)
	img = html.xpath('//img/@src')[0]
	# print(data)
	img = img.replace('data:image/jpeg;base64,', '')
	with open('chapter.jpg', 'wb') as f:
		f.write(base64.b64decode(img))
	print('图片保存成功')
	return p


def process_captcha_image(input_image_path='chapter.jpg', output_image_path='out.jpg'):
	# 读取图像
	image = cv2.imread(input_image_path)

	# 将图像转换为灰度图像
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# 二值化处理
	_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

	# 去除干扰线
	# 定义一个结构元素
	kernel = np.ones((1, 1), np.uint8)

	# 进行形态学操作（膨胀，然后腐蚀）
	processed_image = cv2.dilate(binary, kernel, iterations=1)
	processed_image = cv2.erode(processed_image, kernel, iterations=1)

	# 进一步增强文字
	processed_image = cv2.morphologyEx(processed_image, cv2.MORPH_CLOSE, kernel)

	# 保存处理后的图像
	cv2.imwrite(output_image_path, processed_image)


def split_image(image_path='out.jpg', rows=3, cols=3):
	# 读取图像
	image = cv2.imread(image_path)
	if image is None:
		raise ValueError(f"无法读取图像文件: {image_path}")

	# 获取图像尺寸
	height, width = image.shape[:2]
	block_height = height // rows
	block_width = width // cols

	# 创建输出目录
	# if not os.path.exists(output_dir):
	# 	os.makedirs(output_dir)

	# 分割并保存图像块
	block_count = 1
	for i in range(rows):
		for j in range(cols):
			block = image[i * block_height:(i + 1) * block_height,
			        j * block_width:(j + 1) * block_width]
			block_path = f'{block_count}.png'
			cv2.imwrite(block_path, block)
			block_count += 1


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
	print('图片解析完成')
	if len(tags) == 0:
		return ''
	print(tags)
	return tags[0]['words']


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
	p = get_chapter()
	print(p)
	process_captcha_image()
	split_image()
	chapter_list = []
	for i in range(1, 10):
		tags = get_tag(str(i))
		if tags == '':
			chapter_list.append('')
		else:
			chapter_list.append(tags)
	print(chapter_list)


