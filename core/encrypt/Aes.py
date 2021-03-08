# @Time : 2021/3/3 15:54 

# @Author : Upgrade(570492547@qq.com)
from binascii import b2a_hex, a2b_hex

from Cryptodome.Cipher import AES
from Cryptodome import Random


class Aes:
    def __init__(self, key: str):
        self.key = bytes(key, encoding='utf8')
        self.iv = Random.new().read(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CFB, self.iv)

    def encrypt(self, raw_content):
        encrypted_password = self.iv + self.cipher.encrypt(raw_content.encode())

        encrypted_password = b2a_hex(encrypted_password).decode()
        return encrypted_password

    def decrypt(self, encrypt_content):
        encrypt_content = a2b_hex(encrypt_content.encode())

        decrypt = AES.new(self.key, AES.MODE_CFB, encrypt_content[:16])
        decrypt_result = decrypt.decrypt(encrypt_content[16:]).decode()

        return decrypt_result

