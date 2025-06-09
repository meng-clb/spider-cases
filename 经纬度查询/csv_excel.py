import pandas as pd

# 读取CSV文件
df = pd.read_csv('起亚.csv')

# 将数据保存为Excel文件
df.to_excel('起亚.xlsx', index=False)