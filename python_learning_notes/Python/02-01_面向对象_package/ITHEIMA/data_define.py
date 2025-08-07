"""
封装数据

"""
class Data_Record:             # 数据封装类

    def __init__(self, date, order_id, sale_of_order, province):
        self.date = date                            # 订单日期
        self.order_id = order_id                    # 订单编号
        self.sale_of_order = sale_of_order          # 订单销售额
        self.province = province                    # 订单所在省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.sale_of_order}, {self.province}"
