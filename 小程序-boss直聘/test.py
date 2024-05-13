import requests

headers = {
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Content-Type": "application/x-www-form-urlencoded",
	"Miniappversion": "12.0702",
	"Mpt": "81f2d9e895554f52cfa64b7572ff296a",
	"Platform": "zhipin/windows",
	"Referer": "https://servicewechat.com/wxa8da525af05281f3/502/page-frame.html",
	"Scene": "1256",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "cross-site",
	"Ua": "{\"model\":\"microsoft\",\"platform\":\"windows\"}",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781("
	              "0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF "
	              "WindowsWechat(0x63090a13) XWEB/9129",
	"Ver": "12.0702",
	"Wt2": "EZ_aDU0hvpKCMYw1n5UpXE4gtNJ"
	       "-IYMEwUXWSFzaOGKfhpLRF5aIoeiD2mkSQdE8QEuVMk9xZwftABIVLiNwjZA~~",
	"X-Requested-With": "XMLHttpRequest",
	"Xweb_xhr": "1",
	"Zp_app_id": "10002",
	"Zp_product_id": "10002"
}
url = 'https://www.zhipin.com/wapi/zpgeek/miniapp/homepage/recjoblist.json'
params = {
	"cityCode": "101210100",
	"sortType": "1",
	"page": "4",
	"pageSize": "15",
	"encryptExpectId": "93a547f96ad669293nVz3tq7EVFX",
	"districtCode": "",
	"jobType": "2",
	"experience": "108",
	"blueWelfare": "",
	"appId": "10002"
}

resp = requests.get(url, headers=headers, params=params)
data = resp.json()
job_list = data['jobList']
