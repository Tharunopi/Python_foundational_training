import sys, pyodbc

sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle
from util.PropertyUtil import PropertyUtil
from util.DBConnection import DBConnection

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    # Car Management
    def addCar(self, car):
        cur = self.connection.cursor()

        query = "INSERT INTO Vechile_Table Values (?, ?, ?, ?, ?, ?, ?, ?)"
        values = (car.vechiceID, car.make, car.model, car.year, car.daiyRate, car.status, car.passengerCapacity, car.engineCapacity)

        cur.execute(query, values)
        self.connection.commit()
        cur.close()

    def removeCar(self, carID):
        cur = self.connection.cursor()

        query = f"DELETE FROM Vechile_Table WHERE vechileID = {carID}"

        cur.execute(query)
        self.connection.commit()
        cur.close()

    def listAvailableCars(self):
        cur = self.connection.cursor()

        query = "SELECT vechileID from Lease_Table WHERE CONVERT(DATE, GETDATE()) > endDate"

        cur.execute(query)
        result = cur.fetchall()      
        cur.close()
        return result

    def  listRentedCars(self):
        cur = self.connection.cursor()

        query = "SELECT vechileID FROM Lease_Table WHERE CONVERT(DATE, GETDATE()) BETWEEN startDate AND endDate"
        
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    def findCarById(self, carID):
        cur = self.connection.cursor()

        query = f"SELECT * FROM Vechile_Table WHERE vechileID = {carID}"

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    # Customer Management
    def addCustomer(self, customer):
        cur = self.connection.cursor()

        query = "INSERT INTO Customer_Table VALUES (?, ?, ?, ?, ?)"
        values = (customer.customerID, customer.firstName, customer.lastName, customer.email, customer.phoneNumber)

        cur.execute(query, values)
        self.connection.commit()
        cur.close()

    def removeCustomer(self, customerID):
        cur = self.connection.cursor()

        query = f"DELETE FROM Customer_Table WHERE customerID = {customerID}"

        cur.execute(query)
        self.connection.commit()
        cur.close()

    def listCustomers(self):
        cur = self.connection.cursor()

        query = "SELECT * FROM Customer_Table"

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    def findCustomerById(self, customerID):
        cur = self.connection.cursor()

        query = f"SELECT * FROM Customer_Table WHERE customerID = {customerID}"

        cur.execute(query)
        result = cur.fetchall()[0]
        customer = Customer(result[0], result[1], result[2], result[3], result[4])
        return customer
    
    # Lease Management
    def createLease(self, customerID, carID, startDate, endDate):
        cur = self.connection.cursor()

        type = "MonthlyLease" # work it up later
        query_1 = "INSERT INTO Lease_Table VALUES (?, ?, ?, ?, ?)"
        values = (carID, customerID, startDate, endDate, type) # make sure that lease id is auto incremented

        cur.execute(query_1, values)
        self.connection.commit()
        query_2 = 'SELECT SCOPE_IDENTITY()'
        cur.execute(query_2)
        leaseID = cur.fetchone()
        cur.close()
        return Lease(leaseID, carID, customerID, startDate, endDate, type)
    
    def returnCar(self, leaseID):
        cur = self.connection.cursor()

        query = f"SELECT * FROM Lease_Table WHERE leaseID = {leaseID}"

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    def listActiveLeases(self):
        cur = self.connection.cursor()

        query = "SELECT leaseID from Lease_Table WHERE CONVERT(DATE, GETDATE()) BETWEEN startDate AND endDate"

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    def listLeaseHistory(self):
        cur = self.connection.cursor()

        query = "SELECT * FROM Lease_Table"

        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    
    # Payment Table
    def recordPayment(self, lease, amount):
        cur = self.connection.cursor()

        query = "INSERT INTO Payment_Table VALUES (?, CONVERT(DATE, GETDATE()), ?)"
        values = (lease.leaseID, amount)

        cur.execute(query, values)
        self.connection.commit()
        cur.close()
