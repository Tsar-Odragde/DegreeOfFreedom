class BankAccount:
    bank_names='ABC Bank, DEF Bank, XYZ Bank'

    def __init__(self, name, balance=0, bank=bank_names):
        self.name = name
        self.balance = balance
        self.bank = bank
    def display(self):
        print(self.name, self.balance, self.bank)

    def withdraw(self, amount):
        if self.balance>=500:
            self.balance -= amount
        else:
            print("Please maintan balance")
    def deposit(self, amount):
        self.balance +=amount

ba1 = BankAccount('Mike', 200, 'TRR BANK')
ba2 = BankAccount('Tom')
ba1.withdraw(100)
ba1.deposit(500)
ba1.display()
ba2.display()
