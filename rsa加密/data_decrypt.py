from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 1. 加载私钥
private = RSA.importKey(open('private_key.pem', 'rb').read())
# 2. 创建加密器
rsa = PKCS1_v1_5.new(key=private)


# 3. 对数据进行解密  -> 后一个参数, 当秘钥不对时返回的结果
def decrypt(data):
	data_decrypt = rsa.decrypt(base64.b64decode(data), '身份不合法').decode()
	return data_decrypt

