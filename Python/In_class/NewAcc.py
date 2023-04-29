class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Deposit and Withdraw")
    def deposit(self):
        amount=float(input("Enter the amount:"))
        self.balance += amount
        print("amount deposit is:",amount)
    def withdraw(self):
        amount=float(input("Enter the amount to widhdraw:"))
        self.balance-=amount
        print("YOu have widhdraw is:",amount)
    def display(self):
        print("Your available balance is:",self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
