# @Time : 2021/2/24 14:54 

# @Author : Upgrade(570492547@qq.com)
import os


def check_file_exists(file_path: str) -> bool:
    """check if the file exists

    Args:
        file_path: file path

    Returns:
        bool: True or False

    """
    if os.path.exists(file_path):
        return True
    else:
        return False


def file_create(file_path: str) -> bool:
    """文件创建

    对文件进行创建操作

    Args:
        file_path str: 文件路径

    Returns:
        根据创建结果返回True或False

    Raises:
        FileExistsError: 若文件存在，则返回这个错误
    """
    # 检查路径是否合法
    if not file_path:
        print('路径为空')
        return False

    # 检查文件是否存在
    if not check_file_exists(file_path):
        with open(file_path, 'w'):
            pass
        return True
    else:
        raise FileExistsError
