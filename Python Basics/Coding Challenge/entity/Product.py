import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class Product:
    def __init__(self, productID, productName, description, price, quantityInStock, type):
        self.productID = productID
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type