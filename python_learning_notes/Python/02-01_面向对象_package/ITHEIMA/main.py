"""
main文件, 包含数据计算和图形绘制

"""
from data_define import Data_Record# 直接从文件import想要的类
from file_define import Reader, Csv_Reader

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

csv_reader = Csv_Reader(r"D:\code_joy\python\pythonProject\data\sales_data_may_2025.csv")
data_list = csv_reader.read_data()

data_dict = {}
for entry in data_list:
    if entry.date in data_dict.keys():
        data_dict[entry.date] += entry.sale_of_order
    else:
        data_dict[entry.date] = entry.sale_of_order
print(data_dict)

bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("日销售额", list(data_dict.values()))
bar.set_global_opts(title_opts={"text": "daily_sales_may_1"})
bar.render("daily_sales_may_1.html")