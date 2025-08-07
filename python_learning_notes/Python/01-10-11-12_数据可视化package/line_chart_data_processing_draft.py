# 从所有国家数据中获得美国、印度和日本三个国家的数据,这部分代还没弄懂,暂时先不管了
# import json
#
# with open(r"D:\code_joy\python\pythonProject\data\owid-covid-data.json") as f:
#     data = json.load(f)
#
# for code in ['USA','IND','JPN']:
#     recs = data.get(code, {}).get('data', [])
#     recs2020 = [r for r in recs if r['date'].startswith('2020-')]
#     with open(f'{code}.json','w') as out:
#         json.dump({code: recs2020}, out, indent=2)



# 我和授课视频中的数据结构不一样,这里只积累一下视频中提到的方法等,后面和我自己的数据具体的实现就不一样了
# 导入相关包
import json
from operator import index

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts, TooltipOpts
from pyecharts.options import DataZoomOpts
from collections import Counter
# 得到折线图对象
line = Line()
# 处理数据
f_usa = open(r"D:\code_joy\python\pythonProject\data\USA.json", 'r', encoding = 'UTF-8')
usa_data = f_usa.read()
f_jpn = open(r"D:\code_joy\python\pythonProject\data\JPN.json", 'r', encoding = 'UTF-8')
jpn_data = f_jpn.read()
f_ind = open(r"D:\code_joy\python\pythonProject\data\IND.json", 'r', encoding = 'UTF-8')
ind_data = f_ind.read()
# 去掉不和json规范的开头
"""
usa_data = usa_data.replace("", "")
这里就是用了字符串的replace方法将不规范内容替换为空,不过这样还是要打开文件啊,是否可以通过将第一行或者前几行读取出来的方式看一下哪些是
不符合规范的内容而避免打开文件
"""
# 去掉不和json规范的结尾
"""
usa_data = usa_data[:-2]
这里视频中结尾要去掉的是");",如果用usa_data.replace(");", "")但是整个文件中很多地方有");"那替换多了
避免此问题就用字符串的切片,从头开始切usa_data[:-2], -2表示切到倒数第二个但是不包含倒数第二个
"""
# json转python字典
usa_python_dict = json.loads(usa_data)
# print(type(usa_python_dict))# 输出为<class 'dict'>
# print(usa_python_dict)
jpn_python_dict = json.loads(jpn_data)
ind_python_dict = json.loads(ind_data)
# 过滤掉值为0的数据
filtered_usa_data = [entry for entry in usa_python_dict["USA"] if entry["new_cases"] and entry["new_cases"] > 0]
filtered_jpn_data = [entry for entry in jpn_python_dict["JPN"] if entry["new_cases"] and entry["new_cases"] > 0]
filtered_ind_data = [entry for entry in ind_python_dict["IND"] if entry["new_cases"] and entry["new_cases"] > 0]
# # 计算2020-01-26出现的次数
# print(filtered_jpn_data)
# jpn_dates = [entry["date"] for entry in filtered_jpn_data]
# print(jpn_dates)
# date_count = Counter(jpn_dates)
# print(date_count)
# for date, count in date_count.items():
#     if count > 1:
#         print(f"{date} 出现了 {count} 次")
"""
到这里没有报错成功输出了内容说明json内容已经被转化为python字典了
老师视频中用的是txt文件,和我的json文件都可以被成功转化
"""
# 获取日期数据用于x轴
# 三个国家的日期取交集
# 取三个国家的日期集合
usa_dates = set([entry["date"] for entry in filtered_usa_data if entry["new_cases"] > 0])
jpn_dates = set([entry["date"] for entry in filtered_jpn_data if entry["new_cases"] > 0])
ind_dates = set([entry["date"] for entry in filtered_ind_data if entry["new_cases"] > 0])
# 交集
common_dates = sorted(usa_dates & jpn_dates & ind_dates)

# 根据交集筛选每个国家的数据
def filter_by_dates(data, country_key, valid_dates):
    return [entry for entry in data[country_key] if entry["date"] in valid_dates]

usa_filtered = filter_by_dates(usa_python_dict, "USA", common_dates)
jpn_filtered = filter_by_dates(jpn_python_dict, "JPN", common_dates)
ind_filtered = filter_by_dates(ind_python_dict, "IND", common_dates)

# 分别构造 x 和 y
x_date = common_dates
line.add_xaxis(x_date)
# """
# 思路: 将每一个date取出来赋值给x轴
# 先定义一个列表,用于存放所有的date,然后把这个列表赋值给x轴
# 这个列表的一个元素是一个date
# 这个列表的长度是"USA"这个key对应的value这个列表的长度
# """
# # data_length = 5
# # length_test = len(usa_python_dict["USA"])
# # print(length_test)
# # x_date = [usa_python_dict["USA"][0]["date"]] * data_length
# # x_date = [filtered_usa_data["USA"][0]["date"]] * len(usa_python_dict["USA"])
# x_date = [filtered_usa_data[0]["date"]] * len(filtered_usa_data)
# # print(f"x_date是{x_date}1")# 这个能输出成功,说明上面找到date的代码是没有问题的
# i = 0
# while i < len(filtered_usa_data):
# # while i < data_length:
#     x_date[i] = filtered_usa_data[i]["date"]
#     i += 1
# # print(f"x_date是{x_date}2")
# """
# 这里["USA"]表示取字典中"USA"这个key对应的内容,
# 它对应的是一个列表,列表内的元素是很多个字典
# [0]表示取的下标为0的字典,每个字典中有很多键值对
# ["date"]表示取的是"date"这个key对应的value
# """
# line.add_xaxis(x_date)
# 获取当日新增确诊数据用于y轴
# """
# 思路: 将每一个new_cases取出来赋值给y轴
# 先定义一个列表,用于存放所有的new_cases,然后把这个列表赋值给y轴
# 这个列表的一个元素是一个new_cases数字
# 这个列表的长度是"USA"这个key对应的value这个列表的长度
# """
# y_usa_new_cases = [filtered_usa_data[0]["new_cases"]] * len(filtered_usa_data)
# j = 0
# while j < len(filtered_usa_data):
#     y_usa_new_cases[j] = filtered_usa_data[j]["new_cases"]
#     j += 1
#
# y_jpn_new_cases = [filtered_jpn_data[0]["new_cases"]] * len(filtered_jpn_data)
# j = 0
# while j < len(filtered_jpn_data):
#     y_jpn_new_cases[j] = filtered_jpn_data[j]["new_cases"]
#     j += 1
#
# y_ind_new_cases = [filtered_ind_data[0]["new_cases"]] * len(filtered_ind_data)
# j = 0
# while j < len(filtered_ind_data):
#     y_ind_new_cases[j] = filtered_ind_data[j]["new_cases"]
#     j += 1
#
# print("x轴日期数:", len(x_date))
# print("USA数据点数:", len(y_usa_new_cases))
# print("JPN数据点数:", len(y_jpn_new_cases))
# print("IND数据点数:", len(y_ind_new_cases))

y_usa = [entry["new_cases"] for entry in usa_filtered]
y_jpn = [entry["new_cases"] for entry in jpn_filtered]
y_ind = [entry["new_cases"] for entry in ind_filtered]


line.add_yaxis("USA new_cases", y_usa, is_smooth=True, label_opts=LabelOpts(is_show=False))
line.add_yaxis("JPN new_cases", y_jpn, is_smooth=True, label_opts=LabelOpts(is_show=False))
line.add_yaxis("IND new_cases", y_ind, is_smooth=True, label_opts=LabelOpts(is_show=False))

# line.add_yaxis("USA new_cases", y_usa_new_cases, is_smooth=True, label_opts=LabelOpts(is_show=False))
# # 这里is_smooth=True是可以将折线尽量圆滑过渡,label_opts=LabelOpts(is_show=False)是在图表中的折线上不显示具体的数值,当鼠标移动到对应的
# # 点位时会浮现出现,可以避免图表中很多数据非常的乱,这两个其实就是没讲过的系列配置项了,也就是单独对y轴进行配置
# line.add_yaxis("JPN new_cases", y_jpn_new_cases, is_smooth=True, label_opts=LabelOpts(is_show=False))
# line.add_yaxis("IND new_cases", y_ind_new_cases, is_smooth=True, label_opts=LabelOpts(is_show=False))

print("x轴日期数:", len(x_date))
print("USA数据点数:", len(y_usa))
print("JPN数据点数:", len(y_jpn))
print("IND数据点数:", len(y_ind))
line.set_global_opts(
    title_opts=TitleOpts(title="COVID-19 New Cases Comparison", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    # visualmap_opts=VisualMapOpts(is_show=True),
    # 不加 VisualMap,这个是用于热力图等的,会使得颜色都显示为红色从而无法分辨三个国家的数据
    # yaxis_opts=AxisOpts(type_="log")  # 如果你想用对数坐标解决比例过大问题
    datazoom_opts=[
        DataZoomOpts(type_="slider"),  # 底部滑动条
        DataZoomOpts(type_="inside")  # 鼠标滚轮缩放
    ]# 最终的方案中加入滑动条反而无法在打开浏览器的第一时间看到整个图表的全貌, 所以去掉了这个设置
)

# 生成图表
line.render("2020_covid_new_cases.html")# 原来括号内直接输入名字就能生成不同名称的图表了
"""
数据量太大了,生成了很久,所以改成只取前50个数据
还是运行很久,改成只取前5个数据
在57行生成第一个x_date列表时很快,但是62行的新列表很久都生成不了,只需要找5个数据这么难吗
我的电脑一直在呼呼响,好可怜,我带不动很大的数据怎么做兼职啊

老师的数据里,日期就是以一个列表的形式存储的,每天对应的确诊数据也是以一个列表的形式存储的,这就很方便给x轴和y轴赋值了,
我怀疑我的数据还需要处理成老师那样方便处理的形式
现在只是包含11个数据,并且只需要处理5个数据,处理了10分钟还没有处理完
原来是因为我在while循环里没有执行i += 1 和 j += 1陷入了死循环,让我怎么形容自己呢
改好之后瞬间完成
所以和数据格式等都没关系喽
"""
# 关闭文件对象
f_usa.close()
f_jpn.close()
f_ind.close()
"""
最终我生成的图表看上去不像老师的图表那么连贯,这是因为我的数据中很多日期的新增数据为0,导致折线图看上去不连贯,像是柱状图,
所以很多时候处理数据时也许应该去掉为0的数据
#不一定“必须删”,而是要**根据目标灵活处理**。下面是具体说明: 

什么时候“应该删除”所有为 0 或 null 的数据？
#情况 1: **数据为 0/null 是无效占位或错误值**
* 比如新冠疫情初期,某些国家每天都是 0,说明数据还未开始统计
* 某些 `null` 值是上传失败、未上报,分析时会误导均值、趋势等
* 柱状图、折线图中大量为 0,会压缩可视化比例,影响主数据的表现力。
此时应删除（或筛选）这些无效值。
filtered_data = [entry for entry in data if entry["new_cases"] and entry["new_cases"] > 0]

什么时候“**不应该轻易删掉**”0 或 null？
# ❗情况 1: **你在做趋势图、时间序列预测**
* 即使为 0 也要保留连续性（比如连续30天 0 -> 第31天暴增）
* 删除 0 会破坏时间连续性,让模型或图表不准
* 更好的做法是“用 `0` 或 `NaN` 显示,但图表上略去点/平滑”。
# ❗情况 2: **你在分析检测空缺分布、数据缺失问题本身**
* `null` 本身可能有意义（比如: 缺失集中在某些地区、时间段）
* 可视化 `null` 分布本身就是一种洞察（比如可画缺失热力图）。

最实用的处理建议
| 类型             | 处理建议                            |
| -- | - |
| `0` 值很多,影响图表比例 | 用平滑曲线、对数坐标、最大值裁切                |
| `null` 影响绘图    | 用 `0` 填充、插值、或用 `is not None` 过滤 |
| 需要连续性（时间序列）    | 不删,保留所有日期点                      |

Python示例: 保留非零数据
filtered = [entry for entry in data if entry["new_cases"] and entry["new_cases"] > 0]
"""

# 过滤掉单日新增为0的数据
"""
使用下面的代码把new_cases为0的数据过滤掉之后折线图确实连贯了起来,看着顺眼多了,
filtered_usa_data = [entry for entry in usa_python_dict["USA"] if entry["new_cases"] and entry["new_cases"] > 0]
filtered_jpn_data = [entry for entry in jpn_python_dict["JPN"] if entry["new_cases"] and entry["new_cases"] > 0]
filtered_ind_data = [entry for entry in ind_python_dict["IND"] if entry["new_cases"] and entry["new_cases"] > 0]
但是不知道为什么图表右侧出现了很多日期为2020-01-26的数据,分别查看三个国家的数据发现是日本的数据后面有很多2020-01-26数据,不明白为什么
你发现图表上出现了大量重复的日期 `2020-01-26`,而且集中在右侧尾部,并且确认这些数据都来自日本（JPN）数据源。这种情况通常有两个可能的根本原因
--------------------------------------------------------------进行去重和日期范围取交集之后再作图------------------------------

问题原因分析

原因 1: 数据源中有大量重复项**

你提到“JPN 数据后面有很多 `2020-01-26`”,这意味着: 

* **JPN 的 JSON 数据列表中,有多条记录的 `"date"` 值都是 `"2020-01-26"`**
* 可能是数据爬取或保存过程中格式错误,导致某些日期数据未正确写入,被覆盖为同一日期。

你可以验证一下（推荐加上这段代码）: 

from collections import Counter

jpn_dates = [entry["date"] for entry in jpn_python_dict["JPN"]]
date_count = Counter(jpn_dates)
for date, count in date_count.items():
    if count > 1:
        print(f"{date} 出现了 {count} 次")

如果输出中 `2020-01-26` 出现了几十甚至上百次,那就说明问题确实来自数据文件本身。

原因 2: 你在过滤数据时保留了重复日期**
如果你只按照 `new_cases > 0` 过滤,而不处理日期重复,比如下面这样: 

filtered_jpn = [entry for entry in jpn_data if entry["new_cases"] > 0]

那么即使 new_cases > 0,也会保留重复的 `"2020-01-26"` 数据,这就导致图表的 x 轴（时间轴）中出现了许多重复的点。

解决方案: 去重 + 合理清洗数据

你可以选择以下方法之一: 
方法一: 过滤时**去重（只保留每个日期第一条数据）**
seen = set()
filtered_jpn = []
for entry in jpn_python_dict["JPN"]:
    date = entry["date"]
    if entry["new_cases"] > 0 and date not in seen:
        seen.add(date)
        filtered_jpn.append(entry)

方法二: 按日期聚合（同一天多条记录求和）
如果数据确实应该是多个来源组成,可以按日期合并: 
from collections import defaultdict

aggregated = defaultdict(int)
for entry in jpn_python_dict["JPN"]:
    date = entry["date"]
    new_cases = entry.get("new_cases", 0)
    aggregated[date] += new_cases

# 转为列表格式
filtered_jpn = [{"date": date, "new_cases": count} for date, count in aggregated.items()]
# 可选: 按时间排序
filtered_jpn.sort(key=lambda x: x["date"])

检查数据是否干净: 打印最后几条
for row in filtered_jpn[-10:]:
    print(row)
总结建议
* 重复日期多数是数据源问题,建议在清洗时检查并处理
* 你做得对,**过滤 0 值让图更清晰**
* 但之后要确保“一个日期只出现一次”,否则时间轴就会出问题
* 也可以直接统一三个国家的数据格式、日期范围（交集）后再作图。
"""


# 使用给定的代码检查2020-01-26在日本数据中出现的次数, 发现只出现了一次, 那就不是数据源的问题了, 是我处理的过程中哪里不对
"""
非常好, 你用 `Counter` 验证了 `2020-01-26` 只出现了一次, 说明问题 **不是字面上的“重复数据”**, 而可能是其他 **导致图表异常显示为“多次 2020-01-26”** 的原因。以下是可能的根本原因和解决方法: 


## ✅ 问题根源: **你的 x 轴（日期）和 y 轴数据长度不一致**

这种图表行为背后的本质是: 

> 图表尝试用一个 **长度为 N 的 x 轴日期列表** 对齐多个 **长度不一致的 y 轴序列**, 
> 如果某个国家的数据比较短, `pyecharts` 就会自动**用最后一个 x 轴值（比如 2020-01-26）来补齐缺失部分**, 从而导致你看到的现象。

举个例子来说明: 
x_date = ["2020-01-01", "2020-01-02", ..., "2020-12-31"]  # 总共365天
y_jpn = [0, 1, 2, ..., 100]  # 只有101条

→ 后面 264 个点的 Y 值就没有对应的值了, 但图表仍要画, 所以它不断重复 x_date[-1] = "2020-01-26"

快速验证方法
你可以分别 `print(len(...))` 来确认: 

print("x轴日期数:", len(x_date))
print("USA数据点数:", len(y_usa_new_cases))
print("JPN数据点数:", len(y_jpn_new_cases))
print("IND数据点数:", len(y_ind_new_cases))
> 很大概率你会发现: **x 轴是 USA 的数据长度**, 而 JPN 比它短, 导致图表异常。
解决方案: **统一所有国家的时间长度**

方法一: 以三个国家的时间交集为基础, 只保留同时存在的数据点

# 取三个国家的日期集合
usa_dates = set([entry["date"] for entry in usa_python_dict["USA"] if entry["new_cases"] > 0])
jpn_dates = set([entry["date"] for entry in jpn_python_dict["JPN"] if entry["new_cases"] > 0])
ind_dates = set([entry["date"] for entry in ind_python_dict["IND"] if entry["new_cases"] > 0])

# 交集
common_dates = sorted(usa_dates & jpn_dates & ind_dates)

# 根据交集筛选每个国家的数据
def filter_by_dates(data, country_key, valid_dates):
    return [entry for entry in data[country_key] if entry["date"] in valid_dates]

usa_filtered = filter_by_dates(usa_python_dict, "USA", common_dates)
jpn_filtered = filter_by_dates(jpn_python_dict, "JPN", common_dates)
ind_filtered = filter_by_dates(ind_python_dict, "IND", common_dates)

# 分别构造 x 和 y
x_date = common_dates
y_usa = [entry["new_cases"] for entry in usa_filtered]
y_jpn = [entry["new_cases"] for entry in jpn_filtered]
y_ind = [entry["new_cases"] for entry in ind_filtered]

然后你再: 
line.add_xaxis(x_date)
line.add_yaxis("USA new_cases", y_usa)
line.add_yaxis("JPN new_cases", y_jpn)
line.add_yaxis("IND new_cases", y_ind)

方法二: 以最长国家为主, 其他国家数据补 0 或 `None`

如果你想保留所有日期, 可以用 `dict` 映射填充: 
# 构建日期 -> new_cases 的映射
jpn_dict = {entry["date"]: entry["new_cases"] for entry in jpn_python_dict["JPN"]}
y_jpn = [jpn_dict.get(date, 0) for date in x_date]  # 没有的就填0

总结
你图表中“重复的 2020-01-26”不是数据有误, 而是: 
* **x 轴太长（USA数据长）**
* **y 轴太短（JPN数据短）**
* **pyecharts 自动补点时使用了 x[-1] = 2020-01-26 显示**


通过检查发现我在定义x_date = [filtered_usa_data[0]["date"]] * len(filtered_usa_data)时, 最后len()一开始使用的是未过滤掉0值之前的usa_python_dict
使得x_date的值是好几百, 而y轴的值都只有几十个, 改正之后虽然以下三个值仍然不相等, 但是已经只相差几了
print("USA数据点数:", len(y_usa_new_cases))
print("JPN数据点数:", len(y_jpn_new_cases))
print("IND数据点数:", len(y_ind_new_cases))
下一步, 取date的交集赋值给x轴, 然后再生成最终的图表
"""

# 数据处理实际顺序
"""
你这个问题问得非常专业,实际上**两种方法都会用到,但顺序和重点略有不同**: 

---

## ✅ 一般推荐流程: **先清洗再作图（尤其是正式分析或报告）**

### 标准数据处理步骤（Data Processing Pipeline）如下: 

1. **导入数据（load）**
2. **初步预览数据（head() / 查看结构）**
3. **数据清洗（Data Cleaning）**

   * 缺失值处理（如填充/删除）
   * 类型转换（如日期转时间格式）
   * 异常值剔除或修正
   * 去重（如重复日期）
4. **数据标准化**

   * 统一字段命名、格式（比如国家字段名一致）
   * 时间对齐: 找出交集时间段
5. **探索性分析（EDA）**

   * **可视化 + 描述性统计**
   * 用来发现问题、验证假设、找趋势
6. **建模 / 报告 / 高质量图表输出**

> ✅ 所以,**先清洗再作图,是比较“专业稳妥”的流程**,尤其适用于正式分析、论文、竞赛、生产环境。

---

## 🧪 边画边改: 适合探索阶段

* 当你还在**探索数据（EDA）**阶段,或者不确定数据质量时: 

  * **边画边发现问题是正常的！**
  * 画出来发现: 为啥这个国家没图线？哦,原来 new_cases 全是 0
  * 为啥日期不对？哦,date 有重复,或者格式不一致
  * 然后再回头清洗。

> ✅ 这是一种“交互式发现”的方式,适合初学者、快速原型阶段。

---

## 🧠 实际建议

| 情况                  | 推荐方式                |
| ------------------- | ------------------- |
| 数据来源可靠,目标是分析或做图报告   | **先清洗、对齐格式、去重后再画图** |
| 数据来源不明,初次接触,不清楚问题在哪 | **先作图快速观察问题,再定向清洗** |
| 正式项目、期刊报告、模型训练      | 严格的“清洗→验证→标准化→分析”流程 |
| 练习或课堂演示             | 作图与清洗穿插进行也没问题       |

---

我可以帮你封装一个 [`数据清洗+日期对齐+画图`](f) 的小框架,未来遇到多个国家对比图就能直接套用,要不要？

"""