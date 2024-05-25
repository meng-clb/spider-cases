import base64
from lxml import etree
from fontTools.ttLib import TTFont
import requests
from bs4 import BeautifulSoup

font_map = {
	'100110101001010101011110101000': 2,
	'101010101101010001010101101010101010010010010101001000010': 8,
	'10101100101000111100010101011010100101010100': 3,
	'10101010100001010111010101101010010101000': 6,
	'1111111': 7,
	'10100100100101010010010010': 0,
	'1001101111': 1,
	'10010101001110101011010101010101000100100': 9,
	'1110101001001010110101010100101011111': 5,
	'111111111111111': 4
}


def manger_font(path):
	font_dic = {}
	font = TTFont(path)
	font.saveXML(f'{str(path).split(".")[0]}.xml')
	code = open(f'{str(path).split(".")[0]}.xml', 'r', encoding='utf-8').read()
	soup = BeautifulSoup(code, 'xml')
	TTGlyph = soup.find_all('TTGlyph')[1:]
	# TTname = soup.find_all('TTGlyph/')
	li = []
	for TT in TTGlyph:
		T_name = TT.attrs['name']
		# print(TT.attrs['name'])
		pts = TT.find_all('pt')

		# print('---------> li: ', li)

		for pt in pts:
			# print(pt)
			on = pt.attrs['on']
			# print(on)
			li.append(on)
		to = ''.join(li)
		font_dic[T_name] = font_map[to]
		li.clear()
	# print(to)
	# print('=' * 80)
	return font_dic


session = requests.Session()
session.cookies['sessionid'] = '9a4a0jq8dfjnoaqwigo4p2noqrazvitx'

name_li = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀',
           'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤',
           '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王',
           '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹',
           '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢',
           'ヤ地狱篮枫ゞ',
           '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山',
           '望断、天涯路',
           '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤',
           '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风',
           '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩',
           '屎来运赚',
           '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵']
all_name = []
all_data = []

for page in range(1, 6):
	url = f'https://match.yuanrenxue.cn/api/match/7?page={page}'
	resp = session.get(url)
	data = resp.json()
	bs_font = data['woff']
	with open('font.ttf', 'wb') as f:
		f.write(base64.b64decode(bs_font))

	font_dic = manger_font('font.ttf')
	# print(font_dic)


	data = data['data']
	for val in data:
		data_v = val['value'].replace('&#x', 'uni')
		# data_v
		# print(data_v)
		data_v_li = data_v.strip().split(' ')
		tem = []
		for v in data_v_li:
			tem.append(str(font_dic[v]))
		num = ''.join(tem)
		all_data.append(num)
		tem.clear()
	# print(data)
	# print('=' * 80)
	# print(all_data)
	for i in range(1, 11):
		all_name.append(name_li[i + (page - 1) * 10])

print(max(all_data))
index = all_data.index(max(all_data))
print(index)
answer = all_name[index]
# 提交答案
answer_url = f'https://match.yuanrenxue.cn/api/answer?answer={answer}&id=7'
resp = session.get(answer_url)
print(resp.text)