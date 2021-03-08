# @Time : 2021/2/4 10:52 

# @Author : Upgrade(570492547@qq.com)
from libs.password.password_generate import password_generate
from core.encrypt.encryptor import Encryptor
from core.model.EncryptionDataHandle import EncryptionDataHandle
# TODO(570492547@qq.com): 对外部输入数据进行验证


class EncryptionRat:
    """该程序的核心模块，实现相应的一系列操作

    根据需求生成随机密码，并对外提供各种加密方式统一的访问接口，目前支持的加密方式有md5，AES，RSA

    Attributes:
        encrypt_storage_obj str: 加密文本所在的位置
    """

    def __init__(self, encrypt_storage_obj):
        self.encryption_data_handle = EncryptionDataHandle(encrypt_storage_obj)

    @staticmethod
    def password_generate(password_length: int, if_number: bool, if_letter: bool, if_symbol: bool, chars_exclude: bool) -> str:
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

    def password_add(self, password: str, description: str, open_box_password: str) -> bool:
        """密码保存

        将密码根据加密后保存到相应的加密文本中

        Args:
            password str: 需要保存的密码
            describe str: 该密码的描述

        """
        # 通过md5算出密钥
        key = Encryptor(encrypt_type='md5').encrypt(open_box_password)

        # 使用密钥对密码进行加密
        aes = Encryptor(encrypt_type='aes', key=key)
        encrypted_password = aes.encrypt(password)

        # save the result
        try:
            self.encryption_data_handle.password_add(encrypted_password, description)
            return True
        except Exception as e:
            raise e

    def password_get(self, password_id: str, open_box_password: str) -> str:
        """get require password

        get require password form existing password

        """
        # 通过md5算出密钥
        key = Encryptor(encrypt_type='md5').encrypt(open_box_password)

        # 使用密钥对密码进行解密
        password = self.encryption_data_handle.password_get(password_id)

        try:
            aes = Encryptor(encrypt_type='aes', key=key)
            decrypt_result = aes.decrypt(password['password'])

            return decrypt_result
        except UnicodeDecodeError:
            print('加密密码错误')

    def password_get_all(self):
        result = self.encryption_data_handle.password_get_all()

        if not result:
            print('无被加密密码')
            return ''

        return result

    def password_del(self):
        pass

    def password_update(self):
        pass
