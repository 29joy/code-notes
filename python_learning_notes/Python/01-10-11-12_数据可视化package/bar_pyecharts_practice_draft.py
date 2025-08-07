# =====================================================基础柱状图===================================================================
# from pyecharts.charts import Bar
# from pyecharts.options import LabelOpts
#
# bar = Bar()
# bar.add_xaxis(["china", "usa", "england"])
# # bar.add_yaxis("GDP", [30, 20, 10])
# bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))# 反转两轴之后想要把数值显示在柱的右边而非柱的上方
# # 反转x轴y轴
# bar.reversal_axis()
#
# bar.render("gdp_comparasion_three_countries.html")


# =====================================================时间线柱状图=================================================================
# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import LabelOpts
# from pyecharts.globals import ThemeType

# bar1 = Bar()
# bar1.add_xaxis(["china", "usa", "england"])
# bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))# 反转两轴之后想要把数值显示在柱的右边而非柱的上方
# bar1.reversal_axis()

# bar2 = Bar()
# bar2.add_xaxis(["china", "usa", "england"])
# bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))# 反转两轴之后想要把数值显示在柱的右边而非柱的上方
# bar2.reversal_axis()

# bar3 = Bar()
# bar3.add_xaxis(["china", "usa", "england"])
# bar3.add_yaxis("GDP", [70, 60, 40], label_opts=LabelOpts(position="right"))# 反转两轴之后想要把数值显示在柱的右边而非柱的上方
# bar3.reversal_axis()

# bar4 = Bar()
# bar4.add_xaxis(["china", "usa", "england"])
# bar4.add_yaxis("GDP", [100, 90, 60], label_opts=LabelOpts(position="right"))# 反转两轴之后想要把数值显示在柱的右边而非柱的上方
# bar4.reversal_axis()

# # 创建时间线
# timeline = Timeline()
# # 添加柱状图对象到timeline
# timeline.add(bar1, "2021年GDP")
# timeline.add(bar2, "2022年GDP")
# timeline.add(bar3, "2023年GDP")
# timeline.add(bar4, "2024年GDP")
# # 数据自动播放
# timeline.add_schema(
#     play_interval=1000,# 自动播放的时间间隔, 单位毫秒
#     is_timeline_show=True,# 是否在自动播放的时候显示时间线
#     is_auto_play=True,# 是否自动播放
#     is_loop_play=True# 是否循环自动播放
# )
# # 时间线设置主题
# # timeline = Timeline(
# #     {"theme": ThemeType.LIGHT}
# # )
# """
# 不同主题对应的颜色不一样
# WHITE是红蓝(默认颜色, 等同于bar=Bar())
# LIGHT是蓝黄粉(高亮颜色)
# DARK是红蓝(黑色背景)
# CHALK是红蓝 绿(黑色背景)
# ESSOS是红黄(暖色系)
# INFOGRAPHIC是红蓝黄(偏亮)
# MACARONS是紫绿
# PURPLE_PASSION是粉紫(灰色背景)
# ROMA是红黑灰(偏暗)
# ROMANTIC是红粉蓝(淡黄色背景)
# """
# # 通过时间轴绘图
# timeline.render("timeline_bar.html")


# =====================================================动态柱状图=================================================================
# 列表的sort方法
# 带名函数形式
# my_list = [["a", 33], ["b", 55], ["c", 11]]
# def choose_sort_key(element):
#     return element[1]
#
# my_list.sort(key=choose_sort_key, reverse=True)
# print(my_list)# 输出为[['b', 55], ['a', 33], ['c', 11]]
# # 匿名lambda函数形式
# my_list.sort(key=lambda element:element[1], reverse=True)
# print(my_list)# 输出为[['b', 55], ['a', 33], ['c', 11]]

# 动态图表需求分析
"""
1、GDP数据处理为亿级
2、有时间轴, 按照年份为时间轴的点
3、x轴和y轴反转, 同时每一年的数据只要前8名国家
4、有标题, 标题的年份会动态更改
5、设置了主题的LIGHT
"""
# ---------------------------------------------------数据处理-----------------------------------------------------------
"""
思路:
数据是一个list[]里面都是字典
{"Country Name":"Zimbabwe","Country Code":"ZWE","Year":2023,"Value":26538273498.84614}
先对year进行排序, print之后得到最大的year和最小的year
还要对所有的value转化为以亿为单位, 小数点保留2位吧
"""
import json
from collections import Counter
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 打开文件
f = open(r"D:\code_joy\python\pythonProject\data\GDP.json", 'r', encoding = 'UTF-8')
data = f.read()
# print(data)

# 关闭文件
f.close()

# 转化为python列表
data_python_list = json.loads(data)# 一开始忘了转化成python数据, 下面进行排序一直报错

#先对year进行排序, print之后得到最大的year和最小的year
# 方法一: 先对data排序, 排序是按照year的大小, 获得最大值后再取出其中的year就可以了
max_year = max(data_python_list, key=lambda x:x["Year"])["Year"]
min_year = min(data_python_list, key=lambda x:x["Year"])["Year"]
print("最大年份是: ", max_year)# 2023
print("最小年份是: ", min_year)# 1960
# 方法二: 用集合方式获取所有年份后排序
# years = {entry["Year"] for entry in data_list}
# print("最小年: ", min(years), "最大年: ", max(years))

# 判断每个年份出现的次数, 如果小于8次, 说明当年统计了GDP的国家数量不足8个, 那就把那一年去掉
year_data = [entry["Year"] for entry in data_python_list]
year_count = Counter(year_data)
for year, count in year_count.items():
    if count != 262:
        print(f"Year {year} 出现了 {count} 次")# 没有一个年份不符合要求所以不用删除数据
        # 去掉该年份的数据
        # 列表删除元素

# 创建2023-1960=63个bar
# 建一个bar的列表, 这个列表里存的是对应年份中前8个国家的名称以及它们对应的value, 也就是
countries = {entry["Country Name"] for entry in data_python_list}
country_count = len(countries)
print(country_count)# 262
data_list = [[data_python_list[0]] * country_count]  * (max_year - min_year)
print(f"data_list的类型是{type(data_list)}")
print(type(data_list[0]))
i = 0
# count = 0
print(data_python_list[0]["Year"])
print(type(data_python_list[0]["Year"]))
while i < (max_year - min_year):
    count = 0
    for entry in data_python_list:
        if entry["Year"] == (1960 + i):
            data_list[i].append(entry)
            count += 1
    print(f"{i}一共append{count}次")
    i += 1
"""
根据输出, 在i=0的时候, 1960年的数据被append138次, 是对的, 因为1960这个年份一共出现138次
i=1的时候, 1961年的数据被append 138+142=280次, 也就是多加了1960年的次数, 之后1962等依次累加
why?我写的哪里不对
没有不对, 只是count一直在累加而已, 不是append一直累加, 把count定义的位置变了一下就对了
"""
# 现在data_list里面包含(max_year - min_year)个小的list,每个小list包含(1960+下标)所在年份所有国家的数据
# 对每个小list按照value进行排序
# 按照年份把不同国家的数据分到不同的list, 每个list排序, 然后把前8个country name赋值给x轴, GDP赋值给y轴
j = 0
while j < (max_year - min_year):
    data_list[j].sort(key=lambda element:element["Value"], reverse=True)
    # 排序后只留前8个国家的数据
    data_list[j] = data_list[j][0:8]
    j += 1

# m = 0
# n = 0
# value_list = []
# country_list = []
# while m < (max_year - min_year):
#     while n < 8:
#         value_list.append(round(data_list[m][n]["Value"] / 100000000, 2))# 保留2位小数
#         country_list.append(data_list[m][n]["Country Name"])
#         n += 1
#     m += 1
value_lists = []   # 每年一组值
country_lists = [] # 每年一组国家

for year_data in data_list:  # 遍历每年
    values = [round(item["Value"] / 1e8, 2) for item in year_data]  # GDP 单位亿
    countries = [item["Country Name"] for item in year_data]
    value_lists.append(values)
    country_lists.append(countries)

# ---------------------------------------------------创建图表-----------------------------------------------------------
# 创建一个bar的list, 存储所有的bar
# bar = Bar()
# bar_list = [bar] * (max_year - min_year)
#
# bar_i = 0
# while bar_i < (max_year - min_year):
#     bar_list[bar_i] = Bar()
#     bar_list[bar_i].add_xaxis(value_list)
#     bar_list[bar_i].add_yaxis("Country Name", country_list, label_opts=LabelOpts(position="right"))
#     bar_list[bar_i].reversal_axis()
#     bar_i += 1
bar_list = []
for i in range(len(value_lists)):
    bar = Bar()
    bar.add_xaxis(country_lists[i])  # 国家为 X
    bar.add_yaxis("GDP（亿美元）", value_lists[i], label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar_list.append(bar)
# 创建时间线
timeline = Timeline()
# 将每个bar add到timeline
num = 0
# while num < (max_year - min_year):
#     timeline.add(bar_list[num], f"{1960 + num}Year")
#     num += 1
for i in range(len(bar_list)):
    timeline.add(bar_list[i], f"{min_year + i}")
# 数据自动播放
timeline.add_schema(
    play_interval=1000,# 自动播放的时间间隔, 单位毫秒
    is_timeline_show=True,# 是否在自动播放的时候显示时间线
    is_auto_play=True,# 是否自动播放
    is_loop_play=True# 是否循环自动播放
)
# 时间线设置主题
# timeline = Timeline(
#     {"theme": ThemeType.LIGHT}
# )
# 通过时间轴绘图
timeline.render("ALL_Countries_GDP_Comparison_Bar.html")

"""
生成的图片虽然在动但是每个bar不能正常显示, 感觉还是我x轴和y轴加的有问题？
"""
