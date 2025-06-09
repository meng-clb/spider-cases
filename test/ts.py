import re

import requests
from bs4 import BeautifulSoup
from lxml import etree
import base64
import hashlib

md5 = hashlib.md5()


def get_md5(key, value):
	"""
	获取到当页数据中要隐藏的img的md5值
	:param key:
	:param value:
	:return:
	"""
	s = base64.b64encode((key + value).encode('utf-8')).decode('utf-8').replace('=', '')
	md5.update(s.encode('utf-8'))
	j_key = md5.hexdigest()
	# print(j_key)
	# print(s)
	return j_key
print(get_md5('0K8fdhepqF', '1o90y3ruzn'))