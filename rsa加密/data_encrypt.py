from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 1. 加载公钥
public = RSA.importKey(open('public_key.pem', 'rb').read())
# 2. 创建加密器
rsa = PKCS1_v1_5.new(key=public)


# 3. 对数据进行加密
# data = '加密的数据'.encode('utf-8')  # test


# 对数据进行加密
def encrypt(data):
	data = data.encode('utf-8')
	data_encrypt = base64.b64encode(rsa.encrypt(data)).decode()
	return data_encrypt
