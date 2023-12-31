"""
河南省疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
# 关闭文件
f.close()
# 取到各省数据
cities_data_list = json.loads(data)["areaTree"][0]["children"][3]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = []  # 绘图需要用的数据列表
for city_data in cities_data_list:
    city_name = city_data["name"] + "市"  # 省份名称
    city_confirm = city_data["total"]["confirm"]  # 确诊人数
    data_list.append((city_name, city_confirm))

# 手动添加济源市的数据
data_list.append(("济源市", 5))

# 创建地图对象
map = Map()
# 添加数据
map.add("河南省疫情分布", data_list, "河南")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("河南省疫情地图.html")
