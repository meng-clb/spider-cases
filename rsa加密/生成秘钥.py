from Crypto.PublicKey import RSA

key = RSA.generate(2048)

# rsa生成的秘钥
private_key = key.exportKey()

# rsa生成公钥
public_key = key.public_key().exportKey()

# 将生成的公钥和秘钥保存起来
with open('private_key.pem', 'wb') as f:
	f.write(private_key)

with open('public_key.pem', 'wb') as f:
	f.write(public_key)
