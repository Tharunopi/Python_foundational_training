class Bank:
    def __init__(self, bankname, rateofinterest):
        self.bankname = bankname
        self.rateofinterest = rateofinterest

    def calculate_amt(self, amount, year):
        si = self.rateofinterest * year * amount
        return si

    def customer_function(self, cid, cname, amount, year=1):
        simple_interest = self.calculate_amt(amount, year)
        return f"ID: {cid}, Name: {cname}, Amount: {amount}\nBank: {self.bankname}, ROI: {self.rateofinterest}, Returns: {simple_interest}"
    
customer_history = []
bank_name = input("Enter Bank name: ")
interest_pa = float(input("Enter ROI per annum: "))
bank_1 = Bank(bank_name, interest_pa)
for i in range(3):
    id = int(input("Enter ID: "))
    c_name = input("Enter Name: ")
    amount = float(input("Enter amount: "))
    customer_history.append(bank_1.customer_function(id, c_name, amount))

print("-------------------------------------------")
for i in customer_history:
    print(i)