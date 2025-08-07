# 快捷键
"""
ctrl + d:复制当前行代码
ctrl + a:全选
ctrl + c\v\x:复制\粘贴\剪切
ctrl + f:搜索

ctrl + alt + s:打开软件设置
ctrl + shift + f10:运行当前代码文件

shift + alt + 上\下:将当前行代码上移或下移
shift + f6:重命名文件

alt + 回车: 自动搜索并导包
"""


# translation插件还没安装


# 函数说明
"""
pycharm写函数说明,在def func(x, y):下一行输入三个双引号然后回车会自动补齐:param x等,即可添加函数说明
通过鼠标悬停函数名,可以查看调用函数的说明文档
"""


# 定位异常位置
"""
假设异常输出如下
Traceback (most recent call last):
  File "D:\00-code\python\pythonProject\test.py", line 19, in <module>
    main()
  File "D:\00-code\python\pythonProject\test.py", line 13, in main
    func2()
  File "D:\00-code\python\pythonProject\test.py", line 8, in func2
    func1()
  File "D:\00-code\python\pythonProject\test.py", line 3, in func1  =========>pycharm中点击该行会在代码中定位到报错的位置
                                                                              点击其他的行同理,会定位到出错的调用等
    num = 1 / 0
          ~~^~~
ZeroDivisionError: division by zero
"""


# 模块说明
"""
导入模块时,如import time
在pycharm中按住Ctrl鼠标点击对应的模块名称就可以打开模块文件查看模块的内容,如这里的time
"""


# 代码行变黑提示的情况
"""
1、
创建一个文件my_module1并定义函数test
在my_module2文件中导入并使用它且获得正确的结果
假设有my_module3文件,其中也定义了test函数,但功能和my_module1中的test函数功能不同,在my_module2文件中同时导入了my_module1和my_module3中的test函数
(即调用了两个不同模块中同名的函数),那么后调用的函数会覆盖先调用的函数(实际上pycharm中第一行导入直接变黑提示了)
详见my_module2.py的举例

2、
"""


# 下划线提示
"""
1、重复定义key的字典
score_dict = {"honghong":99, "jingjing":98, "mingming":97, "honghong":96}# 在pycharm中两个honghong会有下划线提示

2、
"""


# 第三方工具链接
"""
1、浏览器
想要生成图表时,点击运行之后发现什么都没有出现,因为图表已经被生成网页文件了,可能会在左侧目录生成一个新的网页文件render.html
打开render.html文件,pycharm的右上角有浏览器打开的按钮,选择一个浏览器即可

2、
"""


# 安装第三方包
"""
打开pycharm右下角的解释器,然后点击interpreter settings,
就可以在File | Settings | Project: pythonProject | Python Interpreter看到当前解释器下已经安装的第三方包,
想要安装其他第三方包,点击+然后输入包名称搜索到之后点击install package就可以了
"""


# 自定义包
"""
在pycharm中新建一个package包后,会自动在包里创建__init__.py文件,这个文件控制着包的导入行为
(如果把__init__.py文件删掉,会看到这个文件夹的图标变成了普通图标而不是包的图标)
并且我将之前创建的几个module文件移动进了包里面
"""


# 自动补全
"""
1、如果一个模块文件中有__all__变量,当使用from XXX import *导入时,只能导入这个列表中的元素,如
__all__ = ['test_b']

def test_a():
    print("test_a")

def test_b():
    print("test_b")
当其他文件通过from XXX import *导入时,只能使用test_b函数
在pycharm中,当我非要使用test_a函数时,会自动在开头帮我加上from my_module1 import test_a引用
详见my_module2.py的举例

2、输入main会直接提示if __name__ == '__main__':,回车即可
"""
