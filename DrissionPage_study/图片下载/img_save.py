from DrissionPage import ChromiumPage

page = ChromiumPage()
tab = page.new_tab()


def get_all_page(url):
	"""
	获取所有的页面链接
	:param url:
	:return:
	"""
	i = 0
	all_page = [url]
	while i != 2:
		page.get(all_page[-1])
		urls = page.ele('.page').eles('tag:a')
		for url in urls:
			if url.link == all_page[0]:
				i += 1
			if url.link not in all_page:
				all_page.append(url.link)
	print(f'共获取到{len(all_page)}条页面链接')
	return all_page


def get_all_info(url):
	"""
	获取所有的详情页面链接
	:param url:
	:return:
	"""
	all_info = []
	page.get(url)
	lis = page.eles('.i_list list_n2')
	# 通过所有的li获取到链接
	for li in lis:
		img_url = li.ele('tag:a').link
		all_info.append(img_url)
		# print(img_url)
		# img_info = li.ele('tag:div@class=meta-title').text
		# print(img_info)
	return all_info


def get_all_img(url):
	"""
	获取所有的img链接并进行保存
	:param url:
	:return:
	"""
	page.get(url)
	urls = page.ele('.page').eles('tag:a')[:-1]
	for url in urls:
		print(f'开始获取{url.link}页图片链接')
		# 使用新的tab标签来执行操作
		tab.get(url.link)
		imgs = tab.ele('.content_left').eles('tag:img')
		# print(imgs)
		for img in imgs:
			# print(img.src())
			img.save(path='./img/', name=f'{str(img.link).split("/")[-1]}')
			print(f'图片{img.link}已保存')


if __name__ == '__main__':
	all_page = get_all_page('https://meirentu.cc/group/xiuren-1.html')
	for page_url in all_page:
		all_info = get_all_info(page_url)
		for info in all_info:
			get_all_img(info)
