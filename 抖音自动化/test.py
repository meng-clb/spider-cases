import time

import pyautogui
from PIL import Image
from datetime import datetime
import os

time.sleep(15)
# 获取当前工作目录
current_path = os.getcwd()

# 生成文件名，包含当前时间
screenshot_filename = datetime.now().strftime('screenshot_%Y%m%d_%H%M%S.png')

# 截取屏幕
screenshot = pyautogui.screenshot()

# 保存整个屏幕截图
screenshot.save(os.path.join(current_path, screenshot_filename))
print(f"Full screenshot saved to {os.path.join(current_path, screenshot_filename)}")

# 打开截图
screenshot = Image.open(os.path.join(current_path, screenshot_filename))

# 定义你想要截取的区域 (left, upper, right, lower)
left = 747
upper = 165
right = 1290
lower = 650

# 截取指定区域
cropped_image = screenshot.crop((left, upper, right, lower))

# 生成裁剪后文件名
cropped_filename = datetime.now().strftime('cropped_%Y%m%d_%H%M%S.png')

# 保存裁剪后的图片
cropped_image.save(os.path.join(current_path, cropped_filename))
print(f"Cropped screenshot saved to {os.path.join(current_path, cropped_filename)}")
