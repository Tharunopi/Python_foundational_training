from entity.Product import Product
import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class Clothing(Product):
    def __init__(self, productID, productName, description, price, quantityInStock, type, size, color):
        self.size = size
        self.color = color
        super().__init__(productID, productName, description, price, quantityInStock, type)