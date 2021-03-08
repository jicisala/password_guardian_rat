# @Time : 2021/3/2 16:50 

# @Author : Upgrade(570492547@qq.com)
from core.controller.EncryptionRat import EncryptionRat
from core.model.EncryptionText import EncryptionText


# TODO(570492547@qq.com): add language choice function(Chinese or English).
# TODO(570492547@qq.com): extract content text to a file which can be selected depend on different language.
# TODO(570492547@qq.com): finish delete, update and others function.

class ConsoleView:
    def __init__(self, encrypt_rat):
        self.encrypt_rat = encrypt_rat

    @staticmethod
    def encrypt_text_choice():
        """Instance creation entry when you use EncryptText"""
        print("请选择你要使用的加密文本（不输入直接按回车则为默认加密文本）")
        encryption_text_name = input()

        if encryption_text_name:
            encrypt_storage_obj = EncryptionText('.\\' + encryption_text_name)
            encryption_rat = EncryptionRat(encrypt_storage_obj)
        else:
            # If encryption_text_name is empty, use default encrypt text named 'default_encrypt_storage_obj.txt'
            encrypt_storage_obj = EncryptionText('.\default_encrypt_text.txt')
            encryption_rat = EncryptionRat(encrypt_storage_obj)

        return ConsoleView(encryption_rat)

    def function_choice(self):
        """function choice

        Returns:
            func_num: number of the function.
        """
        print('请选择你需要使用的功能(输入数字，然后回车)：\n'
              "1,密码生成\n"
              "2,密码保存\n"
              "3,密码获取\n")

        func_num = input()

        return func_num

    def password_generate(self):
        """password generate as your require

        Returns:
            password str: generate password
        """
        print('请输入需要生成的密码位数')
        password_length = int(input())
        print('是否需要自定义?（y/n）')
        if_custom = input().lower()
        if if_custom == 'y':
            print('是否包含数字？（y/n）')
            if_number = input().lower()
            print('是否包含字母？（y/n）')
            if_letter = input().lower()
            print('是否包含符号？（y/n）')
            if_symbol = input().lower()
            print('是否有需要排除的字符（用空格分隔）')
            chars_exclude = input().split(' ')

            password = self.encrypt_rat.password_generate(password_length=password_length, if_number=if_number,
                                                          if_letter=if_letter,
                                                          if_symbol=if_symbol, chars_exclude=chars_exclude)
        else:
            password = self.encrypt_rat.password_generate(password_length=password_length, if_number=True,
                                                          if_letter=True,
                                                          if_symbol=True, chars_exclude=[])

        return password

    def password_add(self):
        print("请输入需要保存的密码")
        password = input()

        if not password:
            print("输入密码不能为空")
            return False

        print("请输入密码的描述")
        description = input()

        print("请输入加密密码")
        open_box_password = input()

        if self.encrypt_rat.password_add(password=password, description=description,
                                         open_box_password=open_box_password):
            print("密码保存成功")

    def password_get(self):
        print("目前所有密码如下，请输入你需要查询的密码的id")
        password_list = self.encrypt_rat.password_get_all()

        for password in password_list:
            print_list = []
            for key, value in password.items():
                if key != 'password':
                    print_list.append(value)
            # the str has own line breaks, so print is no need to generate line breaks again.
            print(' '.join(print_list), end='')
        print('\n')
        password_id = input()

        if not password_id or not password_id.isdigit():
            print("请输入正确的密码id")
            return False

        print("请输入该密码的加密密码")
        open_box_password = input()

        result = self.encrypt_rat.password_get(password_id=password_id, open_box_password=open_box_password)

        if result:
            print(f"获取的密码为:{result}")
