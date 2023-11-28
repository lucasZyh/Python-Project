from file import FileReader, TextFileReader, JsonFileReader
from data import Record

from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_data()  # type: list[Record]
feb_data = json_file_reader.read_data()  # type: list[Record]

# 将2个月份的数据合并为1个list来存储
all_data = jan_data + feb_data  # type: list[Record]

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))       # 添加x轴的数据
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))      # 添加了y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")

