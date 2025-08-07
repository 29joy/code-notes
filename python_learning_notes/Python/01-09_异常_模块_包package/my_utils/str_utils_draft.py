"""
模块说明:
str_utils.py (字符串相关工具),内含:
    函数: str_reverse(s), 接收传入字符串,将字符串反转返回
    函数: substr(s, x, y), 按照下标x和y, 对字符串进行切片
"""


# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = []
#     while i >= -len(s):
#         s_new[j] = s[i]
#         i -= 1
#         j += 1
#     print(s_new)
"""
报出了error
    s_new[j] = s[i]
    ~~~~~^^^
IndexError: list assignment index out of range
"""

# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = []
#     while i > -(len(s) + 1):
#         s_new[j] = s[i]
#         print(f"j现在是{j},s_new[j]是{s_new[j]}")
#         i -= 1
#         j += 1
#     print(s_new)
"""
改成这样还是不对,一条print都没有,所以在第一次为s_new[0]进行赋值时就报错了
网上搜索发现当一个列表s_new为空时,进行s_new[0]就会报错
那么将s_new定义为一个长度为len(s)的列表可行吗
"""

# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = [j] * len(s)# 这个定义方法···感觉怪怪的,难评,记住就得了
#     while i >= -len(s):
#         s_new[j] = s[i]
#         # print(f"j现在是{j},s_new[j]是{s_new[j]}") 试验可行之后这一条就改注释了
#         i -= 1
#         j += 1
#     # print(s_new)
#     # print(str(s_new))
#     # print(type(str(s_new)))
"""
发现s_new输出为['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h'],这是想要的吗,为什么不像s一样输出为hello world这样的
因为现在s_new是列表呀,那么最后输出的时候把s_new转化为字符串就行了,结果用print(str(s_new))输出还是['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
虽然str(s_new)的type已经是class str
忽然想到定义的时候直接将s_new定义为str呀,为什么要定义为list呢
"""

# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = "j" * len(s)
#     while i >= -len(s):
#         s_new[j] = s[i]
#         i -= 1
#         j += 1
#     print(s_new)
"""
报错
    s_new[j] = s[i]
    ~~~~~^^^
TypeError: 'str' object does not support item assignment
因为字符串是不可变类型所以这样是不行的,还是要用一个可变类型的变量来接收,列表、集合、字典可修改但集合和字典无序,那就只能用列表了,否则无法保证输出顺序
那怎么能输出的看上去和字符串s一样呢
"""

# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = [j] * len(s)# 这个定义方法···感觉怪怪的,难评,记住就得了
#     while i >= -len(s):
#         s_new[j] = s[i]
#         # print(f"j现在是{j},s_new[j]是{s_new[j]}") 试验可行之后这一条就改注释了
#         i -= 1
#         j += 1
#     for element in s_new:
#         print(str(element), end='')
"""
用上面的输出方法看上去确实是像字符串一样的输出了,但是为什么输出的是dlrow ollehllo w呢,怎么多出来的llo w呢
"""

# def str_reverse(s):
#     i = -1
#     j = 0
#     s_new = [j] * len(s)# 这个定义方法···感觉怪怪的,难评,记住就得了
#     while i >= -len(s):
#         s_new[j] = s[i]
#         # print(f"j现在是{j},s_new[j]是{s_new[j]}") 试验可行之后这一条就改注释了
#         i -= 1
#         j += 1
#     print(s_new)
#     count = 0
#     for element in s_new:
#         print(str(element), end='')
#         count += 1
#     print(count)
"""
用print(s_new)输出为['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h'],这说明倒序的过程没有问题,但是在挨个输出element的时候出了问题
然后加了一个count计数并输出count,输出为:
['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
dlrow olleh11
llo w
所以确实是输出也没有问题,llo w是下面的函数sub_str输出的····知道真相的我笑不停了哈哈哈哈
那就没有问题了,只需要注意和下面一个函数print的时候要换行,加一个print()就行了
"""
def str_reverse(s):
    i = -1
    j = 0
    s_new = [j] * len(s)# 这个定义方法···感觉怪怪的,难评,记住就得了
    while i >= -len(s):
        s_new[j] = s[i]
        i -= 1
        j += 1
    for element in s_new:
        print(str(element), end='')
    print()
"""
老师给的方法直接是倒着取
def str_reverse(s):
    return s[::-1]
"""
def sub_str(s, x, y):
    print(s[x:y:])
"""
老师没有print只有return
def sub_str(s, x, y):
    return s[x:y]
"""
if __name__ == '__main__':
    str_reverse("hello world")
    sub_str("hello world", 2, 7)
    # print(str_reverse("hello world"))# 用老师的方法要验证就要print了
    # print(sub_str("hello world", 2, 7))# 用老师的方法要验证就要print了
