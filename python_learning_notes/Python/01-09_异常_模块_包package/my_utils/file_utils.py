"""
模块说明:
file_utils.py (文件处理相关工具),内含:
    函数: print_file_info(file_name),接收传入文件的路径,打印文件的全部内容,如文件不存在则捕获异常,输出提示信息,通过finally关闭文件对象
    函数: append_to_file(file_name, data),接收文件路径以及传入数据,将数据追加写入到文件中
"""


import io
import sys
from ctypes import pythonapi
from pathlib import Path

info_file_not_found = "File Not Found"

def print_file_info(file_name):
    """
    print file info
    :param file_name: the path of file
    :return None
    """
    flag = False
    try:
        f = open(file_name, 'r', encoding='UTF-8')
    except FileNotFoundError:
        print(info_file_not_found)
    else:
        flag = True
        for line in f:
            print(line, end='')
    finally:
        if flag:
            f.close()

def append_to_file(file_name, data):
    """
    append data to the file
    :param file_name: the objective file that will have additional data appended to it
    :param data: the data will append to the objective file
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.close()

if __name__ == '__main__':
    file_name = "D:/code_joy/python/pythonProject/my_utils/str_utils_try.py"
    data1 = "added in function append_to_file 1"
    data2 = "added in function append_to_file 2"
    data3 = data1 + data2

    # capture output content
    def print_capture(func, *args, **kwargs):
        """
        Capture the output of the parameter function
        :param func: the objective function aimed at capturing its output
        :param args: the parameters of func, used to receive any number of non-keyword arguments
        :param kwargs: the parameters of func, used to receive any number of keyword arguments
        :return: captured output
        """
        output_capture = io.StringIO()
        sys.stdout = output_capture
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        return captured_output

    # test fun print_file_info: test file not exit
    capture_print_0 = print_capture(print_file_info, file_name)
    if capture_print_0 != info_file_not_found + "\n":
        print("test fun print_file_info: test file not exit unsuccessfully")

    # test fun append_to_file: test file not exit
    append_to_file(file_name, data1)
    capture_print_1 = print_capture(print_file_info, file_name)
    if capture_print_1 != data1:
        print("test fun append_to_file: test file not exit unsuccessfully")

    # test fun append_to_file: test file exit and add data to the end of the file
    append_to_file(file_name, data2)
    capture_print_2 = print_capture(print_file_info, file_name)
    if capture_print_2 != data3:
        print("test fun append_to_file: test file exit and append data unsuccessfully")

    # if the file exists, delete it
    file_path = Path(file_name)
    if file_path.exists():
        file_path.unlink()
