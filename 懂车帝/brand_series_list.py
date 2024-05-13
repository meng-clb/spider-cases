import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'ttwid=1%7Cr8wit_9ekM_si8Zt_HO1kvUJp7kwM05nt12vjBWJ1oU%7C1715345436%7C5438bcbfa79b366c70cdda19142de5c770d5c3d5f8e672032847c0166e19e088; tt_webid=7367352466684741139; tt_web_version=new; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1715345437; s_v_web_id=verify_lw0odvnm_7v50NSeB_ffga_4M3H_BGBZ_4KyZuz8Jj8N5; city_name=%E4%BF%A1%E9%98%B3; msToken=WvmRt7YTa-q5LFEDa-oOUjq-DNiHvtJIARIZag8TOJGYbM7dY_uu4CsT0oM0592YDg-nBFzaHt01wmNvYzaJSXl9C4Cz5IEqBMJkYebC; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1715346364',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.dongchedi.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'aid': '1839',
    'app_name': 'auto_web_pc',
    'no_sales': '1',
    'show_historical_series': '0',
    'with_offline_series_list': '0',
    'brand_id': '37',
}

response = requests.get(
    'https://www.dongchedi.com/motor/brand/v4/brand_series_list/',
    params=params,
    headers=headers,
)

print(response.json())