# @Time : 2021/3/3 15:54 

# @Author : Upgrade(570492547@qq.com)
import hashlib


class Md5:
    def __init__(self):
        self.hash = hashlib.md5()

    def encrypt(self, raw_content):
        self.hash.update(raw_content.encode(encoding='utf-8'))
        result = self.hash.hexdigest()

        return result

    def decrypt(self, encrypt_content):
        print('MD5无法被解密')

        return False
