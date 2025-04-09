from abc import ABC, abstractmethod

from entity.User import User
from entity.Product import Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User, listofProducts):
        pass

    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def createProduct(self, user: User, product):
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, user: User):
        pass