import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line

# 读取CSV文件
df = pd.read_csv("file_ershoucar_untis.csv")

# 获取数量最多的前5个品牌
top5_brands = df['品牌'].value_counts().head(5).index.tolist()

# 创建一个空的DataFrame，用于存储每个价格区间的车辆数量
price_ranges_counts = pd.DataFrame(columns=["价格区间"] + top5_brands)

# 设置价格区间
price_ranges = [(i, i + 3) for i in range(0, 18, 3)]

# 遍历每个价格区间
for price_range in price_ranges:
	range_label = f"{price_range[0]}-{price_range[1]}万"
	price_ranges_counts = pd.concat(
		[price_ranges_counts, pd.DataFrame({"价格区间": [range_label]})], ignore_index=True)

	# 统计每个品牌在当前价格区间的车辆数量
	for brand in top5_brands:
		brand_count = len(df[(df['品牌'] == brand) & (df['价格(万)'] >= price_range[0]) & (
					df['价格(万)'] < price_range[1])])
		price_ranges_counts.at[price_ranges_counts.index[-1], brand] = brand_count

# 创建折线图
line = (
	Line()
	.set_global_opts(
		title_opts=opts.TitleOpts(title="前5个品牌二手车价格区间统计"),
		xaxis_opts=opts.AxisOpts(name="价格区间"),
		yaxis_opts=opts.AxisOpts(name="数量"),
	)
)

# 添加数据
for brand in top5_brands:
	line.add_xaxis(price_ranges_counts["价格区间"].tolist())
	line.add_yaxis(brand, price_ranges_counts[brand].tolist(), is_smooth=True)

# 生成HTML文件
line.render("top5price.html")
