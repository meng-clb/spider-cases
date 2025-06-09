import subprocess
from functools import partial  # 专门用来固定参数的
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
from util import *
import re
import json
from urllib.parse import urljoin
session = requests.Session()

# 对于调用js的文件的读取
with open('第一次w.js', 'r', encoding='UTF-8') as f:
    first_json_data = f.read()

with open('第二次w.js', 'r', encoding='UTF-8') as f:
    second_json_data = f.read()

with open('第三次w.js', 'r', encoding='UTF-8') as f:
    three_json_data = f.read()

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.geetest.com/demo/slide-float.html'
    }
    # 第一次请求
    print('===============第一次请求===================')
    first_url = f'https://www.geetest.com/demo/gt/register-slide?t={get_time()}'
    first_res = session.get(first_url, headers=headers)
    first_data = first_res.json()
    # 一次请求返回的所需参数
    gt = first_data['gt']
    challenge = first_data['challenge']

    # 第二次请求
    print('===============第二次请求===================')

    second_url = 'https://apiv6.geetest.com/gettype.php'
    # 携带参数
    params = {
        'gt': gt,
        'callback': f'geetest_{get_time()}'
    }
    headers['Referer'] = 'https://www.geetest.com/'
    session.get(second_url, headers=headers, params=params)

    # 第三次请求
    print('===============第三次请求===================')
    three_url = 'https://apiv6.geetest.com/get.php'
    context = execjs.compile(first_json_data)
    first_res = context.call('first_w', gt, challenge)
    params = {
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'pt': '0',
        'client_type': 'web',
        'w': first_res['w'],
        'callback': f'geetest_{get_time()}'
    }
    aeskey = first_res['aeskey']  # 为了下次w使用
    print('aeskey',aeskey)
    three_res = session.get(three_url, headers=headers, params=params)
    three_data = three_res.content.decode()
    three_data = json.loads(re.match('geetest_\d+\((.*?)\)', three_data).groups()[0])['data']
    c = three_data['c']
    s = three_data['s']
    time.sleep(1)
    # 第四次请求
    print('===============第四次请求===================')
    four_url = 'https://api.geetest.com/ajax.php'
    context = execjs.compile(second_json_data)
    second_res = context.call('second_w', gt, challenge, c, s, aeskey)
    print(second_res['$_CEEg'])
    print(c)
    print(s)
    params['w'] = second_res['$_CEEg']
    four_res = session.get(four_url, headers=headers, params=params)
    print(four_res.content.decode())
    # three_data = json.loads(re.match('geetest_\d+\((.*?)\)', three_data).groups()[0])['data']

    # 第五次请求  获取新的challenge和验证码图片
    print('===============第五次请求===================')
    five_params = {
            "is_next": "true",
            "type": "slide3",
            "gt": gt,
            "challenge": challenge,
            "lang": "zh-cn",
            "https": "true",
            "protocol": "https://",
            "offline": "false",
            "product": "embed",
            "api_server": "api.geetest.com",
            "isPC": "true",
            "autoReset": "true",
            "width": "100%",
            "callback": f'geetest_{get_time()}'
    }
    time.sleep(1)
    five_url= 'https://api.geetest.com/get.php'
    five_res = session.get(five_url, headers=headers, params=five_params)
    five_res = five_res.content.decode()
    five_data = json.loads(re.match('geetest_\d+\((.*?)\)', five_res).groups()[0])
    # 获取新的gt  和 challenge
    gt = five_data['gt']
    challenge = five_data['challenge']
    # 验证码图片
    # 验证码完整的url    https://static.geetest.com/pictures/gt/7bfaaa72b/slice/18f420b71.png
    # bg = "pictures/gt/d401d55fc/bg/60a4dcfa1.jpg"
    # fullbg = "pictures/gt/d401d55fc/d401d55fc.jpg"
    # slice = "pictures/gt/d401d55fc/slice/60a4dcfa1.png"
    time.sleep(1)
    # 拼接完整的url
    new_bg_url = urljoin('https://static.geetest.com', five_data['bg'])
    new_fullbg_url = urljoin('https://static.geetest.com', five_data['fullbg'])
    new_slice = urljoin('https://static.geetest.com', five_data['slice'])
    print('验证码图片下载')
    # 下载验证码图片
    download_img('bg.jpg', new_bg_url, session)
    download_img('fullbg.jpg', new_fullbg_url, session)
    download_img('slice.jpg', new_slice, session)
    # 图片还原
    draw_code('bg.jpg')
    draw_code('fullbg.jpg')
    time.sleep(1)
    # 从当前响应中获取第三个w中所需要的数据
    c = five_data['c']
    s = five_data['s']
    gt = five_data['gt']  # 获取新的值
    challenge = five_data['challenge']  # 获取新的值

    print(c)
    print(s)
    print(gt)
    print(challenge)
    time.sleep(1)

    # 识别当前滑块的距离
    juli = get_x()
    guiji, shijian = get_slide_track(juli)


    context = execjs.compile(three_json_data)
    three_res = context.call('three_w', guiji, gt, challenge, juli, shijian, c, s)
    three_res["callback"] = f'geetest_{get_time()}'
    print('最后一次请求  携带第三个w---------')
    last_url= 'https://api.geetest.com/ajax.php'
    last_res = session.get(last_url, headers=headers, params=three_res)
    last_data = last_res.content.decode()
    last_data = json.loads(re.match('geetest_\d+\((.*?)\)', last_data).groups()[0])
    print(last_data)
    time.sleep(1)

    # 验证是否通过
    validate_url = 'https://www.geetest.com/demo/gt/validate-slide'
    val = last_data.get('validate')
    if not val:
        print('失败。。。。')

    data = {
        "geetest_challenge": challenge,
        "geetest_validate": val,
        "geetest_seccode": f"{val} | jordan"
    }
    res = session.post(validate_url, data=data)
    print('登录成功!')
    print(res.content.decode())


if __name__ == '__main__':
    for i in range(5):
        main()


# # 如果当前为fail 或者是没有权限
# 你可以加个循环 把当前的所有请求循环请求几次
# 1. 你当前识别的图片和最新下载的是否为同一个图片
# 2. 排查当前传递第三个w里面的参数是否正确
# 3. 查看当前请求的get传参的参数是否缺失
# 4. 如果都没问题 那可能是第二个w 或者第三个请求有问题 说白了就是 第二个或第三个w有没有通过的情况


