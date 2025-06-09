import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import requests

from until import manger_back, get_now, manger_jsonp, download_img, get_x, get_slide_track, \
	get_slide_track2

session = requests.Session()

session.headers[
	'User-Agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                     'like Gecko) Chrome/124.0.0.0 Safari/537.36')

url = 'https://www.geetest.com/demo/slide-popup.html'
session.get(url)  # 保持下cookie

js = execjs.compile(open('first_w.js', 'r', encoding='utf-8').read())

# ================== 第一次请求, 注册极验 =========
register_url = f'https://www.geetest.com/demo/gt/register-slide?t={get_now()}'
register_resp = session.get(register_url)
# print()
register_data = register_resp.json()
gt = register_data['gt']
challenge = register_data['challenge']

# ============= 第二次请求验证码类型 ===============
get_type_params = {
	'gt': gt,
	'callback': f'geetest_{get_now()}'
}
second_url = 'https://apiv6.geetest.com/gettype.php'
type_resp = session.get(second_url, params=get_type_params)
# print(type_resp.content.decode())

# ============= 第一次发送get请求,get.php, 获取所需要的固件 ============
first_get_url = 'https://apiv6.geetest.com/get.php'
# get_php_params = {
# 	"gt": gt,
# 	"challenge": challenge,
# 	"lang": "zh-cn",
# 	"pt": "0",
# 	"client_type": "web",
# 	"w": '',  # TODO 加密数据
# 	"callback": "geetest_1713440516970"
# }

first_get_php_resp = js.call('get_first_w', gt, challenge)
# print(first_get_php_resp)
get_php_params = first_get_php_resp['params']
aeskey = first_get_php_resp['aeskey']
finger_print = first_get_php_resp['finger_print']
get_php_params['callback'] = f'geetest_{get_now()}'

thirdly_resp = session.get(first_get_url, params=get_php_params)
# print(thirdly_resp.text)
ss = manger_jsonp(thirdly_resp.text)['data']['s']
c = manger_jsonp(thirdly_resp.text)['data']['c']

# ============= 第一次发送ajax请求, 激活滑块 =============
cul_second_w = execjs.compile(open('第二次w.js', 'r', encoding='utf-8').read())
second_w = cul_second_w.call('second_w', gt, challenge, c, ss, aeskey)

first_ajax_url = 'https://api.geetest.com/ajax.php'
first_ajax_params = {
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"pt": "0",
	"client_type": "web",
	"w": '',  # second_w,  # 加密参数, 需要逆向 TODO 设置为空, 做一个判断
	"callback": f"geetest_{get_now()}"
}

first_ajax_resp = session.get(first_ajax_url, params=first_ajax_params)
# print(first_ajax_resp.text)

# =============== 第二次发送get.php请求 ===============
second_get_url = 'https://api.geetest.com/get.php'
second_get_params = {
	"is_next": "true",
	"type": "slide3",
	"gt": gt,
	"challenge": challenge,
	"lang": "zh-cn",
	"https": "true",
	"protocol": "https://",
	"offline": "false",
	"product": "popup",
	"api_server": "api.geetest.com",
	"isPC": "true",
	"autoReset": "true",
	"width": "100%",
	"callback": f"geetest_{get_now()}"
}

second_get_res = session.get(second_get_url, params=second_get_params)
second_get_data = manger_jsonp(second_get_res.content.decode())

# challenge这里返回时发生了改变, 更新数据
new_challenge = second_get_data['challenge']

# 拿到三个图片, 下载图片
bg_img = second_get_data['bg']
download_img('bg.jpg', bg_img, session)
fullbg_img = second_get_data['fullbg']
download_img('fullbg.jpg', fullbg_img, session)
slice_img = second_get_data['slice']
download_img('slice.jpg', slice_img, session)

# 处理背景图片
manger_back('bg.jpg')
manger_back('fullbg.jpg')

# ============== 第二次ajax请求 ===========
x_jvli = get_x()
# guiji, shijian = get_slide_track(x_jvli)
# third_w_js = execjs.compile(open('third_w.js', 'r', encoding='utf-8').read())
# third_params = third_w_js.call('third_w', gt, new_challenge, c, ss, x_jvli, guiji, shijian)
guiji, shijian = get_slide_track2(x_jvli)
third_w_js = execjs.compile(open('lucky_3w.js', 'r', encoding='utf-8').read())
third_params = third_w_js.call('three_w', guiji, gt, new_challenge, x_jvli, shijian, c, ss)

third_params['callback'] = f'geetest_{get_now()}'

second_ajax_url = 'https://api.geetest.com/ajax.php'
# session.headers['Referer'] = 'https://www.geetest.com/'
second_ajax_resp = session.get(second_ajax_url, params=third_params, verify=False)

print(third_params)
print(second_ajax_resp.text)
