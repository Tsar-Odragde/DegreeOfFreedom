#position,name, age, level, salary
se1=["software Engineer", "Max", 20, "Junior", 5000]
se2=["Software Engineer", "Lisa", 25, "Senior", 7000]
d1=["Designer", "Philipp"]
#Global function
#def code(se):
#    print(f"{se[1]} is writing the code")
#code(d1)
#class
class SoftwareEngineer:
    #class attribute
    alias = "Keyboard Magician"
    # special method to initilize the object
    def __init__(self, name, age, level, salary):
        #instance attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        #instant method
    def code(self):
        print(f"{self.name} is writing the code")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")
    #def information(self):
    #    information = f"name={self.name},age={self.age}, level={self.level}"
    #    return information
    #dunder method
    def __str__(self):
        information = f"name={self.name},age={self.age}, level={self.level}"
        return information
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    @staticmethod
    def entry_salary(age):
        if age<25:
            return 5000
        if age<30:
            return 7000
        else:
            return 9000
#    print(f"{se[1]} is writing the code")
#instance
se1=SoftwareEngineer("Max", 20, "Junior", 5000)
#print(se1.name, se1.age)
se2=SoftwareEngineer("Lisa", 25, "Senior", 7000)
#print(se2.name, se2.age)
se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("Java")
print(se1==se2)
print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
#print(se1.information())
print(se1)
print(se2)


