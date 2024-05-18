"""
windows 安装ocr教程
https://blog.csdn.net/username666/article/details/126310781
"""

import pytesseract
from PIL import Image

# 指定 tesseract_cmd 的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Tool\Tesseract-OCR\tesseract.exe'

image_path = 'yadang.png'

text = pytesseract.image_to_string(Image.open(image_path), lang='chi_sim')  # 'chi_sim'是中文简体的语言包

# 保存文字到文件
with open('output.txt', 'w', encoding='utf-8') as file:
	file.write(text)

print("文字已成功提取并保存到 output.txt 文件中")
