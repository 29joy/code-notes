# 导入相关包
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

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
# [
#     "北京", "天津", "上海", "重庆", "河北", "河南", "云南", "辽宁", "黑龙江", "湖南", "安徽",
#     "山东", "新疆", "江苏", "浙江", "江西", "湖北", "广西", "甘肃", "山西", "内蒙古", "陕西",
#     "吉林", "福建", "贵州", "广东", "青海", "西藏", "四川", "宁夏", "海南", "台湾", "香港", "澳门"
# ]
map.add("地图", data, maptype="china")

# 设置全局选项
map.set_series_opts(label_opts={"is_show": True})  # 显示省份标签
map.set_global_opts(
    title_opts={"text": "中国各省新增病例分布图"},
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1, "max":9, "label":"1-9人", "color":"#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000人以上", "color": "#990033"},
        ],
    series_index=0
    )
)
map.render("2020_covid_china_map.html")

# -------------------------------------------------地域名称要对应----------------------------------------------------
"""
第一次输入的省份等都是用拼音的, 如beijing、shandong, 但是没有生成出来, 改成汉字之后成功显示了, 第一次没有显示成功是和输入的不是汉字有关吗
是的, **你第一次没有成功显示地图, 是因为省份名称必须使用中文名称**, 不能用拼音。
原因解释: 
在 `pyecharts` 的 `Map` 地图中, 地图区域的匹配是基于 **内置地理数据文件（GeoJSON）** 的。这些文件中: 
* **中国地图使用的是中文行政区名称**, 比如: 
  * `"北京"` ✅
  * `"beijing"` ❌（无法对应）
官方推荐: 如何避免出错？
你可以用这个辅助工具来获取所有支持的地区名: 
from pyecharts.globals import ChartType, SymbolType
from pyecharts.datasets import register_url
# 注册地图文件来源（可选, 不加默认也是中国地图）
register_url("https://echarts-maps.github.io/echarts-countries-js")
# 打印支持的地区（你可根据这个来构造数据）
from pyecharts.globals import GeoType
print(GeoType.get_coordinate_name("china"))
但实际更推荐的方法是: **直接参考这份完整中文省份列表**: 
[
    "北京", "天津", "上海", "重庆", "河北", "河南", "云南", "辽宁", "黑龙江", "湖南", "安徽",
    "山东", "新疆", "江苏", "浙江", "江西", "湖北", "广西", "甘肃", "山西", "内蒙古", "陕西",
    "吉林", "福建", "贵州", "广东", "青海", "西藏", "四川", "宁夏", "海南", "台湾", "香港", "澳门"
]
"""
# -------------------------------------------------颜色对照表----------------------------------------------------
"""
"#FF6666"等是6位颜色值
ab173有一个前端->rgb颜色对照表, 想要哪个颜色通过拖拽并查看其对应的6位颜色值即可
"""
# -------------------------------------------------国际常用工具----------------------------------------------------
"""
在非中国区域, 尤其是欧美、印度、日韩等开发者群体中, 最常使用的、功能与 `pyecharts` 类似的 **数据可视化工具** 有以下几类: 

---

## ✅ 1. **Plotly**（最接近 `pyecharts` 的交互式图表库）

* 📌 特点: 

  * 支持交互式图表（缩放、悬浮、点击等）
  * 可导出为 HTML, 适合网页嵌入
  * 封装良好, 适用于 Python / JavaScript / R 等语言

* 🌍 全球广泛使用, 文档丰富、支持地图、3D、热力图等

* 🎯 推荐替代 `pyecharts` 进行交互式数据分析与演示

```bash
pip install plotly
```

```python
import plotly.express as px

fig = px.choropleth(
    locations=["USA", "JPN", "IND"],
    locationmode="country names",
    color=[1000, 500, 300],
    title="COVID-19 Total Cases"
)
fig.show()
```

---

## ✅ 2. **Matplotlib + Seaborn**（科学分析图表主力）

* 📊 标准科研图、静态图的主力工具
* 📚 用于生成柱状图、折线图、散点图、箱线图等
* 📦 `seaborn` 是在 matplotlib 之上做的高级封装, 语法更简洁、默认美观

```bash
pip install matplotlib seaborn
```

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(x=["Jan", "Feb", "Mar"], y=[100, 300, 200])
plt.title("Monthly Cases")
plt.show()
```

---

## ✅ 3. **Altair**（轻量级、声明式、可导出 HTML）

* 📋 语法与 `pyecharts` 类似（数据驱动式）, 专注于可视化“语义表达”
* 🎨 支持 Vega/Vega-Lite 格式, 便于嵌入网页

```bash
pip install altair
```

```python
import altair as alt
import pandas as pd

df = pd.DataFrame({
    "country": ["USA", "JPN", "IND"],
    "cases": [1000, 500, 300]
})

chart = alt.Chart(df).mark_bar().encode(
    x="country",
    y="cases"
)

chart.show()
```

---

## ✅ 总结对比

| 工具             | 类型         | 是否交互 | 使用范围    | 推荐用途          |
| -------------- | ---------- | ---- | ------- | ------------- |
| **Plotly**     | 高级图表库      | ✅    | 全球广泛    | 仪表盘、HTML输出、地图 |
| **Matplotlib** | 基础图表库      | ❌    | 学术科研    | 静态图、高度自定义图表   |
| **Seaborn**    | 美化封装库      | ❌    | 数据科学    | 统计图表、探索性分析    |
| **Altair**     | 声明式图表      | ✅    | 轻量可嵌入网页 | 可视化简报、网页嵌入    |
| **pyecharts**  | 基于 ECharts | ✅    | 中国区为主   | 地图、交互动画、中文支持强 |

---

是否要我为你提供一个 [`plotly 重现 pyecharts 地图功能的示例`](f)？可以用同样的数据绘制全球国家或中国省份热力图。

"""