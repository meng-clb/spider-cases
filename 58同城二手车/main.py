import time
import requests
from lxml import etree
import base64
import re
from fontTools.ttLib import TTFont

headers = {
	'Cookie': 'f=n; commontopbar_new_city_info=37%7C%E9%87%8D%E5%BA%86%7Ccq; '
	          'userid360_xml=08113A2BD97B3CE7674B9790FEE17F62; time_create=1715133952152; '
	          'id58=CpQQU2YTUMQ3zuKfCItuAg==; 58tj_uuid=d086858f-73b2-4a7f-9465-2b52de5056f4; '
	          'new_uv=1; utm_source=; init_refer=https%253A%252F%252Fwww.google.com%252F; als=0; '
	          '58ua=58m; wmda_uuid=3b2420b6e0f0af7046c8c751d253c7f8; wmda_new_uuid=1; '
	          'fzq_h=077c7dedd4bee2912721c3b78ec2ca2d_1712541911033_6807ed16a1ff462697d3380cea262192_2100138008; new_session=0; spm=; f=n; city=cq; 58home=cq; commontopbar_new_city_info=37%7C%E9%87%8D%E5%BA%86%7Ccq; commontopbar_ipcity=xy%7C%E4%BF%A1%E9%98%B3%7C0; sessionid=ecfaf546-e453-44df-8c9d-0d2279cc48ad; wmda_session_id_1732038237441=1712541951536-08f5b80f-eb8c-f9f6; xxzl_deviceid=kWApWrBT3Q0qLuFYt%2Bi97RYHR2P83ttQY7R%2BI0KAtCp9oTdWtvr%2BpgNg5IKc%2BqAX; wmda_visited_projects=%3B1732039838209%3B1732038237441%3B10104579731767; xxzlclientid=d37ef6a9-a8bd-42ad-b5f8-1712544753520; xxzlxxid=pfmxbE7uLcM37N2wYSwWxQSEHAK04TpNyKY0wMjXSCgwZEU+wIhLTcBgCj+0EATugIwt; www58com="UserID=68256913493004&UserName=48ja819fo"; 58cooper="userid=68256913493004&username=48ja819fo"; 58uname=48ja819fo; passportAccount="atype=0&bstate=0"; xxzl_smartid=d826f585dc11c165f9415c7ecdbe2f30; xxzl_cid=9cfecbe16518460d96d8df22d69586c3; xxzl_deviceid=4zLsur6MrhmlS7cQKPRjCX8BQ6AWdNi+K972w+/Xgfhqn5ArZbD7O92vcfWd+Jl/; xxzlbbid=pfmbM3wxMDI5MnwxLjcuMHwxNzEyNTQ4MDA1MzgwfEM5OUdTRTZ5Zk94eDJ6Ry9sSXpUTEV6elo4TjdkbE4zeW04MklydDJQWEE9fGU5MGUwYjdkOTJiNGNkNzJlNzQ1MzQ1YjE1NjA4NTJiXzE3MTI1NDgwMDQ3ODlfZGM1Njg1NmFkNDljNGQyNjhlMWViNmUwNTE5NGNmMmNfMjEwMDEzODAxMnxiOTkzODE2ZWU1MjE5NTE3YWQ4NjJiNTAwMTJmM2Y1YV8xNzEyNTQ4MDA0OTc0XzI1NA==; PPU="UID=68256913493004&UN=48ja819fo&TT=439ed9ae545e2deacec707aa8906d6e6&PBODY=LMBVNwLuU_xEFehl5DjSZI__sboeU_Pexuu2Tq_UCU8L2-GHdgg7-gS8ySbA-u97NcTnmEjt83wf2-5EaKv_VP1JAannnXgDVQvMjivrEwBGPTODoH2_zubNBtprzIpHx29uOCxQsolTpdkL3hm85j-NgLoQqSXvpXIT2xlahfk&VER=1&CUID=a9Aqls5_2sKAO4qIdng5kA"; fzq_js_usdt_infolist_car=e952cf6bf853309689c30b1b849cf7c2_1712548890960_7',
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	'Referer': 'https://cq.58.com/'
}


def get_type(url):
	"""
	获取车辆是手动还是自动
	:param url: 车辆的url
	:return: 车辆类型
	"""
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
		              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
	}
	res = requests.get(url, headers=headers)
	html = etree.HTML(res.content.decode())
	_type = html.xpath('//ul[@class="info-meta-s h-clearfix"]/li[4]/span/text()')[0]
	# print(_type)
	return _type


def manage_font(code_data):
	"""
	对58的字体反爬做处理, 拿到页面对应的字体文件, 并进行替换页面数据
	:param code_data: 页面源码
	:return: 处理好之后的页面源码
	"""
	font_base = re.findall("base64,(.*?)'", code_data, re.S)[0]
	decoded_font_data = base64.b64decode(font_base)

	with open('58font.ttf', 'wb') as font_file:
		font_file.write(decoded_font_data)

	font = TTFont('58font.ttf')
	font.saveXML('58font.xml')

	font_map = font['cmap'].getBestCmap()
	cmap = {}
	for k, v in font_map.items():
		cmap[hex(k)] = v
	# print(cmap)
	with open('58font.xml', 'r', encoding='utf-8') as f:
		font_data = f.read()
	glyph_order = re.findall('<GlyphID id="(\d+)" name="(.*?)"/>', font_data)[1:]
	# print(glyph_order)
	glyph = {}
	for li in glyph_order:
		num = int(li[0]) - 1
		glyph[li[1]] = num
	# print(glyph)

	result = {}
	for k, v in cmap.items():
		result['&#' + k[1:] + ';'] = glyph[v]
	# print(result)

	# 替换网页源码
	for k, v in result.items():
		if k in code_data:
			code_data = code_data.replace(k, str(v))
	return code_data


def get_next_page(data):
	"""
	页面的下一页请求链接在页面源码内, 需要通过页面源码去获取下一页的请求链接
	:param data: 页面源码
	:return:
	"""
	# 请求的html页面数据
	html = etree.HTML(data)
	next_page = html.xpath('//div[@class="pager"]/strong/following-sibling::a[1]/@href')[0]
	# print(next_page)
	return next_page


def get_page_data(url):
	"""
	请求获取到源代码之后, 对字体反爬进行替换处理, 替换源码, 展示真实的数据
	:param url: 请求的url
	:return: 修改后的源码
	"""
	# 拿到下一页的url进行请求, 返回请求的页面数据
	res = requests.get(url, headers=headers)
	data = res.content.decode()
	code_data = manage_font(data)
	return code_data


def get_info_data(data):
	"""
	把页面数据传递进来, 通过xpath获取要保存的数据
	:param data: 页面源代码
	:return:
	"""
	html = etree.HTML(data)
	ul = html.xpath('//div[@class="list-wrap"]/ul[@class="infos infos-card h-clearfix"]/li')
	for li in ul:
		try:
			car_url = li.xpath('./div[@class="info--wrap"]/a/@href')[0]
			c_type = get_type(car_url)
			# print(c_type)
			brand = \
				li.xpath(
					'./div[@class="info--wrap"]/a/div[@class="info--desc"]/h2/span/font/text()')[0]
			model = \
				li.xpath('./div[@class="info--wrap"]/a/div[@class="info--desc"]/h2/span/text()')[
					0].strip()
			tags = li.xpath(
				'./div[@class="info--wrap"]/a/div[@class="info--desc"]/div[@class="tags '
				'h-clearfix"]//text()')
			tags = '|'.join(tags).replace('\n', '').replace('  ', '').replace('\t', '')
			info = li.xpath('./div[@class="info--wrap"]/a/div[@class="info--desc"]/div['
			                '@class="info_params"]//text()')
			info = ''.join(info).replace('\n', '').replace('  ', '')
			price = li.xpath('./div[@class="info--wrap"]/a/div[@class="info--price"]/b/text()')[0]
			# print(f'{brand} => {model} => {tags} => {info} => {price}万')
			with open('test.csv', 'a', encoding='utf-8') as f:
				f.write(f'{brand}=>{model}=>{c_type}=>{tags}=>{info}=>{price}万\n')
		except Exception as e:
			print(e)


if __name__ == '__main__':
	url = 'https://cq.58.com/ershouche/'
	# 请求到58页数据之后, 会验证ip, 需要打开下边的url
	# url = 'https://cq.58.com/ershouche/pn60/?ClickID=56&PGTID=0d100000-0002-5a10-e2c2
	# -0affcad221f0&needHpCityTest=true&reentries=%7B%22reentry_id%22%3A%223e0408d1-e67c-4a7c-b962
	# -acaa578bd8da%22%7D'
	data = get_page_data(url)
	for i in range(1, 70):  # TODO 58也之后, 打开那个url, 把 这个 1 改成60
		# 获取下一页的请求
		next_page = get_next_page(data)
		# 对数据进行处理
		print(f'======> 第{i}页数据')
		get_info_data(data)
		time.sleep(3)
		data = get_page_data(next_page)
		with open('url.csv', 'a', encoding='utf-8') as f:
			f.write(f'{next_page}\n')
