from DrissionPage import SessionPage

page = SessionPage()

for i in range(1, 5):
	print('=' * 20, f'=> 第{i}页')
	page.get(f'https://m.gongzicp.com/webapi/novel/rankingGetList?tid=75&rid=1&date=1&page={i}')
	data = page.json
	# print(data)
	datas = data['data']['list']
	for data in datas:
		book_name = data['novel_name']
		book_author = data['novel_author']
		print(book_name, book_author)


