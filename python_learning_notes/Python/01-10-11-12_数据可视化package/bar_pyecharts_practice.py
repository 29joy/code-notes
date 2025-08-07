# 只包含动态柱状图
# =====================================================动态柱状图=================================================================

# 动态图表需求分析
"""
1、GDP数据处理为亿级
2、有时间轴, 按照年份为时间轴的点
3、x轴和y轴反转, 同时每一年的数据只要前8名国家
4、有标题, 标题的年份会动态更改
5、设置了主题的LIGHT
"""
# ---------------------------------------------------数据处理-----------------------------------------------------------
import json
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

# 打开文件
f = open(r"D:\code_joy\python\pythonProject\data\GDP.json", 'r', encoding = 'UTF-8')
data = f.read()
# print(data)
# 关闭文件
f.close()
# 转化为python列表
data_python_list = json.loads(data)# 一开始忘了转化成python数据, 下面进行排序一直报错
"""
数据是一个list[]里面都是字典
{"Country Name":"Zimbabwe","Country Code":"ZWE","Year":2023,"Value":26538273498.84614}
还要对所有的value转化为以亿为单位, 小数点保留2位吧
"""
"""
为了方便创建图表的时候赋值, 
两个list, 一个GDP, 一个countries name, 分别add给x轴和y轴
三个list的顺序是一一对应的
GDP的list其中的元素是一个个list, 每个元素list包含8个GDP最高的国家的GDP
countries name的list其中的元素是一个个list, 每个元素list包含8个GDP最高的国家的名字
"""
"""
先建立一个year的集合, 因为集合元素不重复, 所以最后得到的是一个包含所有年份的集合, 
然后将集合转化为list, 然后排序就得到了一个从小到大的年份的list
每个年份都建立一个list, 这个list中存的是该年份所有国家的数据, 然后按照value排序, 取前8的value和国家名字在分别放到value_list和country_name_list
value_list和country_name_list可以根据每一个year取到
"""
# 发现数据中包含很多非单一国家的数据, 如'World', 'High income', 'OECD members'等, 需要对数据进行过滤
sovereign_countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas, The", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", "Costa Rica", "Cote d'Ivoire",
    "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt, Arab Rep.", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
    "Finland", "France", "Gabon", "Gambia, The", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran, Islamic Rep.",
    "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Rep.",
    "Kuwait", "Kyrgyz Republic", "Lao PDR", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia, Fed. Sts.", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovak Republic", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syrian Arab Republic", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkiye", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu",
    "Venezuela, RB", "Viet Nam", "Yemen, Rep.", "Zambia", "Zimbabwe", "Holy See"
]
data_list_unitary_state = [entry for entry in data_python_list if entry["Country Name"] in sovereign_countries]
year_set = set()
for entry in data_list_unitary_state:
    year_set.add(entry["Year"])
year_list = list(year_set)
year_list = sorted(year_list)
# print(year_list)

data_list = [[] for _ in range(len(year_list))]
value_list = [[] for _ in range(len(year_list))]
country_name_list = [[] for _ in range(len(year_list))]
for i in range(len(year_list)):
    data_list[i] = []
    for entry in data_list_unitary_state:
        if entry["Year"] == year_list[i]:
            data_list[i].append(entry)
    for entry in data_list[i]:
        data_list[i].sort(key=lambda element:element["Value"], reverse=True)
    filtered_data_list = data_list[i][0:8]
    value_list[i] = []
    country_name_list[i] = []
    for entry in filtered_data_list:
        value_list[i].append(round(entry["Value"] / 100000000, 2))
        country_name_list[i].append(entry["Country Name"])
    value_list[i].reverse()
    country_name_list[i].reverse()
# print(value_list)
# print(country_name_list)

# ---------------------------------------------------创建图表-----------------------------------------------------------
# 创建时间线
timeline = Timeline()
# 创建一个bar的list, 存储所有的bar================不用创建bar_list了, 每个bar生成的时候直接add到timeline里
# bar_list = [[] for _ in range(len(year_list))]
for i in range(len(year_list)):
    bar = Bar()
    bar.add_xaxis(country_name_list[i])  # 国家为 X
    bar.add_yaxis("GDP（亿美元）", value_list[i], label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts={"text": f"{year_list[i]} 年全球 GDP 前8国家"})
    # bar_list.append(bar)
    timeline.add(bar, f"{year_list[i]}")
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
