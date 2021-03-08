# @Time : 2021/2/24 14:36 

# @Author : Upgrade(570492547@qq.com)
import time

from core.model.ModelInterface import ModelInterface
from libs.file_handle import check_file_exists
from libs.file_handle import file_create
from libs.string_type_validate import is_date
from libs.string_type_validate import is_time
from libs.custome_exception import EncryptTextFormatError


class EncryptionText(ModelInterface):
    """加密文本操作类

    该类包含对加密文本进行的各种操作

    Attributes:
        encrypt_storage_obj str: 加密文本的文件名（包括后缀）
        encrypt_storage_obj_address str: 加密文本的位置（默认为同级目录下）
    """

    def __init__(self, encrypt_storage_obj: str, if_auto_create: bool = True):
        """初始化

        Args:
            encrypt_storage_obj str: 加密文本的完整路径
            if_auto_create bool: 若路径下不存在，是否自动创建加密文本，默认自动创建
        """
        self.encrypt_storage_obj = encrypt_storage_obj

        # 检查路径下文件是否存在，并根据if_auto_create决定处理方式
        if not check_file_exists(self.encrypt_storage_obj):
            if if_auto_create:
                print(self.encrypt_storage_obj + '创建成功')
                self.create_encrypt_storage_obj(self.encrypt_storage_obj)
            else:
                raise FileNotFoundError(self.encrypt_storage_obj)

        # 检查加密文本是否符合要求
        if not self._encrypt_storage_obj_format_check():
            raise EncryptTextFormatError

    def password_add(self, encrypted_password: str, description: str) -> bool:
        """Write password to encrypted text"""
        password_id = self._get_new_password_id()

        password_info = f'{password_id} {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {encrypted_password} {description}\n'

        with open(self.encrypt_storage_obj, 'a', encoding='utf8') as f:
            f.write(password_info)
            return True

    def password_get(self, password_id: str) -> dict:
        """Get saved password information by password_id"""
        # 使用密钥对密码进行解密
        for password in self.password_get_all():
            if password['password_id'] == password_id:
                return password

    def password_get_all(self) -> list:
        """获取目前的密码文本中所有的密码

        Returns:
            password_list list: 目前密码文本中的所有密码和其信息

        """
        password_list = []
        with open(self.encrypt_storage_obj, 'r', encoding='utf8') as file:
            for line in file:
                password_info = {}
                line = line.split(' ')
                password_info['password_id'] = line[0]
                password_info['create_time'] = line[1] + ' ' + line[2]
                password_info['password'] = line[3]
                password_info['describe'] = ' '.join(line[4:])

                password_list.append(password_info)
        return password_list

    def password_del(self, password_id: str):
        """Delete password information by password_id

        The password information needs to be verified before it can be delete

        Returns:
            delete_result: True or False
        """
        password_information = self.password_get(password_id)

    def password_update(self, password_id: str, encrypted_password: str, description: str) -> bool:
        pass

    @staticmethod
    def create_encrypt_storage_obj(encrypt_storage_obj: str) -> bool:
        """创建加密文本

        根据给出路径对加密文本进行创建

        Args:
            encrypt_storage_obj str: 需要创建的加密文本的路径

        Returns:
            bool: 成功为True，失败为False

        """
        create_result = file_create(encrypt_storage_obj)

        return create_result

    def _get_new_password_id(self):
        """用于获得目前的密码文本中下一个保存密码的id

            Returns:
                    password_id int: 下一个保存密码的id

        """
        with open(self.encrypt_storage_obj, 'r', encoding='utf8') as file:
            password_id = 0
            for line in file:
                password_id = line.split(' ')[0]

            return int(password_id) + 1

    def _encrypt_storage_obj_format_check(self):
        """加密文本格式检查"""
        with open(self.encrypt_storage_obj, 'r', encoding='utf8') as encrypt_data_set:
            for encrypt_data in encrypt_data_set:
                encrypt_data = encrypt_data.split(' ')
                if not encrypt_data[0].isdigit():
                    return False
                if not is_date(encrypt_data[1]):
                    return False
                if not is_time(encrypt_data[2]):
                    return False
        return True


