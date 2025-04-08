import sys, pyodbc
from datetime import datetime

sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle
from util.PropertyUtil import PropertyUtil
from util.DBConnection import DBConnection
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.LeaseNotFoundException import LeaseNotFoundException

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    # Car Management
    def addCar(self, car):
        try:
            cur = self.connection.cursor()

            query = "INSERT INTO Vechile_Table Values (?, ?, ?, ?, ?, ?, ?, ?)"
            values = (car.vechiceID, car.make, car.model, car.year, car.daiyRate, car.status, car.passengerCapacity, car.engineCapacity)

            cur.execute(query, values)
            self.connection.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error Adding Car : {e}")

    def removeCar(self, carID):
        try:
            cur = self.connection.cursor()
            
            query = f"DELETE FROM Vechile_Table WHERE vechileID = {carID}"

            cur.execute(query)
            self.connection.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error Removeing Car : {e}")
            

    def listAvailableCars(self):
        try:
            cur = self.connection.cursor()

            query = "SELECT * from Vechile_Table WHERE status = 'available'"

            cur.execute(query)
            result = cur.fetchall()      
            cur.close()
            return result
        
        except Exception as e:
            print(f"Error Listing Available Cars : {e}")

    def  listRentedCars(self):
        try:
            cur = self.connection.cursor()

            query = "SELECT * from Vechile_Table WHERE status = 'notAvailable'"
            
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        
        except Exception as e:
            print(f"Error Listing Rented Cars : {e}")
    
    def findCarById(self, carID):     
        try:  
            cur = self.connection.cursor()

            query = f"SELECT * FROM Vechile_Table WHERE vechileID = {carID}"

            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            if not result:
                raise CarNotFoundException
            return result[0]
        
        except CarNotFoundException:
            raise

        except Exception as e:
            print(f"Error Finding Car : {e}")

    
    # Customer Management
    def addCustomer(self, customer):
        try:
            cur = self.connection.cursor()

            query = "INSERT INTO Customer_Table VALUES (?, ?, ?, ?, ?)"
            values = (customer.customerID, customer.firstName, customer.lastName, customer.email, customer.phoneNumber)

            cur.execute(query, values)
            self.connection.commit()
            cur.close()
            return True

        except Exception as e:
            print(f"Error Adding Customer : {e}")

    def removeCustomer(self, customerID):
        try:
            cur = self.connection.cursor()

            query = f"DELETE FROM Customer_Table WHERE customerID = {customerID}"

            cur.execute(query)
            self.connection.commit()

            cur.close()
            return True
        
        except Exception as e:
            print(f"Error Removing Customer : {e}")

    def listCustomers(self):
        try:
            cur = self.connection.cursor()

            query = "SELECT * FROM Customer_Table"

            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        
        except Exception as e:
            print(f"Error Listing Customers : {e}")
    
    def findCustomerById(self, customerID):
        try:
            cur = self.connection.cursor()

            query = f"SELECT * FROM Customer_Table WHERE customerID = {customerID}"

            cur.execute(query)
            result = cur.fetchall()

            if not result:
                raise CustomerNotFoundException
            
            result = result[0]
            customer = Customer(result[0], result[1], result[2], result[3], result[4])
            
            return customer
        
        except CustomerNotFoundException:
            raise

        except Exception as e:
            print(f"Error Finding Customer by ID : {e}")
    
    # Lease Management
    def createLease(self, customerID, carID, startDate, endDate):
        try:
            cur = self.connection.cursor()

            date_1 = datetime.strptime(startDate, "%Y-%m-%d").date()
            date_2 = datetime.strptime(endDate, "%Y-%m-%d").date()
            difference = date_2 - date_1

            if difference.days >= 30:
                type = "MonthlyLease"
            else:
                type = "DailyLease"
                
            query_1 = "INSERT INTO Lease_Table VALUES (?, ?, ?, ?, ?)"
            values = (carID, customerID, startDate, endDate, type) 

            cur.execute(query_1, values)
            self.connection.commit()
            query_2 = 'SELECT TOP 1 leaseID FROM Lease_Table ORDER BY leaseID DESC'
            cur.execute(query_2)
            leaseID = cur.fetchone()[0]
            query_3 = f"UPDATE Vechile_Table SET status = 'notAvailable' WHERE vechileID = {carID}"
            cur.execute(query_3)
            cur.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error Creating Lease : {e}")
    
    def returnCar(self, leaseID):
        try:
            cur = self.connection.cursor()

            query = f"""SELECT l.vechileID, v.make, v.model, v.year, v.dailyRate, v.status, v.passengerCapacity, v.engineCapacity FROM Lease_Table l
            INNER JOIN Vechile_Table v
            ON v.vechileID = l.vechileID
            WHERE leaseID = {leaseID}"""

            cur.execute(query)
            result = cur.fetchone()
            cur.close()

            if not result:
                raise LeaseNotFoundException

            return result
        
        except LeaseNotFoundException:
            raise

        except Exception as e:
            print(f"Error Returning Car : {e}")
    
    def listActiveLeases(self):
        try:
            cur = self.connection.cursor()

            query = "SELECT * from Lease_Table WHERE CONVERT(DATE, GETDATE()) BETWEEN startDate AND endDate"

            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        
        except Exception as e:
            print(f"Error Listing Active Leases : {e}")
    
    def listLeaseHistory(self):
        try:
            cur = self.connection.cursor()

            query = "SELECT * FROM Lease_Table"

            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        
        except Exception as e:
            print(f"Error Listing Lease History : {e}")
    
    # Payment Table
    def recordPayment(self, lease, amount):
        try:
            cur = self.connection.cursor()

            query = "INSERT INTO Payment_Table VALUES (?, CONVERT(DATE, GETDATE()), ?)"
            values = (lease.leaseID, amount)

            cur.execute(query, values)
            self.connection.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error Recoding Payment : {e}")