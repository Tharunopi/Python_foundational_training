import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class OrderNotFound(Exception):
    def __init__(self, message="Exception: Order Not Found!"):
        super().__init__(message)