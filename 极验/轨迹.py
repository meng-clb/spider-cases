#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/06 20:03
# @Author  : HMP
# @FileName: 轨迹生成2.py
# @Software: PyCharm
import random


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


print(get_slide_track2(120))
# for i in get_slide_track2(178):
# 	print(i, end=',')
# 	# print(',')
