import json
from fontTools.ttLib import TTFont
import requests
from lxml import etree


def get_car():
	headers = {
		'referer': 'https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-2-x'
		           '-411500'
		           '-1-x-x-x-x-x',
		'x-forwarded-for': '',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
		              'like Gecko) Chrome/124.0.0.0 Safari/537.36',
	}

	url = 'https://www.dongchedi.com/motor/pc/sh/sh_sku_list?aid=1839&app_name=auto_web_pc'

	data = {
		'brand': 2,
		'sh_city_name': '全国',
		'page': 3,
		'limit': 20
	}

	resp = requests.post(url, headers=headers, data=data, verify=False)
	print(resp.content.decode())


# url = 'https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-2-x-411500-1-x-x
# -x' \
#       '-x-x'
# headers = {
# 	'referer': 'https://www.dongchedi.com/auto/series/95/model-94467',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
# 	              'like Gecko) Chrome/124.0.0.0 Safari/537.36'
# }
#
# resp = requests.get(url, headers=headers, verify=False)
# print(resp.content.decode('utf-8'))
# with open('test.html', 'w', encoding='gbk') as f:
# 	f.write(resp.content.decode())

def manger_font():
	font = TTFont('96fc7b50b772f52.woff2')
	font.saveXML('font.xml')
	# cmap对应的值是页面中要显示的值
	font_cmap = font['cmap'].getBestCmap()
	print(font_cmap)
	cmap = {}
	for k, v in font_cmap.items():
		cmap[hex(k)] = v
	# print(cmap)
	# exit()
	# ID对应的值, ID的顺序不会改变
	glyph_order = font.getReverseGlyphMap()
	# print(glyph_order)
	glyph_order = list(zip(glyph_order.keys(), glyph_order.values()))[1:]
	# print(glyph_order)
	order = {}
	for li in list(glyph_order):
		num = int(li[1]) - 1
		order[li[0]] = num
	# print(order)

	# 字体映射
	result = {}
	for k, v in cmap.items():
		result[k] = order[v]
	# print(result)
	return result


manger = manger_font()
print(manger)

# 通过xpath获取车辆的信息
with open('index.html', 'r', encoding='utf-8') as f:
	code = f.read()
# print(code)
html = etree.HTML(code)
lis = html.xpath('//ul[@class="tw-grid tw-grid-cols-40 tw-gap-x-12 tw-gap-y-30 tw-min-h-380"]/li')
for li in lis:
	car_name = li.xpath('./a/dl/dt//text()')
	price = li.xpath('./a/dl/dd[@class="tw-mt-12 tw-font-bold tw-text-18 tw-leading-28 '
	                 'xl:tw-text-20 xl:tw-leading-32 tw-text-color-red-500 font-pORE5nVm2QTpLQtk '
	                 'font-G28BNCvDx6IvixLE"]/text()')
	price = str(price).replace('\\u', '0x').replace('[\'', '').replace('\']', '')
	print(car_name)
	print(price)
	exit()


