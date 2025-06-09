import random
import time
import re
import json
from urllib.parse import urljoin

import cv2


def get_now():
	"""
	获取当前系统时间
	:return:
	"""
	return int(time.time() * 1000)


def manger_jsonp(text):
	"""
	处理jsonp数据
	:param text:  jsonp数据
	:return: json
	"""
	data = re.findall('geetest_.*?\((.*)\)', text, re.S)[0]
	return json.loads(data)


def download_img(path, img_url, session):
	"""
	下载图片
	:param path: 图片的名字
	:param img_url: 图片拼接的url
	:return:
	"""
	url = urljoin('https://static.geetest.com', img_url)
	resp = session.get(url)
	with open(path, 'wb') as f:
		f.write(resp.content)


def manger_back(path):
	"""
	# 处理背景图片, 拼接会原来的给用户看的图片
	:param path: 要处理的图片路径
	:return:
	"""
	from PIL import Image
	old_img = Image.open(path)
	new_img = Image.new('RGB', (260, 160))
	Ut = [
		39,
		38,
		48,
		49,
		41,
		40,
		46,
		47,
		35,
		34,
		50,
		51,
		33,
		32,
		28,
		29,
		27,
		26,
		36,
		37,
		31,
		30,
		44,
		45,
		43,
		42,
		12,
		13,
		23,
		22,
		14,
		15,
		21,
		20,
		8,
		9,
		25,
		24,
		6,
		7,
		3,
		2,
		0,
		1,
		11,
		10,
		4,
		5,
		19,
		18,
		16,
		17
	]
	r = 160
	a = r // 2
	for _ in range(0, 52):
		c = Ut[_] % 26 * 12 + 1
		if 25 < Ut[_]:
			u = a
		else:
			u = 0
		# 获取一个区域  x1, y1, x2, y2
		l = old_img.crop((c, u, c + 10, u + a))
		x1 = _ % 26 * 10
		if 25 < _:
			y1 = a
		else:
			y1 = 0
		new_img.paste(l, (x1, y1))
	new_img.save(f'new_{path}')


def get_x():
	# opencv来完成计算
	# 读取两个图片
	bg = cv2.imread('new_bg.jpg')
	slice = cv2.imread('slice.jpg')

	# 做灰度处理
	bg = cv2.cvtColor(bg, cv2.COLOR_RGB2GRAY)
	slice = cv2.cvtColor(slice, cv2.COLOR_RGB2GRAY)

	# 图像边缘处理
	bg_can = cv2.Canny(bg, 255, 255)
	slice = cv2.Canny(slice, 255, 255)

	# 匹配图像的相似度,cv2.TM_CCOEFF_NORMED 参数固定
	r = cv2.matchTemplate(bg_can, slice, cv2.TM_CCOEFF_NORMED)

	# 获取匹配度最好的一个结果
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(r)
	x = maxLoc[0]
	y = maxLoc[1]

	return x


# 三代的极验轨迹..
def __ease_out_expo(sep):
	if sep == 1:
		return 1
	else:
		return 1 - pow(2, -10 * sep)


# 输入拖拽的距离 返回轨迹
def get_slide_track(distance):
	import random
	"""
	根据滑动距离生成滑动轨迹
	:param distance: 需要滑动的距离
	:return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
		x: 已滑动的横向距离
		y: 已滑动的纵向距离, 除起点外, 均为0
		t: 滑动过程消耗的时间, 单位: 毫秒
	"""

	if not isinstance(distance, int) or distance < 0:
		raise ValueError(
			f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
	# 初始化轨迹列表
	slide_track = [
		[random.randint(-50, -10), random.randint(-50, -10), 0],
		[0, 0, 0],
	]
	# 共记录count次滑块位置信息
	count = 150 + int(distance / 2)
	# 初始化滑动时间
	t = random.randint(50, 100)
	# 记录上一次滑动的距离
	_x = 0
	_y = 0
	for i in range(count):
		# 已滑动的横向距离
		x = round(__ease_out_expo(i / count) * distance)
		# 滑动过程消耗的时间
		t += random.randint(10, 20)
		if x == _x:
			continue
		slide_track.append([x, _y, t])
		_x = x
	slide_track.append([distance, 0, t])

	return slide_track, t


def get_slide_track2(x):
	# 初始化轨迹列表
	slide_track = [
		[random.randint(-50, -20), random.randint(-200, -100), 0],
		[0, 0, 0],
	]

	if x < 100:
		move_section = 1  # 如果移动距离小于100 那么move次数为x加上 7到20之间的数
	else:
		move_section = 2  # 如果移动距离小于100 那么move次数为x加上 2乘 7到20之间的数

	up_down = random.randint(0, 1)  # 确定一个方向 x大于0或x小于0
	y = 0  # 数组的y值
	time = random.randint(100, 180)  # 初始时间 即为第二个数组的时间  后续时间累加操作就可以了
	count = 0
	flag = 0
	repetition = int(x / 4)  # 重复x出现的个数
	frist_count = random.randint(6, 10)  # 前面y为0的数组个数
	for i in range(x * random.randint(move_section * 7, move_section * 21)):  # move_section 在这里起作用
		if i + 1 > x:  # 如果i+1要等于x 或者小于x 但这里基本上都是等于x
			break
		if up_down == 0:  # up_down如果大于0 那么这个轨迹就是y增轨迹
			if i > frist_count:
				if count == 0:
					y += random.randint(0, 1)
					count += 1
				if flag > random.randint(8, 10):
					count = 0
					flag = 0
				if i + 1 > int(x / 5) * 4:
					time += random.randint(20, 70)
				elif i + 1 > x - 3:
					time += random.randint(80, 180)
				else:
					time += random.randint(0, 5)
				slide_track.append([i + 1, y, time])
				flag += 1
				if random.randint(0, 1):
					if repetition:
						slide_track.append([i + 1, y, time + random.randint(0, 3)])
						flag += 1
						repetition -= 1
			else:  # 前面几个数组y都为0
				time += random.randint(0, 5)
				slide_track.append([i + 1, y, time])
				if random.randint(0, 1):
					if repetition:
						slide_track.append([i + 1, y, time + random.randint(0, 3)])
						repetition -= 1

		if up_down == 1:  # up_down如果小于0 那么这个轨迹就是y减轨迹
			if i > frist_count:
				if count == 0:
					y -= random.randint(0, 1)
					count += 1
				if flag > random.randint(8, 10):
					count = 0
					flag = 0
				if i + 1 > int(x / 5) * 4:
					time += random.randint(7, 40)
				elif i + 1 > x - 3:
					time += random.randint(80, 180)
				else:
					time += random.randint(0, 5)
				slide_track.append([i + 1, y, time])
				flag += 1
				if random.randint(0, 1):
					if repetition:
						slide_track.append([i + 1, y, time + random.randint(0, 3)])
						flag += 1
						repetition -= 1
			else:
				time += random.randint(0, 5)
				slide_track.append([i + 1, y, time])
				if random.randint(0, 1):
					if repetition:
						slide_track.append([i + 1, y, time + random.randint(0, 3)])
						repetition -= 1

	return slide_track, slide_track[-1][-1]

# print(get_slide_track(120))
