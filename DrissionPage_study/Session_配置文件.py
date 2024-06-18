from DrissionPage import SessionOptions

so = SessionOptions()
# 读取配置文件
# so = SessionOptions(ini_path='./setting.ini')

# 设置headers
so.set_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
	              'like Gecko) '
	              'Chrome/125.0.0.0 Safari/537.36',

}

# 设置超时时间
so.set_timeout(10)

# 设置超时重连次数
so.set_retry(5)

so.save(path='./setting.ini')


