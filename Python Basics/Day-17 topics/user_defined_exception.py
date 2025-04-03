class SalaryError(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)

salary = 60001
try:
    if not 5000 < salary < 10000:
        raise SalaryError("Low Salary")
    
    print(salary)

except SalaryError as e:
    print(e)