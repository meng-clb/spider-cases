import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
from selenium.webdriver.common.action_chains import ActionChains
from baidu_api import get_tag


def get_img(search_val):
	"""
	打开一个浏览器窗口, 输入数据, 然后获取屏幕截图
	:param search_val: 输入的数据
	:return:
	"""
	driver = Chrome()
	driver.maximize_window()
	driver.get('https://www.douyin.com')

	time.sleep(10)

	# 关闭验证窗口
	try:
		print('尝试关闭验证码')
		# 通过执行js代码, 跳过验证码
		driver.execute_script('document.getElementById("captcha_container").style.display="none";')
	except Exception as e:
		print('验证码不存在或者选择错误')
		# print(e)

	# 关闭登录框
	time.sleep(5)
	try:
		login_pannel = driver.find_element(By.ID, 'login-pannel')
		close_pannel = driver.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
		print('登录窗口已关闭')
	except Exception as e:
		print('再次尝试关闭登录窗口')
		time.sleep(10)
		login_pannel = driver.find_element(By.ID, 'login-pannel')
		close_pannel = driver.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
		print('登录窗口已关闭')

	# 获取浏览器窗口的宽度和高度
	window_width = driver.execute_script("return window.innerWidth;")
	window_height = driver.execute_script("return window.innerHeight;")

	# 执行键盘操作, 向下按一次, 然后解除新手指引
	actions = ActionChains(driver)
	driver.find_element(By.TAG_NAME, 'body').click()
	actions.move_by_offset(0, window_height).perform()
	driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)

	time.sleep(5)

	# 在搜索框输入内筒
	print('开始在搜索框输入内容')

	search = driver.find_element(By.XPATH,
	                             '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div['
	                             '2]/div/div/input')
	search.clear()
	search.send_keys(search_val)
	time.sleep(5)
	# TODO 通过运行js获取到元素, 尝试获取下拉列表内的数据
	# element = driver.execute_script("document.getElementsByClassName('wqEoJqmg');")
	# print(element)
	# content = driver.execute_script("element.innerHTML")
	# print(content)
	# time.sleep(5000)
	# 使用截图的方式, 然后使用ocr识别
	print('开始获取屏幕')
	# 获取当前工作目录
	current_path = os.getcwd()
	search_val = search_val.strip().replace(' ', '_')
	# 生成裁剪后文件名，包含当前时间
	cropped_filename = f'{search_val}.png'

	# 截取屏幕
	screenshot = pyautogui.screenshot()

	# 定义你想要截取的区域 (left, upper, right, lower)
	left = 747
	upper = 250
	right = 1290
	lower = 665
	# 截取指定区域
	cropped_image = screenshot.crop((left, upper, right, lower))
	# 保存裁剪后的图片
	cropped_image.save(os.path.join(current_path, cropped_filename))
	print(f"Cropped screenshot saved to {os.path.join(current_path, cropped_filename)}")
	print('屏幕获取完成')
	print('开始识别图片内容')
	get_tag(search_val)
	# driver.quit()
	time.sleep(500)


if __name__ == '__main__':
	# TODO 需要处理的是怎么循环去读取每一个csv的数据
	#  把所有的csv文件放到一个文件夹内, 给一个时间顺序, 然后去循环读取文件夹内的数据
	#  依次读取每个csv文件
	search_val = '亚当兰伯特we will rock you'
	get_img(search_val)

	with open(f'{search_val.strip().replace(" ", "_")}.csv', 'r', encoding='utf-8') as f:
		tags = f.readlines()
	for tag in tags:
		if tag != search_val:
			get_img(tag)
