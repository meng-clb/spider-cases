import requests
from lxml import etree

headers = {
	'Cookie': 'pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE'
	          '/ZGV2aWNlX3N5c3RlbT0meW9kYVJlYWR5PWg1JmNzZWNwbGF0Zm9ybT00JmNzZWN2ZXJzaW9uPTIuNC4wPjo8MTcxMjQwMTc1MTQ5NV1fWw=="; m_flash2=1; _lxsdk_cuid=18eb3191e2dc8-0b180d7fe4141e-26001a51-144000-18eb3191e2dc8; _lxsdk=18eb3191e2dc8-0b180d7fe4141e-26001a51-144000-18eb3191e2dc8; _hc.v=77df8a38-5552-b1f2-696a-e401bd92b527.1712401752; WEBDFPID=335471u1yxx451z1z1y7v5yuuw26979y81vy6808vzw97958447y6y4x-2027761751709-1712401750396UGQGQSCfd79fef3d01d5e9aadc18ccd4d0c95071351; latitude=1.352083; longitude=103.819836; fspop=test; cy=174; cye=xinyang; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1712401865; s_ViewType=10; dper=0202c7224a2d79bf38f3d8fab4553683f50f3f979762c170961daeab826efab098f356fe6879a8435c60209fcae60b82d9eca410d9af99e2ce8f00000000521f00004fb291596718449534ed7abc3a6366037e324cf692c9e07b7095b7c4adae5c123a3f934bb5a23f866f0fa597d2695f81; qruuid=8f4274e5-b246-48d3-bbe6-9b1b45676ce4; ll=7fd06e815b796be3df069dec7836c3df; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1712402040; _lxsdk_s=18eb3191e2e-9f2-cc5-a8c%7C%7C140',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/123.0.0.0 Safari/537.36',
	'Referer': 'https://www.dianping.com/'
}


def get_comment(url):
	with open('comment.csv', 'a', encoding='utf-8') as f:
		res = requests.get(url, headers=headers)
		data = res.content.decode()

		html = etree.HTML(data)
		# =========== 商家信息 =============
		title = html.xpath(
			"//div[@class='review-shop-wrap']/div[@class='shop-info clearfix']/h1["
			"@class='shop-name']/text()")[0]
		score = html.xpath("//div[@class='rank-info']//text()")
		score = ''.join(score).replace('\n', '').replace('\t', '').replace('   ', '')
		address = html.xpath("//div[@class='address-info']//text()")
		address = ''.join(address).replace('\n', '').replace('\xa0', ' ').replace('  ', '')
		phone = html.xpath("//div[@class='phone-info']//text()")
		phone = ''.join(phone).replace('\n', '').replace('\xa0', ' ').replace('  ', '')
		tags = html.xpath("//div[@class='reviews-tags']//text()")
		tags = ''.join(tags).replace('\n', ' ').replace('  ', '')
		print('=========== 商家信息 =============')
		print(f'{title}=>{score}=>{address}=>{phone}=>{tags}')
		f.write('=========== 商家信息 =============\n')
		f.write(f'{title}=>{score}=>{address}=>{phone}=>{tags}\n')
		# =========== 评论信息 =============
		comment_count = html.xpath("//div[@class='filters']//text()")

		comment_list = html.xpath("//div[@class='reviews-items']/ul/li")

		for user in comment_list:

			# 用户信息
			try:
				user_img = user.xpath('./a[1]/img/@src')  # TODO 头像获取出现bug
				user_home = user.xpath('./a/@href')[0]  # 主页链接, 需要拼接处理
				user_id = user.xpath('./a[@class="dper-photo-aside"]/@data-user-id')[0]
				user_name = \
				user.xpath('./div[@class="main-review"]/div[@class="dper-info"]/a/text()')[
					0]
				user_name = user_name.replace('\n', '').replace(' ', '')
			except Exception as e:
				user_img = user.xpath('./a[1]/img/@src')  # TODO 头像获取出现bug
				user_home = user.xpath('./div[@class="dper-photo-aside"]/@data-user-id')[
					0]  # 无主页链接, 通过id进入主页之后疑似是机器人
				user_home = f'/member/{user_home}'
				user_id = user.xpath('./div[@class="dper-photo-aside"]/@data-user-id')[0]
				user_name = \
					user.xpath('./div[@class="main-review"]/div[@class="dper-info"]/span/text('
					           ')')[0]
				user_name = user_name.replace('\n', '').replace(' ', '')

			print('=========== 用户信息 =============')
			print(f'{user_img}=>{user_home}=>{user_id}=>{user_name}')
			f.write('=========== 用户信息 =============\n')
			f.write(f'{user_img}=>{user_home}=>{user_id}=>{user_name}\n')
			# 评论信息
			score = user.xpath('.//span[@class="score"]//text()')
			score = ''.join(score).replace('\n', '').replace('   ', '')
			comment = user.xpath('.//div[@class="review-words Hide"]/text()')
			comment = ''.join(comment).replace('\t', '')
			like = user.xpath('.//div[@class="review-recommend"]//text()')
			like = ''.join(like).replace('\n', '').replace(' ', '')
			time = user.xpath('.//div[@class="misc-info clearfix"]//text()')
			time = ''.join(time).replace('\n', '').replace('  ', '')
			shop_reply = user.xpath('.//div[@class="shop-reply"]//text()')
			shop_reply = ''.join(shop_reply).replace('\n', '').replace('\t', '').replace('  ', '')

			print('=========== 评论信息 =============')
			print(
				f'{score}=>{comment}=>{like}=>{time}=>{shop_reply}')
			f.write('=========== 评论信息 =============\n')
			f.write(f'{score}=>{comment}=>{like}=>{time}=>{shop_reply}\n\n\n')

if __name__ == '__main__':
	user_discern = 'jhrp5tJfZsP63Jk8'
	url = f'https://www.dianping.com/shop/{user_discern}/review_all'
	# 需要抓取多页, 直接改url即可
	get_comment(url)
