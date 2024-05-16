import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
from PIL import Image
from datetime import datetime
import os

driver = Chrome()
driver.maximize_window()
driver.get('https://www.douyin.com')

time.sleep(10)

# 关闭验证窗口
try:
	print('尝试关闭验证码')
	captcha = driver.find_element(By.ID, 'captcha_container')
	# TODO js渲染, 未获取到
	driver.find_element(By.XPATH, '//*[@id="vc_captcha_box"]/div/div/div[1]').click()
except Exception as e:
	print('验证码不存在或者选择错误')
	print(e)

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

# 执行键盘操作, 向下按一次, 然后解除新手指引
driver.find_element(By.TAG_NAME, 'body').click()
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)

time.sleep(10)

# 在搜索框输入内筒
print('开始在搜索框输入内容')
search_val = '亚当'
search = driver.find_element(By.XPATH,
                             '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div['
                             '2]/div/div/input').send_keys(search_val)
time.sleep(10)
# select = driver.find_element(By.XPATH,
#                              '//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div['
#                              '3]/div').get_attribute('value')
# print(select)

# 使用截图的方式, 然后使用ocr识别
# 屏幕截取没有下拉列表的内容, 调用系统自带的截屏工具
# driver.get_screenshot_as_file('test.png')
print('开始获取屏幕')
# 获取当前工作目录
current_path = os.getcwd()

# 生成裁剪后文件名，包含当前时间
# cropped_filename = datetime.now().strftime('cropped_%Y%m%d_%H%M%S.png')
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

time.sleep(500)
