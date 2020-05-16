

class BankAccount(object):  
    def __init__(self, object):
        self.name = object
        self.balance = 0
    # above is the constructor

    def make_deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient Funds to withdraw this amount.')
    
    def check_bal(self):
        return int(self.balance)
        # if self.balance > 0:
        #     print("You have a positive balance.")
        # if self.balance <= 0:
        #     print("You do not have a positive balance.")



# bank = BankAccount("Kyle")
# bank.make_deposit(100)
# bank.is_bal_pos()
# bank.withdraw(200)
#print(bank.__dict__)