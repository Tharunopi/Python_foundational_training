from entity.Product import Product

class Electronics(Product):
    def __init__(self, productID, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productID, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod
