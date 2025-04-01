# private variables 
class Account:
    type = "Savings"
    def __init__(self, name, acc_no, amount):
        self.name = name
        self.__acc_no = acc_no
        self._amount = amount

    def display(self):
        print(self.__acc_no)

class Bank(Account):
    def __init__(self, name, acc_no, amount):
        super().__init__(name, acc_no, amount)

    def displayed(self):
        print(f"{self.name} {self._amount}")
    
c_1 = Bank("Tharun", 8989898, 94943)
c_1.display()
c_1.displayed()
print(c_1.type)