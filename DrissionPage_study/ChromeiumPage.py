# 导入
from DrissionPage import ChromiumPage, ChromiumOptions

# 创建对象
page = ChromiumPage()
# 访问网页
page.get('https://www.baidu.com')

print(page.address)

print(page.tab_id)

# A33F60D9598D7C486616C6313401E4ED