# @Time : 2021/2/5 11:31 

# @Author : Upgrade(570492547@qq.com)
# TODO(570492547@qq.com): 增加密码的删除功能
from core.view.ConsoleView import ConsoleView

print("欢迎使用加密鼠\n"
      "作者：Upgrade(570492547@qq.com)\n"
      "版本: 0.5")

"""At present, only encrypt text is supported"""
# core instance initialize.
console_view = ConsoleView.encrypt_text_choice()

while True:
    try:
        func_num = console_view.function_choice()

        if func_num == "1":
            password = console_view.password_generate()

            print(f'生成密码为:{password}')
        elif func_num == "2":
            console_view.password_add()
        elif func_num == "3":
            console_view.password_get()
        else:
            print("所输入的选项无效\n")

    except Exception as e:
        print(e)
