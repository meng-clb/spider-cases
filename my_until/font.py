from fontTools.ttLib import TTFont


def manger_font(path):
	"""
	字体反爬关系映射表, 只适合只有数字的映射, 汉字映射需要单独建立映射表
	:param path: 字体文件路径
	:return:
	"""
	font = TTFont(path)
	font.saveXML(f'{str(path).split(".")[0]}.xml')
	# cmap对应的值是页面中要显示的值
	font_cmap = font['cmap'].getBestCmap()
	# print(font_cmap)
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


if __name__ == '__main__':
	path = '96fc7b50b772f52.woff2'
	print(manger_font(path))
