import base64
import re

from fontTools.ttLib import TTFont

with open('test.html', 'r', encoding='utf-8') as f:
	code_data = f.read()

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
print(result)

# 替换网页源码
for k, v in result.items():
	if k in code_data:
		code_data = code_data.replace(k, str(v))

