class product:
    def __init__(self, pid, pname, desc, price):
        self.pid = pid
        self.pname = pname
        self.desc = desc
        self.price = price

    def get_product(self):
        return (self.pid, self.pname, self.desc, self.price)