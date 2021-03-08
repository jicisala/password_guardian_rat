# @Time : 2021/2/4 11:01 

# @Author : Upgrade(570492547@qq.com)
from core.encrypt.Aes import Aes
from core.encrypt.Md5 import Md5
from core.encrypt.Rsa import Rsa


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
            self.encryptor_core = Rsa(key_pub=kwargs['key_pub'], key_priv=kwargs['key_priv'])
        elif encrypt_type.lower() == 'aes':
            self.encryptor_core = Aes(key=kwargs['key'])
        elif encrypt_type.lower() == 'md5':
            self.encryptor_core = Md5()
        else:
            assert False, '所使用的加密方式暂不支持，请联系作者以进行添加'

    def encrypt(self, raw_content):
        """统一的加密操作"""
        encrypted_password = self.encryptor_core.encrypt(raw_content)

        return encrypted_password

    def decrypt(self, encrypt_content):
        """统一的解密操作"""
        decrypt_content = self.encryptor_core.decrypt(encrypt_content)

        return decrypt_content
