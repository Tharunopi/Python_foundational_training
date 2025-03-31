# default constructor
class One:
    def __init__(self):
        pass

    def __repr__(self):
        return "Hello, World"
    
# parameterized constructor
class Two:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hi, {self.name}"
    
a = Two("Tharun")
print(a.greet())