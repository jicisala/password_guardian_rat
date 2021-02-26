# @Time : 2021/2/4 10:52 

# @Author : songshangru

# @File : EncryptionRat.py

# @Software: PyCharm
import time

from libs.password.password_generate import password_generate
from libs.password.Encryptor import Encryptor


# TODO(570492547@qq.com): 将对加密文本得操作进行分离
# TODO(570492547@qq.com): 对数据类型进行整理
# TODO(570492547@qq.com): 对外部输入数据进行验证
from core.EncryptionText import EncryptionText


class EncryptionRat:
    """该程序的核心模块，实现相应的一系列操作

    根据需求生成随机密码，并对外提供各种加密方式统一的访问接口，目前支持的加密方式有md5，AES，RSA

    Attributes:
        encrypt_text str: 加密文本所在的位置

    """

    def __init__(self, encrypt_text: EncryptionText):
        self.encrypt_text = encrypt_text

    @staticmethod
    def password_generate(password_length, if_number, if_letter, if_symbol, chars_exclude):
        """根据要求生成密码

        使用的是已有工具类中的密码生成函数

        Args:
            password_length int: 密码长度
            if_number bool: 是否包含数字
            if_letter bool: 是否包含字母
            if_symbol bool: 是否包含符号
            chars_exclude list: 需要排除的字符

        Returns:
            password str: 生成的密码字符串
        """
        password = password_generate(password_length=password_length, if_number=if_number, if_letter=if_letter,
                                     if_symbol=if_symbol, chars_excludes=chars_exclude)

        return password

    def password_save(self, password, describe):
        """密码保存

        将密码根据加密后保存到相应的加密文本中

        Args:
            password str: 需要保存的密码
            describe str: 该密码的描述

        """
        # 给出加密密码
        print('请给出加密密码')
        open_box_password = input()

        # 通过md5算出密钥
        key = Encryptor(encrypt_type='md5').encrypt(open_box_password)

        # 使用密钥对密码进行加密
        aes = Encryptor(encrypt_type='aes', key=key)
        encrypt_result = aes.encrypt(password)

        # 获得密码保存id
        password_id = self.encrypt_text.get_new_password_id()

        write_content = str(password_id) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                                               time.localtime()) + ' ' + encrypt_result + ' ' + describe + '\n'
        if self.encrypt_text.password_add(write_content):
            print("密码保存成功")

    def password_get(self):
        """获得所保存的密码

        从已保存的密码中获得需要的密码

        """
        password_list = self.encrypt_text.get_all_password()
        if not password_list:
            print('该加密文本为空')
            return False

        print('目前所有密码如下,请选择需要查看的密码的id')

        for password in password_list:
            print(' '.join(password[:-1]))

        password_id = input()

        # 给出开箱密码
        print('请给出加密密码')
        open_box_password = input()

        # 通过md5算出密钥
        key = Encryptor(encrypt_type='md5').encrypt(open_box_password)

        # 使用密钥对密码进行解密
        for password in password_list:
            if password[0] == password_id:
                try:
                    aes = Encryptor(encrypt_type='aes', key=key)
                    decrypt_result = aes.decrypt(password[3])

                    print('解密结果为:' + decrypt_result)
                except UnicodeDecodeError:
                    print('加密密码错误')



if __name__ == '__main__':
    x = EncryptionRat()
    new_password = x.password_generate(16, True, True, True, [])
    # x.password_save(password=password, describe='测试')
    x.password_get()
