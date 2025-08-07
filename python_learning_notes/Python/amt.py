"""
老师的写法好的地方:
1、查询函数中flag的传递,可以在存钱和取钱时调用查询函数
2、存钱取钱时num的传递
3、while True避免主菜单函数的递归调用
"""
money = 5000000
name = None

def check_balance():# 老师用的是query(),似乎更准确
    print("---------------------查询余额---------------------")
    print(f"{name}你好,你的余额为{money}")

def save_money():
    save_num = 50000

    global money
    money += save_num
    print("---------------------存款---------------------")
    print(f"{name}你好,你存款{save_num}成功\n你的余额为{money}")

def draw_money():
    draw_num = 50000

    global money
    money -= draw_num

    print("---------------------取款---------------------")
    print(f"{name}你好,你取款{take_num}成功\n你的余额为{money}")

def quit():
    print("感谢您的光临")

def menu():
    print("---------------------主菜单---------------------")
    # print("查询余额\t\[输入1\]\n存款\t\[输入2\]\n取款\t\[输入3\]\n退出\t\[输入4\]\n")    第一个问题,输出[]前面不用加反斜杠
    # print("查询余额\t[输入1]\n存款\t[输入2]\n取款\t[输入3]\n退出\t[输入4]\n")    第二个问题,几个输入数字在显示的时候并没有对齐
    print("%-*s\t%s" % (8, "查询余额", "[输入1]"))# *定义宽度,-为左对齐,关于对齐的方法还有好几种,这里我没有完全弄懂
    print("%-*s\t%s" % (10, "存款", "[输入2]"))
    print("%-*s\t%s" % (10, "取款", "[输入3]"))
    print("%-*s\t%s" % (10, "退出", "[输入4]"))
    num = int(input("请输入您的选择"))

    """
    下面的写法导致了死循环,实际上因为一直会调用menu()所以不用任何判断就可以实现一直运行
    """
    # while num:
    #     if num == 1:
    #         check_balance()
    #         menu()
    #     elif num == 2:
    #         save_money()
    #         menu()
    #     elif num == 3:
    #         take_money()
    #         menu()
    #     elif num == 4:
    #         quit()
    #         break
    #     else:
    #         # print("输入错误,请重新输入")
    #         # menu()

    if num == 1:# 一开始==写成了=,报错了
        check_balance()
        menu()
    elif num == 2:
        save_money()
        menu()
    elif num == 3:
        take_money()
        menu()
    elif num == 4:
        quit()
    else:
        print("输入错误,请重新输入")
        menu()

def atm_main():
    global name
    name = input("请输入您的姓名")
    menu()

atm_main()

"""
money = 5000000
name = None
name = input("请输入您的名字:")

# 老师用的是query(),似乎更准确
# 这里的show_header是因为在后面的存款和取款中都要显示余额,所以会调用query函数,但是又不想显示查询余额那一行
def query(show_header):
    if show_header:
        print("---------------------查询余额---------------------")
    print(f"{name}你好,你的余额为{money}")

# 和我的相比,这里存取款的金额num是作为参数传进来的
def saving(num):
    global money
    money += num
    print("---------------------存款---------------------")
    print(f"{name}你好,你存款{save_num}成功")
    query(False)

def get_money(num):
    global money
    money -= num

    print("---------------------取款---------------------")
    print(f"{name}你好,你取款{take_num}成功")
    query(False)

def main():
    print("---------------------主菜单---------------------")
    print("欢迎光临,请选择您的操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")# 老师的对齐很粗暴
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择:")

while True:
    keyboard_input() = main()

    if keyboard_input == "1":# 一开始==写成了=,报错了
        query(True)
        continue
        # 这里直接跳出本次循环进行下一次循环,因为默认是True所以又会进入while循环,然后一进来就执行keyboard_input() = main()就实现了每次都打印主菜单
        # 但是这里不使用continue也不会继续了,因为是逻辑判断啊
    elif keyboard_input == "2":
        num = int(input("请输入您想要存的金额:"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入您想要取的金额:"))
        get_money(num)
        continue
    else:# 老师这里输入错误或输入4都退出,我觉得没有我的好
        print("程序退出啦")
        break
        # 这里就break跳出循环啦

"""