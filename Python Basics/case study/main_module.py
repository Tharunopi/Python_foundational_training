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
        print("\n\t\t\t\t\tCar Rental System")
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
                    try:
                        carID = int(input("Enter carID: "))
                        make = input("Enter make: ")
                        model = input("Enter car model: ")
                        year = str(input("Enter year: "))
                        dailyRate = float(input("Enter Daiy Rate: "))
                        status = input("Enter Status(available / notAvailable): ")
                        passengerCapacity = int(input("Enter Passenger Capacity: "))
                        engineCapacity = float(input("Enter Engine Capacity: "))

                        car = Vechicle(vechiceID=carID, make=make, model=model, year=year, dailyRate=dailyRate, status=status, passengerCapacity=passengerCapacity, engineCapacity=engineCapacity)
                        if repository.addCar(car):
                            print("Car Added Successfully.")
                    
                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 2:
                    try:
                        carID = int(input("Enter CarID: "))
                        cur = conn.cursor()
                        query = "SELECT vechileID FROM Vechile_Table"
                        cur.execute(query)
                        carsID = cur.fetchall()

                        if not any(carID in i for i in carsID):
                            raise CarNotFoundException
                        
                        if repository.removeCar(carID):
                            print("Car Removed Successfully.")

                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print("Error : {e}")

                elif operation == 3:
                    try:
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

                        if not avaliableCars:
                            print("No Available Cars Found.")
                        else:
                            for i in avaliableCars:
                                print(f"ID: {i[0]}, Make: {i[1]}, Model: {i[2]}, Year: {i[3]}, DailyRate: {i[4]}, Status: {i[5]}, PassengerCapacity: {i[6]}, EngineCapacity: {i[7]}ltr")

                        cur.close()

                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 4:
                    try:
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

                        if not rentedCars:
                            print("No Rented Cars Found.")
                        else:
                            for i in rentedCars:
                                print(f"ID: {i[0]}, Make: {i[1]}, Model: {i[2]}, Year: {i[3]}, DailyRate: {i[4]}, Status: {i[5]}, PassengerCapacity: {i[6]}, EngineCapacity: {i[7]}ltr")

                        cur.close()

                    except Exception as e:
                        print(f"Error : {e}")

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
                        print(f"ID: {result[0]}, Make: {result[1]}, Model: {result[2]}, Year: {result[3]}, DailyRate: {result[4]}, Status: {result[5]}, PassengerCapacity: {result[6]}, EngineCapacity: {result[7]}ltr")
                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : {e}")

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
                    try:
                        customerID = int(input("Enter CustomerID: "))
                        firstName = input("Enter First Name: ")
                        lastName = input("Enter Last Name: ")
                        email = input("Enter E-Mail: ")
                        phoneNumber = input("Enter Phone Number: ")

                        customer = Customer(customerID, firstName, lastName, email, phoneNumber)

                        if repository.addCustomer(customer):
                            print("Customer Added Successfully.")

                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 2:
                    try:
                        customerID = int(input("Enter CustomerID: "))
                        cur = conn.cursor()

                        query = "SELECT customerID FROM Customer_Table"

                        cur.execute(query)
                        customersID = cur.fetchall()

                        if not any(customerID in i for i in customersID):
                            raise CustomerNotFoundException
                        
                        if repository.removeCustomer(customerID):
                            print("Customer Removed Successfully.")

                        cur.close()

                    except CustomerNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 3:
                    try:
                        listCustomers = repository.listCustomers()

                        if not listCustomers:
                            print("No Customer Found.")
                        else:
                            for i in listCustomers:
                                print(f"ID: {i[0]}, FirstName: {i[1]}, LastName: {i[2]}, E-Mail: {i[3]}, MobileNumber: {i[4]}")

                    except Exception as e:
                        print(f"Error : {e}")

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
                        print(f"ID: {customerz.customerID}, FirstName: {customerz.firstName}, LastName: {customerz.lastName}, E-Mail: {customerz.email}, PhoneNumber: {customerz.phoneNumber}")
                        cur.close()

                    except CustomerNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : {e}")
                
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
                        if lease:
                            print("Lease Created Successfully.")

                        cur.close()

                    except CarNotFoundException as e:
                        print(e)

                    except CustomerNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : e")

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
                        print(f"ID: {leaseInfo[0]}, Make: {leaseInfo[1]}, Model: {leaseInfo[2]}, Year: {leaseInfo[3]}, DailyRate: {leaseInfo[4]}, Status: {leaseInfo[5]}, PassengerCapacity: {leaseInfo[6]}, EngineCapacity: {leaseInfo[7]}")
                        cur.close()

                    except LeaseNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 3:
                    try:
                        activeLeases = repository.listActiveLeases()
                        if not activeLeases:
                            print("No Active Leases Found.")
                        else:
                            for i in activeLeases:
                                print(f"ID: {i[0]}, CustomerID: {i[1]}, CarID: {i[2]}, StartDate: {i[3]}, EndDate: {i[4]}, Type: {i[5]}")
                    
                    except Exception as e:
                        print(f"Error : {e}")

                elif operation == 4:
                    try:
                        leaseHistory = repository.listLeaseHistory()
                        if not leaseHistory:
                            print("No Lease History FOund.")
                        else:
                            for i in leaseHistory:
                                print(f"ID: {i[0]}, CustomerID: {i[1]}, CarID: {i[2]}, StartDate: {i[3]}, EndDate: {i[4]}, Type: {i[5]}")

                    except Exception as e:
                        print(f"Error : {e}")

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

                        if repository.recordPayment(lease, amount):
                            print("Payment Recorded Successfully.")

                        cur.close()

                    except LeaseNotFoundException as e:
                        print(e)

                    except Exception as e:
                        print(f"Error : {e}")

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