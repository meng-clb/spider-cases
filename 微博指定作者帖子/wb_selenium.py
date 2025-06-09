import re
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os

chapter_csv_path = 'chapter_info_csv'  # 文章的信息csv文件夹
chapter_json_path = 'chapter_info_json'  # 文章的信息json文件夹
comment_csv_path = 'comment_csv_path'  # 评论csv文件夹
comment_json_path = 'comment_json_path'  # 评论json文件夹
if not os.path.exists(chapter_csv_path):
	os.makedirs(chapter_csv_path)

if not os.path.exists(chapter_json_path):
	os.makedirs(chapter_json_path)

if not os.path.exists(comment_csv_path):
	os.makedirs(comment_csv_path)

if not os.path.exists(comment_json_path):
	os.makedirs(comment_json_path)

driver = Chrome()

with open('all_mid.csv', 'r', encoding='utf-8') as f:
	lines = f.readlines()

for line in lines:
	# line 是帖子的id
	print(f'开始获取ID:{line.strip()}信息')
	url = f'https://m.weibo.cn/detail/{line.strip()}'
	driver.get(url)
	time.sleep(3)  # 等待页面数据加载, 如果为获取到数据, 可以选择等待更长时间
	# ====================  获取帖子信息   =================================
	try:
		create = driver.find_element(By.XPATH, '//h4[@class="m-text-cut"]')
		create_info = create.text
		create_time = create_info.split('来自')[0].strip()
		create_ip = create_info.split('来自')[-1].strip()
		info = driver.find_elements(By.XPATH,
		                            '//div[@class="lite-page-tab"]/div[@class="tab-item" or '
		                            '@class="tab-item cur"]')
		content = ''
		for ele in info:
			content += ele.text
		content = content.replace('\n', '')
		match = re.search('转发(?P<reposts>\d+)评论(?P<comment>\d+)赞(?P<like>\d+)', content)
		if match:
			chapter_info = {
				'id': line.strip(),
				'reposts_count': match.group('reposts'),
				'attitudes_count': match.group('like'),
				'comment_count': match.group('comment'),
				'time': create_time,
				'mode': create_ip
			}
		else:
			print('未获取到数据')
		with open(f'{os.path.join(chapter_csv_path, line.strip())}.csv', 'w',
		          encoding='utf-8') as f:
			f.write(f'帖子ID=>发布时间=>点赞数量=>转发数量=>评论数量=>发布方式\n')
			f.write(
				f"{chapter_info['id']}=>{chapter_info['time']}=>{chapter_info['attitudes_count']}="
				f">{chapter_info['reposts_count']}=>"
				f"{chapter_info['comment_count']}=>{chapter_info['mode']}\n")
		with open(f'{os.path.join(chapter_json_path, line.strip())}.json', 'w',
		          encoding='utf-8') as f:
			f.write(str(chapter_info).replace("'", '"'))
	except Exception as e:
		print('error ==> 获取帖子信息出现错误')
	# ====================  获取评论信息   =================================
	user_info = {}
	try:
		user_list = driver.find_elements(By.XPATH, '//div[@class="m-box-col m-box-dir '
		                                           'm-box-center '
		                                           'lite-line"]')
		if len(user_list) > 0:
			with open(f'{os.path.join(comment_csv_path, line.strip())}.csv', 'w',
			          encoding='utf-8') as f:
				f.write(f'作者=>发布时间=>发布ip=>点赞数量=>评论内容\n')
				for user in user_list:
					user_name = user.find_element(By.XPATH, './/div[@class="m-text-box"]/h4').text
					# user_name = user_name.text
					comment = user.find_element(By.XPATH, './/div[@class="m-text-box"]/h3').text
					# comment = comment.text
					comment_info = user.find_element(By.XPATH,
					                                 './/div[@class="lite-bot m-text-cut"]').text
					like_count = comment_info.strip().split('\n')[-1]
					create_info = comment_info.strip().split('\n')[0]
					user_time = create_info.split('来自')[0]
					user_ip = create_info.split('来自')[-1]
					f.write(f'{user_name}=>{user_time}=>{user_ip}=>{like_count}=>{comment}\n')
					user_info[f'{user_name}'] = {
						"作者": f"{user_name}",
						"发布时间": f"{user_time}",
						"发布ip": f"{user_ip}",
						"点赞数量": f"{like_count}",
						"评论内容": f"{comment}",

					}
				with open(f'{os.path.join(comment_json_path, line.strip())}.json', 'w',
				          encoding='utf-8') \
						as file:
					file.write(str(user_info).replace("'", '"'))
		else:
			print(f'帖子ID: {line}没有评论或者获取评论出现错误')
	except Exception as e:
		print('error ==> 获取评论信息出现错误')
