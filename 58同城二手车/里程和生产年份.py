import csv
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Line

# 读取 CSV 文件
csv_file = 'file_ershoucar_untis.csv'  # 替换为您的 CSV 文件路径
data = []
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# 提取品牌数据并统计数量
brand_counter = Counter(row[0] for row in data[1:])

# 获取数量前五的车品牌
top_brands = brand_counter.most_common(5)

# 提取数量前五的车品牌数据
brand_data = {brand[0]: [] for brand in top_brands}
for row in data[1:]:
    if row[0] in brand_data:
        brand_data[row[0]].append((row[4], row[5], row[6]))

# 计算 x 轴的刻度
x_ticks = [str(2004 + i * 2) for i in range(11)]

# 创建折线图
c = Line()

# 添加数据系列
for brand, brand_values in brand_data.items():
    # 统计每年的数量
    counts = [0] * 11
    for value in brand_values:
        year = int(value[0][:4])
        index = (year - 2004) // 2
        counts[index] += 1

    # 添加折线图系列
    c.add_xaxis(xaxis_data=x_ticks)
    c.add_yaxis(
        series_name=brand,
        y_axis=counts,
        symbol_size=10,
        label_opts=opts.LabelOpts(
            formatter="{c}",
            position="top",
            font_size=12,
            font_weight="bold",
            color="rgba(0,0,0,0.8)",
        ),
    )

# 设置全局选项
c.set_global_opts(
    title_opts=opts.TitleOpts(title="汽车上牌时间分布", pos_left="center"),
    xaxis_opts=opts.AxisOpts(
        type_="category",
        name="上牌时间(年)",
        splitline_opts=opts.SplitLineOpts(is_show=True),
        axislabel_opts=opts.LabelOpts(interval=0),  # 设置 x 轴标签间隔
    ),
    yaxis_opts=opts.AxisOpts(
        type_="value",
        name="数量",
        splitline_opts=opts.SplitLineOpts(is_show=True),
    ),
    legend_opts=opts.LegendOpts(
        orient="vertical", pos_right="5%", pos_top="middle"
    ),  # 设置图例垂直布局，位于图表右侧
)

# 保存图表为 HTML 文件
c.render("汽车数据分布.html")
