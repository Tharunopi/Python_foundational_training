def deduct_tax(salary:float)-> float:
    if salary > 5_000_00 and salary <= 8_000_00:
        taxable_10 = abs(5_000_00 - salary) * 0.10
        salary -= taxable_10
    if salary > 8_000_00:
        taxable_20 = 3_000_00 * 0.10
        taxable_20 += abs(8_000_00 - salary) * 0.20
        salary -= taxable_20
    return salary

def add_employee_info(no_of_employees:int)-> list:
    if no_of_employees <= 0:
        return "Return Invaild!"

    employee_name = []
    employee_salary = []
    for i in range(no_of_employees):
        name = input("Enter name: ")
        salary_monthly = float(input("Enter salary: "))
        employee_name.append(name)
        employee_salary.append(salary_monthly)
    return employee_name, employee_salary

def salary_calculation(salary_details:list) -> list:
    for i in range(len(salary_details)):
        taxed_salary = deduct_tax(salary_details[i] * 12)
        salary_details[i] = round(taxed_salary / 12, 2)
    return salary_details

name, salary = add_employee_info(int(input("Enter number of employees: ")))
salary = salary_calculation(salary)

for i in range(len(name)):
    print(f"-- {name[i]} - {salary[i]}")