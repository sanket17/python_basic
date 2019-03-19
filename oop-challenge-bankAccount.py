# bank account problem

class Account():

    def __init__(self, owner, balance = 100):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'{self.owner} has {self.balance} in his/her account'
    
    def get_owner_name(self):
        return self.owner

    def get_owner_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Your account has been credited with amount {amount}, so your current balance is: {self.balance}')

    def withdrawal(self, amount):
        if amount > self.balance:
            print('You do not have sufficient amount for withdrawal! Please enter another amount.\n')
        else:
            self.balance -= amount
            print(f'Your account has been deducted with amount {amount}, so your current balance is: {self.balance}')

    
sanket_obj = Account('Sanket')
print(sanket_obj)
sanket_obj.deposit(1000)
sanket_obj.withdrawal(2000)
sanket_obj.withdrawal(1000)
print(sanket_obj)
