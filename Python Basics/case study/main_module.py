from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl

from util.DBConnection import DBConnection

from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle

from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.CarNotFoundException import CarNotFoundException
from exception.LeaseNotFoundException import LeaseNotFoundException

import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

def main():
    conn = DBConnection.getConnection()
    repository = ICarLeaseRepositoryImpl()

    while True:
        print("\n\t\t\t\t\tCar Rental Application")
        print("1. Car Management")
        print("2. Customer Management")
        print("3. Lease Management")
        print("4. Payment Handling")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Choose a valid number.")
            continue

        if choice == 1:
            while True:
                print("\n--1. Add Car")
                print("--2. Remove Car")
                print("--3. List Available Cars")
                print("--4. List Rented Cars")
                print("--5. Find Car By ID")
                print("--6. Exit Operations Menu")

                try:
                    operation = int(input("Choose an operation: "))
                except ValueError:
                    print("Choose a valid number.")
                    continue

                if operation == 1:
                    carID = int(input("Enter carID: "))
                    make = input("Enter make: ")
                    model = input("Enter car model: ")
                    year = str(input("Enter year: "))
                    dailyRate = float(input("Enter Daiy Rate: "))
                    status = input("Enter Status(available / notAvailable): ")
                    passengerCapacity = int(input("Enter Passenger Capacity: "))
                    engineCapacity = float(input("Enter Engine Capacity: "))

                    car = Vechicle(vechiceID=carID, make=make, model=model, year=year, dailyRate=dailyRate, status=status, passengerCapacity=passengerCapacity, engineCapacity=engineCapacity)
                    repository.addCar(car)

                elif operation == 2:
                    try:
                        carID = int(input("Enter CarID: "))
                        cur = conn.cursor()
                        query = "SELECT vechileID FROM Vechile_Table"
                        cur.execute(query)
                        carsID = cur.fetchall()

                        if not any(carID in i for i in carsID):
                            raise CarNotFoundException
                        
                        repository.removeCar(carID)
                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                elif operation == 3:
                    cur = conn.cursor()
                    query = """UPDATE Vechile_Table 
                    SET status = 'available' 
                    WHERE vechileID IN (SELECT v.vechileID FROM Vechile_Table v 
                        INNER JOIN Lease_Table l
                        ON l.vechileID = v.vechileID 
                        WHERE CONVERT(DATE, GETDATE()) > l.endDate)"""
                    cur.execute(query)
                    conn.commit()
                    avaliableCars = repository.listAvailableCars()
                    print(avaliableCars)
                    cur.close()

                elif operation == 4:
                    cur = conn.cursor()
                    query = """UPDATE Vechile_Table 
                    SET status = 'notAvailable' 
                    WHERE vechileID IN (SELECT v.vechileID FROM Vechile_Table v 
                        INNER JOIN Lease_Table l 
                        ON l.vechileID = v.vechileID 
                        WHERE CONVERT(DATE, GETDATE()) BETWEEN l.startDate AND l.endDate)"""
                    cur.execute(query)
                    conn.commit()
                    rentedCars = repository.listRentedCars()
                    print(rentedCars)
                    cur.close()

                elif operation == 5:
                    try:
                        carID = int(input("Enter CarID: "))
                        cur = conn.cursor()
                        query = "SELECT vechileID FROM Vechile_Table"
                        cur.execute(query)
                        carsID = cur.fetchall()

                        if not any(carID in i for i in carsID):
                            raise CarNotFoundException
                        
                        result = repository.findCarById(carID)
                        print(result)
                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                else:
                    print("Exited from operations menu.")
                    break

        elif choice == 2:
            while True:
                print("\n--1. Add Customer")
                print("--2. Remove Customer")
                print("--3. List Customers")
                print("--4. Find Customer By ID")
                print("--5. Exit Operations Menu")

                try:
                    operation = int(input("\nChoose an operation: "))
                except ValueError:
                    print("Choose a valid number.")
                    continue

                if operation == 1:
                    customerID = int(input("Enter CustomerID: "))
                    firstName = input("Enter First Name: ")
                    lastName = input("Enter Last Name: ")
                    email = input("Enter E-Mail: ")
                    phoneNumber = input("Enter Phone Number: ")

                    customer = Customer(customerID, firstName, lastName, email, phoneNumber)

                    repository.addCustomer(customer)

                elif operation == 2:
                    try:
                        customerID = int(input("Enter CustomerID: "))
                        cur = conn.cursor()

                        query = "SELECT customerID FROM Customer_Table"

                        cur.execute(query)
                        customersID = cur.fetchall()

                        if not any(customerID in i for i in customersID):
                            raise CustomerNotFoundException
                        
                        repository.removeCustomer(customerID)
                        cur.close()

                    except CustomerNotFoundException as e:
                        print(e)

                elif operation == 3:
                    listCustomers = repository.listCustomers()
                    print(listCustomers)

                elif operation == 4:
                    try:
                        customerID = int(input("Enter CustomerID: "))
                        cur = conn.cursor()

                        query = "SELECT customerID FROM Customer_Table"

                        cur.execute(query)
                        customersID = cur.fetchall()                       

                        if not any(customerID in i for i in customersID):
                            raise CustomerNotFoundException
                        
                        customerz = repository.findCustomerById(customerID)
                        print(f"{customerz.customerID}, {customerz.firstName}, {customerz.lastName}, {customerz.email}, {customerz.phoneNumber}")
                        cur.close()

                    except CustomerNotFoundException as e:
                        print(e)
                
                else:
                    print("Exited from operations menu.")
                    break


        elif choice == 3:
            while True:
                print("\n--1. Create Lease")
                print("--2. Return Car")
                print("--3. List Active Leases")
                print("--4. List Lease History")
                print("--5. Exit Operations Menu")

                try:
                    operation = int(input("Choose an operation: "))
                except ValueError:
                    print("Choose a valid number.")
                    continue

                if operation == 1:
                    try:
                        cur = conn.cursor()
                        customerID = int(input("Enter customerID: "))
                        query_1 = "SELECT customerID FROM Customer_Table"
                        cur.execute(query_1)

                        customersID = cur.fetchall()
                        if not any(customerID in i for i in customersID):
                            raise CustomerNotFoundException

                        carID = int(input("Enter carID: "))
                        query_2 = "SELECT vechileID FROM Vechile_Table"
                        cur.execute(query_2)
                        carsID = cur.fetchall()
                        if not any(carID in i for i in carsID):
                            raise CarNotFoundException
                        
                        startDate = input("Enter Start Date(YYYY-MM-DD): ")
                        endDate = input("Enter End Date(YYYY-MM-DD): ")

                        lease = repository.createLease(customerID=customerID, carID=carID, startDate=startDate, endDate=endDate)
                        print(f"{lease.leaseID}, {lease.customerID}, {lease.vehicleID}, {lease.startDate}, {lease.endDate}, {lease.type}")

                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                    except CustomerNotFoundException as e:
                        print(e)

                elif operation == 2:
                    try:
                        leaseID = int(input("Enter LeaseID: "))
                        cur = conn.cursor()

                        query = "SELECT leaseID FROM Lease_Table"
                        cur.execute(query)
                        leasesID = cur.fetchall()

                        if not any(leaseID in i for i in leasesID):
                            raise LeaseNotFoundException
                        
                        leaseInfo = repository.returnCar(leaseID)
                        print(leaseInfo)
                        cur.close()

                    except LeaseNotFoundException as e:
                        print(e)

                elif operation == 3:
                    activeLeases = repository.listActiveLeases()
                    print(activeLeases)

                elif operation == 4:
                    leaseHistory = repository.listLeaseHistory()
                    print(leaseHistory)

                else:
                    print("Exited from operations menu.")
                    break

        
        elif choice == 4:
            while True:
                print("\n--1. Record Payment")
                print("--2. Exit Operations Menu")

                try:
                    operation = int(input("Choose an operation: "))
                except ValueError:
                    print("Choose a valid number.")
                    continue

                if operation == 1:
                    try:
                        cur = conn.cursor()
                        
                        leaseID = int(input("Enter leaseID: "))
                        query_1 = f"SELECT leaseID FROM Lease_Table"
                        cur.execute(query_1)
                        leasesID = cur.fetchall()

                        if not any(leaseID in i for i in leasesID):
                            raise LeaseNotFoundException

                        query_2 = f"SELECT * FROM Lease_Table WHERE leaseID = {leaseID}"
                        cur.execute(query_2)
                        leaseInfo = cur.fetchone()

                        carID = leaseInfo[1]
                        customerID = leaseInfo[2]
                        startDate = leaseInfo[3]
                        endDate = leaseInfo[4]
                        type = leaseInfo[5]
                        amount = float(input("Enter Amount: "))

                        lease = Lease(leaseID, carID, customerID, startDate, endDate, type)
                        repository.recordPayment(lease, amount)
                        cur.close()

                    except LeaseNotFoundException as e:
                        print(e)

                else:
                    print("Exited from operations menu.")
                    break

        elif choice == 5:
            print("\nLogged out...")
            break

        else:
            print("\nChoose a number within range.")

    conn.close()

if __name__ == "__main__":
    main()