import csv
from collections import Counter
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Line
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Page


# 第一个图表：饼图
def generate_brand_pie_chart(df):
    brand_counts_pie = df['品牌'].value_counts().head(15)
    pie_chart = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    pie_chart.add("", [list(z) for z in
                       zip(brand_counts_pie.index.tolist(), brand_counts_pie.values.tolist())],
                  radius=["40%", "75%"],
                  label_opts=opts.LabelOpts(position="outside", formatter="{b}: {c} ({d}%)"),
                  center=["50%", "50%"])
    pie_chart.set_global_opts(title_opts=opts.TitleOpts(title="前15个品牌车辆占比"),
                              legend_opts=opts.LegendOpts(orient="vertical", pos_left="left",
                                                          pos_top="15%"))
    return pie_chart


# 第二个图表：折线图
def generate_top5_price_line_chart(df):
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

    return line


if __name__ == "__main__":
    # 读取 CSV 文件
    csv_file = 'file_ershoucar_untis.csv'  # 替换为您的 CSV 文件路径
    df = pd.read_csv(csv_file)

    # 生成图表
    pie_chart = generate_brand_pie_chart(df)
    line_chart = generate_top5_price_line_chart(df)

    # 读取第二个 CSV 文件
    csv_file_2 = 'file_ershoucar_untis.csv'  # 替换为您的 CSV 文件路径
    data = []
    with open(csv_file_2, 'r', encoding='utf-8') as file:
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
    line2 = Line()

    # 添加数据系列
    for brand, brand_values in brand_data.items():
        # 统计每年的数量
        counts = [0] * 11
        for value in brand_values:
            year = int(value[0][:4])
            index = (year - 2004) // 2
            counts[index] += 1

        # 添加折线图系列
        line2.add_xaxis(xaxis_data=x_ticks)
        line2.add_yaxis(
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
    line2.set_global_opts(
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

    # 创建一个Page对象
    page = Page(layout=Page.DraggablePageLayout)

    # 将图表添加到Page对象中
    page.add(pie_chart)
    page.add(line_chart)
    page.add(line2)

    # 渲染包含所有图表的Page对象到HTML文件
    page.render("show_data.html")
