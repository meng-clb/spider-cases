from data_encrypt import encrypt
from data_decrypt import decrypt
from select_orders import generate_select_order

# 用来判断是否可以继续往下执行
bool_ = {
	'check': 1,  # 消费者信息认证
	'send': 1,  # 发送账单
	'claim': 1,  # 索要费用
}

# 用来保存消费场所认证
place_info = {
	'uname': '消费场所',
	'pwd': '唯一支付'
}


# 1. 场所认证
def place():
	print('========= 场所的认证码 ==========')
	place_authentication = encrypt(str(place_info['uname'] + place_info['pwd']))
	with open('key.txt', 'w', encoding='utf-8') as f:
		f.write('您场所的认证码\n')
		f.write(place_authentication)
		f.write('\n')
	print(place_authentication)


# 用来保存用户注册信息
user = {}


# 2. 消费者进行注册, 将ID加密作为认证信息
def login():
	print('\n========== 账号注册 ===========\n')
	print(
		'注意事项: 您所有的key将会保存在key.txt文件内\n是您进入场所的唯一标识, 请不要泄露给任何人, 以免造成您的财产损失!')
	uname = input('请设置你的账号: ')
	pwd = input('请设置你的密码: ')
	user['uname'] = uname
	user['pwd'] = pwd
	user_id = encrypt(uname)
	user_pwd = encrypt(pwd)
	with open('key.txt', 'a', encoding='utf-8') as f:
		f.write('\n消费者令牌: \n')
		f.write(user_id)
		f.write('\n')
		f.write('\n支付指令: \n')
		f.write(user_pwd)
		f.write('\n')
	print('您的场所唯一标识==>消费者令牌, 请保存好, 不要泄露出去 ======>\n', user_id)
	print('您的支付指令, 请保存好, 不要泄露出去 ======>\n', user_pwd)


# 3. 消费者信息核验
def check_user():
	data = input('请输入您的消费者令牌:')
	try:
		user_id = decrypt(data)  # 对传递过来的令牌进行解密, 拿到用户信息, 进行对比
		# print(user_id)
		if user_id == user['uname']:
			bool_['check'] = 0
			print('认证成功, 身份核实正确, 已进入场所')
		else:
			bool_['check'] = 1
			print('认证失败, 请检验您的令牌, 或者查看是否注册')
	except Exception as e:
		bool_['check'] = 1
		print('指令输入不合法, 请检查您的指令')


# 4. 场所发送消费信息
def send_info():
	generate_select_order()
	data = input(
		'请确认您的账单信息是否有误, 如果账单信息有误 \n请输入"no", 如果正确请输入您的支付指令: ')
	if data != 'no':
		try:
			user_pwd = decrypt(data)  # 对传递过来的令牌进行解密, 拿到支付密码
			# print('user_pwd', user_pwd)
			if user_pwd == user['pwd']:
				bool_['send'] = 0
				print('指令正确, 已扣费成功')
			else:
				bool_['send'] = 1
				print('\n指令错误\n')
		except Exception as e:
			print('\n 指令输入不合法 \n')
	else:
		bool_['send'] = 1
		print('\n以下是新的账单\n')


# 5. 场所索取费用
def place_claim():
	print('========== 场所向平台索要费用 ===========')
	data = input('请输入场所认证码: ')
	try:
		place_de = decrypt(data)
		if place_de == str(place_info['uname'] + place_info['pwd']):
			bool_['claim'] = 0
			print('认证成功, 平台已向消费场所付费')
		else:
			bool_['claim'] = 1
			print('认证失败, 请检查场所认证码')
	except Exception as e:
		bool_['claim'] = 1
		print('请输入合法的场所认证码')


if __name__ == '__main__':
	start = 1
	while start == 1:
		# 1. 消费场所认证
		place()
		# 2. 消费者认证
		login()
		# 3. 消费者进入场所认证
		while bool_['check'] == 1:
			check_user()

		# 4. 场所发送消费者信息
		while bool_['send'] == 1:
			send_info()

		# 5. 消费场所索取费用
		while bool_['claim'] == 1:
			place_claim()
		# 执行结束
		start = 0
