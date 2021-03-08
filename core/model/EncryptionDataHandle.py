# @Time : 2021/3/8 15:36 

# @Author : Upgrade(570492547@qq.com)


class EncryptionDataHandle:
    def __init__(self, Model):
        self.model = Model

    def password_add(self, encrypted_password: str, description: str) -> bool:
        result = self.model.password_add(encrypted_password=encrypted_password, description=description)
        return result

    def password_del(self, password_id: str) -> bool:
        result = self.model.password_del(password_id=password_id)
        return result

    def password_update(self, password_id: str, encrypted_password: str, description: str) -> bool:
        result = self.model.password_update(password_id=password_id, encrypted_password=encrypted_password, description=description)
        return result

    def password_get(self, password_id: str) -> dict:
        result = self.model.password_get(password_id=password_id)
        return result

    def password_get_all(self) -> list:
        result = self.model.password_get_all()
        return result
