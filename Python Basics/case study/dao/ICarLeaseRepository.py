from abc import ABC, abstractmethod
import sys

sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle

class ICarLeaseRepository(ABC):

    # Car Management
    @abstractmethod
    def addCar(self, car: Vechicle):
        pass

    @abstractmethod
    def removeCar(self, carID: int):
        pass

    @abstractmethod
    def listAvailableCars(self):
        pass

    @abstractmethod
    def listRentedCars(self):
        pass

    @abstractmethod
    def findCarById(self, carID: int):
        pass

    # Customer Management
    @abstractmethod
    def addCustomer(self, customer: Customer):
        pass

    @abstractmethod
    def removeCustomer(self, customerID: int):
        pass

    @abstractmethod
    def listCustomers(self):
        pass

    @abstractmethod
    def findCustomerById(self, customerID: int):
        pass

    # Lease Management
    @abstractmethod
    def createLease(self, customerID: int, carID: int, startDate: str, endDate: str):
        pass

    @abstractmethod
    def returnCar(self, leaseID: int):
        pass

    @abstractmethod
    def listActiveLeases(self):
        pass

    @abstractmethod
    def listLeaseHistory(self):
        pass

    # Payment Handling
    @abstractmethod
    def recordPayment(self, lease: Lease, amount:float):
        pass