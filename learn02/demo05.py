"""
演示全国疫情可视化地图开发
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
province_data_list = json.loads(data)["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = []  # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数

    # 北京、上海、天津、重庆，需要添加市
    if province_name in ["北京", "上海", "天津", "重庆"]:
        province_name += "市"
    # 内蒙古、西藏，需要添加自治区
    elif province_name in ["内蒙古", "西藏"]:
        province_name += "自治区"
    # 广西，需要添加壮族自治区
    elif province_name == "广西":
        province_name += "壮族自治区"
    # 宁夏，需要添加回族自治区
    elif province_name == "宁夏":
        province_name += "回族自治区"
    # 新疆，需要添加维吾尔自治区
    elif province_name == "新疆":
        province_name += "维吾尔自治区"
    # 香港、澳门，需要添加特别行政区
    elif province_name in ["香港", "澳门"]:
        province_name += "特别行政区"
    # 其他省份添加省
    else:
        province_name += "省"

    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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
map.render("全国疫情地图.html")
