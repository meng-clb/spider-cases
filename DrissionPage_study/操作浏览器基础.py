import time

from DrissionPage import ChromiumPage

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

# 定位到账号文本框，获取文本框元素并输入账号
ele = page.ele('#email')
ele.input('17527326877')
# 定位到密码文本框并输入密码
page.ele('#pwd').input('aa123456')
time.sleep(10)
# 点击登录按钮
page.ele('@value=登录').click()
