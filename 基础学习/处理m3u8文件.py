import os


def down_mp4(path, line):
	pass


def manger_m3u8(path, file_naem='index.m3u8'):
	"""
	处理ts文件
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


manger_m3u8('歌手')
