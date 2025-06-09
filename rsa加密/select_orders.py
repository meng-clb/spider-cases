import csv


def generate_order():
	# 读取shop.csv文件并获取商品列表和价格列表
	with open('shop.csv', 'r', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)  # 跳过标题行
		products = [row[0] for row in reader]
		file.seek(0)  # 将文件指针重置到开头
		next(reader)  # 跳过标题行
		prices = [float(row[1]) for row in reader]

	# 用户选择商品
	print("请选择要购买的商品（输入商品编号），输入 'done' 完成选择：")
	print("编号  商品")
	for idx, product in enumerate(products, 1):
		print(f"{idx}. {product}")

	selected_items = []
	while True:
		choice = input("商品编号：")
		if choice.lower() == 'done':
			break
		try:
			choice = int(choice)
		except ValueError:
			print("请输入有效的商品编号或 'done' 完成选择。")
			continue

		if choice < 1 or choice > len(products):
			print("请输入有效的商品编号或 'done' 完成选择。")
			continue

		selected_product = products[choice - 1]
		selected_item = next(
			(item for item in selected_items if item['product'] == selected_product), None)
		if selected_item:
			selected_item['quantity'] += 1
		else:
			selected_items.append(
				{'product': selected_product, 'price': prices[choice - 1], 'quantity': 1})
		print(f"已选择商品: {selected_product}")

	return {'items': selected_items}


def print_order(order):
	total_price = sum(item['price'] * item['quantity'] for item in order['items'])
	print(f"订单总价: {total_price}")
	for idx, item in enumerate(order['items'], 1):
		print(
			f"  商品 {idx}: 商品名: {item['product']}, 价格: {item['price']}, 数量: {item['quantity']}")


# 生成订单
def generate_orders(num_orders):
	orders = []
	for _ in range(num_orders):
		order = generate_order()
		orders.append(order)
	return orders


# 选择要支付的订单
def select_order_to_pay(orders):
	print("\n请选择要支付的订单（输入订单编号）：")
	for idx, order in enumerate(orders, 1):
		print(
			f"{idx}. 订单总价: {sum(item['price'] * item['quantity'] for item in order['items'])}")
	while True:
		choice = input("订单编号：")
		try:
			choice = int(choice)
			if 1 <= choice <= len(orders):
				return orders[choice - 1]
			else:
				print("请输入有效的订单编号。")
		except ValueError:
			print("请输入有效的订单编号。")


# # 测试生成订单
# num_orders = int(input("请输入要生成的订单数："))
# orders = generate_orders(num_orders)
# for idx, order in enumerate(orders, 1):
# 	print(f"\n订单 {idx}:")
# 	print_order(order)
#
# # 选择要支付的订单并单独打印该订单的详细信息
# chosen_order = select_order_to_pay(orders)
# print("\n您选择支付的订单：")
# print_order(chosen_order)


def generate_select_order():
	# 测试生成订单
	num_orders = int(input("请输入要生成的订单数："))
	orders = generate_orders(num_orders)
	for idx, order in enumerate(orders, 1):
		print(f"\n订单 {idx}:")
		print_order(order)

	# 选择要支付的订单并单独打印该订单的详细信息
	chosen_order = select_order_to_pay(orders)
	print("\n您选择支付的订单：")
	print_order(chosen_order)
