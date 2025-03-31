class Employee:
    def __init__(self, empid, empname, dept, salary):
        self.empid = empid
        self.empname = empname
        self.dept = dept
        self.salary = salary

    def display_emp_details(self):
        print(f"ID: {self.empid}, Name: {self.empname}")
        print(f"Department: {self.dept}, Salary: {self.salary}")

    def final_salary(self):
        hra, da = 400 , 200
        self.salary += (hra + da)
        self.salary -= self.salary * 0.05
        return self.salary
    
id = int(input("Enter emp_id: "))
name = input("Enter name: ")
dept = input("Enter department: ")
salary = float(input("Enter salary: "))

emp_1 = Employee(id, name, dept, salary)
emp_1.display_emp_details()
print(f"Final salary - {emp_1.final_salary()}")