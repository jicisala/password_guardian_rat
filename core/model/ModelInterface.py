# @Time : 2021/3/2 16:18 

# @Author : Upgrade(570492547@qq.com)
from abc import ABCMeta, abstractmethod


class ModelInterface(metaclass=ABCMeta):
    @abstractmethod
    def password_add(self, encrypted_password: str, description: str) -> bool:
        pass

    @abstractmethod
    def password_del(self, password_id: int) -> bool:
        pass

    @abstractmethod
    def password_update(self, password_id: int, encrypted_password: str, description: str) -> bool:
        pass

    @abstractmethod
    def password_get(self, password_id: int) -> dict:
        pass
