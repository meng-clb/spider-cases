import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Line, Bar
from pyecharts.globals import ThemeType
from pyecharts.charts import Page

# 读取CSV文件
df = pd.read_csv('file_ershoucar_untis.csv')

# 第一个图表：饼图
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

# 第二个图表：折线图
brand_counts_line = df.groupby('品牌').size().reset_index(name='车辆数量')
top_15_brands_line = brand_counts_line.nlargest(15, '车辆数量')
line_chart = Line()
line_chart.add_xaxis(top_15_brands_line['品牌'].tolist())
line_chart.add_yaxis("车辆数量", top_15_brands_line['车辆数量'].tolist())
line_chart.set_global_opts(title_opts=opts.TitleOpts(title="前15个品牌车辆数量折线图"),
                           xaxis_opts=opts.AxisOpts(name="品牌"),
                           yaxis_opts=opts.AxisOpts(name="车辆数量"),
                           tooltip_opts=opts.TooltipOpts(trigger="axis"))

# 第三个图表：柱状图
brand_counts_bar = df['品牌'].value_counts().head(8).reset_index()
brand_counts_bar.columns = ['品牌', '数量']
bar_chart = Bar()
bar_chart.add_xaxis(brand_counts_bar['品牌'].tolist())
bar_chart.add_yaxis("品牌数量", brand_counts_bar['数量'].tolist())
bar_chart.set_global_opts(title_opts=opts.TitleOpts(title="品牌数量分布（排名前8）"),
                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))

# 创建一个Page对象
page = Page(layout=Page.DraggablePageLayout)

# 将图表添加到Page对象中
page.add(pie_chart)
page.add(line_chart)
page.add(bar_chart)

# 渲染包含所有图表的Page对象到HTML文件
page.render("all_charts.html")