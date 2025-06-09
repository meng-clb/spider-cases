import subprocess
import sys
import os
from functools import partial
import execjs


# 用于获取资源文件的路径
def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)


subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8

# 使用 resource_path 来获取 rsa.js 的路径
js_code = execjs.compile(open(resource_path('rsa.js'), 'r', encoding='utf-8').read())

print('=' * 80)
print('请你确保"old_pwd.txt"文件内的数据存在')
print('执行完毕后, 会生成新的"new_pwd.csv"文件')
print('=' * 80)
input('回车后继续执行文件\n')

try:
	with open('old_pwd.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
except Exception as e:
	print('"old_pwd.csv"文件不存在')
	# sys.exit(10)

try:
	with open('new_pwd.csv', 'w', encoding='utf-8') as f:
		f.write('原密码, 加密后的密码\n')
		for line in lines:
			if line == '\n':
				f.write('这里是空行, 这里是空行\n')
				continue
			line = line.rstrip()
			result = js_code.call('get_result', line)
			f.write(f'{line},{result}')
			f.write('\n')
except Exception as e:
	print('请你检查"old_pwd.txt"内的数据')
	# sys.exit(10)

input('文件执行完毕, 输入回车键结束')
