class Mobile:
    def __init__(self, mobile_model, mobile_price):
        self.mobile_model = mobile_model
        self.mobile_price = mobile_price

    def mobile_display(self):
        print(f"{self.mobile_model} {self.mobile_price}")

class Laptop(Mobile):
    def __init__(self, mobile_model, mobile_price, laptop_model, laptop_price):
        Mobile.__init__(self, mobile_model, mobile_price)
        self.laptop_model = laptop_model
        self.laptop_price = laptop_price
    
    def laptop_display(self):
        print(f"{self.laptop_model} {self.laptop_price}")

class Store(Laptop):
    def __init__(self, mobile_model, mobile_price, laptop_model, laptop_price, shop_name):
        Laptop.__init__(self, mobile_model, mobile_price, laptop_model, laptop_price)
        self.shop_name = shop_name
    
    def shop_details(self):
        print(self.shop_name)

store_1 = Store("S23", 60000, "ROG", 90000, "C-Moon")
store_1.mobile_display()
store_1.laptop_display()
store_1.shop_details()