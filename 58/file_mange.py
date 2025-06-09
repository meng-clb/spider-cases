with open('car.csv', 'r', encoding='utf-8') as f:
	lines = f.readlines()

for line in lines:
	info = line.split('=>')
	if '·' in info[-2]:
		info[-2] = info[-2].replace('·', ',')
	line = ','.join(info)
	line = line.replace('年上牌', '').replace('公里', '').replace('万', '')
	# print(line)
	# exit()
	with open('file_ershoucar_untis.csv', 'a', encoding='utf-8') as f:
		f.write(line)
# exit()
