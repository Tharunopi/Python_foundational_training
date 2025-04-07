class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer Not Found!"):
        super().__init__(message)