import os

with open('url_list.csv', 'r', encoding='utf-8') as f:
	lines = f.readlines()
f_name_list = []
for line in lines:
	f_name = line.split('/')[-1].strip() + '.csv'
	f_name_list.append(f_name)


def find_missing_files(directory, file_names):
	# 获取文件夹内所有文件的文件名
	all_files = os.listdir(directory)
	# 将文件名转换为集合，以便进行快速比较
	all_files_set = set(all_files)
	# 将你的文件名列表转换为集合
	file_names_set = set(file_names)
	# 找到缺失的文件名
	missing_files = list(file_names_set - all_files_set)
	return missing_files


# 替换为你要读取的文件夹路径
directory = './comment'

missing_files = find_missing_files(directory, f_name_list)
print("缺失的文件:", missing_files)


#缺失的文件: ['LxcPj73Ts.csv', 'LowBX3tnr.csv', 'Max60g1op.csv']