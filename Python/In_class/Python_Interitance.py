# Inherits, extends and override
# Multiple Interitance using python
class Employee:  # parent class or super class or base class
    #instance attributes
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working in TCS")
class SoftwareEngineer(Employee):
    def __init__(self, name,age,salary, level):
        super().__init__(name, age, salary)
        self.level = level
    def work(self):
        print(f"{self.name} is working in Google and he is {self.level} and salary is {self.salary}")
    def debug(self):
        print(f"{self.name} is debugging")
class Designer(Employee):   # subclass or child class
    def work(self):
        print(f"{self.name} is working in amazon")
    def draw(self):
        print(f"{self.name} is drawing")
    def sal_cal(self, age):
        if age < 25:
            return 5000
        if age < 35:
            return 7000
        else:
            return 8000
    def eval(self):
        #self.salary
        amount = float(input(f"Enter how many Hr {self.name} worked:"))
        self.salary *=amount
        print(f"The total salary is:{self.salary}")
#instance
se= SoftwareEngineer("John",22, 5000, "Junior")
print(se.name, se.age, se.salary)
#se2 = SoftwareEngineer("David", 28, 4000, "Senior")

se.work()
se.debug()
#se2.work()
d=Designer("David", 28, 4000)
print(d.name, d.age, d.salary)
d.work()
d.draw()
print(d.sal_cal(30))
d.eval()



