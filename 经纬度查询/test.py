"""
1. 读取文件每一行
2. 然后处理长度问题
3. 处理文件的写入
"""
name = 'location起亚'
c_name = '起亚'
path = f'./未处理/{name}.csv'
with open(path, 'r', encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		# print(line)
		data = line.split(',')
		id = data[0]
		uname = data[1]

		try:
			l = "{:.6f}".format(float(data[-2]))
			r = "{:.6f}".format(float(data[-1]))
			with open(f'{c_name}.csv', 'a', encoding='utf-8') as f:
				f.write(f'{id}, {uname}, {l}, {r}\n')
		except Exception as e:
			with open(f'{c_name}.csv', 'a', encoding='utf-8') as f:
				print(line)
				f.write(f'{line}')

