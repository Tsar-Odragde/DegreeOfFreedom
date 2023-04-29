# Python Encapsulation
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 5000  # private
        #private int salary; in java
        self._num_bugs_solved=0 # private
    def code(self):
        self._num_bugs_solved+=1
    #getter function
    def get_salary(self):
        return self._salary
    #setter function
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
class Empsalary(SoftwareEngineer):
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved<10:
            return base_value
        if self._num_bugs_solved<100:
            return base_value * 2
        return base_value * 3
class Empworking(SoftwareEngineer):
    def __init__(self, name):
        #self.wage = 0
        self.name = name
    def eesalary(self):
        total_wage = 0
        wage = float(input(f"Enter the Hr Salary if {self.name}:"))
        hr = int(input(f"Enter No of Hr {self.name} worked:"))
        total_wage = wage * hr
        print(f"Total salary of {self.name} is", total_wage)
# instance
es = Empsalary("Max", 25)
#se = SoftwareEngineer("Max", 25)
print(es.name, es.age)
for i in range(90):
    es.code()
es.set_salary(60)
print(es.get_salary())
ew =Empworking("John")
ew.eesalary()