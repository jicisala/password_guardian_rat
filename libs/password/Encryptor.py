# @Time : 2021/2/4 11:01 

# @Author : songshangru

# @File : Encryptor.py

# @Software: PyCharm
import hashlib
import rsa
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex, a2b_hex


class Encryptor:
    """加密模块核心

    对多种加密方式进行统一分装，并对外提供统一的访问接口
    目前支持的加密方式有：
    1，md5
    2，AES
    3，RSA（还需要完善）

    Attributes:
        encrypt_type str: 需要使用的加密方式,不区分大小写，可选方式为RSA，AES, md5
        kwargs['key_pub'], kwargs['key_priv'] str: 使用RSA加密方式时特有,分别为公钥和私钥
        kwargs['key'] str: 使用AES时特有，为所使用的密钥
    """
    def __init__(self, encrypt_type, **kwargs):
        """实例初始化函数，对加密类型进行确定，根据加密类型生成相应的加密对象"""
        self.encrypt_type = encrypt_type
        if encrypt_type.lower() == 'rsa':
            self.encryptor = Rsa(key_pub=kwargs['key_pub'], key_priv=kwargs['key_priv'])
        elif encrypt_type.lower() == 'aes':
            self.encryptor = Aes(key=kwargs['key'])
        elif encrypt_type.lower() == 'md5':
            self.encryptor = Md5()
        else:
            assert False, '所使用的加密方式暂不支持，请联系作者以进行添加'

    def encrypt(self, raw_content):
        """统一的加密操作"""
        encrypt_result = self.encryptor.encrypt(raw_content)

        return encrypt_result

    def decrypt(self, encrypt_content):
        """统一的解密操作"""
        decrypt_content = self.encryptor.decrypt(encrypt_content)

        return decrypt_content


# TODO(570492547@qq.com): 未经测试
class Rsa:
    def __init__(self, key_pub, key_priv):
        self.key_pub = key_pub
        self.key_priv = key_priv

    @staticmethod
    def generate_keys(key_length):
        # TODO(570492547@qq.com): 获取的公钥私钥不是字符串形式
        key_pub, key_priv = rsa.newkeys(key_length)

        return key_pub, key_priv

    def encrypt(self, raw_content):
        encrypt_content = rsa.encrypt(raw_content, self.key_pub)

        return encrypt_content

    def decrypt(self, encrypt_content):
        decrypt_content = rsa.decrypt(encrypt_content, self.key_priv)

        return decrypt_content


class Aes:
    def __init__(self, key):
        self.key = bytes(key, encoding='utf8')
        self.iv = Random.new().read(AES.block_size)
        self.mycipher = AES.new(self.key, AES.MODE_CFB, self.iv)

    def encrypt(self, raw_content):
        encrypt_result = self.iv + self.mycipher.encrypt(raw_content.encode())

        encrypt_result = b2a_hex(encrypt_result).decode()
        return encrypt_result

    def decrypt(self, encrypt_content):
        encrypt_content = a2b_hex(encrypt_content.encode())

        mydecrypt = AES.new(self.key, AES.MODE_CFB, encrypt_content[:16])
        decrypt_result = mydecrypt.decrypt(encrypt_content[16:]).decode()

        return decrypt_result


class Md5:
    def __init__(self):
        self.hash = hashlib.md5()

    def encrypt(self, raw_content):
        self.hash.update(raw_content.encode(encoding='utf-8'))
        result = self.hash.hexdigest()

        return result

    def decrypt(self, encrypt_content):
        print('md5加密无法解密')
        return False


if __name__ == '__main__':
    rsa = Encryptor(encrypt_type='rsa')
    # md5 = Encryptor(encrypt_type='md5')
    # key = md5.encrypt(raw_content='jingwan0111')
    #
    # aes_en = Encryptor(encrypt_type='aes', key=key)
    # en_res = aes_en.encrypt(raw_content='wanjing0111')
    #
    # aes_de = Encryptor(encrypt_type='aes', key=key)
    # de_res = aes_de.decrypt(en_res)
    #
    # print(de_res)



