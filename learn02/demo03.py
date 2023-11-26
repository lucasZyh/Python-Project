"""
折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

f_us = open("折线图数据/美国.txt", "r", encoding="utf-8")
f_jp = open("折线图数据/日本.txt", "r", encoding="utf-8")
f_in = open("折线图数据/印度.txt", "r", encoding="utf-8")

data_us = f_us.read().replace("jsonp_1629344292311_69436(", "")[:-2]
data_jp = f_jp.read().replace("jsonp_1629350871167_29498(", "")[:-2]
data_in = f_in.read().replace("jsonp_1629350745930_63180(", "")[:-2]

# JSON转换成字典
dict_us = json.loads(data_us)
dict_jp = json.loads(data_jp)
dict_in = json.loads(data_in)

# 取出trend数据
trend_us = dict_us["data"][0]["trend"]
trend_jp = dict_jp["data"][0]["trend"]
trend_in = dict_in["data"][0]["trend"]

# 获取日期数据
x_data_us = trend_us["updateDate"][:314]
x_data_jp = trend_jp["updateDate"][:314]
x_data_in = trend_in["updateDate"][:314]

# 获取确诊数据
y_data_us = trend_us["list"][0]["data"][:314]
y_data_jp = trend_jp["list"][0]["data"][:314]
y_data_in = trend_in["list"][0]["data"][:314]

# 折线图
line = Line()

line.add_xaxis(x_data_us)

line.add_yaxis("美国确诊人数", y_data_us, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", y_data_jp, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", y_data_in, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020年确诊人数对比折线图", pos_left="center", pos_bottom="1%"),

)

line.render("疫情折线图.html")

f_us.close()
f_jp.close()
f_in.close()



