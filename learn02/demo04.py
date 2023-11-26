from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 1. 创建地图对象
map = Map()

# 2. 添加数据
map.add("测试", [("广东省", 100), ("北京市", 200), ("上海市", 300)], "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_piecewise=True,
        pieces=[
            {"min": 0, "max": 50, "label": "0-100", "color": "#CCFFFF"},
            {"min": 50, "max": 100, "label": "100-200", "color": "#CC6666"},
            {"min": 100, "max": 200, "label": "200-300", "color": "#990033"},
            {"min": 200, "max": 300, "label": "300-400", "color": "#0000FF"},
        ],
    )
)

# 3. 生成网页
map.render("map.html")
