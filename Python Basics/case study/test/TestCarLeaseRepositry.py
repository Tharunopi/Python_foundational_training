import unittest, sys

sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle

from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.LeaseNotFoundException import LeaseNotFoundException

from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl

class TestCarLeaseRepositry(unittest.TestCase):

    def setUp(self):
        self.repository = ICarLeaseRepositoryImpl()

    # to test car created or not
    def testCarAdd(self):
        car = Vechicle(vechiceID=18, make="toyota", model="fortuner", year="2005", dailyRate=4593, status="available", passengerCapacity=8, engineCapacity=2.1)
        result = self.repository.addCar(car)
        print(f"result : {result}")
        self.assertTrue(result)

    # to test lease created or not
    def testLeaseAdd(self):
        result = self.repository.createLease(customerID=1, carID=1, startDate="2025-04-05", endDate="2025-04-07")
        print(f"result : {result}")
        self.assertTrue(result)

    # to test lease retrieved or not
    def testLeaseRetrival(self):
        result_1 = self.repository.listActiveLeases()
        print(f" len of result_1 : {len(result_1)}")
        self.assertIsNotNone(result_1)

        result_2 = self.repository.listLeaseHistory()
        print(f" len of result_2 : {len(result_2)}")
        self.assertIsNotNone(result_2)

    # to test exception is correctly thrown or not
    def testExceptionThrown(self):
        with self.assertRaises(CarNotFoundException):
            self.repository.findCarById(carID=-1)

        with self.assertRaises(CustomerNotFoundException):
            self.repository.findCustomerById(customerID=-1)

        with self.assertRaises(LeaseNotFoundException):
            self.repository.returnCar(leaseID=-1)

unittest.main()