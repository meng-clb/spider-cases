import asyncio
import os.path
import requests
import re
import aiofiles
import aiohttp

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


async def down_mp4(path, url):
	async with aiohttp.ClientSession(headers=headers) as session:
		while True:
			try:
				async with session.get(url, timeout=60) as resp:
					print(f'开始下载{url}')
					content = await resp.read()
					async with aiofiles.open(path, 'wb') as f:
						await f.write(content)
					break
			except:
				print(url, '下载失败')


def manger_m3u8(path, file_naem='index.m3u8'):
	"""
	处理m3u8文件, 用来合并视频
	:param path:  ts文件所在的路径
	:param file_naem:
	:return:
	"""
	file = open(os.path.join(path, file_naem), 'w', encoding='utf-8')
	with open('index.m3u8.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	i = 0
	for line in lines:
		if '#' in line:
			file.write(line)
			continue
		else:
			file.write(f't_{i}.ts' + '\n')
		i += 1


if __name__ == '__main__':
	get_m3u8_file()
	with open('m3u8.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	path = '歌手'
	if not os.path.exists(path):
		os.makedirs(path)
	loop = asyncio.get_event_loop()
	tasks = [down_mp4(os.path.join(path, f't_{i}.ts'), line.strip()) for i, line in
	         enumerate(lines)]
	loop.run_until_complete(asyncio.gather(*tasks))
