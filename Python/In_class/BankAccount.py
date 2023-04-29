class BankAccount: # parent class
    def __int__(self):
        self.balance = 0
       # self.amount
    def customer_info(self):
        print("Welcome to TA CANADA BANK")
        self.acc = input("Enter the Account Type:")
        self.c_name = input("Enter the name of the customer:")
class Saving(BankAccount):
    balance = 0
    def deposit(self):
        if self.acc=="saving":
            amount=float(input("Enter the amount to deposit in saving acc:"))
            self.balance+=amount
            print("Your Balance is:",amount)
        else:
           return exit()
    def widhdraw(self):
        amount=float(input("Enter the amount to withdraw from saving acc:"))
        if self.balance>=amount:
            self.balance -=amount
            print("Amount you have withdraw:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("You Available balance is:",self.balance)
#class Checking(BankAccount):
sc = Saving()
sc.customer_info()
sc.deposit()
sc.widhdraw()
sc.display()