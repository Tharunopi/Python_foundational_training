from entity.Product import Product

class Electronics(Product):
    def __init__(self, productID, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod
        super().__init__(productID, productName, description, price, quantityInStock, type)
        