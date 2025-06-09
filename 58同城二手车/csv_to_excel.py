import pandas as pd

# 读取CSV文件
df = pd.read_csv('file_ershoucar_untis.csv')

# 将数据保存为Excel文件
df.to_excel('file_ershoucar_untis.xlsx', index=False)