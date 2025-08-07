from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

map = Map()

data = [
    ("北京", 399),
    ("天津", 299),
    ("上海", 699),
    ("湖北", 1299),
    ("山东", 699),
    ("河南", 799),
    ("广东", 1199),
    ("重庆", 899),
    ("浙江", 899),
    ("江苏", 899),
    ("山西", 299),
    ("辽宁", 399),
]

map.add("各省新增病例", data, maptype="china")

map.set_global_opts(
    title_opts=TitleOpts(title="中国各省新增病例分布图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000人以上", "color": "#990033"},
        ],
        series_index=0
    )
)

map.render("china_covid_cases_map.html")
