import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class UserNotFound(Exception):
    def __init__(self, message="Exception: User Not Found"):
        super().__init__(message)