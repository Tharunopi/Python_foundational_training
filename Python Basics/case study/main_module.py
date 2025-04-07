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
            print("1. Add Car")
            print("2. Remove Car")
            print("3. List Available Cars")
            print("4. List Rented Cars")
            print("5. Find Car By ID")

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
                status = input("Enter Status(available / notAvailable): ")
                passengerCapacity = int(input("Enter Passenger Capacity: "))
                engineCapacity = input("Enter Engine Capacity: ")

                car = Vechicle(carID, make, model, year, status, passengerCapacity, engineCapacity)
                repository.addCar(car)

            elif operation == 2:
                try:
                    carID = int(input("Enter CarID: "))
                    cur = conn.cursor()
                    query = "SELECT vechileID FROM Vechile_Table"
                    cur.execute(query)
                    carsID = cur.fetchall()

                    if carID not in carsID:
                        raise CarNotFoundException
                    
                    repository.removeCar(carID)

                except CarNotFoundException as e:
                    print(e)

            elif operation == 3:
                avaliableCars = repository.listAvailableCars()
                print(avaliableCars)

            elif operation == 4:
                rentedCars = repository.listRentedCars()
                print(rentedCars)

            elif operation == 5:
                try:
                    carID = int(input("Enter CarID: "))
                    cur = conn.cursor()
                    query = "SELECT vechileID FROM Vechile_Table"
                    cur.execute(query)
                    carsID = cur.fetchall()

                    if carID not in carsID:
                        raise CarNotFoundException
                    
                    result = repository.findCarById(carID)
                    print(result)

                except CarNotFoundException as e:
                    print(e)

            else:
                print("Enter valid Number")

        elif choice == 2:
            print("1. Add Customer")
            print("2. Remove Customer")
            print("3. List Customers")
            print("4. Find Customer By ID")

            try:
                operation = int(input("Choose an operation: "))
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

                    if customerID not in customersID:
                        raise CustomerNotFoundException
                    
                    repository.removeCustomer(customerID)

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

                    if customerID not in customersID:
                        raise CustomerNotFoundException
                    
                    repository.findCustomerById(customerID)

                except CustomerNotFoundException as e:
                    print(e)


        elif choice == 3:
            print("1. Create Lease")
            print("2. Return Car")
            print("3. List Active Leases")
            print("4. List Lease History")
        
        elif choice == 4:
            print("1. Record Payment")


        elif choice == 5:
            print("Logging out...")
            break

        else:
            print("Choose a number within range.")

    conn.close()

if __name__ == "__main__":
    main()