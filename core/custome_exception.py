# @Time : 2021/2/24 16:43 

# @Author : Upgrade(jicisala@126.com)

# @File : custome_exception.py 

# @Software: PyCharm


class EncryptTextFormatError(Exception):
    def __str__(self):
        print('加密文本格式有误')
