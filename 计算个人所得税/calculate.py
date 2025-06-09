# 定义个人所得税计算函数
def calculate_income_tax(wage, social_insurance):
	tax_free = 5000  # 免征额
	taxable_income = wage - social_insurance - tax_free  # 应纳税所得额

	# 税率表
	tax_rates = [(5000, 0, 0), (8000, 0.03, 0), (17000, 0.10, 210), (30000, 0.20, 1410),
	             (40000, 0.25, 2660), (60000, 0.30, 4410)]

	tax = 0
	for threshold, rate, quick_deduction in tax_rates:
		if taxable_income <= threshold:
			tax = taxable_income * rate - quick_deduction
			break

	return max(tax, 0)


# 读取文件并计算个人所得税
def calculate_tax_for_all(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	result = []

	for line in lines[1:]:  # 跳过标题行
		data = line.strip().split(',')
		name = data[0]
		wage = float(data[1])
		social_insurance = float(data[2]) + float(data[3]) + float(data[4]) + float(
			data[5]) + float(data[6])
		tax = calculate_income_tax(wage, social_insurance)
		result.append((name, tax))

	# 将结果写入文件
	with open(output_file, 'w', encoding='utf-8') as f:
		f.write("姓名,个人所得税\n")
		for name, tax in result:
			f.write(f"{name},{tax}\n")


if __name__ == '__main__':
	input_file = "test_data.csv"  # 读取放置数据的文件
	output_file = "test_result.csv"  # 输出的文件
	calculate_tax_for_all(input_file, output_file)
