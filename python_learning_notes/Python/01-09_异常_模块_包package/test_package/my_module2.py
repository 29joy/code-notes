
# import my_module1
# print(my_module1.test(2, 5))

# from my_module1 import test
# test(2, 5)

# 验证导入不同模块的同名函数
# from my_module1 import test
# from my_module3 import test
# print(test(5, 2))

# 验证__all__变量
# from my_module1 import *
# from my_module1 import test_a
#
# print(test(1, 2))# test红色下划线提示不能用
# print(test_a(5, 1))# test_a红色下划线提示不能用
# print(test_b(7, 1))
#
# test_a(6, 8)

