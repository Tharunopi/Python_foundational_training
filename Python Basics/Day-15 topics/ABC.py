from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def view_balance(self):
        pass

class SBI(Bank):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit success")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw success")
        
    def view_balance(self):
        print(f"Balance: {self.balance}")
    
sbi = SBI(300)
sbi.deposit(700)
sbi.withdraw(500)
sbi.view_balance()