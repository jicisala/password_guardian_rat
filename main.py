# @Time : 2021/2/5 11:31 

# @Author : songshangru

# @File : main.py 

# @Software: PyCharm
# TODO(570492547@qq.com): 增加密码的删除功能
from projects.password_manager.core.EncryptionRat import EncryptionRat
from projects.password_manager.core.EncryptionText import EncryptionText

print("密码保险箱0.3\n"
      "作者：Upgrade\n"
      "请选择你要使用的加密文本（输入为空则为默认加密文本）")
encryption_text_name = input()

if encryption_text_name:
    encrypt_text = EncryptionText('.\\' + encryption_text_name)
    encryption_rat = EncryptionRat(encrypt_text)
else:
    encrypt_text = EncryptionText('.\default_encrypt_text.txt')
    encryption_rat = EncryptionRat(encrypt_text)

while True:
    try:
        print('请选择你需要使用的功能：')
        print("1,密码生成")
        print("2,密码保存")
        print("3,密码获取")
        func_num = input()

        if func_num == "1":
            # 生成密码
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

                password = encryption_rat.password_generate(password_length=password_length, if_number=if_number,
                                                            if_letter=if_letter,
                                                            if_symbol=if_symbol, chars_exclude=chars_exclude)
            else:
                password = encryption_rat.password_generate(password_length=password_length, if_number=True, if_letter=True,
                                                            if_symbol=True, chars_exclude=[])

            print(f'生成密码为:{password}')

        elif func_num == "2":
            print("请输入需要保存的密码")
            password = input()

            if not password:
                print("输入密码不能为空")
                continue

            print("请输入密码的描述")
            describe = input()

            encryption_rat.password_save(password, describe)
        elif func_num == "3":
            encryption_rat.password_get()
        else:
            print("所输入的选项无效\n")

    except Exception as e:
        print(e)
