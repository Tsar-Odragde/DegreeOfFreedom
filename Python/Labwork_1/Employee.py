class Employee:
    def __init__(self, name, hr_rate, hr_worked, exp):
        self.name = name
        self.hr_rate = hr_rate
        self.hr_worked = hr_worked
        self.experience = exp

    def _calculate_salary(self):
        base_salary = self.hr_rate * self.hr_worked
        tax_deduction = base_salary * 0.13
        net_salary = base_salary - tax_deduction
        yearly_salary = net_salary * 12
        bonus = 0
        if self.experience > 15:
            bonus = 1000
        return f"{self.name}'s base salary is ${base_salary} with a bonus of ${bonus}, yearly salary is " \
               f"${yearly_salary}, and their net salary after tax deduction is ${net_salary} per month."

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Hourly Rate: ${self.hr_rate}")
        print(f"Hours Worked: {self.hr_worked}")
        print(f"Experience: {self.experience} years")

    def display_salary_details(self):
        salary_details = self._calculate_salary()
        print(salary_details)


my_name = input("Enter employee name: ")
my_hr_rate = float(input("Enter your hourly rate: "))
my_hr_worked = float(input("Enter hours worked this month: "))
my_exp = int(input("Enter experience in years: "))

employee = Employee(my_name, my_hr_rate, my_hr_worked, my_exp)

employee.display_details()
employee.display_salary_details()
