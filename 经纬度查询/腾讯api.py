import pandas as pd
import requests


# 腾讯地图API地址解析函数
def get_coordinates_from_tencent_map(address, api_key):
	url = f"https://apis.map.qq.com/ws/geocoder/v1/?address={address}&key={api_key}"
	response = requests.get(url)
	data = response.json()
	if data.get('status') == 0:
		location = data.get('result').get('location')
		return f"{location.get('lng')},{location.get('lat')}"  # 返回经度,纬度，用逗号隔开
	else:
		print(f"地址解析失败：{address}")
		return None


# 原始Excel文件名
original_excel_file = '汽车.xlsx'
# 新的Excel文件名
new_excel_file = '汽车max.xlsx'
# 腾讯地图API密钥
tencent_map_api_key = ''

# 读取原始Excel文件中的所有sheet名
with pd.ExcelFile(original_excel_file) as xls:
	sheet_names = xls.sheet_names

# 遍历每个sheet，查询经纬度并保存到新的DataFrame
with pd.ExcelWriter(new_excel_file, mode='w', engine='openpyxl') as writer:
	for sheet_name in sheet_names:
		# 读取原始sheet的数据
		df = pd.read_excel(original_excel_file, sheet_name=sheet_name)
		# 初始化一个新的DataFrame来存储结果，只包含序号和公司名
		new_df = pd.DataFrame(columns=['序号', '公司名'])

		# 遍历每行数据，查询经纬度
		for index, row in df.iterrows():
			company_name = row['公司名']  # 假设公司名称在'公司名'列
			serial_number = row['序号']  # 假设序号在'序号'列

			coordinates = get_coordinates_from_tencent_map(company_name, tencent_map_api_key)
			if coordinates:
				# 将查询到的经纬度添加到新DataFrame的'公司名'列后面作为新列
				new_row = {'序号': serial_number, '公司名': company_name, '经纬度': coordinates}
				new_df = new_df.append(new_row, ignore_index=True)
			else:
				print(f"公司名 {company_name} 的经纬度查询失败")

			# 将新的DataFrame保存到新的Excel文件的对应sheet中
		new_df.to_excel(writer, sheet_name=sheet_name, index=False)

# 打印保存成功的消息
print(f"新的Excel文件'{new_excel_file}'已保存，包含查询到的公司经纬度信息。")