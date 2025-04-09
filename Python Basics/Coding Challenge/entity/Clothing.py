from entity.Product import Product

class Clothing(Product):
    def __init__(self, productID, productName, description, price, quantityInStock, type, size, color):
        self.size = size
        self.color = color
        super().__init__(productID, productName, description, price, quantityInStock, type)