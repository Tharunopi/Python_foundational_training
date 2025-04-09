import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class NotAnAdmin(Exception):
    def __init__(self, message="Exception: Give ID is Not an Admin"):
        super().__init__(message)