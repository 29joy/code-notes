"""
模块说明:
file_utils.py (文件处理相关工具),内含:
    函数: print_file_info(file_name),接收传入文件的路径,打印文件的全部内容,如文件不存在则捕获异常,输出提示信息,通过finally关闭文件对象
    函数: append_to_file(file_name, data),接收文件路径以及传入数据,将数据追加写入到文件中
"""


"""
一、设计思路:
1、因为学习了if __name__ == '__main__':所以很自然的想到了要对自己写的模块进行内部测试验证
2、在进行第二个函数的测试时,想到了
1）要对输出的内容进行判断从而验证追加行为是否成功
2）要验证对一个存在的文件进行追加,如何判断文件内容呢,因为不知道原始文件的内容,难道读取之后从最后的输出字符依次往前与追加的字符进行倒序的比较吗
3）每次运行对已存在文件的追加测试都会进行追加,那么在多次追加后如何验证是否正确追加以及如何确保内存不会被过分的占用呢
4）为了每次验证文件不存在的模块都能被运行,那么必须有文件被创建后又被删除的操作
5）追加后验证时恰好可以使用print_file_info函数来进行,所以在验证print_file_info函数时,只需要验证文件不存在的情况
   在验证append_to_file函数时可以顺便验证print_file_info函数中文件存在的情况
6）对append_to_file函数文件已存在的情况的验证刚好可以在append_to_file函数文件不存在的情况的验证之后,这时文件已经被创建且文件的原始内容已知,
   且因为最后要执行对文件的删除操作,解决了3）的问题

二、设计方案:
经过以上过程,最终确定了验证顺序是
1、print_file_info函数中文件不存在的情况
2、append_to_file函数中文件不存在的情况
    print_file_info函数中文件存在的情况
3、append_to_file函数中文件存在的情况
    print_file_info函数中文件存在的情况
4、删除文件
二、方案改进:
1、最后想到,对于输出的捕获和比较可以整理成一个统一的函数来定义和调用,并以此知道了if __name__ == '__main__':下面可以定义函数
   √梳理成了print_capture(func, *args, **kwargs)函数
2、考虑是否还有没考虑到的测试用例,应该是没有了√
3、第一个测试用例print_file_info函数中文件不存在的情况,也应该对输出内容进行判定而在执行测试代码时尽量不要输出File Not Found这种内容
   否则很容易在后续代码使用中在log中被误判为error等
   √改完,和另外的两个测试一样都对输出内容进行判断==============这样还有一个好处是,使得整个模块内测试函数如果成功没有任何打印,如果有打印
   就是某个测试用例失败了,可以看打印去找对应的失败的地方
三、仍待改进:
1、捕获输出后进行比较的代码也可以加到print_capture(func, *args, **kwargs)函数中,不过这样就包装的更加隐蔽了,一旦出了问题可能找起来不是很好找
   而且,这样print_capture(func, *args, **kwargs)函数应该要返回一个True或False,在测试用例中还是要判断返回值是True还是False
   所以暂时不改动
2、二方案改进的3里面中提到的失败打印应该在前面加上类似前缀[I]info[W]warning[E]error这种有标志性的内容
   或者增加行数等,更方便的定位到失败的case==================这部分以后再学
   也可以做成异常直接使程序停止运行(在某些需要的情况的话)
3、capture_print_0和data1这种变量的命名还可以改进,在正式项目中再注意吧
4、还可以把包说明、模块说明、函数说明等都写的精细一点,养成良好的习惯


果然每个设计都是因为有了使用场景,多思考多练习多总结
这次自己写测试代码,对测试好像有了一些思路和灵感,也许会帮助我加深对测试的理解
"""


import io
import sys
from ctypes import pythonapi
from pathlib import Path

info_file_not_found = "File Not Found"

def print_file_info(file_name):
    flag = False
    try:
        f = open(file_name, 'r', encoding='UTF-8')
    except FileNotFoundError as e:
        # 这里的e我在后面没有使用到,如果要使用它作为异常时的print内容,在后面main里进行比较时会报错说e没有定义
        # 所以正式方案里还是没有用它而是直接用except FileNotFoundError且定义了info_file_not_found = "File Not Found"
        # 但是如果用e,像老师写的那样,会把异常本身的内容打印出来,似乎比我自己写的"File Not Found"要好
        print(info_file_not_found)
    else:
        flag = True
        # print(f.read())
        """
        如果文件过大,一次性读取会占用大量内存,所以一般会用for循环逐行读取
        """
        for line in f:
            print(line, end='')
    finally:
        if flag:
            f.close()
"""
当测试一个不存在的文件时会报错
    f.close()
    ^
UnboundLocalError: cannot access local variable 'f' where it is not associated with a value
且可以注意到f.close()中的f一直有一个黄色的下划线作为警示
通过增加一个flag来判断文件是否需要关闭,不存在的文件被执行了以r模式打开之后,因为未成功打开,所以不需要也无法关闭该文件
"""
"""
老师的写法:
def print_file_info(file_name):
    f = None   ======================>老师用f本身进行判断比我的flag好,不过我觉得他的整体写的没有我的好
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        content = f.read()
        print("文件内容如下:")
        print(content)
    except FileNotFoundError as e:
        print(f"程序出现异常了,原因是: {e}")
    finally:
        if f:
            f.close()
"""

def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.close()
"""
老师的写法:
def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.write("\n")# ========================>老师这里为什么要写换行符
    f.close()
"""

# if __name__ == '__main__':
#     # 将捕获输出内容并进行比较的代码块整理为函数反复调用
#     file_name = "D:/code_joy/python/pythonProject/my_utils/str_utils_try.py"
#     data1 = "added in function append_to_file 1"
#     data2 = "added in function append_to_file 2"
#     # data3 = "added in function append_to_file 1added in function append_to_file 2"# 这里有什么办法实现data1后接data2吗
#     data3 = data1 + data2
#     # test fun print_file_info: test file not exit
#     # print("----------test unit 1, test fun print_file_info: test file not exit----------")
#     # ============================类似的这种输出都给注释掉了,因为它们的输出会影响捕获输出时捕获的内容所以就不加了
#     print_file_info(file_name)# 这里测试一个不存在的文件,正确输出了提示信息File Not Found
#     # 这里也应该对输出内容进行判断=============================================================================================
#
#     # test fun print_file_info: test file exit and read file content
#     # print_file_info("D:/code_joy/python/pythonProject/my_utils/str_utils_for_try.py")# 在下面进行测试验证
#
#
#     # test fun append_to_file: test file not exit
#     # print("----------test unit 2, test fun append_to_file: test file not exit----------")
#     append_to_file(file_name, data1)
#     # 增加验证文件内容的操作
#     output_capture1 = io.StringIO()
#     sys.stdout = output_capture1
#     # test fun print_file_info: test file exit and read file content
#     # print("----------test unit 2-1, test fun print_file_info: test file exit and read file content----------")
#     print_file_info(file_name)
#     sys.stdout = sys.__stdout__
#     captured_output1_value = output_capture1.getvalue()
#     # print(captured_output1_value)
#     # print(data1)
#     if captured_output1_value != data1:
#         print("test fun append_to_file: test file not exit unsuccessfully")# 这里之后改成报出一个异常
#
#
#     # test fun append_to_file: test file exit and add data to the end of the file
#     # print("----------test unit 2, test fun append_to_file: test file exit and add data to the end of the file----------")
#     append_to_file(file_name, data2)
#     output_capture2 = io.StringIO()
#     sys.stdout = output_capture2
#     # test fun print_file_info: test file exit and read file content
#     # print("----------test unit 2-1, test fun print_file_info: test file exit and read file content----------")
#     print_file_info(file_name)
#     sys.stdout = sys.__stdout__
#     captured_output2_value = output_capture2.getvalue()
#     # print("输出内容为: ", captured_output2_value)
#     if captured_output2_value != data3:
#         print("test fun append_to_file: test file exit and read append to file content unsuccessfully")
#     # 增加验证文件内容的操作,如何验证,最后几个字符依次对应追加的内容吗
#     # 这里验证可以用print_file_info函数文件存在的情况来验证,捕获解释器输出内容与追加的内容进行判断即可,同时验证了两个函数
#     # 要不要执行一个删掉追加内容的操作,否则每次运行都会被追加一次
#
#     # 这里可以在上面不存在的文件被创建后验证,然后再删除文件,这样也解决了每次运行都会追加内容的问题,每次文件都被删掉了
#     # 每次执行完之后增加一个删除因不存在而被创建的文件的过程,保证这块代码永远都能用于验证文件不存在的情况
#     file_path = Path(file_name)
#     # 检查文件是否存在,然后删除
#     if file_path.exists():
#         file_path.unlink()
#         # print(f"{file_path} 已被删除")
#     # else:
#         # print(f"{file_path} 不存在")
if __name__ == '__main__':
    # 变量的定义在函数前面
    file_name = "D:/code_joy/python/pythonProject/my_utils/str_utils_try.py"
    data1 = "added in function append_to_file 1"
    data2 = "added in function append_to_file 2"
    data3 = data1 + data2

    # 将捕获输出内容的代码块整理为函数反复调用
    def print_capture(func, *args, **kwargs):
        """

        :param func:
        :param args:
        :param kwargs:
        :return:
        """
        output_capture = io.StringIO()
        sys.stdout = output_capture
        func(*args, **kwargs)#这里执行的函数以及它的参数都需要传参进来,哇哦,传进来的函数的参数数量是不确定的,这种传参我还没写过
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        return captured_output

    # test fun print_file_info: test file not exit
    capture_print_0 = print_capture(print_file_info, file_name)
    if capture_print_0 != info_file_not_found + "\n":
        # 这里不加换行符会报错,这是因为print_file_info中except FileNotFoundError as e:时print默认加了换行符
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

    # 检查文件是否存在,然后删除
    file_path = Path(file_name)
    if file_path.exists():
        file_path.unlink()
"""
老师的写法非常简单就是运行一下函数然后打开文件看看有没有追加成功,不如我的好
"""


# ------------------------------------------------------文件路径不正确问题----------------------------------------------------
"""
报错SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 37-38: truncated \uXXXX escape
意思是: 在字符串中使用了 **反斜杠 `\`**,而 Python 试图把它当作 **Unicode 转义字符**（`\uXXXX`）解析,但没有成功。
常见原因
可能写了这样的代码（尤其在 Windows 系统）: 
path = "C:\Users\Joy\Documents\data.json"
Python 会尝试把 `\U`、`\J` 等解释为转义字符（例如 `\uXXXX` 是 Unicode 字符）,但 `\U` 后面没有 8 位数字,于是就报错了。
解决办法
有三种方法可以避免这个错误: 
方法 1: 使用 **原始字符串**
在字符串前加上 `r`,让它不要解释反斜杠: 
path = r"C:\Users\Joy\Documents\data.json"
方法 2: 使用正斜杠（推荐）
Windows 也支持 `/`,所以你可以改成: 
path = "C:/Users/Joy/Documents/data.json"
方法 3: 使用双反斜杠
每个 `\` 写成 `\\`,防止转义: 
path = "C:\\Users\\Joy\\Documents\\data.json"
建议
最推荐的方法是用正斜杠 `/` 或加 `r""`,代码更清晰也不容易出错。
"""
# --------------------------------r模式打开一个不存在的文件, 文件并未成功打开, 不需要也无法关闭文件--------------------------------
"""
在 Python 中,如果尝试以 'r' 模式（只读模式）打开一个不存在的文件,会抛出 FileNotFoundError 异常。
在这种情况下,文件并未成功打开,因此不需要也无法关闭文件。

以下是一个示例代码: 

复制代码
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("文件不存在,无需关闭。")

关键点: 
with 语句: 推荐使用 with 语句管理文件操作,它会在文件操作完成后自动关闭文件,即使发生异常也无需手动调用 close()。
异常处理: 在文件不存在的情况下,open() 会抛出 FileNotFoundError,可以通过 try-except 捕获并处理。

因此,如果文件未成功打开（例如因为文件不存在）,根本不会生成文件对象,自然也无需调用 close()
"""
# --------------------------------------------------python拼接两个字符串-------------------------------------------
"""
在 Python 中,可以通过多种方式将两个字符串拼接成一个新的字符串。以下是几种常见的方法: 

1. 使用加号 (+) 运算符
复制代码
str1 = "你好"
str2 = "世界"
result = str1 + str2
print(result)  # 输出: 你好世界

2. 使用 f-string 格式化
复制代码
str1 = "你好"
str2 = "世界"
result = f"{str1}{str2}"
print(result)  # 输出: 你好世界

3. 使用 join() 方法
复制代码
str1 = "你好"
str2 = "世界"
result = "".join([str1, str2])
print(result)  # 输出: 你好世界


以上方法都可以高效地拼接字符串,具体选择哪种方式可以根据你的需求和代码风格来决定。
"""
# --------------------------------------------------python中捕获print输出的内容-------------------------------------------
"""
在 Python 中,可以通过重定向标准输出（sys.stdout）来捕获其他函数的 print 输出。以下是实现方法的示例: 

方法: 使用 io.StringIO

复制代码
import io
import sys

def some_function():
    print("这是函数的输出内容！")

# 创建一个 StringIO 对象
output_capture = io.StringIO()

# 重定向 sys.stdout 到 StringIO 对象
sys.stdout = output_capture

# 调用目标函数
some_function()

# 恢复 sys.stdout
sys.stdout = sys.__stdout__

# 获取捕获的输出内容
captured_output = output_capture.getvalue()
print("捕获的内容: ", captured_output)
说明
io.StringIO: 用作内存中的文件对象,能够捕获写入的内容。
sys.stdout 重定向: 将标准输出流指向 StringIO 对象。
恢复标准输出: 在捕获完成后,将 sys.stdout 恢复为默认值（sys.__stdout__）,以避免影响后续代码的输出。
注意事项
确保在捕获完成后恢复 sys.stdout,否则可能导致程序的其他部分无法正常输出。
如果需要捕获异常输出（print 到 sys.stderr 的内容）,可以类似地重定向 sys.stderr。
这种方法非常适合在测试或调试时捕获函数的输出内容！
"""
# -------------------------------------------------------python中删除文件---------------------------------------------
"""
在 Python 中,可以使用 os 模块或 pathlib 模块来删除文件。以下是两种常见的方法: 

方法 1: 使用 os 模块
复制代码
import os

file_path = "example.txt"

# 检查文件是否存在,然后删除
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} 已被删除")
else:
    print(f"{file_path} 不存在")

方法 2: 使用 pathlib 模块
复制代码
from pathlib import Path

file_path = Path("example.txt")

# 检查文件是否存在,然后删除
if file_path.exists():
    file_path.unlink()
    print(f"{file_path} 已被删除")
else:
    print(f"{file_path} 不存在")

注意事项
确保路径正确: 删除操作是不可逆的,请确保路径指向正确的文件。
权限问题: 如果文件受权限限制,可能需要管理员权限才能删除。
避免误删: 在执行删除操作前,可以通过日志或提示确认操作。
"""
# -------------------------------------------------------python自己报一个异常---------------------------------------------
"""
在 Python 中,你可以通过自定义异常类和手动抛出异常来实现“报出 bug”的功能。以下是一个简单的示例,展示如何定义和使用自定义异常来报告特定的错误或 bug: 

示例代码
复制代码
# 定义一个自定义异常类
class BugReportException(Exception):
    def __init__(self, message, bug_id=None):
        super().__init__(message)
        self.bug_id = bug_id

    def __str__(self):
        if self.bug_id:
            return f"[Bug ID: {self.bug_id}] {super().__str__()}"
        return super().__str__()

# 模拟一个函数,可能会触发 bug
def process_data(data):
    if not isinstance(data, list):
        # 抛出自定义异常
        raise BugReportException("数据类型错误,期望为列表类型！", bug_id=101)
    if len(data) == 0:
        raise BugReportException("数据列表为空,无法处理！", bug_id=102)
    # 正常处理逻辑
    return [x * 2 for x in data]

# 使用 try-except 捕获异常
try:
    result = process_data("not_a_list")  # 这里会触发异常
    print("处理结果: ", result)
except BugReportException as e:
    print(f"捕获到异常: {e}")

输出示例

运行上述代码时,会输出: 

复制代码
捕获到异常: [Bug ID: 101] 数据类型错误,期望为列表类型！

说明
自定义异常类: 通过继承 Exception 类,可以创建一个带有额外信息（如 bug_id）的异常类。
抛出异常: 使用 raise 关键字手动抛出异常。
捕获异常: 通过 try-except 块捕获并处理异常,避免程序崩溃。

这种方式可以帮助你在调试或开发过程中快速定位问题,同时提供清晰的错误信息。
"""
# -------------------------------------------if __name__ == "__main__": 下面是否可以定义函数---------------------------------
"""
是的,在 Python 中,if __name__ == "__main__": 下面是可以定义函数的。实际上,这是一种常见的做法,尤其是在编写模块化代码时。

在 Python 中,if __name__ == "__main__": 的作用是确保只有在直接运行该脚本时,代码块才会被执行,而不会在脚本被导入为模块时执行。这种结构可以用来定义函数、类,甚至执行代码逻辑。

以下是一个示例: 

复制代码
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # 定义一个函数
    def farewell(name):
        print(f"Goodbye, {name}!")

    # 调用函数
    greet("Alice")
    farewell("Alice")

解释: 
greet 函数: 在 if __name__ == "__main__": 之外定义,可以在脚本中直接调用,也可以在其他模块中导入使用。
farewell 函数: 在 if __name__ == "__main__": 之内定义,仅在直接运行脚本时可用,无法通过导入模块访问。

这种灵活性允许你根据需求组织代码,同时避免在模块导入时执行不必要的逻辑。
"""
# ----------------------------------------Python定义一个函数,其参数是另一个函数以及该函数的参数---------------------------------
"""
在 Python 中,可以定义一个函数,其参数是另一个函数以及该函数的参数。这种设计通常用于高阶函数（higher-order functions）,即接受函数作为参数或返回函数的函数。

以下是一个示例,展示如何实现这样的功能: 

复制代码
def execute_function(func, *args, **kwargs):
    # 接受一个函数 `func` 以及它的参数 `*args` 和 `**kwargs`,
    # 然后调用该函数并返回结果。
    return func(*args, **kwargs)

# 示例函数
def add(a, b):
    return a + b

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 调用 execute_function
result1 = execute_function(add, 3, 5)  # 等价于 add(3, 5)
result2 = execute_function(greet, "Alice", greeting="Hi")  # 等价于 greet("Alice", greeting="Hi")

print(result1)  # 输出: 8
print(result2)  # 输出: Hi, Alice!

代码说明: 

*args 和 **kwargs: 

*args 用于接收任意数量的非关键字参数。
**kwargs 用于接收任意数量的关键字参数。
这使得 execute_function 能够适配不同的函数及其参数。

高阶函数的灵活性: 

通过这种方式,你可以将任意函数及其参数传递给 execute_function,从而实现通用的函数调用逻辑。

这种模式在需要动态调用不同函数的场景中非常有用,例如回调函数、装饰器或函数式编程风格的代码中。
"""
