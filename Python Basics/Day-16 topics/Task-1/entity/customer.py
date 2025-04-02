class customer:
    def __init__(self, cid, cname, address, mob):
        self.cid = cid
        self.cname = cname 
        self.address = address
        self.mob = mob

    def get_customer(self):
        return (self.cid, self.cname, self.address, self.mob)
