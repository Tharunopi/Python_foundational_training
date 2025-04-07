class CarNotFoundException(Exception):
    def __init__(self, message="Car Not Found!"):
        super().__init__(message)