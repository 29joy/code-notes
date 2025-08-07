"""
数据读取抽象类, 因为文件内数据存储的方式不同
"""
from data_define import Data_Record
import csv

class Reader():                   # 数据读取过程封装

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self) -> list[Data_Record]:
        pass

    # def write_data(self): # 此次案例用不到
    #     pass
    #
    # def add_data(self): # 此次案例用不到
    #     pass

class Csv_Reader(Reader):

    def read_data(self) -> list[Data_Record]:
        data_list = []
        with open(self.file_path, 'r', encoding = 'UTF-8') as f:
            reader = csv.DictReader(f)
            data_from_file = list(reader)
            # print(self.__data_from_file)# [{'日期': '2025-05-01', '订单编号': 'ORD20250501001', '销售额': '4540.63', '省份': '广东省'}, {'
            for entry in data_from_file:
                # data_record = Data_Record(entry['日期'], entry['订单编号'], round(float(entry['销售额']), 2), entry['省份'])
                data_record = Data_Record(entry['日期'], entry['订单编号'], int(float(entry['销售额'])), entry['省份'])
                # data_record = Data_Record(entry['日期'], entry['订单编号'], float(entry['销售额']), entry['省份'])
                data_list.append(data_record)

        # for l in data_list:
        # 要打印一个包含很多Data_Record的list，直接print只能获得所有Data_Record的内存地址，必须要这样逐个打印__str__才生效
        #     print(l)
        return data_list

if __name__ == '__main__':
    csv_reader = Csv_Reader(r"D:\code_joy\python\pythonProject\data\sales_data_may_2025.csv")
    csv_reader.read_data()
