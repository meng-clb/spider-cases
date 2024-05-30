import os.path
import requests
import re
import threading
from concurrent.futures import ProcessPoolExecutor, wait

headers = {
	'referer': 'https://yingshi.tv/',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


def get_m3u8_file():
	url = 'https://yingshi.tv/vod/play/id/202036/sid/1/nid/7/source/H.html'
	resp = requests.get(url, headers=headers)
	data = resp.text
	m3u8_url = re.findall('"url":"(.*?)",', data)[0]
	m3u8_url = m3u8_url.replace('\\', '')
	# print(m3u8_url)
	resp = requests.get(m3u8_url, headers=headers)
	data = resp.text
	with open('index.m3u8.txt', 'w', encoding='utf-8') as f:
		f.write(data)
	data_list = data.split('\n')
	with open('m3u8.txt', 'w', encoding='utf-8') as f:
		for data in data_list:
			if '#' in data:
				continue
			f.write(data)
			f.write('\n')


def down_mp4(path, url):
	while True:
		try:
			print(f'开始下载{url}')
			resp = requests.get(url, headers=headers, timeout=60)
			with open(path, 'wb') as file:
				file.write(resp.content)
			break
		except:
			print(url, '请求超时, 重新下载')


if __name__ == '__main__':
	get_m3u8_file()
	with open('m3u8.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	path = '歌手'
	if not os.path.exists(path):
		os.makedirs(path)
	# tasks = [down_mp4(os.path.join(path, f't_{i}.mp4'), line.strip()) for i, line in enumerate(
	# 	lines)]
	pool = ProcessPoolExecutor(61)
	task_list = [pool.submit(down_mp4, os.path.join(path, f't_{i}.ts'), line.strip()) for i, line
	             in enumerate(lines)]
	wait(task_list)
