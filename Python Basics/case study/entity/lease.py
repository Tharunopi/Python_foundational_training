class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate, type):
        self.leaseID = leaseID
        self.vehicleID = vehicleID
        self.customerID = customerID
        self.startDate = startDate
        self.endDate = endDate
        self.type = type