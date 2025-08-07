# ---------------------------------------------------数据处理-----------------------------------------------------------
"""
数据分析案例
1、使用面向对象思想完成数据读取和处理
2、基于面向对象思想重新认知第三方库使用(pyecharts)
某公司的2份数据文件, 对其进行分析处理, 计算每日的销售额并以柱状图表的形式对其进行展示
"""
import csv
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

"""
类是读取和处理数据这件事
"""
class Data_Processing:
    # 最终所有的函数再整合一下, 是不是用一个__init__函数直接全部包含处理过程就可以
    # 读取文件这件事, 需要哪个文件, 如何读取, 读完放到哪里
    file_path = None
    __data_rom_file = None
    # __data_rom_file = []# 类似于这一句, 一开始定义时我把很多列表和字符串都定义成了空列表或者空字符串, 但是这样其实会占内存的, None最合适
    date_list = None
    daily_sales = None

    # 打开文件读取
    def open_file(self):
        with open(self.file_path, 'r', encoding = 'UTF-8') as f:
            reader = csv.DictReader(f)
            self.__data_rom_file = list(reader)

        # 数据结构
        # [{'日期': '2025-06-01', '订单编号': 'ORD20250601300', '销售额': '791.92', '省份': '山东省'}, ···]
    def get_date(self):
        date_set = set()

        self.open_file()
        for entry in self.__data_rom_file:
            date_set.add(entry['日期'])
        self.date_list = list(date_set)
        self.date_list = sorted(self.date_list)
        # print(date_list)

        # 处理数据
        """
        把某一日的所有销售额加起来得到一个当日销售额int num
        x轴是日期
        y轴就是销售额
        就是得到一个list, list内包含的是一个个字典, 字典的结构是{date:daily_sales}
        """
    def data_processing(self):
        self.get_date()

        self.daily_sales = [1 for _ in range(len(self.date_list))]

        for i in range(len(self.date_list)):
            for entry in self.__data_rom_file:
                if entry['日期'] == self.date_list[i]:
                    self.daily_sales[i] += float(entry['销售额'])
            self.daily_sales[i] = round(self.daily_sales[i], 2)
        print(self.date_list)
        print(self.daily_sales)

    def __init__(self, file_path):# 实现处理数据的自动执行
        self.file_path = file_path
        self.data_processing()

# 得到[{'2025-05-01': 14572.03}, {'2025-05-02': 30617.760000000002}, ····]列表

class Creat_Bar:
    date = None
    sales = None
    bar_title = None

    def __init__(self, date, sales, bar_title):# 实现处理数据的自动执行
        self.date = date
        self.sales = sales
        self.bar_title = bar_title
        self.creat_bar()

    def creat_bar(self):
        bar = Bar()
        bar.add_xaxis(self.date)
        bar.add_yaxis("日销售额", self.sales)
        bar.set_global_opts(title_opts={"text": self.bar_title})
        bar.render(f"{self.bar_title}.html")

may_data = Data_Processing(r"D:\code_joy\python\pythonProject\data\sales_data_may_2025.csv")# file_path需要是传进去的参数
june_data = Data_Processing(r"D:\code_joy\python\pythonProject\data\sales_data_june_2025.csv")
may_bar = Creat_Bar(may_data.date_list, may_data.daily_sales, "daily_sales_may")
june_bar = Creat_Bar(june_data.date_list, june_data.daily_sales, "daily_sales_june")

"""
如果创建bar也做一个类
对象直接继承两个类
那么两个类之间可以互相引用数据吗==================>需要通过子类来共享
因为需要把Data_Processing类中得到的数据add到bar的x轴和y轴

把这个写完, 然后看一下一个接单任务和这样的工作量相比大小如何, 可以估算自己完成一个任务的时间
"""

"""
把写过的类整理成固定的包, 以后执行类似的任务就在固定包的基础上改动
看老师的视频, 感觉我对抽象类的理解还是没有到位
"""
