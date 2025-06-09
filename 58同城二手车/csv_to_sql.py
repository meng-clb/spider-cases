import csv

import pymysql

# 链接数据库
db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='root',
                     database='meng')

# 创建游标对象
cursor = db.cursor()

with open('file_ershoucar_untis.csv', 'r', encoding='utf-8') as f:
	csv_reader = csv.reader(f)
	# 跳过第一行
	next(csv_reader, None)
	# 读取并处理剩余的行
	i = 1
	for row in csv_reader:
		# print(row)
		sql = (f"insert into cq_ershoucar values(null, '{row[0]}', '{row[1]}', '{row[2]}','{row[3]}',"
		       f"'{row[4]}',{row[5]},{row[6]});")
		try:
			print(f'开始插入第{i}条数据')
			cursor.execute(sql)
			db.commit()
			i += 1
		except Exception as e:
			db.rollback()
			with open('log.txt', 'a', encoding='utf-8') as f:
				f.write(f'{e} => {sql}')

# # 使用有游标对象执行sql命令
# sql = 'select * from douban'
# cursor.execute(sql)
#
# data = cursor.fetchall()
# print(data)

db.close()

# CREATE TABLE IF NOT EXISTS cq_ershouCAR (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     brand VARCHAR(255) NOT NULL,
#     model VARCHAR(255) NOT NULL,
#     type VARCHAR(255) NOT NULL,
#     tags VARCHAR(255),
#     registration_year varchar(255) NOT NULL,
#     mileage DECIMAL(10, 2) NOT NULL,
#     price DECIMAL(10, 2) NOT NULL
# );
