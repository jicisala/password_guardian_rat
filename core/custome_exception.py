# @Time : 2021/2/24 16:43 

# @Author : Upgrade(570492547@qq.com)


class EncryptTextFormatError(Exception):
    def __str__(self):
        print('加密文本格式有误')
