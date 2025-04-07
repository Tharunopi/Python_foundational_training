class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease Not Found!"):
        super().__init__(message)