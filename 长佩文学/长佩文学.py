import requests
import subprocess
from functools import partial  # 作用: 用来锁定某个参数的固定值

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 让其node调用的环境编码改变为utf-8
import execjs
import ssl

requests.packages.urllib3.disable_warnings()
sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
sslcontext.verify_mode = ssl.CERT_NONE

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
	              "like Gecko) Chrome/124.0.0.0 Safari/537.36",
	"Token": "",
	"Referer": "https://m.gongzicp.co",
	"Content-Type": "application/json",
	"Client": "pc",
	"Connection": "keep-alive",
<<<<<<< HEAD
	"Cookie": "EADjKmnKUxHmIAcmpAHWE0MmEcDKvc-YnxSTUJgXOTeFGc-hUtlSh71S6cBKAQ9YZbP9F52qNDxijfe7dffUhyznd6cyLC1uSlp1aWHtE5Yrx-2Utf6t1q3ZppctMYhfrMv8t7cwCptljsy_iJlspumaaAMAB8hZrMJA6-1m1J3PbJXt_9ks9wLfKOwzifObqlcqw_56pC44DxACUdHusUo3nJc4Umv-rYAMOom3dYp83aU-YajNaU4DGWSHxpOpe-7WPHxHdYp83aU8xHvBBLeVPUO."
=======
	"Cookie": "_c_n_=ac7cf163c51cbd7bfc576ef45d41dc0a; PHPSESSID=n8uvpsogdo84vkhblnsi8pbe2o; "
	          "tfstk=fkCZByqXL5FN9ZXDYHO2YrR2ytA9gQE5mstXoZbD5hxG5ZmV0MS-lNZ9G9-VxM"
	          "-MlPe9u68WSVYDSnDhLGQkCI1Vkj8coiU9cPeCWNdviuZ5g7_OWx"
	          "-6Ek52IHAHPwcijK0RX93kiuZ7OkUr5mAchdcP9B7HvE8infjDKexpSEADjKmnKUxHmIAcmpAHWE0MmEcDKvc-YnxSTUJgXOTeFGc-hUtlSh71S6cBKAQ9YZbP9F52qNDxijfe7dffUhyznd6cyLC1uSlp1aWHtE5Yrx-2Utf6t1q3ZppctMYhfrMv8t7cwCptljsy_iJlspumaaAMAB8hZrMJA6-1m1J3PbJXt_9ks9wLfKOwzifObqlcqw_56pC44DxACUdHusUo3nJc4Umv-rYAMOom3dYp83aU-YajNaU4DGWSHxpOpe-7WPHxHdYp83aU8xHvBBLeVPUO."
>>>>>>> b9f98330296742bd5fe7b14808e1716380dac7d7
}

book_id = 1244667  # 书本的ID 通过书本ID获取章节ID
get_chapter_list_url = f'https://m.gongzicp.com/webapi/novel/chapterGetList?nid={book_id}'
resp = requests.get(get_chapter_list_url, headers=headers, verify=False)
data = resp.json()
# print(data)
chapter_list = data['data']['list']  # 通过循环list里边的对象,拿到章节的信息和id
print(chapter_list)
# exit()
chapter_id = 4867434  # 章节ID
get_chapter_url = f'https://m.gongzicp.com/webapi/novel/chapterGetInfo?cid={chapter_id}&server=0'

context = execjs.compile(open('decrpyt.js', 'r', encoding='utf-8').read())

resp = requests.get(get_chapter_url, headers=headers, verify=False)
data = resp.json()
print()
content = data['data']['chapterInfo']['content']  # 加密的章节内容

de_content = context.call('decrypt', content)
print(de_content)
