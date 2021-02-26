# @Time : 2021/2/24 14:36 

# @Author : Upgrade(jicisala@126.com)

# @File : EncryptionText.py 

# @Software: PyCharm
from libs.file_handle import check_file_exists
from libs.file_handle import file_create
from libs.string_type_validate import is_date
from libs.string_type_validate import is_time
from core.custome_exception import EncryptTextFormatError


class EncryptionText:
    """加密文本操作类

    该类包含对加密文本进行的各种操作

    Attributes:
        encrypt_text str: 加密文本的文件名（包括后缀）
        encrypt_text_address str: 加密文本的位置（默认为同级目录下）
    """

    def __init__(self, encrypt_text: str, if_auto_create=True):
        """初始化

        Args:
            encrypt_text str: 加密文本的完整路径
            if_auto_create bool: 若路径下不存在，是否自动创建加密文本，默认自动创建
        """
        self.encrypt_text = encrypt_text

        # 检查路径下文件是否存在，并根据if_auto_create决定处理方式
        if not check_file_exists(self.encrypt_text):
            if if_auto_create:
                print(self.encrypt_text + '创建成功')
                self.create_encrypt_text(self.encrypt_text)
            else:
                raise FileNotFoundError(self.encrypt_text)

        # 检查加密文本是否符合要求
        if not self.encrypt_text_format_check():
            raise EncryptTextFormatError

    @staticmethod
    def create_encrypt_text(encrypt_text: str) -> bool:
        """创建加密文本

        根据给出路径对加密文本进行创建

        Args:
            encrypt_text str: 需要创建的加密文本的路径

        Returns:
            bool: 成功为True，失败为False

        """
        create_result = file_create(encrypt_text)

        return create_result

    def encrypt_text_format_check(self):
        """加密文本格式检查"""
        with open(self.encrypt_text, 'r', encoding='utf8') as encrypt_data_set:
            for encrypt_data in encrypt_data_set:
                encrypt_data = encrypt_data.split(' ')
                if not len(encrypt_data) == 5:
                    return False
                if not encrypt_data[0].isdigit():
                    return False
                if not is_date(encrypt_data[1]):
                    return False
                if not is_time(encrypt_data[2]):
                    return False
        return True

    def password_add(self, password_info):
        with open(self.encrypt_text, 'a', encoding='utf8') as f:
            f.write(password_info)
            return True

    def get_new_password_id(self):
        """用于获得目前的密码文本中下一个保存密码的id

            Returns:
                    password_id int: 下一个保存密码的id

        """
        with open(self.encrypt_text, 'r', encoding='utf8') as file:
            password_id = 0
            for line in file:
                password_id = line.split(' ')[0]

            return int(password_id) + 1

    def get_all_password(self):
        """获取目前的密码文本中所有的密码

        Returns:
            password_list list: 目前密码文本中的所有密码和其信息

        """
        password_list = []
        with open(self.encrypt_text, 'r', encoding='utf8') as file:
            for line in file:
                line = line.split(' ')
                password_id = line[0]
                create_time = line[1] + ' ' + line[2]
                describe = line[-1][:-1]
                password = line[3]

                password_list.append([password_id, create_time, describe, password])
        return password_list


if __name__ == '__main__':
    _ = EncryptionText('E:\Projects\Python-projects\Creative Workshop\projects\password_manager\default_encrypt_text.txt')
    print(_.encrypt_text_format_check())
