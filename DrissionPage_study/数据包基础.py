from DrissionPage import SessionPage


page = SessionPage()
for i in range(1, 5):
	page.get(f'https://gitee.com/explore/all?page={i}')
	links = page.eles('.title project-namespace-path')
	for line in links:
		print(line.text)
		print(line.link)
		print('=' * 20)
