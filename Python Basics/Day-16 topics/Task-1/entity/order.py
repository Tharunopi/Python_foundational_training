class order:
    def __init__(self, oid, date, cid, pid, qty, price):
        self.oid = oid
        self.date = date
        self.cid = cid
        self.pid = pid
        self.qty = qty
        self.price = price
        self.total_amt = self.qty * self.price
    
    def make_order(self):
        return (self.oid, self.date, self.cid, self.pid, self.qty, self.price, self.total_amt)