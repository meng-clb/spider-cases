import requests
from lxml import etree

headers = {
	'Cookie': 'pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE'
	          '/ZGV2aWNlX3N5c3RlbT0meW9kYVJlYWR5PWg1JmNzZWNwbGF0Zm9ybT00JmNzZWN2ZXJzaW9uPTIuNC4wPjo8MTcxMjQwMTc1MTQ5NV1fWw=="; m_flash2=1; _lxsdk_cuid=18eb3191e2dc8-0b180d7fe4141e-26001a51-144000-18eb3191e2dc8; _lxsdk=18eb3191e2dc8-0b180d7fe4141e-26001a51-144000-18eb3191e2dc8; _hc.v=77df8a38-5552-b1f2-696a-e401bd92b527.1712401752; WEBDFPID=335471u1yxx451z1z1y7v5yuuw26979y81vy6808vzw97958447y6y4x-2027761751709-1712401750396UGQGQSCfd79fef3d01d5e9aadc18ccd4d0c95071351; latitude=1.352083; longitude=103.819836; fspop=test; cy=174; cye=xinyang; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1712401865; s_ViewType=10; dper=0202c7224a2d79bf38f3d8fab4553683f50f3f979762c170961daeab826efab098f356fe6879a8435c60209fcae60b82d9eca410d9af99e2ce8f00000000521f00004fb291596718449534ed7abc3a6366037e324cf692c9e07b7095b7c4adae5c123a3f934bb5a23f866f0fa597d2695f81; qruuid=8f4274e5-b246-48d3-bbe6-9b1b45676ce4; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1712402040; _lxsdk_s=18eb3191e2e-9f2-cc5-a8c%7C%7C140',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.dianping.com/xinyang/ch10/g219'
}


def get_store(url):
	res = requests.get(url, headers=headers)
	html = etree.HTML(res.content.decode())
	li_list = html.xpath('//div[@class="content-wrap"]//div[@class="shop-list J_shop-list '
	                     'shop-all-list"]/ul/li')

	for li in li_list:
		# 店铺头像
		img_url = li.xpath('./div[@class="pic"]/a/img/@src')[0]
		# 店铺的链接
		store_url = li.xpath('./div[@class="pic"]/a/@href')[0]
		# 店铺名字
		uname = li.xpath('./div[@class="txt"]/div[@class="tit"]/a/h4/text()')[0]
		# 店铺星级
		star = li.xpath('./div[@class="txt"]/div[@class="comment"]/div[@class="nebula_star"]/div['
		                '@class="star_icon"]/span/@class')[0]
		star = star.split(' ')[1].split('_')[1]
		# 评论数量
		comment_count = li.xpath('./div[@class="txt"]/div[@class="comment"]/a[1]//text()')
		comment_count = ''.join(comment_count).replace('\n', '').replace(' ', '').strip()
		# 人均价格
		price = li.xpath('./div[@class="txt"]/div[@class="comment"]/a[2]//text()')
		price = ''.join(price).replace('\n', '').replace(' ', '').strip()
		# 菜系 位置
		category = li.xpath('./div[@class="txt"]/div[@class="tag-addr"]/a//text()')
		category = '|'.join(category)
		# 位置
		# location = li.xpath('./div[@class="txt"]/div[@class="tag-addr"]/a[1]//text()')
		# 推荐菜
		recommend = li.xpath('./div[@class="txt"]/div[@class ="recommend"]//text()')
		recommend = '|'.join(recommend).replace('\n', '').replace(' ', '')
		# print(
		# 	f'{img_url}=>{store_url}=>{uname}=>{star}=>{comment_count}=>{price}=>{category}=>'
		# 	f'{recommend}')
		with open('store.csv', 'a', encoding='utf-8') as f:
			f.write(
				f'{img_url}=>{store_url}=>{uname}=>{star}=>{comment_count}=>{price}=>{category}=>'
				f'{recommend}\n')


if __name__ == '__main__':
	# TODO 获取页面有多少页, 未完成, 通过第一次请求可以获得
	# TODO 链接内隐藏了请求的类型, 未处理, 每次自己复制链接
	url = f'https://www.dianping.com/xinyang/ch10/g34284'
	for page in range(1, 5):
		if page == 1:
			print(f'====> 开始获取第{page}页')
			get_store(url)
		else:
			print(f'====> 开始获取第{page}页')
			url = f'https://www.dianping.com/xinyang/ch10/g34284p{page}'
			get_store(url)
