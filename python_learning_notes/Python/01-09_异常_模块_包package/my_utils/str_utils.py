"""
模块说明:
str_utils.py (字符串相关工具),内含:
    函数: str_reverse(s), 接收传入字符串,将字符串反转返回
    函数: substr(s, x, y), 按照下标x和y, 对字符串进行切片
"""


def str_reverse(s):
    """
    reverse a str
    :param s: the string that is going to be reversed
    :return: reverse version of the str
    """
    return s[::-1]

def sub_str(s, x, y):
    """
    Slice a string
    :param s: the objective string
    :param x: the starting index for slicing
    :param y: the ending index for slicing (excluding)
    :return: print slice of the str
    """
    return s[x:y:]

if __name__ == '__main__':
    print(str_reverse("hello world"))
    print(sub_str("hello world", 2, 7))
