# @Time : 2021/3/1 17:30

# @Author : Upgrade(570492547@qq.com)
import time

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME, TEXT
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class EncryptDatabase(Base):
    """加密数据库操作类

    该类包含对加密文本进行的各种操作

    Attributes:
        encrypt_storage_obj str: 加密文本的文件名（包括后缀）
        encrypt_storage_obj_address str: 加密文本的位置（默认为同级目录下）
    """

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    update_date = Column(DATETIME, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    encrypted_password = Column(VARCHAR, nullable=False)
    description = Column(TEXT)

    def __init__(self, encrypted_password, description):
        """初始化

        Args:
            encrypted_password str: 加密后的结果
            description str: 该密码文本的描述
        """
        self.encrypted_password = encrypted_password
        self.description = description

    # @staticmethod
    # def create_encrypt_storage_obj(encrypt_storage_obj: str) -> bool:
    #     """创建加密文本
    #
    #     根据给出路径对加密文本进行创建
    #
    #     Args:
    #         encrypt_storage_obj str: 需要创建的加密文本的路径
    #
    #     Returns:
    #         bool: 成功为True，失败为False
    #
    #     """
    #     create_result = file_create(encrypt_storage_obj)
    #
    #     return create_result
    #
    # def encrypt_storage_obj_format_check(self):
    #     """加密文本格式检查"""
    #     with open(self.encrypt_storage_obj, 'r', encoding='utf8') as encrypt_data_set:
    #         for encrypt_data in encrypt_data_set:
    #             encrypt_data = encrypt_data.split(' ')
    #             if not len(encrypt_data) == 5:
    #                 return False
    #             if not encrypt_data[0].isdigit():
    #                 return False
    #             if not is_date(encrypt_data[1]):
    #                 return False
    #             if not is_time(encrypt_data[2]):
    #                 return False
    #     return True
    #
    # def password_add(self, password_id, encrypted_password, describe):
    #     """Write password to encrypted text"""
    #     password_info = f'{password_id} {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {encrypted_password} {describe}\n'
    #
    #     with open(self.encrypt_storage_obj, 'a', encoding='utf8') as f:
    #         f.write(password_info)
    #         return True
    #
    # def get_new_password_id(self):
    #     """用于获得目前的密码文本中下一个保存密码的id
    #
    #         Returns:
    #                 password_id int: 下一个保存密码的id
    #
    #     """
    #     with open(self.encrypt_storage_obj, 'r', encoding='utf8') as file:
    #         password_id = 0
    #         for line in file:
    #             password_id = line.split(' ')[0]
    #
    #         return int(password_id) + 1
    #
    # def get_all_password(self):
    #     """获取目前的密码文本中所有的密码
    #
    #     Returns:
    #         password_list list: 目前密码文本中的所有密码和其信息
    #
    #     """
    #     password_list = []
    #     with open(self.encrypt_storage_obj, 'r', encoding='utf8') as file:
    #         for line in file:
    #             line = line.split(' ')
    #             password_id = line[0]
    #             create_time = line[1] + ' ' + line[2]
    #             describe = line[-1][:-1]
    #             password = line[3]
    #
    #             password_list.append([password_id, create_time, describe, password])
    #     return password_list


def init_db():
    """Database init"""
    engine = create_engine(
        "mysql+pymysql://root:@localhost:3306/encrypt",
        encoding="utf-8",
        echo=True
    )
    Base.metadata.create_all(engine)
    print("Create table successfully")


if __name__ == '__main__':
    init_db()
