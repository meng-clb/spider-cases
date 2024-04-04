def processing_url(path):
	url_list = []
	with open(path, 'r', encoding='utf-8') as f:
		data = f.readlines()
		for line in data:
			url = line.split('=>')[1].strip()
			url_list.append(url)
	return url_list


if __name__ == '__main__':
	url_list = processing_url('hot_word.csv')
	print(url_list)
