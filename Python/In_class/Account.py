class Account:  # Base class/super class/parent class
    cust_name=""
    def saving(self):
        print("Customer opened saving acc")
class Accdetail(Account):  #subclass

    def checking(self,x):
        for i in x:
            print(i)
    #to override the method
    def saving(self,cust_name):
       print("Names are",cust_name[1])
#create an object for subclass
accdt = Accdetail() # creating object using subclass
#access superclass attribute and method
accdt.cust_name=["John","David","Ajay"]
accdt.saving(accdt.cust_name) #calling super class method using subclass object
#call subclass method
accdt.checking(accdt.cust_name) # calling subclass method using subclass object