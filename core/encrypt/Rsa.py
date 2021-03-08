# @Time : 2021/3/3 15:54 

# @Author : Upgrade(570492547@qq.com)
import rsa


# TODO(570492547@qq.com): 未经测试
class Rsa:
    def __init__(self, key_pub, key_priv):
        self.key_pub = key_pub
        self.key_priv = key_priv

    @staticmethod
    def generate_keys(key_length: int):
        # TODO(570492547@qq.com): 获取的公钥私钥不是字符串形式
        key_pub, key_priv = rsa.newkeys(key_length)

        return key_pub, key_priv

    def encrypt(self, raw_content):
        encrypt_content = rsa.encrypt(raw_content, self.key_pub)

        return encrypt_content

    def decrypt(self, encrypt_content):
        decrypt_content = rsa.decrypt(encrypt_content, self.key_priv)

        return decrypt_content
