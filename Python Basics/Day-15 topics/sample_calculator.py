class Add:
    def add(self, a, b):
        return a + b

class Sub:
    def sub(self, a, b):
        return a - b
    
class Mul:
    def mul(self, a, b):
        return a * b
    
class Div:
    def div(self, a, b):
        return a / b
    
class Calculator(Add, Sub, Mul, Div):
    def __init__(self):
        Add.__init__(self)
        Sub.__init__(self)
        Mul.__init__(self)
        Div.__init__(self)

cal = Calculator()
print(cal.add(1, 2))
print(cal.sub(1, 2))
print(cal.mul(1, 2))
print(cal.div(1, 2))