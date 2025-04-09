from dao.OrderProcessor import OrderProcesor

from entity.Product import Product
from entity.User import User
from entity.Electronics import Electronics
from entity.Clothing import Clothing

processor = OrderProcesor()

while True:
    print("\nOrder Management System")
    print("\n1. Create user")
    print("2. Create Product")
    print("3. Create Order")
    print("4. Cancel Order")
    print("5. Get All Products")
    print("6. Get Order By User")
    print("7. Exit")

    try:
        choice = int(input("Choose any option: "))
    except ValueError as e:
        print(e)

    if choice == 1:
        try:
            userId = int(input("Enter UserId: "))
            username = input("Enter UserName: ")
            password = input("Enter Password: ")
            role = input("Enter Role(Admin / User): ")

            user = User(userId=userId, username=username, password=password, role=role)

            result = processor.createUser(user)

            if result:
                print("User created Successfully")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 2:
        try:
            userId = int(input("Enter UserId: "))
            username = input("Enter UserName: ")
            password = input("Enter Password: ")
            role = input("Enter Role(Admin / User): ")

            user = User(userId=userId, username=username, password=password, role=role)

            productId = int(input("Enter ProductID: "))
            productName = input("Enter ProductName: ")
            description = input("Enter Description: ")
            price = float(input("Enter Price: "))
            quantityInStock = int(input("Enter Quantity in Stock: "))
            type = input("Enter Type(Electronics / Clothing): ")  
            if type == "Electronics":
                brand = input("Enter Brand: ")
                warrantyPeriod = int(input("Enter Warranty Period: "))
                product = Electronics(productID=productId, productName=productName, description=description, price=price, quantityInStock=quantityInStock, type=type, brand=brand, warrantyPeriod=warrantyPeriod)

            else:
                size = input("Enter Size: ")
                color = input("Enter Colour: ")
                product = Clothing(productID=productId, productName=productName, description=description, price=price, quantityInStock=quantityInStock, type=type, size=size, color=color)


            result = processor.createProduct(user=user, product=product)

            if result:
                print("Product Created Successfully")

        except Exception as e:
            print(f"Error: {e}")  

    elif choice == 3:
        try:
            userId = int(input("Enter UserId: "))
            username = input("Enter UserName: ")
            password = input("Enter Password: ")
            role = input("Enter Role(Admin / User): ")
            user = User(userId=userId, username=username, password=password, role=role)

            productIds = input("Enter Products: ")

            result = processor.createOrder(user, productIds)
            if result:
                print("Order created Successfully")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 4:
        try:
            userId = int(input("Enter UserID: "))
            orderId = int(input("Enter OrderID: "))

            result = processor.cancelOrder(userId=userId, orderId=orderId)
            if result:
                print("Order Canceled")
            else:
                print("Order Not Canceled")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 5:
        try: 
            result = processor.getAllProducts()
            if result:
                for i in result:
                    if i[5] == 'Electronics':
                        print(f"ID: {i[0]}, Name: {i[1]}, Description: {i[2]}, Price: {i[3]}, InStock: {i[4]}, Type: {i[5]}, Brand: {i[6]}, Warranty Period: {i[7]}")
                    else:
                        print(f"ID: {i[0]}, Name: {i[1]}, Description: {i[2]}, Price: {i[3]}, InStock: {i[4]}, Type: {i[5]}, Size: {i[8]}, Colour: {i[9]}")

            else:
                print("No Products Found")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 6:
        try:
            userId = int(input("Enter UserId: "))
            username = input("Enter UserName: ")
            password = input("Enter Password: ")
            role = input("Enter Role(Admin / User): ")
            user = User(userId=userId, username=username, password=password, role=role)

            result = processor.getOrderByUser(user=user)

            if result:
                for i in result:
                    print(i)
            else:
                print("Order Not Found")

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 7:
        print("Logged Out..")
        break

    else: 
        print("Choose a valid option")