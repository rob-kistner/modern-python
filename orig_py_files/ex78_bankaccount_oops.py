
class BankAccount:
    def __init__(self, ownername):
        self.ownername = ownername
        self.balance = 0.0
    
    def show_balance(self):
        print(f"{self.ownername}'s balance is: ${self.balance}")
    
    def deposit(self, amt):
        self.balance += amt
        self.show_balance()
    
    def withdraw(self, amt):
        self.balance -= amt
        self.show_balance()

acct = BankAccount("Rob")
acct.show_balance()
acct.deposit(1000)
