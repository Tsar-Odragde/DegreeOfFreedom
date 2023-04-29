# inherits, extends, override
class Employee:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working")
class SoftwareEngineer(Employee):
    def __init__(self,name, age, salary,level):
        super().__init__(name, age,salary)
        self.leve = level
    def work(self):
        print(f"{self.name} is Coding")
    def debug(self):
        print(f"{self.name} is debugging")

class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing")

    def draw(self):
        print(f"{self.name} is drawing")

se = SoftwareEngineer("Max", 32, 5000, "Junior")
print(se.name,se.age,se.salary)
se.work()
#se.debug()

#print(se.leve)
d = Designer("Philipp", 27, 7000)
print(d.name,d.age, d.salary)
d.work()
#d.draw()
# Polymorphism

employees = [SoftwareEngineer("Max", 25, 5500,"Junior"),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Philipp", 27, 7000)]
def motivate_emp(employees):
    for employee in employees:
        employee.work()

motivate_emp(employees)

