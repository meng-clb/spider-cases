import requests
from lxml import etree

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/123.0.0.0 Safari/537.36",
}


def get_type(url):
	res = requests.get(url, headers=headers)
	html = etree.HTML(res.content.decode())
	_type = html.xpath('//ul[@class="info-meta-s h-clearfix"]/li[4]/span/text()')[0]
	# print(_type)
	return _type
